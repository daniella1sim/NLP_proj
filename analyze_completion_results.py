"""Audit completion runs and probe shortcuts, paired controls, and clustered uncertainty."""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json
import math
import sys
import numpy as np
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'pilot_v2'))
sys.path.insert(0,str(ROOT/'tmp/tokenizer_audit_deps'))
from tokenizers import Tokenizer
from completion_evaluation import parse_name,winner
from build_data import path as proof_path
OUT=ROOT/'results/completion_analysis'; OUT.mkdir(exist_ok=True)
TOK=Tokenizer.from_file(str(ROOT/'pilot_v2/tokenizer_source/tokenizer.json'))
EOS=json.loads((ROOT/'pilot_v2/tokenizer_source/config.json').read_text())['eos_token_id']
def read(p): return [json.loads(s) for s in p.read_text().splitlines()]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
BOOT=np.random.default_rng(20260909).integers(0,100,size=(10000,100))
def ci(values):
    v=np.array(values,dtype=float)
    assert len(v)==100
    return np.quantile(v[BOOT].mean(axis=1),[.025,.975]).tolist()
def avg(xs): return sum(xs)/len(xs) if xs else None
def category(r):
    name=r['free_label']
    if name==r['gold']: return 'correct_target'
    if name in r['candidates']: return 'wrong_candidate'
    p=proof_path(r['edges'],[r['query_source'],name]) if name else None
    if p:
        return {1:'source_itself',2:'reachable_one_hop'}.get(len(p),'other_reachable')
    if name in {x for e in r['edges'] for x in e}: return 'unreachable_fact_name'
    return 'other_or_unparsed'
def metric(rs):
    fam=defaultdict(list)
    for r in rs: fam[r['family']].append(r)
    free=[int(r['free_correct']) for r in rs]; cand=[int(r['correct']) for r in rs]
    valid=[r for r in rs if r['format_ok']]
    goldcounts=Counter(r['gold'] for r in rs)
    freq_expected=[]; freq_agreement=[]
    for r in rs:
        counts=Counter(x for e in r['edges'] for x in e)
        a,b=r['candidates']; ga,gb=counts[a],counts[b]
        choice=a if ga>gb else b if gb>ga else None
        freq_expected.append(0.5 if choice is None else int(choice==r['gold']))
        if choice is not None: freq_agreement.append(choice==r['predicted'])
    return dict(n=len(rs),free_correct=sum(free),candidate_correct=sum(cand),
        free_accuracy=avg(free),candidate_accuracy=avg(cand),valid_candidate_rate=len(valid)/len(rs),
        free_accuracy_given_valid=avg([int(r['free_correct']) for r in valid]),
        free_ci95=ci([avg([int(r['free_correct']) for r in fam[f]]) for f in range(100)]),
        candidate_ci95=ci([avg([int(r['correct']) for r in fam[f]]) for f in range(100)]),
        errors=dict(Counter(category(r) for r in rs)),
        mean_score_accuracy=avg([r['mean_score_predicted']==r['gold'] for r in rs]),
        mean_vs_sum_disagreements=sum(r['mean_score_predicted']!=r['predicted'] for r in rs),
        candidate_first_rate=avg([r['predicted']==r['candidates'][0] for r in rs]),
        candidate_accuracy_by_gold_position={str(i):avg([r['correct'] for r in rs if r['candidates'].index(r['gold'])==i]) for i in (0,1)},
        by_answer_length={relation:dict(n=len(sub),candidate_accuracy=avg([r['correct'] for r in sub]),free_accuracy=avg([r['free_correct'] for r in sub])) for relation in ('shorter','equal','longer') for sub in [[r for r in rs if r['_length_relation']==relation]]},
        frequency_baseline_expected_accuracy=avg(freq_expected),frequency_choice_agreement=avg(freq_agreement),
        most_common_generated=Counter(r['free_label'] for r in rs).most_common(8),
        majority_name_baseline=max(goldcounts.values())/len(rs),
        free_wrong_candidate_right=sum(not r['free_correct'] and r['correct'] for r in rs),
        free_right_candidate_wrong=sum(r['free_correct'] and not r['correct'] for r in rs))

