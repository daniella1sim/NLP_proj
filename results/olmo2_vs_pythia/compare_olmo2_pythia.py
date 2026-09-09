#!/usr/bin/env python3
"""OLMo-2-7B vs Pythia-6.9B on the v3.1 battery: full comparison + decision rule."""
import json, math, collections, re

def wilson(k, n, z=1.96):
    if not n: return (float('nan'), float('nan'))
    p = k/n
    c = (p + z*z/(2*n))/(1+z*z/n)
    r = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/(1+z*z/n)
    return (c-r, c+r)

def load(path):
    return [json.loads(l) for l in open(path, encoding='utf-8')]

RUNS = {
    ('olmo', s): f'olmo/olmo2_7b_v3_1_{s}shot/results.jsonl' for s in (0, 4, 12)
} | {
    ('pythia', s): f'pythia/completion_v3_1_{s}shot/results.jsonl' for s in (0, 4, 12)
}

def analyze(rows, world_filter=None):
    if world_filter: rows = [r for r in rows if r['world'] == world_filter]
    by_id = {r['id']: r for r in rows}
    out = {}
    groups = collections.defaultdict(list)
    for r in rows:
        groups[(r['check'], r['variant'])].append(r)
    for key, rs in groups.items():
        per_order = {o: [r for r in rs if r['option_order'] == o] for o in (0, 1)}
        acc = {o: (sum(r['correct'] for r in v), len(v)) for o, v in per_order.items()}
        both = []
        for r in per_order[0]:
            mate = by_id.get(r['option_pair_id'])
            if mate: both.append(r['correct'] and mate['correct'])
        free = sum(r['free_correct'] for r in rs)
        out[key] = dict(
            n=len(rs),
            acc0=acc[0][0]/acc[0][1] if acc[0][1] else None,
            acc1=acc[1][0]/acc[1][1] if acc[1][1] else None,
            both=(sum(both), len(both)),
            free=free/len(rs),
        )
    return out

def free_error_types(rows, check, variant):
    """What does the model SAY when free generation is wrong? bridge/distractor/other."""
    c = collections.Counter()
    for r in rows:
        if (r['check'], r['variant']) != (check, variant): continue
        lab = r['free_label']
        if lab == r['gold']: c['gold'] += 1
        elif lab == r.get('bridge'): c['bridge'] += 1
        elif lab in r['candidates']: c['distractor'] += 1
        elif lab is None: c['none'] += 1
        else: c['other_name'] += 1
    return dict(c)

ALL = {k: load(p) for k, p in RUNS.items()}

ORDER = [('direct','base'),('twohop','base'),('broken','first'),('broken','second'),
         ('robustness','reorder'),('robustness','distractors'),('robustness','rename')]

for world in [None, 'kinship']:
    tag = world or 'ALL WORLDS'
    print(f'\n{"="*100}\n{tag}\n{"="*100}')
    print(f'{"check/variant":<24}' + ''.join(f'{m}-{s}sh'.ljust(19) for m in ('pythia','olmo') for s in (4,12)))
    print(' ' * 24 + 'ord0/ord1/both      ' * 4)
    for key in ORDER:
        line = f'{key[0]+"/"+key[1]:<24}'
        for m in ('pythia', 'olmo'):
            for s in (4, 12):
                a = analyze(ALL[(m, s)], world).get(key)
                if not a: line += ' ' * 19; continue
                bk, bn = a['both']
                line += f'{a["acc0"]:.2f}/{a["acc1"]:.2f}/{bk/bn:.2f}'.ljust(19)
        print(line)
    print('\n0-shot (intrinsic prior):')
    for key in ORDER:
        line = f'{key[0]+"/"+key[1]:<24}'
        for m in ('pythia', 'olmo'):
            a = analyze(ALL[(m, 0)], world).get(key)
            bk, bn = a['both']
            line += f'{a["acc0"]:.2f}/{a["acc1"]:.2f}/{bk/bn:.2f}'.ljust(24)
        print(line)

print('\n--- both-orders with Wilson CI (kinship, 12-shot) ---')
for key in ORDER:
    line = f'{key[0]+"/"+key[1]:<24}'
    for m in ('pythia', 'olmo'):
        a = analyze(ALL[(m, 12)], 'kinship')[key]
        bk, bn = a['both']
        lo, hi = wilson(bk, bn)
        line += f'{bk}/{bn} = {bk/bn:.2f} [{lo:.2f},{hi:.2f}]   '
    print(line)

print('\n--- free-generation error anatomy (kinship, 12-shot) ---')
for key in [('twohop','base'),('broken','first'),('robustness','reorder')]:
    for m in ('pythia','olmo'):
        rows = [r for r in ALL[(m,12)] if r['world']=='kinship']
        print(f'{m:<8}{key[0]}/{key[1]:<14}', free_error_types(rows, *key))

print('\n--- per-world both-orders (12-shot) ---')
for world in ('kinship','containment','location'):
    line = f'{world:<14}'
    for m in ('pythia','olmo'):
        for key in [('direct','base'),('twohop','base')]:
            a = analyze(ALL[(m,12)], world)[key]
            bk, bn = a['both']
            line += f'{key[0][:6]} {bk/bn:.2f}  '
        line += ' | '
    print(line)

print('\n--- controls (OLMo) ---')
ctrl = load('olmo/olmo2_7b_v3_1_controls/results.jsonl')
for variant in ('stated','verbatim'):
    rs = [r for r in ctrl if r['variant']==variant]
    print(f'{variant}: candidate {sum(r["correct"] for r in rs)}/{len(rs)}, free {sum(r["free_correct"] for r in rs)}/{len(rs)}')

print('\n--- DECISION RULE (pre-registered; kinship, candidate metric, both-orders) ---')
for s in (4, 12):
    p = analyze(ALL[('pythia', s)], 'kinship'); o = analyze(ALL[('olmo', s)], 'kinship')
    def b(a, key): k, n = a[key]['both']; return k/n
    r1 = b(o,('direct','base')) >= b(p,('direct','base')) - 0.03 and b(o,('twohop','base')) >= 0.72
    of = o[('broken','first')]
    r2 = of['acc0'] > 0.5 and of['acc1'] > 0.5
    r3 = min(o[('broken','second')]['acc0'], o[('broken','second')]['acc1']) >= min(p[('broken','second')]['acc0'], p[('broken','second')]['acc1'])
    rk, rn = o[('robustness','reorder')]['both']
    lo, hi = wilson(rk, rn)
    print(f'{s}-shot: (1) direct+twohop>=pythia: {r1} | (2) broken/first>50% both orders: {r2} '
          f'({of["acc0"]:.2f}/{of["acc1"]:.2f}) | (3) broken/second>=pythia: {r3} | '
          f'secondary reorder both-orders {rk}/{rn}={rk/rn:.2f} CI[{lo:.2f},{hi:.2f}] vs chance .25: {"ABOVE" if lo>0.25 else "not sep."}')
EOF_MARKER_UNUSED = None
