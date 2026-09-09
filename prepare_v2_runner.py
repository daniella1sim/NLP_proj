"""Build a separate runner from the original pilot, leaving past runs untouched."""
from pathlib import Path

root = Path(__file__).resolve().parent
if (root/'pilot_v2/pilot.py').exists():
    raise SystemExit('pilot_v2/pilot.py is now maintained directly; refusing to overwrite later parallel-execution changes.')
source = (root/'pythia_pilot/pilot.py').read_text(encoding='utf-8')
source = source.replace('Portable Pythia behavioral pilot.', 'Pythia-6.9B distinct-name behavioral pilot.')
source = source.replace("MODEL = 'EleutherAI/pythia-1b'", "MODEL = 'EleutherAI/pythia-6.9b'")
source = source[:source.index('def proof(')] + source[source.index('def download('):]
start = source.index('def load_runtime():')
end = source.index('def label_tokens(',start)
source = source[:start] + '''def load_runtime():
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    if not torch.cuda.is_available():
        raise RuntimeError('No CUDA GPU. Submit a GPU job first.')
    lock = json.loads((ROOT / 'model_lock.json').read_text())
    if lock['model_id'] != MODEL:
        raise ValueError('Wrong model lock.')
    model_dir = STATE / 'model' / lock['revision']
    torch.manual_seed(20260907)
    torch.backends.cuda.matmul.allow_tf32 = False
    memory = {}
    for i in range(torch.cuda.device_count()):
        free, total = torch.cuda.mem_get_info(i)
        memory[i] = max(0, free - 2 * 2**30)
    memory['cpu'] = 0
    print('Loading Pythia-6.9B; GPU budgets:', memory, flush=True)
    tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_dir, local_files_only=True, torch_dtype=torch.float16,
        use_safetensors=True, attn_implementation='eager', low_cpu_mem_usage=True,
        device_map='auto', max_memory=memory)
    mapping = model.hf_device_map
    if any(str(v) in ('cpu', 'disk') for v in mapping.values()):
        raise RuntimeError('GPU memory is insufficient. Use a larger GPU or two GPUs; CPU offload is disabled.')
    model.eval()
    model.config.use_cache = False
    print('Model loaded. Device map:', mapping, flush=True)
    return torch, tokenizer, model, lock


''' + source[end:]
start = source.index('def evaluate_one(')
end = source.index('def read_results(',start)
source = source[:start] + '''def evaluate_one(torch, tokenizer, model, row):
    prompt = row['prompt']
    enc = tokenizer(prompt, add_special_tokens=False, return_offsets_mapping=True)
    base = enc['input_ids']
    if len(base) + 8 > model.config.max_position_embeddings:
        raise ValueError('Context limit exceeded; truncation is disabled.')
    labels = {}
    for label in LABELS:
        prefix_ids, tail = label_tokens(tokenizer, prompt, label)
        if prefix_ids != base or len(tail) != 1:
            raise ValueError('This Pythia runner requires one-token answer labels.')
        labels[label.strip()] = tail[0]
    input_device = model.get_input_embeddings().weight.device
    ids = torch.tensor([base], device=input_device)
    with torch.inference_mode():
        # One shared forward pass: scoring and first generated token use identical logits.
        first = model(ids, attention_mask=torch.ones_like(ids), use_cache=False).logits[0, -1].float()
        if not torch.isfinite(first).all():
            raise ValueError('Non-finite logits.')
        logp = first.log_softmax(-1)
        scores = {label: logp[token].item() for label,token in labels.items()}
        first_logits = {label: first[token].item() for label,token in labels.items()}
        tail = []
        next_logits = first
        for step in range(8):
            token = next_logits.argmax().item()
            tail.append(token)
            if token == tokenizer.eos_token_id or step == 7:
                break
            ids = torch.cat([ids, torch.tensor([[token]], device=input_device)], dim=1)
            next_logits = model(ids, attention_mask=torch.ones_like(ids), use_cache=False).logits[0, -1].float()
    generated = tokenizer.decode(tail, skip_special_tokens=True)
    match = re.match(r'^\\s*(Yes|No)\\b', generated)
    free_label = match.group(1) if match else None
    margin = scores['Yes'] - scores['No']
    predicted = 'Yes' if margin > 0 else 'No' if margin < 0 else 'Tie'
    anchors = [dict(span, token_indices=[j for j,(a,b) in enumerate(enc['offset_mapping'])
                                        if a < span['end'] and b > span['start']])
               for span in row['entity_spans']]
    return dict(row, candidate_logprobs=scores, first_answer_logits=first_logits,
                answer_token_ids=labels, generated_token_ids=tail,
                yes_minus_no=margin, predicted=predicted, correct=predicted==row['gold'],
                generated=generated, free_label=free_label, format_ok=free_label is not None,
                free_correct=free_label==row['gold'], token_ids=base,
                token_offsets=enc['offset_mapping'], token_anchors=anchors)


''' + source[end:]
source = source.replace("candidate_accuracy=k/n, ci95_low=low", "candidate_accuracy=k/n, tie_rate=sum(v['predicted']=='Tie' for v in values)/n, ci95_low=low")
source = source.replace("gpu_gib=gpu.total_memory/2**30, cuda=torch.version.cuda,", "gpu_gib=gpu.total_memory/2**30, cuda=torch.version.cuda,\n                   all_gpus=[dict(name=torch.cuda.get_device_name(i), total_gib=torch.cuda.get_device_properties(i).total_memory/2**30) for i in range(torch.cuda.device_count())],\n                   device_map={k:str(v) for k,v in model.hf_device_map.items()},")
source = source.replace("torch.cuda.reset_peak_memory_stats()", "for i in range(torch.cuda.device_count()):\n        torch.cuda.reset_peak_memory_stats(i)")
source = source.replace("peak_allocated_gpu_gib=torch.cuda.max_memory_allocated()/2**30", "peak_allocated_gpu_gib=[torch.cuda.max_memory_allocated(i)/2**30 for i in range(torch.cuda.device_count())]")
start = source.index("    data = sub.add_parser('data')")
end = source.index("    sub.add_parser('download')",start)
source = source[:start]+source[end:]
source = source.replace("choices=[0,4], default=4", "choices=[4,12], default=12")
source = source.replace("    if args.cmd == 'data': write_data(args)\n    elif args.cmd == 'download': download(args)", "    if args.cmd == 'download': download(args)")
(root/'pilot_v2/pilot.py').write_text(source,encoding='utf-8',newline='\n')
print('Created pilot_v2/pilot.py')
