"""Rename the frozen pilot graphs and create paired 4/12-shot conditions."""
from collections import deque
import hashlib
import json
from pathlib import Path
import random
import re

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / 'results/full_4shot_review/data/pilot_4shot.jsonl'
SEED = 20260907
TEST_NAMES = '''daxes wugs blickets lomits sprocks vibbles zorks tufas nerps
plinets korvas zemples nufrons shalds brovets crundles flomps grivaks
helpons jastles kelbrins murdles oskets prandils quavels ruspins
snorps tivaks ulvets vromps welbins xandles yorbits zeltrons'''.split()
# Separate names for demonstrations; no entity name appears in the test vocabulary.
DEMO_NAMES = '''bantrels chovaks drelpins eskums farnels glupits
hestrops ilvans jondles krusps lartins mevkets
naldrops omvils pruvaks quistons rendips stalvons
thumlets ubnars valprets werduks xipnols yembars
zaltips benvorks caskrels durnips elvrops fimbars
garnups holviks isprels juntrops klavets lumbars
meldrops norvaks olprens palviks quenbars rilvets
sundrels tarveks umplits velnars wiskrops xulvets
yaldrops zenpaks borvils chundets dalprets ognurs
felquins grovaks hispels irvonts jalmeks kenvrops
lispaks mornets nembars ovprils pelnaks quaspuls
ravnips skumlets teldrops unvaks vespils waldrets'''.split()
INTRO = ('Decide whether the conclusion follows from the stated facts. '
         'Answer Yes if it follows, otherwise answer No.\n\n')


def distance(a, b):
    row = list(range(len(b)+1))
    for i,x in enumerate(a,1):
        new = [i]
        for j,y in enumerate(b,1):
            new.append(min(new[-1]+1, row[j]+1, row[j-1]+(x!=y)))
        row = new
    return row[-1]


def distinct(names):
    return all(distance(a,b)>=3 and distance(a,b)/max(len(a),len(b))>=0.5
               for i,a in enumerate(names) for b in names[i+1:])


def text(edges, query):
    return '\n'.join(f'All {a} are {b}.' for a,b in edges) + (
        f'\nQuestion: Does it follow that all {query[0]} are {query[1]}?\nAnswer:')


def path(edges, query):
    todo = deque([[query[0]]]); seen = {query[0]}
    while todo:
        p = todo.popleft()
        if p[-1]==query[1]: return p
        for a,b in edges:
            if a==p[-1] and b not in seen:
                seen.add(b); todo.append(p+[b])
    return None


def demonstrations():
    demos = []
    # Each block of four covers the same four example types and is Yes/No balanced.
    for i in range(12):
        a,b,c,d,e,f = DEMO_NAMES[6*i:6*i+6]
        assert distinct([a,b,c,d,e,f])
        kind = i % 4
        edges = [(a,b),(b,c)] if kind in (0,1) else [(a,b),(c,d)]
        query = [(a,c),(c,a),(a,b),(a,d)][kind]
        p = path(edges,query)
        demos.append(dict(id=f'demo_{i:02d}', edges=edges, query=query,
                          gold='Yes' if p else 'No', proof=p))
    return demos


def build():
    old = [json.loads(line) for line in SOURCE.read_text().splitlines()]
    rng = random.Random(SEED)
    maps = {}
    for family in sorted({r['family'] for r in old}):
        # Twelve mutually dissimilar names, six for baseline and six for rename.
        for attempt in range(10000):
            names = rng.sample(TEST_NAMES,12)
            if distinct(names): break
        else: raise RuntimeError('Cannot sample distinct names')
        keys = [f'group{family:03d}{c}' for c in 'abcdef'] + [f'class{family:03d}{c}' for c in 'uvwxyz']
        maps[family] = dict(zip(keys,names))
    demos = demonstrations()
    outputs = {}
    for shots in (4,12):
        prefix = INTRO + ''.join(text(d['edges'],d['query'])+' '+d['gold']+'\n\n' for d in demos[:shots])
        rows = []
        for original in old:
            r = dict(original)
            mapping = maps[r['family']]
            r['edges'] = [[mapping[a],mapping[b]] for a,b in r['edges']]
            r['query'] = [mapping[x] for x in r['query']]
            r['proof'] = path(r['edges'],r['query'])
            assert r['gold'] == ('Yes' if r['proof'] else 'No')
            r['bridge'] = mapping[r['bridge']] if r['bridge'] else None
            r['rename_mapping'] = ({mapping[a]:mapping[b] for a,b in r['rename_mapping'].items()}
                                    if r['rename_mapping'] else None)
            r['prompt'] = prefix + text(r['edges'],r['query'])
            names = sorted({x for edge in r['edges'] for x in edge} | set(r['query']))
            r['entity_spans'] = [dict(entity=name,start=m.start(),end=m.end()) for name in names
                for m in re.finditer(r'\b'+re.escape(name)+r'\b',r['prompt'])]
            r.update(shots=shots, dataset_version='distinct_names_v2', naming_seed=SEED,
                     demo_ids=[d['id'] for d in demos[:shots]], baseline_id=original['id'])
            rows.append(r)
        outputs[shots] = rows
        folder = ROOT/'data'; folder.mkdir(exist_ok=True)
        (folder/f'pilot_{shots}shot.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in rows),encoding='utf-8')
    (ROOT/'demonstrations.json').write_text(json.dumps(demos,indent=2),encoding='utf-8')
    (ROOT/'name_mappings.json').write_text(json.dumps(maps,indent=2),encoding='utf-8')
    manifest = dict(dataset_version='distinct_names_v2', baseline_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        naming_seed=SEED, families=100, rows_per_condition=1200, conditions=[4,12],
        notes=['Same graphs, labels and fact order as baseline; names changed.',
               'Test names reused across independent prompts, roles randomly assigned.',
               'Demonstration vocabulary disjoint from test vocabulary.',
               '4-shot demonstrations are the first four of the 12-shot condition.',
               'Spelling distinctness is verified, tokenizer audit awaits model selection.'])
    (ROOT/'dataset_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    first = outputs[12][2]
    preview = '# קלט לדוגמה: 12 הדגמות\n\nזהו הקלט המלא לפני שהמודל עונה. תשובת האמת: Yes.\n\n```text\n'+first['prompt']+'\n```\n'
    preview += '\n# קלט מקביל: 4 הדגמות\n\n```text\n'+outputs[4][2]['prompt']+'\n```\n'
    (ROOT/'INPUT_EXAMPLES_HE.md').write_text(preview,encoding='utf-8')
    print('Built 1200 paired prompts each for 4-shot and 12-shot.')


if __name__=='__main__': build()
