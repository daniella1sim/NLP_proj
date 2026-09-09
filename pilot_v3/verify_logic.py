#!/usr/bin/env python3
"""Independent logic verifier for v3-family name-completion datasets.

Re-solves every question from the PROMPT TEXT ALONE (no trust in generator
fields): parses the fact lines of the test block, applies the world's chain
semantics for the row's hop count, and demands the derived answer equals the
row's gold while the distractor does not. Also re-solves every demonstration
block against its stated answer. Control rows (check=='control') are skipped —
their semantics are pipeline calibration, not inference.

Usage: python verify_logic.py data_olmo2/*.jsonl
Exit code 1 on any violation.
"""
import json, re, sys
from pathlib import Path

KIN = re.compile(r'^([A-Za-z]+) is the mother of ([A-Za-z]+)\.$')
CON = re.compile(r'^All ([a-z]+) are ([a-z]+)\.$')
LOC = re.compile(r'^The ([a-z]+) is inside the ([a-z]+)\.$')

def parse_block(world, block):
    """Return (relation dict child->parent, question entity, hops_from_text, stated answer or None)."""
    rel, q_entity, q_hops, answer = {}, None, None, None
    for line in block.split('\n'):
        line = line.strip()
        if not line: continue
        if world == 'kinship':
            m = KIN.match(line)
            if m:
                parent, child = m.group(1), m.group(2)
                assert child not in rel, f'duplicate edge for {child}'
                rel[child] = parent; continue
            m = re.match(r'^Question: Who is the (mother|grandmother) of ([A-Za-z]+)\?$', line)
            if m:
                q_hops = 1 if m.group(1) == 'mother' else 2
                q_entity = m.group(2); continue
            m = re.match(r'^Answer:(?: ([A-Za-z]+)\.)?$', line)
            if m: answer = m.group(1); continue
            raise ValueError(f'unparsed kinship line: {line!r}')
        elif world == 'containment':
            m = CON.match(line)
            if m:
                sub, sup = m.group(1), m.group(2)
                assert sub not in rel, f'duplicate edge for {sub}'
                rel[sub] = sup; continue
            m = re.match(r'^Therefore, all ([a-z]+) are(?: ([a-z]+)\.)?$', line)
            if m:
                q_entity, answer = m.group(1), m.group(2); continue
            raise ValueError(f'unparsed containment line: {line!r}')
        elif world == 'location':
            m = LOC.match(line)
            if m:
                inner, outer = m.group(1), m.group(2)
                assert inner not in rel, f'duplicate edge for {inner}'
                rel[inner] = outer; continue
            m = re.match(r'^Question: Where is the ([a-z]+)\?$', line)
            if m: q_entity = m.group(1); continue
            m = re.match(r'^Answer:(?: ([a-z]+)\.)?$', line)
            if m: answer = m.group(1); continue
            raise ValueError(f'unparsed location line: {line!r}')
    return rel, q_entity, q_hops, answer

def solve(rel, entity, hops):
    for _ in range(hops):
        if entity not in rel: return None
        entity = rel[entity]
    return entity

def hops_of_demo(world, rel, q_entity, q_hops, answer):
    if q_hops is not None: return q_hops                     # kinship: explicit in wording
    return 1 if rel.get(q_entity) == answer else 2           # containment/location demos

def main(paths):
    errors, rows, demo_blocks = [], 0, 0
    for path in paths:
        for line in Path(path).open(encoding='utf-8'):
            r = json.loads(line)
            if r['check'] == 'control': continue
            rows += 1
            blocks = r['prompt'].split('\n\n')
            # demonstrations: stated answer must be derivable
            for b in blocks[:-1]:
                demo_blocks += 1
                rel, qe, qh, ans = parse_block(r['world'], b)
                if ans is None:
                    errors.append((r['id'], 'demo without stated answer')); continue
                h = hops_of_demo(r['world'], rel, qe, qh, ans)
                if solve(rel, qe, h) != ans:
                    errors.append((r['id'], f'demo answer {ans} not derivable'))
            # test block
            rel, qe, qh, ans = parse_block(r['world'], blocks[-1])
            if ans is not None:
                errors.append((r['id'], 'test block leaks an answer')); continue
            hops = qh if qh is not None else r['hops']
            if r['world'] == 'kinship' and qh != r['hops']:
                errors.append((r['id'], f'hops field {r["hops"]} != question wording {qh}'))
            derived = solve(rel, qe, hops)
            distractor = [c for c in r['candidates'] if c != r['gold']][0]
            if derived != r['gold']:
                errors.append((r['id'], f'derived {derived} != gold {r["gold"]}'))
            elif derived == distractor:
                errors.append((r['id'], 'distractor equals derived answer'))
    print(f'{rows} rows, {demo_blocks} demo blocks verified; {len(errors)} errors')
    for e in errors[:15]: print(' ', e)
    sys.exit(1 if errors else 0)

if __name__ == '__main__':
    main(sys.argv[1:])
