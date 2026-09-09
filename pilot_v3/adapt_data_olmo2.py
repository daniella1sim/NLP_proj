#!/usr/bin/env python3
"""Adapt the v3.1 name-completion data to OLMo-2 with MINIMAL, consistent renames.

Problem: v3.1 candidate pairs are token-length matched under the Pythia
tokenizer. Under OLMo-2's tokenizer (dolma2) ~40% of pairs break, which would
bias the summed-log-prob comparison. Fix: for every family whose candidate
pair(s) mismatch, rename the MINIMUM number of entities so that every pair is
length-matched under BOTH tokenizers. Everything else — question structure,
fact layout, demo blocks, ids, seeds — is byte-identical to v3.1.

Per family we build the graph of unordered candidate pairs, anchor each
connected component on the gold of the twohop/base question (falling back to
the first row's gold), and rename every other node whose (' '+name) token
signature (len under Pythia, len under OLMo-2) differs from the anchor's.
Replacement names come from the same world's name grammar, must carry the
anchor's exact signature under both tokenizers, and must not occur anywhere in
any prompt of any file (word-boundary check), so demo blocks and distractor
chains are untouched by construction.

Outputs data_olmo2/completion_v3_olmo2_{0,4,12}shot.jsonl and
controls_v3_olmo2_4shot.jsonl with dataset_version 'name_completion_v3_1_olmo2'
and a matched_tokenizers field, plus adapt_audit_olmo2.json documenting every
rename. Run audit_tokenizer.py (both tokenizers) and verify_logic.py on the
outputs afterwards; this script also re-checks mention balance itself.
"""
import collections, json, random, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'data_olmo2'; OUT.mkdir(exist_ok=True)
SEED = 20260909
rng = random.Random(SEED)

from tokenizers import Tokenizer
PYTHIA = Tokenizer.from_file(str(HERE.parent / 'pilot_v2' / 'tokenizer_source' / 'tokenizer.json'))
OLMO = Tokenizer.from_file(str(HERE / 'olmo2_tokenizer' / 'tokenizer.json'))
def sig(name):
    return (len(PYTHIA.encode(' ' + name, add_special_tokens=False).ids),
            len(OLMO.encode(' ' + name, add_special_tokens=False).ids))

FILES = {
    'completion_v3_0shot.jsonl':  'completion_v3_olmo2_0shot.jsonl',
    'completion_v3_4shot.jsonl':  'completion_v3_olmo2_4shot.jsonl',
    'completion_v3_12shot.jsonl': 'completion_v3_olmo2_12shot.jsonl',
    'controls_v3_4shot.jsonl':    'controls_v3_olmo2_4shot.jsonl',
}
DATA = {src: [json.loads(l) for l in (HERE / 'data' / src).open(encoding='utf-8')]
        for src in FILES}
CORPUS = '\n'.join(r['prompt'] for rows in DATA.values() for r in rows)

# ---------- name grammars (copied verbatim from build_data_v3.py) ----------
def kinship_names():
    onsets = list('BDFGHJKLMNPRSTVWZ')
    v1 = ['a','e','i','o','u']
    mids = ['ln','rn','ld','rl','st','nd','lm','rv','lt','sm','rd','nt']
    ends = ['a','ia','na','la','ra']
    combos = [(o,a,m,e) for o in onsets for a in v1 for m in mids for e in ends]
    rng.shuffle(combos)
    for o,a,m,e in combos: yield o + a + m + e
def containment_names():
    onsets = ['bl','br','cr','dr','fl','gl','gr','kl','kr','pl','pr','sk','sl','sm','sn','sp','st','tr','vr','zl']
    v = ['a','e','i','o','u']
    codas = ['mp','nd','nk','rt','lk','rm','sp','ft','lp','rk']
    combos = [(o,a,c) for o in onsets for a in v for c in codas]
    rng.shuffle(combos)
    for o,a,c in combos: yield o + a + c + 's'
def location_names():
    onsets = list('bdfgjklmnprstvz')
    v = ['a','e','i','o','u']
    mids = ['rv','st','ld','nt','rp','lg','sk','nd','rm','lt']
    ends = ['el','in','ot','ar','ul']
    combos = [(o,a,m,e) for o in onsets for a in v for m in mids for e in ends]
    rng.shuffle(combos)
    for o,a,m,e in combos: yield o + a + m + e
GRAMMARS = {'kinship': kinship_names, 'containment': containment_names, 'location': location_names}

used = set()
def fresh_name(world, want_sig):
    for cand in GRAMMARS[world]():
        if cand in used or sig(cand) != want_sig: continue
        if cand in CORPUS and re.search(r'(?<![A-Za-z])' + re.escape(cand) + r'(?![A-Za-z])', CORPUS):
            continue
        used.add(cand)
        return cand
    raise RuntimeError(f'no fresh {world} name with signature {want_sig}')

# ---------- decide renames ----------
pairs = {}   # (family) -> {frozenset(pair): anchor_gold_of_twohop_or_None}
fam_world, anchor_of = {}, {}
def is_verbatim_control(r):
    # verbatim controls use DEMO names as candidates (literal-copy calibration);
    # demo names must never be renamed, so these pairs stay unmatched and are
    # marked length_matched=False for the audit and the analysis to exclude.
    return r['check'] == 'control' and r['variant'] == 'verbatim'

