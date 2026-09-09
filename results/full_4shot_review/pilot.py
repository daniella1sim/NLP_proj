"""Portable Pythia behavioral pilot. Data and reporting need only Python's stdlib."""
import argparse
from collections import defaultdict, deque
import csv
import hashlib
import importlib.metadata
import json
import math
import os
from pathlib import Path
import platform
import random
import re
import shutil
import sys
import time

ROOT = Path(__file__).resolve().parent
STATE = Path(os.environ.get('PILOT_STORAGE', str(ROOT / 'storage'))).resolve()
RUNS = Path(os.environ.get('PILOT_RUNS', str(STATE / 'runs'))).resolve()
os.environ.setdefault('HF_HOME', str(STATE / 'hf'))
os.environ.setdefault('TOKENIZERS_PARALLELISM', 'false')
MODEL = 'EleutherAI/pythia-1b'
LABELS = (' Yes', ' No')


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2), encoding='utf-8')
    temp.replace(path)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def proof(edges, query):
    todo = deque([[query[0]]])
    seen = {query[0]}
    while todo:
        path = todo.popleft()
        if path[-1] == query[1]:
            return path
        for a, b in edges:
            if a == path[-1] and b not in seen:
                seen.add(b)
                todo.append(path + [b])
    return None


def task_text(edges, query):
    return ('\n'.join(f'All {a} are {b}.' for a, b in edges)
            + f'\nQuestion: Does it follow that all {query[0]} are {query[1]}?\nAnswer:')


def prefix(shots):
    intro = ('Decide whether the conclusion follows from the stated facts. '
             'Answer Yes if it follows, otherwise answer No.\n\n')
    demos = [([('daxes', 'wugs'), ('wugs', 'zups')], ('daxes', 'zups'), ' Yes'),
             ([('blickets', 'tufas'), ('tufas', 'pims')], ('pims', 'blickets'), ' No'),
             ([('fepas', 'lomits'), ('nerps', 'sprocks')], ('fepas', 'lomits'), ' Yes'),
             ([('vibbles', 'zorks'), ('mepas', 'tovels')], ('vibbles', 'tovels'), ' No')]
    return intro + ''.join(task_text(e, q) + y + '\n\n' for e, q, y in demos[:shots])


def make_data(families=100, seed=20260906, shots=4):
    rng = random.Random(seed)
    rows = []
    for i in range(families):
        # Random roles, identical-length names, and disjoint vocabulary per family.
        names = [f'group{i:03d}{c}' for c in 'abcdef']
        rng.shuffle(names)
        a, b, c, d, e, f = names
        chain = [(a, b), (b, c)]
        rng.shuffle(chain)
        def add(check, variant, edges, query, polarity, mapping=None):
            p = proof(edges, query)
            body = task_text(edges, query)
            prompt = prefix(shots) + body
            spans = [{'entity': name, 'start': m.start(), 'end': m.end()}
                     for name in sorted({x for edge in edges for x in edge} | set(query))
                     for m in re.finditer(r'\b' + re.escape(name) + r'\b', prompt)]
            row = dict(id=f'{i:03d}/{check}/{variant}/{polarity}', family=i,
                       check=check, variant=variant, polarity=polarity,
                       edges=edges, query=query, gold='Yes' if p else 'No',
                       proof=p, hops=len(p)-1 if p else None,
                       bridge=p[1] if p and len(p)==3 else None,
                       prompt=prompt, entity_spans=spans, seed=seed, shots=shots,
                       rename_mapping=mapping)
            rows.append(row)
        # Negative direct query reverses an explicit edge; graph size is matched.
        direct = rng.choice([(a, b), (b, c)])
        add('direct', 'base', chain, direct, 'positive')
        add('direct', 'base', chain, direct[::-1], 'negative')
        add('twohop', 'base', chain, (a, c), 'positive')
        add('twohop', 'base', chain, (c, a), 'negative')
        # Each break changes one occurrence, retaining query entities and 2 facts.
        for which, edges in [('first', [(a, d), (b, c)]),
                             ('second', [(a, b), (d, c)])]:
            if chain[0] == (b, c):
                edges = list(reversed(edges))
            add('broken', which, edges, (a, c), 'negative')
        variants = {'reorder': list(reversed(chain)),
                    'distractors': chain + [(d, e), (e, f)]}
        rng.shuffle(variants['distractors'])
        rename = dict(zip(names, [f'class{i:03d}{x}' for x in 'uvwxyz']))
        variants['rename'] = [(rename[x], rename[y]) for x, y in chain]
        for variant, edges in variants.items():
            for polarity, query in [('positive', (a, c)), ('negative', (c, a))]:
                q = tuple(rename[x] for x in query) if variant == 'rename' else query
                add('robustness', variant, edges, q, polarity,
                    rename if variant == 'rename' else None)
    return rows


