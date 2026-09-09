"""Audit repetition and tokenization; render prompts without repeating ICL prefixes."""
import collections
import itertools
import json
from pathlib import Path
import statistics
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT/'tmp/tokenizer_audit_deps'))
from tokenizers import Tokenizer
tok = Tokenizer.from_file(str(ROOT/'pilot_v2/tokenizer_source/tokenizer.json'))
OUT = ROOT/'results/full_sdpa_analysis'

def rows(path):
    return [json.loads(s) for s in path.read_text().splitlines()]

def canonical(row):
    names = sorted({x for edge in row['edges'] for x in edge}|set(row['query']))
    # Invariant under renaming, but preserves fact order and query direction.
    return min((tuple((p[names.index(a)],p[names.index(b)]) for a,b in row['edges']),
                tuple(p[names.index(x)] for x in row['query'])) for p in itertools.permutations(range(len(names))))

sets = {n:rows(ROOT/f'pilot_v2/data/pilot_{n}shot.jsonl') for n in (4,12)}
report = {}
for n,rs in sets.items():
    targets = [r['prompt'].rsplit('\n\n',1)[1] for r in rs]
    c=collections.Counter(targets)
    report[n] = dict(rows=len(rs),unique_prompts=len({r['prompt'] for r in rs}),
        unique_targets=len(c),extra_duplicate_targets=sum(v-1 for v in c.values()),
        duplicate_groups=[dict(target=k,count=v) for k,v in c.items() if v>1],
        unique_prefixes=len({r['prompt'].rsplit('\n\n',1)[0] for r in rs}),
        groups=dict(collections.Counter((r['check']+'/'+r['variant']) for r in rs)),
        family_count=len({r['family'] for r in rs}))
old=rows(ROOT/'results/full_4shot_review/data/pilot_4shot.jsonl')
report['old_new'] = dict(old_unique_prompts=len({r['prompt'] for r in old}),
    aligned_ids=[r['id'] for r in old]==[r['id'] for r in sets[4]],
    same_graphs_up_to_renaming=all(canonical(a)==canonical(b) for a,b in zip(old,sets[4])),
    same_gold=all(a['gold']==b['gold'] for a,b in zip(old,sets[4])))
namesets = {'old_test':sorted({x for r in old for edge in r['edges'] for x in edge}),
            'new_test':sorted({x for r in sets[4] for edge in r['edges'] for x in edge})}
for name,names in namesets.items():
    splits={x:tok.encode(' '+x,add_special_tokens=False).tokens for x in names}
    report[name]=dict(count=len(names),min_tokens=min(map(len,splits.values())),
        max_tokens=max(map(len,splits.values())),mean_tokens=statistics.mean(map(len,splits.values())),
        examples=dict(list(splits.items())[:6]))
report['selected_tokens']={x:tok.encode(' '+x,add_special_tokens=False).tokens for x in ['group000a','group000e','wugs','daxes','tufas','kelbrins','bantrels','cats','dogs','B','C']}
report['shared_targets_across_shots']=len({r['prompt'].rsplit('\n\n',1)[1] for r in sets[4]} & {r['prompt'].rsplit('\n\n',1)[1] for r in sets[12]})
(OUT/'prompt_design_audit.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8')
prefix=sets[12][0]['prompt'].rsplit('\n\n',1)[0]
(OUT/'ICL_ONLY_HE.md').write_text('# ההדגמות שניתנו למודל\n\nב־12-shot זהו החלק הקבוע שהופיע לפני כל שאלה. ב־4-shot ניתנו ההוראה וארבע ההדגמות הראשונות בלבד. אין צבירת היסטוריה בין השאלות.\n\n```text\n'+prefix+'\n```\n',encoding='utf-8')
res={n:{r['id']:r for r in rows(ROOT/f'results/full_sdpa_review/full_sdpa_{n}shot_v1/results.jsonl')} for n in (4,12)}
blocks=['# שאלות המבחן בלבד — ללא חזרה על ההדגמות\n\nכל שאלה מוצגת פעם אחת, עם התשובות משתי ההרצות. 100 משפחות, 12 בדיקות בכל משפחה. בביקורת נמצאו 1,200 שאלות שונות ללא כפילויות טקסטואליות בתוך כל הרצה.\n']
for r in sets[4]:
    a,b=res[4][r['id']],res[12][r['id']]
    blocks.append(f"## {r['id']}\n\nאמת: **{r['gold']}**; 4-shot: **{a['free_label']}**; 12-shot: **{b['free_label']}**.\n\n```text\n{r['prompt'].rsplit(chr(10)+chr(10),1)[1]}\n```\n")
(OUT/'TEST_ONLY_HE.md').write_text('\n'.join(blocks),encoding='utf-8')
print(json.dumps(report,indent=2,ensure_ascii=True))
