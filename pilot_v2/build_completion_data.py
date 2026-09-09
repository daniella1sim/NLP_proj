"""Three paired shot conditions for constrained name completion (no Yes/No labels)."""
from collections import Counter
import copy
import hashlib
import json
from pathlib import Path
import random
import re
import sys
import build_data as b

ROOT=Path(__file__).resolve().parent
SEED=20260909
INTRO=('Use only the facts in each example. Choose one of the two possible completions. '
       'Complete the final sentence with that name, followed by a period. '
       'Each example is independent.\n\n')
EXTRA_DEMO=['abnorks','cedvils','fostrems','gundraks','hapvorns','jervults','klonspets','mavtorks',
            'noptrils','pevgrans','quendrops','raspulks','sovtrens','tavplins','uvdraks','vemdrops']

def read(p): return [json.loads(s) for s in p.read_text().splitlines()]
def dump(p,x): p.write_text(json.dumps(x,indent=2,ensure_ascii=False),encoding='utf-8')
def sample_names(rng,pool,count):
    for _ in range(100000):
        ns=rng.sample(pool,count)
        if b.distinct(ns): return ns
    raise RuntimeError('Could not sample distinct names')

def render(r):
    return ('\n'.join(f'All {a} are {c}.' for a,c in r['edges'])+
            f"\nPossible completions: {r['candidates'][0]} or {r['candidates'][1]}."+
            f"\nTherefore, all {r['query_source']} are")

def check(r):
    assert len(r['candidates'])==2 and len(set(r['candidates']))==2
    paths={x:b.path(r['edges'],[r['query_source'],x]) for x in r['candidates']}
    assert [x for x,p in paths.items() if p]==[r['gold']],(r,paths)
    assert paths[r['gold']]==r['proof']
    assert len(r['proof'])-1==r['hops']
    # Both options occur in facts, so presence alone cannot solve the question.
    names={x for e in r['edges'] for x in e}
    assert set(r['candidates'])<=names
    assert b.distinct(sorted(names))

def make_family(family):
    rng=random.Random(SEED+1009*family)
    a,bb,c,d,e,f,g,h=sample_names(rng,b.TEST_NAMES,8)
    base=[[a,bb],[bb,c],[e,d],[f,c]]
    rng.shuffle(base)
    reverse=[[c,bb],[bb,a],[e,d],[f,a]]
    rng.shuffle(reverse)
    rows=[]
    def add(check_name,variant,slot,edges,source,gold,foil,hops,base_id=None):
        candidates=[gold,foil]
        # Each specific variant/slot is exactly balanced across the 100 families.
        if (family+slot)%2: candidates.reverse()
        r=dict(id=f'{family:03d}/{check_name}/{variant}/{slot}',family=family,
               task='name_completion',check=check_name,variant=variant,slot=slot,
               edges=copy.deepcopy(edges),query_source=source,candidates=candidates,gold=gold,
               proof=b.path(edges,[source,gold]),hops=hops,paired_base_id=base_id,
               dataset_version='name_completion_v1',seed=SEED)
        check(r); rows.append(r)
        return r
    add('direct','base',0,base,a,bb,d,1)
    add('direct','base',1,base,bb,c,d,1)
    forwards=add('twohop','base',0,base,a,c,d,2)
    backwards=add('twohop','base',1,reverse,c,a,d,2)
    for slot,which in enumerate(('first','second')):
        edges=copy.deepcopy(base)
        old,new=([a,bb],[a,e]) if slot==0 else ([bb,c],[bb,d])
        edges[edges.index(old)]=new
        r=add('broken',which,slot,edges,a,d,c,2,forwards['id'])
        # Identical options/order and source; exactly one fact changes the answer.
        r['candidates']=list(forwards['candidates']); check(r)
    for variant in ('reorder','distractors','rename'):
        for slot,original in enumerate((forwards,backwards)):
            edges=copy.deepcopy(original['edges']); src=original['query_source']
            gold=original['gold']; foil=d
            mapping=None
            if variant=='reorder':
                while edges==original['edges']: rng.shuffle(edges)
            elif variant=='distractors':
                edges.extend([[g,h],[h,d]])
                rng.shuffle(edges)
            else:
                old=sorted({x for edge in edges for x in edge})
                new=sample_names(rng,[x for x in b.TEST_NAMES if x not in old],len(old))
                mapping=dict(zip(old,new))
                edges=[[mapping[x],mapping[y]] for x,y in edges]
                src=mapping[src]; gold=mapping[gold]; foil=mapping[d]
            r=add('robustness',variant,slot,edges,src,gold,foil,2,original['id'])
            if mapping: r['rename_mapping']=mapping
    assert len(rows)==12
    return rows