def write_data(args):
    rows = make_data(args.families, args.seed, args.shots)
    path = ROOT / 'data' / f'pilot_{args.shots}shot.jsonl'
    path.parent.mkdir(exist_ok=True)
    content = ''.join(json.dumps(r) + '\n' for r in rows)
    if path.exists() and path.read_text(encoding='utf-8') != content:
        raise RuntimeError('Data exists with different settings. Use a separate kit directory.')
    path.write_text(content, encoding='utf-8', newline='\n')
    print(f'{len(rows)} prompts / {args.families} families: {path}')


def download(args):
    from huggingface_hub import HfApi, snapshot_download
    lock_path = ROOT / 'model_lock.json'
    if lock_path.exists():
        lock = json.loads(lock_path.read_text())
        if lock['model_id'] != MODEL:
            raise ValueError('Model lock does not match this pilot.')
    else:
        info = HfApi().model_info(MODEL, revision='main')
        lock = {'model_id': MODEL, 'revision': info.sha, 'requested_revision': 'main'}
        dump(lock_path, lock)
    target = STATE / 'model' / lock['revision']
    snapshot_download(MODEL, revision=lock['revision'], local_dir=str(target),
                      allow_patterns=['*.safetensors', '*.safetensors.index.json',
                                      'config.json', 'tokenizer.json', 'tokenizer_config.json',
                                      'special_tokens_map.json', 'generation_config.json'])
    print(f'Model ready: {target}\nKeep model_lock.json when moving between providers.')


def load_runtime():
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM
    if not torch.cuda.is_available():
        raise RuntimeError('No CUDA GPU. On Slurm use sbatch/srun; on Colab enable GPU runtime.')
    lock = json.loads((ROOT / 'model_lock.json').read_text())
    model_dir = STATE / 'model' / lock['revision']
    torch.manual_seed(20260906)
    torch.backends.cuda.matmul.allow_tf32 = False
    tokenizer = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_dir, local_files_only=True, torch_dtype=torch.float16,
        use_safetensors=True, attn_implementation='eager', low_cpu_mem_usage=True)
    model = model.to('cuda').eval()
    model.config.use_cache = False
    return torch, tokenizer, model, lock


def label_tokens(tokenizer, prompt, label):
    base = tokenizer.encode(prompt, add_special_tokens=False)
    full = tokenizer.encode(prompt + label, add_special_tokens=False)
    if full[:len(base)] != base:
        raise ValueError('Answer boundary changes prompt tokenization.')
    return base, full[len(base):]


def evaluate_one(torch, tokenizer, model, row):
    prompt = row['prompt']
    enc = tokenizer(prompt, add_special_tokens=False, return_offsets_mapping=True)
    base = enc['input_ids']
    if len(base) + 8 > model.config.max_position_embeddings:
        raise ValueError('Prompt exceeds context limit; no silent truncation is allowed.')
    scores = {}
    with torch.inference_mode():
        for label in LABELS:
            ids, tail = label_tokens(tokenizer, prompt, label)
            all_ids = torch.tensor([ids + tail], device='cuda')
            logits = model(all_ids, use_cache=False).logits[0]
            answer_logits = logits[len(ids)-1:len(ids)+len(tail)-1].float()
            logp = answer_logits.log_softmax(-1)
            score = logp[torch.arange(len(tail), device='cuda'),
                         torch.tensor(tail, device='cuda')].sum().item()
            if not math.isfinite(score):
                raise ValueError('Non-finite candidate score; inspect dtype and GPU compatibility.')
            scores[label.strip()] = score
        ids = torch.tensor([base], device='cuda')
        out = model.generate(ids, attention_mask=torch.ones_like(ids), do_sample=False,
                             max_new_tokens=8, use_cache=False,
                             pad_token_id=tokenizer.eos_token_id)
    generated = tokenizer.decode(out[0, len(base):], skip_special_tokens=True)
    match = re.match(r'^\s*(Yes|No)\b', generated)
    free_label = match.group(1) if match else None
    margin = scores['Yes'] - scores['No']
    predicted = 'Yes' if margin > 0 else 'No' if margin < 0 else 'Tie'
    anchors = [dict(span, token_indices=[j for j, (a,b) in enumerate(enc['offset_mapping'])
                                        if a < span['end'] and b > span['start']])
               for span in row['entity_spans']]
    return dict(row, candidate_logprobs=scores, yes_minus_no=margin,
                predicted=predicted, correct=predicted == row['gold'],
                generated=generated, free_label=free_label,
                format_ok=free_label is not None, free_correct=free_label == row['gold'],
                token_ids=base, token_offsets=enc['offset_mapping'], token_anchors=anchors)