for rows in DATA.values():
    for r in rows:
        if is_verbatim_control(r): continue
        gold = r['gold']; other = [c for c in r['candidates'] if c != gold][0]
        fam_world[r['family']] = r['world']
        pairs.setdefault(r['family'], set()).add(frozenset((gold, other)))
        if r['check'] == 'twohop' and r['variant'] == 'base':
            anchor_of[r['family']] = r['gold']

rename = {}   # old name -> new name
renames_log = []
for fam, fam_pairs in sorted(pairs.items()):
    world = fam_world[fam]
    # connected components over the pair graph
    adj = collections.defaultdict(set)
    for p in fam_pairs:
        a, b = tuple(p)
        adj[a].add(b); adj[b].add(a)
    seen = set()
    for start in sorted(adj):
        if start in seen: continue
        comp, stack = set(), [start]
        while stack:
            n = stack.pop()
            if n in comp: continue
            comp.add(n); stack.extend(adj[n] - comp)
        seen |= comp
        if len({sig(n) for n in comp}) == 1:
            continue  # already consistent under both tokenizers
        anchor = anchor_of.get(fam) if anchor_of.get(fam) in comp else sorted(comp)[0]
        target = sig(anchor)
        for n in sorted(comp):
            if n == anchor or sig(n) == target: continue
            new = fresh_name(world, target)
            rename[n] = new
            renames_log.append(dict(family=fam, world=world, old=n, new=new,
                                    old_sig=list(sig(n)), target_sig=list(target), anchor=anchor))

print(f'{len(rename)} entities renamed across {len({r["family"] for r in renames_log})} families')

# guard: renamed names must not appear inside any demo block (demo pools are disjoint by design)
demos = json.load((HERE / 'data' / 'demonstrations_v3.json').open())
demo_text = '\n'.join(t for w in demos['demos'].values() for t in w)
for old in rename:
    assert not re.search(r'(?<![A-Za-z])' + re.escape(old) + r'(?![A-Za-z])', demo_text), \
        f'{old} leaks into demo text'

# ---------- apply ----------
def apply_text(text):
    def sub_one(t, old, new):
        return re.sub(r'(?<![A-Za-z])' + re.escape(old) + r'(?![A-Za-z])', new, t)
    for old, new in rename.items():
        t2 = sub_one(text, old, new)
        text = t2
    return text

def spans(prompt, names):
    out = []
    for n in set(names):
        for m in re.finditer(r'(?<![A-Za-z])' + re.escape(n) + r'(?![A-Za-z])', prompt):
            out.append(dict(entity=n, start=m.start(), end=m.end()))
    return sorted(out, key=lambda s: s['start'])

def mention_balance_ok(row):
    # count gold vs distractor inside the fact lines of the TEST block only
    test_block = row['prompt'].split('\n\n')[-1]
    lines = [l for l in test_block.split('\n')
             if not l.startswith(('Question:', 'Answer:', 'Therefore,'))]
    ftext = '\n'.join(lines)
    gold = row['gold']; other = [c for c in row['candidates'] if c != gold][0]
    c = lambda n: len(re.findall(r'(?<![A-Za-z])' + re.escape(n) + r'(?![A-Za-z])', ftext))
    return c(gold) == c(other)

balance_problems, changed_rows = [], 0
for src, dst in FILES.items():
    out_rows = []
    for r in DATA[src]:
        r = dict(r)
        touched = any(re.search(r'(?<![A-Za-z])' + re.escape(o) + r'(?![A-Za-z])', r['prompt'])
                      for o in rename)
        if touched:
            changed_rows += 1
            r['prompt'] = apply_text(r['prompt'])
            r['gold'] = rename.get(r['gold'], r['gold'])
            r['candidates'] = [rename.get(c, c) for c in r['candidates']]
            if r.get('bridge'): r['bridge'] = rename.get(r['bridge'], r['bridge'])
            names = list(r['candidates']) + ([r['bridge']] if r.get('bridge') else [])
            r['entity_spans'] = spans(r['prompt'], names) if r['entity_spans'] else []
        r['dataset_version'] = 'name_completion_v3_1_olmo2'
        r['matched_tokenizers'] = ['EleutherAI/pythia-6.9b', 'allenai/OLMo-2-1124-7B']
        r['adapted_from'] = 'name_completion_v3_1'
        r['length_matched'] = not is_verbatim_control(r)
        if r['check'] != 'control' and not mention_balance_ok(r):
            balance_problems.append(r['id'])
        out_rows.append(r)
    with (OUT / dst).open('w', encoding='utf-8') as f:
        for r in out_rows: f.write(json.dumps(r) + '\n')
    print(f'{dst}: {len(out_rows)} rows')

assert not balance_problems, f'mention balance broken: {balance_problems[:5]}'
json.dump(dict(seed=SEED, renamed_entities=len(rename), changed_rows=changed_rows,
               renames=renames_log),
          (OUT / 'adapt_audit_olmo2.json').open('w'), indent=1)
print(f'{changed_rows} rows touched; mention balance verified on all non-control rows.')
