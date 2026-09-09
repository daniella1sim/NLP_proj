"""Offline audit of the received run; never modifies archived evidence."""
from collections import Counter, defaultdict, deque
import hashlib
import json
from pathlib import Path
import statistics

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'results/full_4shot_review'
RUN = SOURCE / 'storage/runs/full_4shot'
OUT = ROOT / 'results/full_4shot_analysis'
OUT.mkdir(exist_ok=True)
rows = [json.loads(s) for s in (RUN/'results.jsonl').read_text().splitlines()]
manifest = json.loads((RUN/'manifest.json').read_text())
assert hashlib.sha256((SOURCE/'pilot.py').read_bytes()).hexdigest() == manifest['code_sha256']
assert hashlib.sha256((SOURCE/'data/pilot_4shot.jsonl').read_bytes()).hexdigest() == manifest['data_sha256']
assert len(rows) == len({r['id'] for r in rows}) == 1200
data = {r['id']:r for r in map(json.loads,(SOURCE/'data/pilot_4shot.jsonl').read_text().splitlines())}
for r in rows:
    assert all(r[k] == v for k,v in data[r['id']].items())
    seen = {r['query'][0]}
    queue = deque(seen)
    while queue:
        node = queue.popleft()
        for a,b in r['edges']:
            if a==node and b not in seen:
                seen.add(b); queue.append(b)
    assert r['gold'] == ('Yes' if r['query'][1] in seen else 'No')
    assert r['correct'] == (r['predicted']==r['gold'])
    assert r['free_correct'] == (r['free_label']==r['gold'])
    assert r['yes_minus_no'] == r['candidate_logprobs']['Yes']-r['candidate_logprobs']['No']

groups = defaultdict(list)
for r in rows: groups[r['check']+'/'+r['variant']].append(r)
stats = {}
for group, rr in groups.items():
    non_ties = [r for r in rr if r['predicted']!='Tie']
    stats[group] = dict(n=len(rr), predictions=dict(Counter(r['predicted'] for r in rr)),
        free_predictions=dict(Counter(r['free_label'] for r in rr)),
        candidate_accuracy=statistics.mean(r['correct'] for r in rr),
        free_accuracy=statistics.mean(r['free_correct'] for r in rr),
        non_tie_disagreements=sum(r['predicted']!=r['free_label'] for r in non_ties),
        tie_free_correct=sum(r['predicted']=='Tie' and r['free_correct'] for r in rr))
families = defaultdict(dict)
for r in rows: families[r['family']][(r['check'],r['variant'],r['polarity'])] = r
paired = {}
for variant in ('first','second'):
    pairs = [(f['twohop','base','positive'], f['broken',variant,'negative']) for f in families.values()]
    paired[variant] = dict(free_both_correct=sum(a['free_correct'] and b['free_correct'] for a,b in pairs),
                          candidate_both_correct=sum(a['correct'] and b['correct'] for a,b in pairs),
                          mean_margin_change=statistics.mean(b['yes_minus_no']-a['yes_minus_no'] for a,b in pairs))
report = dict(integrity='1200 unique rows; hashes, data matching, gold reachability and scoring fields verified',
              groups=stats, paired=paired,
              prompt_token_length=[min(len(r['token_ids']) for r in rows),max(len(r['token_ids']) for r in rows)],
              entity_token_counts=dict(Counter(len(a['token_indices']) for r in rows for a in r['token_anchors'])),
              non_tie_disagreements=sum(r['predicted']!='Tie' and r['predicted']!=r['free_label'] for r in rows),
              ties=sum(r['predicted']=='Tie' for r in rows))
(OUT/'audit.json').write_text(json.dumps(report,indent=2),encoding='utf-8')

# A readable export of every prompt and actual completion, organized by family.
lines = ['# Pythia-1B — inputs and actual outputs',
         'Source: full_4shot. All 1,200 examples; search an ID such as 000/direct/base/negative.',
         '`generated` is the actual greedy completion. `predicted` is the candidate score decision; Tie is not a model utterance.\n']
for r in rows:
    lines += [f"## {r['id']}", f"Gold: **{r['gold']}** | Candidate decision: **{r['predicted']}** | Generated label: **{r['free_label']}**",
              f"Yes−No log-probability: {r['yes_minus_no']}",
              'Input (including the four demonstrations):', '```text', r['prompt'], '```',
              'Actual generated continuation:', '```text', r['generated'], '```',
              'Candidate log-probabilities: '+json.dumps(r['candidate_logprobs']), '']
(OUT/'all_examples.md').write_text('\n\n'.join(lines),encoding='utf-8')
print(json.dumps(report,indent=2))
for r in rows[:6]:
    print(json.dumps({k:r[k] for k in ['id','gold','predicted','generated','yes_minus_no']},ensure_ascii=False))