def read_results(path, repair=False):
    if not path.exists():
        return []
    raw = path.read_bytes()
    lines = raw.splitlines(keepends=True)
    rows, valid_bytes = [], 0
    for i, line in enumerate(lines):
        try:
            rows.append(json.loads(line))
            valid_bytes += len(line)
        except (ValueError, UnicodeDecodeError):
            if repair and i == len(lines)-1 and not line.endswith(b'\n'):
                with path.open('r+b') as handle:
                    handle.truncate(valid_bytes)
            else:
                raise
    # A complete JSON record without newline also needs a separator before append.
    if repair and rows and path.read_bytes() and not path.read_bytes().endswith(b'\n'):
        with path.open('ab') as handle:
            handle.write(b'\n')
    return rows


def wilson(k, n):
    if not n:
        return [None, None]
    z = 1.96
    p = k/n
    center = (p + z*z/(2*n))/(1+z*z/n)
    radius = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/(1+z*z/n)
    return [center-radius, center+radius]


def summarize(out):
    rows = read_results(out / 'results.jsonl')
    groups = defaultdict(list)
    for row in rows:
        groups[(row['check'], row['variant'], row['gold'])].append(row)
    stats = []
    for (check, variant, gold), values in sorted(groups.items()):
        n = len(values)
        k = sum(v['correct'] for v in values)
        low, high = wilson(k, n)
        stats.append(dict(check=check, variant=variant, gold=gold, n=n,
                          candidate_accuracy=k/n, ci95_low=low, ci95_high=high,
                          format_rate=sum(v['format_ok'] for v in values)/n,
                          free_accuracy=sum(v['free_correct'] for v in values)/n,
                          mean_yes_minus_no=sum(v['yes_minus_no'] for v in values)/n))
    with (out / 'summary.csv').open('w', newline='', encoding='utf-8') as f:
        if stats:
            writer = csv.DictWriter(f, fieldnames=list(stats[0]))
            writer.writeheader()
            writer.writerows(stats)
    families = defaultdict(dict)
    for r in rows:
        families[r['family']][(r['check'], r['variant'], r['polarity'])] = r
    paired = defaultdict(list)
    for values in families.values():
        clean = values.get(('twohop', 'base', 'positive'))
        for variant in ('first', 'second'):
            broken = values.get(('broken', variant, 'negative'))
            if clean and broken:
                paired['clean_and_broken_correct_' + variant].append(clean['correct'] and broken['correct'])
                paired['margin_decreases_' + variant].append(clean['yes_minus_no'] > broken['yes_minus_no'])
        for variant in ('reorder', 'distractors', 'rename'):
            for polarity in ('positive', 'negative'):
                original = values.get(('twohop', 'base', polarity))
                changed = values.get(('robustness', variant, polarity))
                if original and changed:
                    key = variant + '_' + polarity
                    paired['both_correct_' + key].append(original['correct'] and changed['correct'])
                    paired['prediction_agrees_' + key].append(original['predicted'] == changed['predicted'])
    dump(out / 'paired_metrics.json', {k: {'n_families': len(v), 'rate': sum(v)/len(v),
                                          'ci95': wilson(sum(v), len(v))} for k,v in paired.items()})
    print(f'{len(rows)} completed prompts. Read {out / "summary.csv"}')


