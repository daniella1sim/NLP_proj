"""Download model metadata and tokenizer only; never download weights."""
import hashlib
import json
from pathlib import Path
import urllib.request

root = Path(__file__).resolve().parent
model = 'EleutherAI/pythia-6.9b'
def fetch(url):
    with urllib.request.urlopen(url, timeout=60) as response: return response.read()
lock_path = root/'model_lock.json'
if lock_path.exists():
    lock = json.loads(lock_path.read_text())
    assert lock['model_id']==model
else:
    info = json.loads(fetch('https://huggingface.co/api/models/'+model))
    lock = dict(model_id=model, revision=info['sha'], requested_revision='main')
    lock_path.write_text(json.dumps(lock,indent=2),encoding='utf-8')
folder = root/'tokenizer_source'; folder.mkdir(exist_ok=True)
for name in ('tokenizer.json','tokenizer_config.json','special_tokens_map.json','config.json'):
    data = fetch(f'https://huggingface.co/{model}/resolve/{lock["revision"]}/{name}')
    (folder/name).write_bytes(data)
    print(name, len(data), hashlib.sha256(data).hexdigest())
print('Pinned:',lock)
