"""Name completion: exact first-word generation and full multi-token candidate scores."""
from collections import Counter, defaultdict
import csv
import json
import re


def parse_name(text, eos=False):
    # A partial prefix at the generation budget is not a completed word.
    m=re.match(r'^\s*([A-Za-z]+)(?=[^A-Za-z])',text)
    if m: return m.group(1)
    if eos:
        m=re.fullmatch(r'\s*([A-Za-z]+)\s*',text)
        if m: return m.group(1)
    return None


def answer_ids(tokenizer, prompt, name):
    prefix=tokenizer.encode(prompt,add_special_tokens=False)
    full=tokenizer.encode(prompt+' '+name+'.',add_special_tokens=False)
    if full[:len(prefix)]!=prefix or len(full)==len(prefix):
        raise ValueError('Name completion changes the prompt tokenization boundary.')
    return prefix,full[len(prefix):]


def winner(scores):
    high=max(scores.values())
    names=[name for name,value in scores.items() if value==high]
    return names[0] if len(names)==1 else 'Tie'


def evaluate_one(torch, tokenizer, model, row):
    from torch.nn.attention import sdpa_kernel, SDPBackend
    prompt=row['prompt']
    enc=tokenizer(prompt,return_offsets_mapping=True,add_special_tokens=False)
    base=enc['input_ids']; device=model.get_input_embeddings().weight.device
    tails={}
    for name in row['candidates']:
        prefix,tail=answer_ids(tokenizer,prompt,name)
        if prefix!=base: raise ValueError('Tokenization mismatch')
        tails[name]=tail
    if len(base)+max(8,max(map(len,tails.values())))>model.config.max_position_embeddings:
        raise ValueError('Context overflow; truncation is disabled.')
    scores={}; per_token={}
    with torch.inference_mode(),sdpa_kernel(SDPBackend.MATH):
        for name,tail in tails.items():
            # Position P-1 predicts the first answer token; never score prompt tokens.
            ids=torch.tensor([base+tail[:-1]],device=device)
            logits=model(ids,attention_mask=torch.ones_like(ids),use_cache=False).logits
            selected=logits[0,len(base)-1:len(base)+len(tail)-1].float()
            if not torch.isfinite(selected).all(): raise ValueError('Non-finite candidate logits: '+row['id'])
            target=torch.tensor(tail,device=selected.device).unsqueeze(-1)
            values=selected.log_softmax(-1).gather(-1,target).squeeze(-1)
            per_token[name]=values.tolist(); scores[name]=values.sum().item()
            del logits, selected, values
        generated_ids=[]; ended=False
        ids=torch.tensor([base],device=device)
        for step in range(8):
            logits=model(ids,attention_mask=torch.ones_like(ids),use_cache=False).logits[0,-1].float()
            if not torch.isfinite(logits).all(): raise ValueError('Non-finite generation logits: '+row['id'])
            token=logits.argmax().item(); generated_ids.append(token)
            ended=token==tokenizer.eos_token_id
            text=tokenizer.decode(generated_ids,skip_special_tokens=True)
            if ended or parse_name(text) is not None: break
            ids=torch.cat([ids,torch.tensor([[token]],device=device)],dim=1)
    text=tokenizer.decode(generated_ids,skip_special_tokens=True)
    free=parse_name(text,eos=ended)
    predicted=winner(scores)
    other=[x for x in row['candidates'] if x!=row['gold']]
    anchors=[dict(span,token_indices=[j for j,(a,b) in enumerate(enc['offset_mapping']) if a<span['end'] and b>span['start']]) for span in row['entity_spans']]
    means={n:scores[n]/len(tails[n]) for n in scores}
    return dict(row,candidate_logprobs=scores,candidate_mean_logprobs=means,
        candidate_token_logprobs=per_token,answer_token_ids=tails,
        predicted=predicted,correct=predicted==row['gold'],
        mean_score_predicted=winner(means),gold_minus_best_other=scores[row['gold']]-max(scores[x] for x in other),
        generated=text,generated_token_ids=generated_ids,free_label=free,
        free_correct=free==row['gold'],format_ok=free in row['candidates'],
        token_ids=base,token_offsets=enc['offset_mapping'],token_anchors=anchors)


def summarize(out, rows):
    import pilot
    groups=defaultdict(list)
    for r in rows: groups[r['check'],r['variant']].append(r)
    summary=[]
    for (check,variant),rs in sorted(groups.items()):
        n=len(rs)
        summary.append(dict(check=check,variant=variant,n=n,
            free_accuracy=sum(r['free_correct'] for r in rs)/n,
            candidate_accuracy=sum(r['correct'] for r in rs)/n,
            candidate_ties=sum(r['predicted']=='Tie' for r in rs),
            valid_candidate_format_rate=sum(r['format_ok'] for r in rs)/n,
            mean_gold_minus_other=sum(r['gold_minus_best_other'] for r in rs)/n))
    with (out/'summary.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(summary[0])); w.writeheader(); w.writerows(summary)
    by_id={r['id']:r for r in rows}; paired=defaultdict(list)
    for r in rows:
        if r.get('paired_base_id') in by_id:
            base=by_id[r['paired_base_id']]
            paired[r['check']+'/'+r['variant']].append(dict(
                both_free_correct=base['free_correct'] and r['free_correct'],
                both_candidate_correct=base['correct'] and r['correct'],
                free_answer_changed=r.get('rename_mapping',{}).get(base['free_label'],base['free_label'])!=r['free_label']))
    pilot.dump(out/'paired_metrics.json',{k:dict(n=len(v),**{m:sum(r[m] for r in v)/len(v) for m in v[0]}) for k,v in paired.items()})
    order_pairs=defaultdict(list)
    for r in rows:
        if r.get('option_order')==0 and r.get('option_pair_id') in by_id:
            other=by_id[r['option_pair_id']]
            order_pairs[r['check']+'/'+r['variant']].append(dict(
                both_free_correct=r['free_correct'] and other['free_correct'],
                both_candidate_correct=r['correct'] and other['correct'],
                free_same_name=r['free_label']==other['free_label'],
                candidate_same_name=r['predicted']==other['predicted']))
    if order_pairs:
        pilot.dump(out/'option_order_metrics.json',{k:dict(n=len(v),**{m:sum(x[m] for x in v)/len(v) for m in v[0]}) for k,v in order_pairs.items()})
    pilot.dump(out/'completion_metrics.json',dict(n=len(rows),free_correct=sum(r['free_correct'] for r in rows),
        candidate_correct=sum(r['correct'] for r in rows),generated_names=dict(Counter(r['free_label'] for r in rows)),
        mean_score_correct=sum(r['mean_score_predicted']==r['gold'] for r in rows)))
    print(f'{len(rows)} completed name-completion prompts. Read {out / "summary.csv"}')