report={}; sets={}; compact=['# כל שאלות ההשלמה — השוואת 0/4/12 הדגמות\n']
for shots in (0,4,12):
    folder=ROOT/f'results/completion_review/completion_{shots}shot_v1'
    rs=read(folder/'results.jsonl'); sets[shots]=rs
    data=ROOT/f'pilot_v2/data/completion_{shots}shot.jsonl'; expected={r['id']:r for r in read(data)}
    issues=[]; workers=list((folder/'workers').iterdir()); worker_rows=[]; sessions=[]
    for w in workers:
        m=json.loads((w/'manifest.json').read_text()); worker_rows+=read(w/'results.jsonl')
        sessions += [json.loads(p.read_text()) for p in w.glob('session_*.json')]
        for k,p in [('data_sha256',data),('code_sha256',ROOT/'pilot_v2/pilot.py'),('completion_code_sha256',ROOT/'pilot_v2/completion_evaluation.py')]:
            if m[k]!=sha(p): issues.append(k)
        if m['attention']!='sdpa_math': issues.append('backend')
    if len(rs)!=1200 or len({r['id'] for r in rs})!=1200 or set(expected)!={r['id'] for r in rs}: issues.append('coverage')
    if sorted(worker_rows,key=lambda r:r['id'])!=sorted(rs,key=lambda r:r['id']): issues.append('merged')
    for r in rs:
        if any(r.get(k)!=v for k,v in expected[r['id']].items()): issues.append('input '+r['id'])
        valid=[c for c in r['candidates'] if proof_path(r['edges'],[r['query_source'],c])]
        if valid!=[r['gold']]: issues.append('logical gold '+r['id'])
        if proof_path(r['edges'],[r['query_source'],r['gold']])!=r['proof']: issues.append('proof')
        enc=TOK.encode(r['prompt'],add_special_tokens=False)
        if enc.ids!=r['token_ids']: issues.append('tokenizer IDs '+r['id'])
        # HF disables whitespace trimming in byte-level offsets; token IDs are identical.
        if len(enc.offsets)!=len(r['token_offsets']) or any(
            r['prompt'][a:b].strip()!=r['prompt'][c:d].strip()
            for (a,b),(c,d) in zip(enc.offsets,r['token_offsets'])):
            issues.append('offset content '+r['id'])
        for c in r['candidates']:
            full=TOK.encode(r['prompt']+' '+c+'.',add_special_tokens=False).ids
            if full[:len(enc.ids)]!=enc.ids or full[len(enc.ids):]!=r['answer_token_ids'][c]: issues.append('answer boundary')
            vals=r['candidate_token_logprobs'][c]
            if len(vals)!=len(r['answer_token_ids'][c]) or not all(math.isfinite(x) for x in vals): issues.append('scores')
            if not math.isclose(sum(vals),r['candidate_logprobs'][c],abs_tol=2e-5): issues.append('sum')
            if not math.isclose(r['candidate_logprobs'][c]/len(vals),r['candidate_mean_logprobs'][c],abs_tol=1e-6): issues.append('mean')
        text=TOK.decode(r['generated_token_ids'],skip_special_tokens=True)
        free=parse_name(text,eos=r['generated_token_ids'][-1]==EOS)
        pred=winner(r['candidate_logprobs'])
        if text!=r['generated'] or free!=r['free_label'] or pred!=r['predicted'] or (free==r['gold'])!=r['free_correct'] or (pred==r['gold'])!=r['correct']: issues.append('scoring '+r['id'])
        if (free in r['candidates'])!=r['format_ok']: issues.append('format')
        if winner(r['candidate_mean_logprobs'])!=r['mean_score_predicted']: issues.append('mean winner')
        lens=[len(r['answer_token_ids'][c]) for c in r['candidates']]
        gi=r['candidates'].index(r['gold']); delta=lens[gi]-lens[1-gi]
        r['_length_relation']='shorter' if delta<0 else 'longer' if delta>0 else 'equal'
    groups={k:metric([r for r in rs if r['check']==k]) for k in ('direct','twohop','broken','robustness')}
    subs={f'{k}/{v}':metric([r for r in rs if r['check']==k and r['variant']==v]) for k,vs in [('broken',['first','second']),('robustness',['reorder','distractors','rename'])] for v in vs}
    index={r['id']:r for r in rs}; pairs={}
    for k,v in [('broken','first'),('broken','second'),('robustness','reorder'),('robustness','distractors'),('robustness','rename')]:
        vals=[]
        for r in rs:
            if (r['check'],r['variant'])!=(k,v): continue
            a=index[r['paired_base_id']]
            mapping=r.get('rename_mapping',{})
            oldfree=mapping.get(a['free_label'],a['free_label']); oldpred=mapping.get(a['predicted'],a['predicted'])
            vals.append(dict(both_free=a['free_correct'] and r['free_correct'],both_candidate=a['correct'] and r['correct'],
                free_semantic_agreement=oldfree==r['free_label'],candidate_semantic_agreement=oldpred==r['predicted'],
                gold_margin_shift_expected=(a['gold_minus_best_other']+r['gold_minus_best_other'])>0 if k=='broken' else None))
        pairs[k+'/'+v]=dict(n=len(vals),**{m:sum(x[m] for x in vals) for m in vals[0] if vals[0][m] is not None})
    report[shots]=dict(issues=issues,offset_note='Local raw tokenizer trims leading whitespace; HF saved offsets include it. IDs and non-whitespace contents verified.',overall=metric(rs),groups=groups,subgroups=subs,paired=pairs,
        elapsed_minutes=sum(s['elapsed_seconds'] for s in sessions)/60,
        partial_unparsed=sum(r['free_label'] is None for r in rs),
        lengths=[min(len(r['token_ids']) for r in rs),max(len(r['token_ids']) for r in rs)])
