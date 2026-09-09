"""Rebuild only ICL context; preserve all frozen test facts, names and labels."""
from collections import Counter, defaultdict
import copy
import hashlib
import json
from pathlib import Path
import random
import re
import sys
import build_data as b

ROOT=Path(__file__).resolve().parent
INTRO=('Use only the stated facts. Treat each example as a separate problem. '
       'Answer Yes when the conclusion is stated directly or follows by chaining the facts. '
       'Answer No when the conclusion does not follow; you do not need to prove its opposite. '
       'All X are Y does not imply that all Y are X. Answer with Yes or No.\n\n')
SEED=20260908

def load(p): return [json.loads(x) for x in p.read_text().splitlines()]
def save(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False),encoding='utf-8')
def shuffled(ds,rng,last):
    ds=list(ds)
    while True:
        rng.shuffle(ds)
        if ds[-1]['gold']==last and any(a['gold']==c['gold'] for a,c in zip(ds,ds[1:])):
            return ds

def main():
    sys.path.insert(0,str(ROOT.parent/'tmp/tokenizer_audit_deps'))
    from tokenizers import Tokenizer
    tok=Tokenizer.from_file(str(ROOT/'tokenizer_source/tokenizer.json'))
    old={n:load(ROOT/f'data/pilot_{n}shot.jsonl') for n in (4,12)}
    families=defaultdict(list)
    for r in old[4]: families[r['family']].append(r)
    family_ids=sorted(families)
    assignment=['Yes']*(len(family_ids)//2)+['No']*(len(family_ids)//2)
    random.Random(SEED).shuffle(assignment)
    bank={}; prefixes={}; output={4:[],12:[]}; lengths={4:[],12:[]}
    for family,last in zip(family_ids,assignment):
        rng=random.Random(SEED+1009*family)
        templates={(r['check'],r['variant'],r['polarity']):r for r in families[family]}
        # Four matched basics, then eight additional examples with six Yes/six No overall.
        keys=[('direct','base','positive'),('twohop','base','positive'),
              ('direct','base','negative'),('twohop','base','negative'),
              ('robustness','reorder','positive'),('robustness','distractors','positive'),
              ('robustness','rename','positive'),('direct','base','positive'),
              ('robustness','reorder','negative'),('robustness','distractors','negative'),
              ('broken','first','negative'),('broken','second','negative')]
        # Templates are taken from a separate, randomly selected family and renamed.
        donor=rng.choice([f for f in family_ids if f!=family])
        templates={(r['check'],r['variant'],r['polarity']):r for r in families[donor]}
        blocks=[b.DEMO_NAMES[i:i+6] for i in range(0,72,6)]
        rng.shuffle(blocks)
        demos=[]
        for i,key in enumerate(keys):
            source=templates[key]; names=sorted({x for e in source['edges'] for x in e}|set(source['query']))
            target=list(blocks[i]); rng.shuffle(target)
            mapping=dict(zip(names,target))
            edges=[[mapping[a],mapping[c]] for a,c in source['edges']]
            query=[mapping[x] for x in source['query']]
            if i==7: query=list(edges[1]) # direct retrieval of the other fact
            proof=b.path(edges,query)
            d=dict(id=f'f{family:03d}_demo{i:02d}',edges=edges,query=query,
                   gold='Yes' if proof else 'No',proof=proof,source_kind=list(key))
            assert d['gold']==source['gold']
            assert not set(mapping.values()) & set(b.TEST_NAMES)
            demos.append(d)
        first=shuffled(demos[:4],rng,last)
        remaining=shuffled(demos[4:],rng,last)
        full=first+remaining
        bank[family]=dict(last_label=last,donor_family=donor,demos=full)
        for n in (4,12):
            ds=full[:n]
            assert Counter(d['gold'] for d in ds)=={'Yes':n//2,'No':n//2}
            assert ds[-1]['gold']==last
            prefixes[family,n]=INTRO+''.join(b.text(d['edges'],d['query'])+' '+d['gold']+'\n\n' for d in ds)
    mutable={'prompt','entity_spans','demo_ids','dataset_version','prompt_version','prompt_seed','icl_last_label'}
    for n in (4,12):
        for source in old[n]:
            r=copy.deepcopy(source); family=r['family']
            target=source['prompt'].rsplit('\n\n',1)[1]
            r['prompt']=prefixes[family,n]+target
            names={x for e in r['edges'] for x in e}|set(r['query'])
            r['entity_spans']=[dict(entity=x,start=m.start(),end=m.end()) for x in sorted(names)
                for m in re.finditer(r'\b'+re.escape(x)+r'\b',r['prompt'])]
            r.update(demo_ids=[d['id'] for d in bank[family]['demos'][:n]],
                     dataset_version='distinct_names_v2_prompt_v3',prompt_version='v3',
                     prompt_seed=SEED,icl_last_label=bank[family]['last_label'])
            assert all(r[k]==v for k,v in source.items() if k not in mutable)
            assert r['gold']==('Yes' if b.path(r['edges'],r['query']) else 'No')
            enc=tok.encode(r['prompt'],add_special_tokens=False).ids
            for label in (' Yes',' No'):
                full=tok.encode(r['prompt']+label,add_special_tokens=False).ids
                assert full[:-1]==enc
            assert len(enc)+8<=2048
            lengths[n].append(len(enc)); output[n].append(r)
        path=ROOT/f'data/pilot_{n}shot_prompt_v3.jsonl'
        path.write_text(''.join(json.dumps(r)+'\n' for r in output[n]),encoding='utf-8')
    save(ROOT/'data/demonstrations_prompt_v3.json',bank)
    report=dict(seed=SEED,status='passed',test_facts_names_queries_labels_unchanged=True,
                unique_prefixes={n:len({prefixes[f,n] for f in family_ids}) for n in (4,12)},
                conditions={n:dict(rows=len(output[n]),token_range=[min(lengths[n]),max(lengths[n])],
                sha256=hashlib.sha256((ROOT/f'data/pilot_{n}shot_prompt_v3.jsonl').read_bytes()).hexdigest()) for n in (4,12)},
                last_label_families=dict(Counter(assignment)))
    # Balance last label within every check/variant/gold, not merely over all prompts.
    for n in (4,12):
        groups=defaultdict(Counter)
        for r in output[n]: groups[r['check'],r['variant'],r['gold']][r['icl_last_label']]+=1
        assert all(c['Yes']==c['No'] for c in groups.values())
        assert len({r['prompt'] for r in output[n]})==1200
    save(ROOT/'data/prompt_v3_validation.json',report)
    preview=['# הפרומפט המתוקן — אותן שאלות מבחן\n\nהדגמות שונות לכל משפחה; בתוך משפחה כולן מקבלות אותו prefix. בארבע הדגמות 2/2, בשתים־עשרה 6/6. התשובה האחרונה מאוזנת 50/50 בין המשפחות.\n']
    for n in (4,12):
        preview.append(f'## {n} הדגמות, משפחה 0\n\n```text\n'+output[n][0]['prompt']+'\n```\n')
    (ROOT/'PROMPT_V3_EXAMPLES_HE.md').write_text('\n'.join(preview),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
