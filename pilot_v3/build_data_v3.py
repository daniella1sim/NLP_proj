#!/usr/bin/env python3
"""v3 name-completion dataset: natural-language multi-hop with a NAMED composed relation.

Design (agreed 2026-09-11):
- Anchor world: kinship (mother -> grandmother), families 000-067. The composed
  relation has its own name, so the bridge entity is NEVER a valid answer.
- Breadth worlds: containment ("All X are Y", families 068-083) and location
  ("inside", families 084-099). There the 2-hop bridge is logically true but is
  excluded from the candidate pair; free-generation bridge answers are a tracked
  error category, not noise.
- No instruction preamble. No "Possible answers" line. Candidate scoring happens
  outside the prompt, so there is no position bias and no mention-count pollution.
- Mention balance: within every test block, gold and distractor appear the SAME
  number of times in the facts. A frequency rule scores exactly 50%.
- Candidate pairs are token-length matched (' '+name under the Pythia tokenizer).
- Demo names are globally disjoint from test names; demos never answer a query
  that appears in the test block.
- 600 questions x 2 fact-order variants (order0: query family first; order1:
  distractor family first; for 'reorder' two different shuffles) = 1200 rows
  per shot condition (0/4/12). Controls live in separate files.
"""
import json, random, re, collections
from pathlib import Path

SEED = 20260911
HERE = Path(__file__).resolve().parent
OUT = HERE / 'data'; OUT.mkdir(exist_ok=True)
rng = random.Random(SEED)

from tokenizers import Tokenizer
TOK = Tokenizer.from_file(str(HERE.parent / 'pilot_v2' / 'tokenizer_source' / 'tokenizer.json'))
def ntok(name):
    return len(TOK.encode(' ' + name, add_special_tokens=False).ids)

# ---------- name pools ----------
def make_pool(builder, need):
    seen, buckets = set(), collections.defaultdict(list)
    for name in builder():
        if name in seen: continue
        seen.add(name)
        buckets[ntok(name)].append(name)
    for k in buckets: rng.shuffle(buckets[k])
    total = sum(len(v) for v in buckets.values())
    assert total >= need, f'pool too small: {total} < {need}'
    return buckets

def kinship_names():
    onsets = list('BDFGHJKLMNPRSTVWZ')
    v1 = ['a','e','i','o','u']
    mids = ['ln','rn','ld','rl','st','nd','lm','rv','lt','sm','rd','nt']
    ends = ['a','ia','na','la','ra']
    combos = [(o,a,m,e) for o in onsets for a in v1 for m in mids for e in ends]
    rng.shuffle(combos)
    for o,a,m,e in combos:
        yield o + a + m + e
def containment_names():
    onsets = ['bl','br','cr','dr','fl','gl','gr','kl','kr','pl','pr','sk','sl','sm','sn','sp','st','tr','vr','zl']
    v = ['a','e','i','o','u']
    codas = ['mp','nd','nk','rt','lk','rm','sp','ft','lp','rk']
    combos = [(o,a,c) for o in onsets for a in v for c in codas]
    rng.shuffle(combos)
    for o,a,c in combos:
        yield o + a + c + 's'
def location_names():
    onsets = list('bdfgjklmnprstvz')
    v = ['a','e','i','o','u']
    mids = ['rv','st','ld','nt','rp','lg','sk','nd','rm','lt']
    ends = ['el','in','ot','ar','ul']
    combos = [(o,a,m,e) for o in onsets for a in v for m in mids for e in ends]
    rng.shuffle(combos)
    for o,a,m,e in combos:
        yield o + a + m + e

POOLS = {'kinship': make_pool(kinship_names, 900),
         'containment': make_pool(containment_names, 400),
         'location': make_pool(location_names, 400)}

def draw(world, n, bucket=None):
    b = POOLS[world]
    if bucket is None:
        bucket = max(b, key=lambda k: len(b[k]))
    assert len(b[bucket]) >= n, f'{world} bucket {bucket} exhausted'
    out = [b[bucket].pop() for _ in range(n)]
    return out, bucket

# ---------- world grammars ----------
def kin_fact(parent, child):   return f'{parent} is the mother of {child}.'
def con_fact(sub, sup):        return f'All {sub} are {sup}.'
def loc_fact(inner, outer):    return f'The {inner} is inside the {outer}.'

