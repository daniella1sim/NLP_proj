"""Explicit shortest-path completion with frequency-preserving counterfactuals."""
from collections import Counter, deque
import copy
import hashlib
import json
import random
import re
import sys
from pathlib import Path
import build_data as b
import build_completion_data as old

ROOT=Path(__file__).resolve().parent
SEED=20260910
INTRO=('Use only the facts in each example. One step means following one stated fact from its first group to its second group. '
       'Count the steps in the shortest chain from the starting group to the answer. '
       'For a one-step question, give the directly linked group. For a two-step question, follow two facts and give the endpoint, not the intermediate group. '
       'Complete Answer with only the group name and a period. Each example is independent.\n\n')

def render(r):
    return ('\n'.join(f'All {a} are {c}.' for a,c in r['edges'])+
            f"\nQuestion: Starting from {r['query_source']}, which group has a shortest chain of exactly {r['hops']} "
            +('step' if r['hops']==1 else 'steps')+'?'+
            f"\nPossible answers: {r['candidates'][0]} or {r['candidates'][1]}.\nAnswer:")

def distances(edges,source):
    ds={source:0}; q=deque([source])
    while q:
        u=q.popleft()
        for a,z in edges:
            if a==u and z not in ds: ds[z]=ds[u]+1; q.append(z)
    return ds

def check(r):
    old.check(r)
    ds=distances(r['edges'],r['query_source'])
    assert [x for x,n in ds.items() if n==r['hops']]==[r['gold']]
    for counts in (Counter(x for e in r['edges'] for x in e), Counter(e[0] for e in r['edges']),Counter(e[1] for e in r['edges'])):
        assert counts[r['candidates'][0]]==counts[r['candidates'][1]]

def make_family(family):
    rng=random.Random(SEED+1009*family)
    a,bb,c,e,f,d,g,h=old.sample_names(rng,b.TEST_NAMES,8)
    base=[[a,bb],[bb,c],[e,f],[f,d]]; rng.shuffle(base)
    reverse=[[c,bb],[bb,a],[e,f],[f,d]]; rng.shuffle(reverse)
    rows=[]
    def add(kind,variant,slot,edges,source,gold,foil,hops,base_id=None,mapping=None):
        options=[gold,foil]
        if (family+slot)%2: options.reverse()
        r=dict(id=f'{family:03d}/{kind}/{variant}/{slot}',family=family,task='name_completion',
               check=kind,variant=variant,slot=slot,edges=copy.deepcopy(edges),query_source=source,
               candidates=options,gold=gold,proof=b.path(edges,[source,gold]),hops=hops,
               paired_base_id=base_id,dataset_version='name_completion_v2',seed=SEED)
        if mapping: r['rename_mapping']=mapping
        check(r); rows.append(r); return r
    add('direct','base',0,base,a,bb,f,1)
    add('direct','base',1,base,bb,c,d,1)
    forward=add('twohop','base',0,base,a,c,d,2)
    backward=add('twohop','base',1,reverse,c,a,d,2)
    for slot,variant in enumerate(('first','second')):
        replacements={a:f,e:bb} if slot==0 else {bb:d,f:c}
        edges=[[x,replacements.get(x,y)] for x,y in base]
        r=add('broken',variant,slot,edges,a,d,c,2,forward['id'])
        r['candidates']=list(forward['candidates'])
        r['changed_fact_indices']=[i for i,(x,y) in enumerate(zip(base,edges)) if x!=y]
        assert len(r['changed_fact_indices'])==2
        assert Counter(x for edge in base for x in edge)==Counter(x for edge in edges for x in edge)
    for variant in ('reorder','distractors','rename'):
        for slot,original in enumerate((forward,backward)):
            edges=copy.deepcopy(original['edges']); source=original['query_source']; gold=original['gold']; foil=d; mapping=None
            if variant=='reorder':
                while edges==original['edges']: rng.shuffle(edges)
            elif variant=='distractors':
                edges.append([g,h]); rng.shuffle(edges)
            else:
                names=sorted({x for edge in edges for x in edge})
                mapping=dict(zip(names,old.sample_names(rng,[x for x in b.TEST_NAMES if x not in names],len(names))))
                edges=[[mapping[x],mapping[y]] for x,y in edges]
                source=mapping[source]; gold=mapping[gold]; foil=mapping[foil]
            add('robustness',variant,slot,edges,source,gold,foil,2,original['id'],mapping)
    return rows