report['changes']={}
for a,b in ((0,4),(4,12),(0,12)):
    out={}
    for k in ('direct','twohop','broken','robustness'):
        out[k]={}
        for m in ('free_correct','correct'):
            fam=defaultdict(list); gains=losses=0
            for x,y in zip(sets[a],sets[b]):
                assert x['id']==y['id']
                if x['check']==k:
                    fam[x['family']].append(int(y[m])-int(x[m]))
                    gains+=int(y[m] and not x[m]); losses+=int(x[m] and not y[m])
            means=[avg(fam[f]) for f in range(100)]
            out[k][m]=dict(delta=avg(means),ci95=ci(means),gains=gains,losses=losses)
    report['changes'][f'{b}_minus_{a}']=out
for triplet in zip(sets[0],sets[4],sets[12]):
    r=triplet[0]
    compact.append(f"## {r['id']}\n\n```text\n{r['prompt'].rsplit(chr(10)+chr(10),1)[1]}\n```\n\nאמת: **{r['gold']}**\n\n| הדגמות | פלט מדויק | free | candidate | סוג התשובה |\n|---|---|---|---|---|")
    for n,t in zip((0,4,12),triplet):
        compact.append(f"| {n} | {json.dumps(t['generated'],ensure_ascii=False)} | {t['free_label']} | {t['predicted']} | {category(t)} |")
(OUT/'ALL_EXAMPLES_HE.md').write_text('\n'.join(compact),encoding='utf-8')
(OUT/'audit_and_statistics.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({n:dict(issues=report[n]['issues'],groups={k:{m:v[m] for m in ('n','free_accuracy','candidate_accuracy','valid_candidate_rate','errors','frequency_baseline_expected_accuracy')} for k,v in report[n]['groups'].items()},paired=report[n]['paired']) for n in (0,4,12)},indent=2))