WORLDS = {
 'kinship': dict(fact=kin_fact,
    q1=lambda fam: f'Question: Who is the mother of {fam["qm"]}?',
    q2=lambda fam: f'Question: Who is the grandmother of {fam["qc"]}?',
    answer_line=True),
 'containment': dict(fact=con_fact,
    q1=lambda fam: f'Therefore, all {fam["qm"]} are',
    q2=lambda fam: f'Therefore, all {fam["qc"]} are',
    answer_line=False),
 'location': dict(fact=loc_fact,
    q1=lambda fam: f'Question: Where is the {fam["qm"]}?',
    q2=lambda fam: f'Question: Where is the {fam["qc"]}?',
    answer_line=True),
}

def new_family(world):
    # query chain qc -> qm -> qg ; distractor chain dc -> dm -> dg ; fx spare (same bucket as qg/dg)
    (qg, dg, fx), bucket = draw(world, 3)
    (qc, qm, dc, dm), _ = draw(world, 4, bucket=None)
    return dict(qc=qc, qm=qm, qg=qg, dc=dc, dm=dm, dg=dg, fx=fx, bucket=bucket)

def edge(world, low, high):
    # 'high' is the answer-side entity (mother / superset / outer container)
    F = WORLDS[world]['fact']
    return F(high, low) if world == 'kinship' else F(low, high)

def facts_of(world, fam, order):
    q = [edge(world, fam['qc'], fam['qm']), edge(world, fam['qm'], fam['qg'])]
    d = [edge(world, fam['dc'], fam['dm']), edge(world, fam['dm'], fam['dg'])]
    return q + d if order == 0 else d + q

def block(world, fam, facts, hops, answer=None):
    q = WORLDS[world]['q2'](fam) if hops == 2 else WORLDS[world]['q1'](fam)
    lines = facts + [q]
    if WORLDS[world]['answer_line']:
        lines.append('Answer:' + (f' {answer}.' if answer else ''))
        return '\n'.join(lines) if answer else '\n'.join(lines)
    else:
        if answer: lines[-1] = lines[-1] + f' {answer}.'
        return '\n'.join(lines)

# ---------- demonstrations ----------
DEMOS = {}
for world in WORLDS:
    demos = []
    for i in range(14):
        fam = new_family(world)
        hops = 1 if i % 2 == 0 else 2
        order = i % 2
        answer = fam['qg']  # both q1 (mother of qm) and q2 (grandmother of qc) resolve to qg
        demos.append(dict(id=f'{world}/demo/{i}', world=world, hops=hops,
                          text=block(world, fam, facts_of(world, fam, order), hops, answer=answer),
                          names=[fam[k] for k in ('qc','qm','qg','dc','dm','dg')]))
    DEMOS[world] = demos

