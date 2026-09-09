"""Verify new dataset invariants and actual Pythia tokenizer behavior."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'tmp/tokenizer_audit_deps'))
from tokenizers import Tokenizer
import build_data as b

tok = Tokenizer.from_file(str(ROOT/'tokenizer_source/tokenizer.json'))
cfg = json.loads((ROOT/'tokenizer_source/config.json').read_text())
sets = {shots:[json.loads(l) for l in (ROOT/f'data/pilot_{shots}shot.jsonl').read_text().splitlines()]
        for shots in (4,12)}
demos = b.demonstrations()
assert not set(b.TEST_NAMES) & set(b.DEMO_NAMES)
assert len({d['gold'] for d in demos})==2
assert Counter(d['gold'] for d in demos[:4]) == {'Yes':2,'No':2}
assert Counter(d['gold'] for d in demos) == {'Yes':6,'No':6}
for r4,r12 in zip(sets[4],sets[12]):
    for key in set(r4)-{'shots','prompt','entity_spans','demo_ids'}:
        assert r4[key]==r12[key],key
    assert r12['demo_ids'][:4]==r4['demo_ids']
report = {}
for shots,rows in sets.items():
    assert len(rows)==len({r['id'] for r in rows})==1200
    lengths=[]; tie_labels=[]
    for row in rows:
        assert row['prompt'].count('Question:')==shots+1
        assert row['prompt'].endswith('Answer:')
        assert row['proof']==b.path(row['edges'],row['query'])
        assert row['gold']==('Yes' if row['proof'] else 'No')
        if row['proof']: assert len(row['proof'])-1==row['hops']
        names={x for edge in row['edges'] for x in edge}|set(row['query'])
        assert b.distinct(sorted(names))
        assert all(x.isalpha() and x.islower() for x in names)
        encoded=tok.encode(row['prompt'],add_special_tokens=False)
        lengths.append(len(encoded.ids))
        for label in (' Yes',' No'):
            full=tok.encode(row['prompt']+label,add_special_tokens=False).ids
            assert full[:len(encoded.ids)]==encoded.ids
            assert len(full)==len(encoded.ids)+1
        assert len(encoded.ids)+8<=cfg['max_position_embeddings']
        for s in row['entity_spans']:
            assert row['prompt'][s['start']:s['end']]==s['entity']
    report[str(shots)] = dict(rows=len(rows),counts=dict(Counter(r['check'] for r in rows)),
                             token_length_min=min(lengths), token_length_max=max(lengths),
                             data_sha256=hashlib.sha256((ROOT/f'data/pilot_{shots}shot.jsonl').read_bytes()).hexdigest())
name_tokens={name:tok.encode(' '+name,add_special_tokens=False).tokens for name in b.TEST_NAMES}
assert len({tuple(tok.encode(' '+name,add_special_tokens=False).ids) for name in b.TEST_NAMES})==len(b.TEST_NAMES)
report.update(status='passed',context_limit=cfg['max_position_embeddings'],name_tokens=name_tokens,
              answer_tokens={s:tok.encode(s,add_special_tokens=False).ids for s in (' Yes',' No')},
              no_model_inference_performed=True)
(ROOT/'data_validation.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='name_tokens'},indent=2))