def make_demos(family,templates):
    rng=random.Random(SEED+7001*family)
    blocks=[b.DEMO_NAMES[i:i+6] for i in range(0,72,6)]
    rng.shuffle(blocks); extras=list(EXTRA_DEMO); demos=[]
    for i,r in enumerate(templates):
        old=sorted({x for edge in r['edges'] for x in edge})
        new=list(blocks[i]); rng.shuffle(new)
        while len(new)<len(old):
            possible=[x for x in extras if b.distinct(new+[x])]
            x=rng.choice(possible); extras.remove(x); new.append(x)
        mapping=dict(zip(old,new))
        d=dict(id=f'{family:03d}/demo/{i}',edges=[[mapping[x],mapping[y]] for x,y in r['edges']],
               query_source=mapping[r['query_source']],candidates=[mapping[x] for x in r['candidates']],
               gold=mapping[r['gold']],hops=r['hops'],kind=r['check'])
        d['proof']=b.path(d['edges'],[d['query_source'],d['gold']]); check(d); demos.append(d)
    # Four initial examples cover direct + two-hop, with each answer position twice.
    first=demos[:4]; rest=demos[4:]
    def mix(ds):
        ds=list(ds)
        while True:
            rng.shuffle(ds)
            positions=[d['candidates'].index(d['gold']) for d in ds]
            if any(a==c for a,c in zip(positions,positions[1:])): return ds
    first=mix(first); rest=mix(rest)
    # Explicitly balance answer position, even after the changed-answer controls.
    for ds in (first,rest):
        positions=[0]*(len(ds)//2)+[1]*(len(ds)//2)
        while True:
            rng.shuffle(positions)
            if any(x==y for x,y in zip(positions,positions[1:])): break
        for d,pos in zip(ds,positions):
            wrong=next(x for x in d['candidates'] if x!=d['gold'])
            d['candidates']=[d['gold'],wrong] if pos==0 else [wrong,d['gold']]
    return first+rest

def main():
    sys.path.insert(0,str(ROOT.parent/'tmp/tokenizer_audit_deps'))
    from tokenizers import Tokenizer
    tok=Tokenizer.from_file(str(ROOT/'tokenizer_source/tokenizer.json'))
    families={f:make_family(f) for f in range(100)}
    demo_bank={}
    for f in families:
        donor=(f+37)%100
        demo_bank[f]=make_demos(f,families[donor])
    report=dict(seed=SEED,task='name_completion',status='passed',conditions={},
                note='1200 shared questions in three shot conditions; not the old Yes/No test.',
                checks=dict(Counter(r['check'] for rs in families.values() for r in rs)))
    previews=['# השלמת שמות — דוגמאות קלט מלאות\n\nהמודל משלים שם מתוך שני מועמדים. רק אחד נובע מהעובדות; שם הביניים אינו מועמד במבחן שני הצעדים. שני המועמדים מופיעים בעובדות.\n']
    for shots in (0,4,12):
        rows=[]; lengths=[]; answer_lengths=[]
        for family,rs in families.items():
            demos=demo_bank[family][:shots]
            assert not shots or Counter(d['candidates'].index(d['gold']) for d in demos)=={0:shots//2,1:shots//2}
            prefix=INTRO+''.join(render(d)+' '+d['gold']+'.\n\n' for d in demos)
            for original in rs:
                r=copy.deepcopy(original)
                r.update(shots=shots,prompt=prefix+render(r),demo_ids=[d['id'] for d in demos])
                names={x for edge in r['edges'] for x in edge}
                r['entity_spans']=[dict(entity=name,start=m.start(),end=m.end()) for name in sorted(names)
                    for m in re.finditer(r'\b'+re.escape(name)+r'\b',r['prompt'])]
                enc=tok.encode(r['prompt'],add_special_tokens=False).ids
                for name in r['candidates']:
                    full=tok.encode(r['prompt']+' '+name+'.',add_special_tokens=False).ids
                    assert full[:len(enc)]==enc
                    answer_lengths.append(len(full)-len(enc))
                assert len(enc)+8<=2048
                lengths.append(len(enc)); rows.append(r)
        assert len(rows)==len({r['id'] for r in rows})==len({r['prompt'] for r in rows})==1200
        for check_name,variant,slot in {(r['check'],r['variant'],r['slot']) for r in rows}:
            subset=[r for r in rows if (r['check'],r['variant'],r['slot'])==(check_name,variant,slot)]
            assert Counter(r['candidates'].index(r['gold']) for r in subset)=={0:50,1:50}
        path=ROOT/f'data/completion_{shots}shot.jsonl'
        path.write_text(''.join(json.dumps(r)+'\n' for r in rows),encoding='utf-8')
        report['conditions'][shots]=dict(n=len(rows),token_range=[min(lengths),max(lengths)],
            answer_tokens_including_period=[min(answer_lengths),max(answer_lengths)],
            sha256=hashlib.sha256(path.read_bytes()).hexdigest())
        previews.append(f'## {shots} הדגמות — דוגמת שני צעדים\n\n```text\n'+rows[2]['prompt']+'\n```\n\nתשובת אמת: '+rows[2]['gold']+'\n')
    dump(ROOT/'data/completion_demonstrations.json',demo_bank)
    dump(ROOT/'data/completion_validation.json',report)
    (ROOT/'COMPLETION_EXAMPLES_HE.md').write_text('\n'.join(previews),encoding='utf-8')
    print(json.dumps(report,indent=2))

if __name__=='__main__': main()
