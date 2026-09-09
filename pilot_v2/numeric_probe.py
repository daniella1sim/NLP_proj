"""One-model numerical diagnostic. No weights downloaded or benchmark outputs modified."""
import argparse
import contextlib
import json
import os
from pathlib import Path
import socket
import sys
import sysconfig
import time
import traceback

ROOT = Path(__file__).resolve().parent


def tensors(value, path='output'):
    # Duck typing keeps the tree walker testable without a local torch install.
    if hasattr(value,'is_floating_point'):
        yield path,value
    elif isinstance(value,(tuple,list)):
        for i,item in enumerate(value): yield from tensors(item,f'{path}[{i}]')
    elif isinstance(value,dict):
        for key,item in value.items(): yield from tensors(item,f'{path}.{key}')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--storage',type=Path,required=True,help='Existing storage containing model/<revision>')
    parser.add_argument('--attention',choices=['eager','sdpa_math'],required=True)
    parser.add_argument('--dtype',choices=['float16','float32'],default='float16')
    args=parser.parse_args()
    import torch
    import transformers
    from transformers import AutoTokenizer,AutoModelForCausalLM
    report=dict(host=socket.gethostname(),python=sys.executable,python_version=sys.version,
                python_header=str(Path(sysconfig.get_paths()['include'])/'Python.h'),
                header_exists=(Path(sysconfig.get_paths()['include'])/'Python.h').is_file(),
                torch=torch.__version__,torch_path=torch.__file__,transformers=transformers.__version__,
                cuda=torch.version.cuda,visible=os.environ.get('CUDA_VISIBLE_DEVICES'),
                native_jit_disabled=os.environ.get('TORCH_DISABLE_NATIVE_JIT'),
                attention=args.attention,dtype=args.dtype,tests=[],status='starting')
    folder=ROOT/'diagnostics'; folder.mkdir(exist_ok=True)
    output=folder/f'{os.environ.get("SLURM_JOB_ID","local")}_{args.attention}_{time.time_ns()}.json'
    def save():
        output.write_text(json.dumps(report,indent=2),encoding='utf-8')
    def stats(t):
        valid=torch.isfinite(t)
        finite=t[valid]
        return dict(shape=list(t.shape),dtype=str(t.dtype),device=str(t.device),
                    nan=int(torch.isnan(t).sum().item()),inf=int(torch.isinf(t).sum().item()),
                    finite_absmax=float(finite.abs().max().item()) if finite.numel() else None)
    handles=[]
    try:
        print(json.dumps(report,indent=2),flush=True)
        if not torch.cuda.is_available(): raise RuntimeError('No allocated CUDA GPU.')
        torch.manual_seed(20260907)
        torch.backends.cuda.matmul.allow_tf32=False
        memory={i:max(0,torch.cuda.mem_get_info(i)[0]-2*2**30) for i in range(torch.cuda.device_count())}
        memory['cpu']=0
        lock=json.loads((ROOT/'model_lock.json').read_text())
        model_dir=args.storage.resolve()/'model'/lock['revision']
        if not (model_dir/'config.json').exists():
            raise FileNotFoundError(f'Model not present at {model_dir}. Pass its existing storage root; do not redownload.')
        report.update(model=lock,model_dir=str(model_dir),gpu_memory_budgets=memory)
        tokenizer=AutoTokenizer.from_pretrained(model_dir,local_files_only=True)
        print('Loading once for',args.attention,args.dtype,flush=True)
        model=AutoModelForCausalLM.from_pretrained(model_dir,local_files_only=True,
            torch_dtype=getattr(torch,args.dtype),use_safetensors=True,low_cpu_mem_usage=True,
            attn_implementation='eager' if args.attention=='eager' else 'sdpa',
            device_map='auto',max_memory=memory).eval()
        report['device_map']={k:str(v) for k,v in model.hf_device_map.items()}
        if any(v in ('cpu','disk') for v in report['device_map'].values()):
            raise RuntimeError('Insufficient GPU memory; CPU/disk offload not allowed.')
        model.config.use_cache=False
        print('Scanning loaded weights and buffers for NaN/Inf',flush=True)
        for name,tensor in list(model.named_parameters())+list(model.named_buffers()):
            if tensor.is_floating_point() and not torch.isfinite(tensor).all():
                report['invalid_parameter_or_buffer']=dict(name=name,stats=stats(tensor))
                raise RuntimeError('Non-finite loaded parameter/buffer: '+name)
        report['loaded_weights_finite']=True
        def hook(name):
            def inspect(module,inputs,result):
                for where,t in tensors(result):
                    if t.is_floating_point() and not torch.isfinite(t).all():
                        report['first_nonfinite_module']=dict(name=name,output=where,stats=stats(t),
                            inputs=[dict(path=p,stats=stats(x)) for p,x in tensors(inputs,'input') if x.is_floating_point()])
                        raise RuntimeError(f'First observed non-finite module output: {name} ({where})')
            return inspect
        for name,module in model.named_modules():
            handles.append(module.register_forward_hook(hook(name or 'model')))
        examples=[('plain_text','The capital of France is')]
        for shots in (4,12):
            row=json.loads((ROOT/f'data/pilot_{shots}shot.jsonl').read_text().splitlines()[0])
            examples.append((f'first_{shots}shot',row['prompt']))
        device=model.get_input_embeddings().weight.device
        for name,prompt in examples:
            item=dict(name=name,prompt=prompt)
            report['tests'].append(item)
            encoded=tokenizer(prompt,return_tensors='pt',add_special_tokens=False).to(device)
            item['tokens']=encoded.input_ids.shape[1]
            report.pop('first_nonfinite_module',None)
            print('Forward:',name,'tokens',item['tokens'],flush=True)
            try:
                backend=contextlib.nullcontext()
                if args.attention=='sdpa_math':
                    from torch.nn.attention import sdpa_kernel,SDPBackend
                    backend=sdpa_kernel(SDPBackend.MATH)
                with torch.inference_mode(),backend:
                    logits=model(**encoded,use_cache=False).logits[0,-1].float()
                    item.update(finite=bool(torch.isfinite(logits).all()),logit_stats=stats(logits),
                                top_token=tokenizer.decode([logits.argmax().item()]))
                print(name,'finite:',item['finite'],flush=True)
            except Exception as error:
                item.update(finite=False,error=str(error),traceback=traceback.format_exc(),
                            first_nonfinite_module=report.get('first_nonfinite_module'))
                print(name,'FAILED:',error,flush=True)
            save()
        report['status']='passed' if all(t['finite'] for t in report['tests']) else 'nonfinite_or_forward_error'
    except Exception as error:
        report.update(status='setup_error',error=str(error),traceback=traceback.format_exc())
        print(traceback.format_exc(),flush=True)
    finally:
        for handle in handles: handle.remove()
        save()
        print('DIAGNOSTIC REPORT:',output,'STATUS:',report['status'],flush=True)
    return 0 if report['status']=='passed' else 1


if __name__=='__main__': sys.exit(main())