def run(args):
    path = ROOT / 'data' / f'pilot_{args.shots}shot.jsonl'
    rows = read_results(path)
    if not rows:
        raise ValueError('Dataset missing or empty; run data first.')
    if args.limit_families:
        rows = [r for r in rows if r['family'] < args.limit_families]
    torch, tokenizer, model, lock = load_runtime()
    out = RUNS / args.name
    out.mkdir(parents=True, exist_ok=True)
    versions = {p: importlib.metadata.version(p) for p in
                ['torch', 'transformers', 'huggingface-hub', 'safetensors', 'accelerate']}
    settings = dict(model=lock, data_sha256=digest(path), code_sha256=digest(Path(__file__)),
                    shots=args.shots, limit_families=args.limit_families, dtype='float16',
                    attention='eager', versions=versions, generation_max_new_tokens=8)
    manifest = out / 'manifest.json'
    if manifest.exists():
        if json.loads(manifest.read_text()) != settings:
            raise ValueError('Run settings differ: choose a new --name to avoid mixing experiments.')
    else:
        dump(manifest, settings)
    gpu = torch.cuda.get_device_properties(0)
    session_id = str(time.time_ns())
    session = dict(python=sys.version, platform=platform.platform(), gpu=gpu.name,
                   gpu_gib=gpu.total_memory/2**30, cuda=torch.version.cuda,
                   disk_free_gib=shutil.disk_usage(STATE).free/2**30,
                   slurm_job_id=os.environ.get('SLURM_JOB_ID'), versions=versions)
    dump(out / f'session_{session_id}.json', session)
    old = read_results(out / 'results.jsonl', repair=True)
    done = {r['id'] for r in old}
    if len(done) != len(old):
        raise ValueError('Duplicate result IDs; do not run concurrent writers with the same name.')
    torch.cuda.reset_peak_memory_stats()
    start = time.monotonic()
    count = 0
    with (out / 'results.jsonl').open('a', encoding='utf-8') as f:
        for row in rows:
            if row['id'] in done:
                continue
            result = evaluate_one(torch, tokenizer, model, row)
            result['session_id'] = session_id
            f.write(json.dumps(result) + '\n')
            f.flush()
            os.fsync(f.fileno())
            count += 1
            if count % 12 == 0:
                elapsed = time.monotonic()-start
                print(f'{len(done)+count}/{len(rows)} prompts; {elapsed/count:.2f} s/prompt', flush=True)
    session.update(elapsed_seconds=time.monotonic()-start, completed_this_session=count,
                   peak_allocated_gpu_gib=torch.cuda.max_memory_allocated()/2**30)
    dump(out / f'session_{session_id}.json', session)
    summarize(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='cmd', required=True)
    data = sub.add_parser('data')
    data.add_argument('--families', type=int, default=100)
    data.add_argument('--seed', type=int, default=20260906)
    data.add_argument('--shots', type=int, choices=[0,4], default=4)
    sub.add_parser('download')
    eval_parser = sub.add_parser('run')
    eval_parser.add_argument('--name', required=True)
    eval_parser.add_argument('--shots', type=int, choices=[0,4], default=4)
    eval_parser.add_argument('--limit-families', type=int, default=0)
    report = sub.add_parser('report')
    report.add_argument('--name', required=True)
    args = parser.parse_args()
    if getattr(args, 'name', None) and not re.fullmatch(r'[A-Za-z0-9_-]+', args.name):
        parser.error('--name must contain only letters, numbers, underscores or hyphens.')
    if getattr(args, 'limit_families', 0) < 0 or getattr(args, 'families', 1) <= 0:
        parser.error('Family counts must be positive (0 means no run limit).')
    if args.cmd == 'data': write_data(args)
    elif args.cmd == 'download': download(args)
    elif args.cmd == 'run':
        # Kernel lock releases automatically on job termination (Linux providers).
        import fcntl
        # Keep locks on compute storage: Colab Drive FUSE may not support flock.
        lock_dir = STATE / 'locks'
        lock_dir.mkdir(parents=True, exist_ok=True)
        with (lock_dir / (args.name + '.lock')).open('a') as handle:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except BlockingIOError:
                raise RuntimeError('This run already has an active writer. Use another --name.')
            run(args)
    elif args.cmd == 'report': summarize(RUNS / args.name)


if __name__ == '__main__':
    main()