def main():
    sys.path.insert(0,str(ROOT.parent/'tmp/tokenizer_audit_deps'))
    from tokenizers import Tokenizer
    tok=Tokenizer.from_file(str(ROOT/'tokenizer_source/tokenizer.json'))
    families={f:make_family(f) for f in range(50)}
    demos={f:old.make_demos(f,families[(f+17)%50]) for f in families}
    for bank in demos.values():
        for d in bank: check(d)
    report=dict(version='name_completion_v2',seed=SEED,families=50,unique_questions=600,
                presentations=1200,conditions={},counterfactual_changed_facts=2)
    previews=['# מבחן השלמה v2 — פרומפטים מלאים\n']
    for shots in (0,4,12):
        rows=[]; lengths=[]
        for family,originals in families.items():
            bank=demos[family][:shots]
            assert not shots or Counter(d['candidates'].index(d['gold']) for d in bank)=={0:shots//2,1:shots//2}
            prefix=INTRO+''.join(render(d)+' '+d['gold']+'.\n\n' for d in bank)
            for original in originals:
                for order in (0,1):
                    r=copy.deepcopy(original); r['question_id']=original['id']; r['option_order']=order
                    r['id']=original['id']+f'/order{order}'
                    r['option_pair_id']=original['id']+f'/order{1-order}'
                    if r['paired_base_id']: r['paired_base_id']+=f'/order{order}'
                    if order: r['candidates'].reverse()
                    check(r)
                    r.update(shots=shots,prompt=prefix+render(r),demo_ids=[d['id'] for d in bank])
                    names={x for edge in r['edges'] for x in edge}
                    assert not names & {x for d in bank for edge in d['edges'] for x in edge}
                    r['entity_spans']=[dict(entity=n,start=m.start(),end=m.end()) for n in sorted(names)
                        for m in re.finditer(r'\b'+re.escape(n)+r'\b',r['prompt'])]
                    ids=tok.encode(r['prompt'],add_special_tokens=False).ids
                    assert len(ids)+8<=2048
                    for n in r['candidates']:
                        full=tok.encode(r['prompt']+' '+n+'.',add_special_tokens=False).ids
                        assert full[:len(ids)]==ids and len(full)-len(ids)<=8
                    lengths.append(len(ids)); rows.append(r)
        assert len(rows)==len({r['id'] for r in rows})==len({r['prompt'] for r in rows})==1200
        index={r['id']:r for r in rows}
        for r in rows:
            p=index[r['option_pair_id']]
            assert r['candidates']==p['candidates'][::-1] and r['edges']==p['edges'] and r['gold']==p['gold']
        baseline={}
        for kind in ('direct','twohop','broken','robustness'):
            sub=[r for r in rows if r['check']==kind]
            scores={}
            for rule in ('option_first','option_last','fact_first','fact_last','frequency'):
                vals=[]
                for r in sub:
                    flat=[x for e in r['edges'] for x in e]; cs=r['candidates']
                    if rule=='frequency': vals.append(.5); continue
                    pred=cs[0] if rule=='option_first' else cs[1] if rule=='option_last' else min(cs,key=flat.index) if rule=='fact_first' else min(cs,key=flat[::-1].index)
                    vals.append(int(pred==r['gold']))
                scores[rule]=sum(vals)/len(vals)
            baseline[kind]=scores
        target=ROOT/f'data/completion_v2_{shots}shot.jsonl'
        target.write_text(''.join(json.dumps(r)+'\n' for r in rows),encoding='utf-8')
        report['conditions'][shots]=dict(n=len(rows),token_range=[min(lengths),max(lengths)],
            sha256=hashlib.sha256(target.read_bytes()).hexdigest(),baselines=baseline)
        previews.append(f'## {shots} הדגמות\n\n```text\n'+rows[4]['prompt']+'\n```\n\nתשובה: '+rows[4]['gold']+'\n')
    old.dump(ROOT/'data/completion_v2_demonstrations.json',demos)
    old.dump(ROOT/'data/completion_v2_validation.json',report)
    (ROOT/'COMPLETION_V2_EXAMPLES_HE.md').write_text('\n'.join(previews),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