def demo_ids_for(world, qseed, shots):
    r = random.Random(qseed)
    demos = DEMOS[world]
    ones = [d for d in demos if d['hops'] == 1]; twos = [d for d in demos if d['hops'] == 2]
    take = r.sample(ones, shots // 2) + r.sample(twos, shots // 2)
    r.shuffle(take)
    return take

# ---------- questions ----------
def spans(prompt, names):
    out = []
    for n in set(names):
        for m in re.finditer(r'(?<![A-Za-z])' + re.escape(n) + r'(?![A-Za-z])', prompt):
            out.append(dict(entity=n, start=m.start(), end=m.end()))
    return sorted(out, key=lambda s: s['start'])

def questions_for_family(world, fidx):
    fam = new_family(world)
    qs = []
    def add(check, variant, hops, gold, distractor, factfn, famv=None, bridge=None):
        qs.append(dict(check=check, variant=variant, hops=hops, gold=gold,
                       distractor=distractor, factfn=factfn, fam=famv or fam, bridge=bridge))
    # 1) direct: gold appears once, distractor grandmother once
    add('direct','base',1, fam['qg'], fam['dg'], lambda o,f=fam: facts_of(world,f,o))
    # 2) twohop
    add('twohop','base',2, fam['qg'], fam['dg'], lambda o,f=fam: facts_of(world,f,o), bridge=fam['qm'])
    # 3) broken (alternate)
    if fidx % 2 == 0:
        def bf(o, f=fam):
            fx = facts_of(world, f, o)
            i = fx.index(edge(world, f['qc'], f['qm'])); fx[i] = edge(world, f['qc'], f['dm'])
            return fx
        add('broken','first',2, fam['dg'], fam['qg'], bf, bridge=fam['dm'])
    else:
        def bs(o, f=fam):
            fx = facts_of(world, f, o)
            i = fx.index(edge(world, f['qm'], f['qg'])); fx[i] = edge(world, f['qm'], f['fx'])
            return fx
        add('broken','second',2, fam['fx'], fam['dg'], bs, bridge=fam['qm'])
    # 4) reorder: two different shuffles as the order pair
    def ro(o, f=fam, fi=fidx):
        fx = facts_of(world, f, 0)
        random.Random(1000*fi + o).shuffle(fx)
        return fx
    add('robustness','reorder',2, fam['qg'], fam['dg'], ro, bridge=fam['qm'])
    # 5) distractors: third chain added (does not mention candidates)
    (tg,), tb = draw(world, 1)
    (tc, tm), _ = draw(world, 2)
    tfam = dict(qc=tc, qm=tm, qg=tg)
    def dist(o, f=fam, t=tfam):
        extra = [edge(world, t['qc'], t['qm']), edge(world, t['qm'], t['qg'])]
        fx = facts_of(world, f, o)
        r = random.Random(2000 + hash((f['qc'], o)) % 1000)
        pos = r.randrange(len(fx) + 1)
        return fx[:pos] + extra + fx[pos:]
    add('robustness','distractors',2, fam['qg'], fam['dg'], dist, bridge=fam['qm'])
    # 6) rename: fresh family entirely
    rfam = new_family(world)
    add('robustness','rename',2, rfam['qg'], rfam['dg'], lambda o, f=rfam: facts_of(world, f, o), famv=rfam, bridge=rfam['qm'])
    return fam, qs

def build():
    rows_by_shots = {0: [], 4: [], 12: []}
    demo_name_set = {w: set(n for d in DEMOS[w] for n in d['names']) for w in WORLDS}
    fam_worlds = [('kinship', i) for i in range(68)] + [('containment', i) for i in range(68, 84)] + [('location', i) for i in range(84, 100)]
    audit = collections.defaultdict(int); problems = []
    for world, fidx in fam_worlds:
        fam, qs = questions_for_family(world, fidx)
        for qi, q in enumerate(qs):
            qid = f'{fidx:03d}/{q["check"]}/{q["variant"]}/{qi}'
            for order in (0, 1):
                facts = q['factfn'](order)
                test_block = block(world, q['fam'], facts, q['hops'])
                # audit: mention balance inside the facts
                ftext = '\n'.join(facts)
                cg = len(re.findall(r'(?<![A-Za-z])' + re.escape(q['gold']) + r'(?![A-Za-z])', ftext))
                cd = len(re.findall(r'(?<![A-Za-z])' + re.escape(q['distractor']) + r'(?![A-Za-z])', ftext))
                if cg != cd: problems.append(('mention_imbalance', qid, order, cg, cd))
                if ntok(q['gold']) != ntok(q['distractor']): problems.append(('token_mismatch', qid, q['gold'], q['distractor']))
                for shots in (0, 4, 12):
                    if shots:
                        demos = demo_ids_for(world, f'{qid}/{order}/{shots}', shots)
                        if any(n in demo_name_set[world] for n in (q['gold'], q['distractor'])):
                            problems.append(('demo_name_leak', qid))
                        prompt = '\n\n'.join([d['text'] for d in demos] + [test_block])
                        dids = [d['id'] for d in demos]
                    else:
                        prompt = test_block; dids = []
                    cands = [q['gold'], q['distractor']]
                    random.Random(qid + str(order)).shuffle(cands)
                    rows_by_shots[shots].append(dict(
                        id=f'{qid}/order{order}', question_id=qid, family=fidx, world=world,
                        task='name_completion', check=q['check'], variant=q['variant'],
                        hops=q['hops'], gold=q['gold'], candidates=cands, bridge=q['bridge'],
                        option_order=order, option_pair_id=f'{qid}/order{1 - order}',
                        paired_base_id=f'{fidx:03d}/twohop/base/1' if q['check'] in ('broken', 'robustness') else None,
                        dataset_version='name_completion_v3', seed=SEED, shots=shots,
                        demo_ids=dids, prompt=prompt,
                        entity_spans=spans(prompt, [q['gold'], q['distractor']] + ([q['bridge']] if q['bridge'] else []))))
                    audit[(world, q['check'], q['variant'], shots)] += 1
    return rows_by_shots, dict(audit), problems

rows_by_shots, audit, problems = build()
for shots, rows in rows_by_shots.items():
    p = OUT / f'completion_v3_{shots}shot.jsonl'
    with open(p, 'w') as f:
        for r in rows: f.write(json.dumps(r) + '\n')
    print(p.name, len(rows))
json.dump({'demos': {w: [d['text'] for d in DEMOS[w]] for w in DEMOS}}, open(OUT / 'demonstrations_v3.json', 'w'), indent=1)
json.dump({'counts': {str(k): v for k, v in audit.items()}, 'problems': problems},
          open(OUT / 'build_audit_v3.json', 'w'), indent=1)
print('problems:', len(problems))
for p in problems[:10]: print(p)
