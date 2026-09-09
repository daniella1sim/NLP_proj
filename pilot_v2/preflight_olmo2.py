#!/usr/bin/env python3
"""Preflight for the OLMo-2-7B comparison run. CPU-only; run on the login node
AFTER `python3 pilot.py download --model olmo2-7b`.

Checks, in order:
  1. transformers supports the olmo2 architecture (needs a recent version).
  2. model_lock_olmo2.json exists, matches the base (non-instruct) model id,
     and pins a concrete commit sha.
  3. The snapshot is complete (config + tokenizer + safetensors) and the config
     is the expected shape (model_type olmo2, 32 layers x 32 heads).
  4. The SNAPSHOT tokenizer (not the offline copy the data was built with)
     re-passes the full audit on the olmo2 data files: candidate pairs
     length-matched, prompt/answer boundary property intact.
  5. pilot.py's dataset<->model guard accepts the combination.
  6. Longest prompt + answer budget fits the context window.
Exit code 0 = safe to submit the smoke job.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import pilot

FAIL = []
def check(name, ok, detail=''):
    print(f'[{"ok" if ok else "FAIL"}] {name}' + (f' — {detail}' if detail else ''))
    if not ok: FAIL.append(name)

# 1. library support
import transformers
has_olmo2 = True
try:
    from transformers import Olmo2ForCausalLM  # noqa: F401
except ImportError:
    has_olmo2 = False
check('transformers supports olmo2', has_olmo2,
      f'transformers {transformers.__version__}' + ('' if has_olmo2 else ' — pip install -U transformers'))

# 2. lock
spec = pilot.MODELS['olmo2-7b']
lock_path = ROOT / spec['lock']
check('model lock exists', lock_path.exists(), str(lock_path))
lock = json.loads(lock_path.read_text()) if lock_path.exists() else {}
check('lock pins the base model', lock.get('model_id') == 'allenai/OLMo-2-1124-7B'
      and 'Instruct' not in lock.get('model_id', '') and 'SFT' not in lock.get('model_id', ''),
      str(lock.get('model_id')))
check('lock pins a commit sha', bool(lock.get('revision')) and lock.get('revision') != 'main',
      str(lock.get('revision'))[:12])

# 3. snapshot completeness + config shape
model_dir = pilot.STATE / 'model' / lock.get('revision', 'MISSING')
have = {p.name for p in model_dir.glob('*')} if model_dir.exists() else set()
check('snapshot has config + tokenizer', {'config.json', 'tokenizer.json'} <= have, str(model_dir))
check('snapshot has weights', any(n.endswith('.safetensors') for n in have),
      f'{sum(p.stat().st_size for p in model_dir.glob("*.safetensors"))/2**30:.1f} GiB' if model_dir.exists() else '')
cfg = json.loads((model_dir / 'config.json').read_text()) if 'config.json' in have else {}
check('config is olmo2, 32L x 32H', cfg.get('model_type') == 'olmo2'
      and cfg.get('num_hidden_layers') == 32 and cfg.get('num_attention_heads') == 32,
      f"{cfg.get('model_type')} L={cfg.get('num_hidden_layers')} H={cfg.get('num_attention_heads')} "
      f"vocab={cfg.get('vocab_size')} ctx={cfg.get('max_position_embeddings')}")

# 4. tokenizer audit with the snapshot tokenizer
data_files = [pilot.dataset_path(s, 'completion_v3_olmo2') for s in (0, 4, 12)]
data_files.append(pilot.dataset_path(4, 'completion_v3_olmo2_controls'))
missing = [str(f) for f in data_files if not f.exists()]
check('olmo2 data files present', not missing, '; '.join(missing) or f'{len(data_files)} files')
max_tokens = 0
if not missing and 'tokenizer.json' in have:
    from transformers import AutoTokenizer
    tok = AutoTokenizer.from_pretrained(model_dir, local_files_only=True)
    enc = lambda s: tok.encode(s, add_special_tokens=False)
    import audit_tokenizer
    total_pairs = total_boundary = 0
    for f in data_files:
        rep = audit_tokenizer.audit_file(f, enc)
        total_pairs += len(rep['broken_pairs']); total_boundary += len(rep['broken_boundary'])
        for line in Path(f).open(encoding='utf-8'):
            row = json.loads(line)
            max_tokens = max(max_tokens, len(enc(row['prompt'])))
    check('candidate pairs length-matched under snapshot tokenizer', total_pairs == 0, f'{total_pairs} broken')
    check('prompt/answer boundary property holds', total_boundary == 0, f'{total_boundary} violations')

    # 5. dataset<->model guard
    rows = pilot.read_results(data_files[1])
    try:
        pilot.check_data_model_match(rows, 'olmo2-7b')
        check('pilot.py accepts olmo2-7b + completion_v3_olmo2', True)
    except ValueError as e:
        check('pilot.py accepts olmo2-7b + completion_v3_olmo2', False, str(e))
    try:
        pilot.check_data_model_match(rows, 'pythia-6.9b')
        check('guard also accepts pythia on the dual-matched data', True)
    except ValueError as e:
        check('guard also accepts pythia on the dual-matched data', False, str(e))

    # 6. context budget
    ctx = cfg.get('max_position_embeddings', 0)
    check('longest prompt fits context', max_tokens + 16 <= ctx, f'{max_tokens} + 16 <= {ctx}')

print()
if FAIL:
    print('PREFLIGHT FAILED:', ', '.join(FAIL)); sys.exit(1)
print('PREFLIGHT PASSED. Next: the smoke job, then the full runs (see README).')
