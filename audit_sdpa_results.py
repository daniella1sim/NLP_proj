"""Read-only audit of the archived SDPA pilot; writes derived JSON/Markdown."""
from pathlib import Path
import collections
import hashlib
import json
import math
import re
import statistics

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'results/full_sdpa_analysis'
OUT.mkdir(exist_ok=True)

def read(path):
    return [json.loads(s) for s in path.read_text(encoding='utf-8').splitlines()]

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def reachable(edges, query):
    seen = {query[0]}
    while True:
        more = seen | {b for a,b in edges if a in seen}
        if more == seen:
            return query[1] in seen
        seen = more

audits = {}
examples = ['# קלטים ותשובות בפועל — Pythia 6.9B\n',
            'בכל דוגמה מוצג תחילה החלק האחרון של הקלט. ההדגמות המלאות זמינות תחת הפרטים.\n']
all_examples = ['# כל 2,400 הקלטים והתשובות\n']
for shots in (4,12):
    folder = ROOT / f'results/full_sdpa_review/full_sdpa_{shots}shot_v1'
    rows = read(folder / 'results.jsonl')
    data = ROOT / f'pilot_v2/data/pilot_{shots}shot.jsonl'
    source = {r['id']:r for r in read(data)}
    worker = next((folder / 'workers').iterdir())
    manifest = json.loads((worker / 'manifest.json').read_text())
    session = json.loads(next(worker.glob('session_*.json')).read_text())
    issues = []
    if len(rows) != 1200 or len({r['id'] for r in rows}) != 1200:
        issues.append('Wrong row count or duplicate IDs')
    if {r['id'] for r in rows} != set(source): issues.append('ID coverage mismatch')
    if manifest['data_sha256'] != sha(data): issues.append('Dataset hash mismatch')
    if manifest['code_sha256'] != sha(ROOT / 'pilot_v2/pilot.py'): issues.append('Runner hash mismatch')
    if rows != read(worker / 'results.jsonl'): issues.append('Worker/merged mismatch')
    for r in rows:
        expected = source.get(r['id'], {})
        if any(r.get(k) != v for k,v in expected.items()): issues.append('Input mismatch: '+r['id'])
        if r['gold'] != ('Yes' if reachable(r['edges'], r['query']) else 'No'):
            issues.append('Logical label mismatch: '+r['id'])
        values = [r['yes_minus_no'], *r['candidate_logprobs'].values(), *r['first_answer_logits'].values()]
        if not all(math.isfinite(v) for v in values): issues.append('Nonfinite saved score: '+r['id'])
        margin = r['candidate_logprobs']['Yes'] - r['candidate_logprobs']['No']
        pred = 'Yes' if margin > 0 else 'No' if margin < 0 else 'Tie'
        match = re.match(r'^\s*(Yes|No)\b',r['generated'])
        free = match.group(1) if match else None
        if pred != r['predicted'] or free != r['free_label'] or (pred == r['gold']) != r['correct'] or (free == r['gold']) != r['free_correct']:
            issues.append('Scoring mismatch: '+r['id'])
        if not math.isclose(margin,r['yes_minus_no'],abs_tol=1e-7): issues.append('Margin mismatch')
        first_token = r['generated_token_ids'][0]
        if free and first_token != r['answer_token_ids'][free]: issues.append('First token mismatch')
        if len(r['token_ids']) + 8 > 2048: issues.append('Context overflow')
    groups = collections.defaultdict(list)
    for r in rows: groups[f"{r['check']}/{r['variant']}"] .append(r)
    metrics = {}
    for group, rs in groups.items():
        pos = [r['yes_minus_no'] for r in rs if r['gold']=='Yes']
        neg = [r['yes_minus_no'] for r in rs if r['gold']=='No']
        auc = sum((p>n)+0.5*(p==n) for p in pos for n in neg)/(len(pos)*len(neg)) if pos and neg else None
        fams = collections.defaultdict(dict)
        for r in rs: fams[r['family']][r['gold']] = r
        pairs = [v['Yes']['yes_minus_no']-v['No']['yes_minus_no'] for v in fams.values() if len(v)==2]
        metrics[group] = dict(n=len(rs),candidate_accuracy=sum(r['correct'] for r in rs)/len(rs),
            free_accuracy=sum(r['free_correct'] for r in rs)/len(rs),auc=auc,
            positive_mean=statistics.mean(pos) if pos else None,negative_mean=statistics.mean(neg) if neg else None,
            paired_positive_higher=sum(x>0 for x in pairs)/len(pairs) if pairs else None)
    audit = dict(issues=issues,rows=len(rows),manifest=manifest,
        predictions=dict(collections.Counter(r['predicted'] for r in rows)),
        free_predictions=dict(collections.Counter(r['free_label'] for r in rows)),
        gold=dict(collections.Counter(r['gold'] for r in rows)),
        candidate_correct=sum(r['correct'] for r in rows),free_correct=sum(r['free_correct'] for r in rows),
        token_range=[min(len(r['token_ids']) for r in rows),max(len(r['token_ids']) for r in rows)],
        elapsed_minutes=session['elapsed_seconds']/60,peak_gpu_gib=session['peak_allocated_gpu_gib'],
        generated_counts=collections.Counter(r['generated'] for r in rows).most_common(8),metrics=metrics)
    audits[shots] = audit
    selected = [r for r in rows if r['family']==0 and r['check'] in ('direct','twohop','broken')]
    selected += [r for r in rows if r['variant']=='distractors' and r['predicted']=='Yes'][:2]
    selected += [r for r in rows if r['predicted']=='Tie'][:2]
    for r in rows:
        block = (f"\n## {shots} הדגמות — {r['id']}\n\n"
                 f"תשובת אמת: **{r['gold']}**; בחירה: **{r['predicted']}**; פער Yes−No: {r['yes_minus_no']:.6f}\n\n"
                 f"```text\n{r['prompt'].split(chr(10)+chr(10))[-1]}\n```\n\n"
                 f"המשך הטקסט שנוצר בפועל:\n\n```text\n{r['generated']}\n```\n\n"
                 f"<details><summary>הקלט המלא, כולל ההדגמות</summary>\n\n```text\n{r['prompt']}\n```\n\n</details>\n")
        all_examples.append(block)
        if r in selected: examples.append(block)
(OUT/'audit.json').write_text(json.dumps(audits,indent=2,ensure_ascii=False),encoding='utf-8')
(OUT/'examples_HE.md').write_text('\n'.join(examples),encoding='utf-8')
(OUT/'all_examples_HE.md').write_text('\n'.join(all_examples),encoding='utf-8')
print(json.dumps(audits,indent=2,ensure_ascii=False))
