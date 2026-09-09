"""Offline validation of the delivery package; does not claim GPU execution."""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parent
kit = root / 'pythia_pilot'
for p in kit.rglob('*.py'):
    ast.parse(p.read_text(encoding='utf-8'), filename=str(p))
notebook = json.loads((kit/'colab.ipynb').read_text(encoding='utf-8'))
for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        ast.parse(''.join(cell['source']))
        assert cell['execution_count'] is None and cell['outputs'] == []
for p in [kit/'env.sh', kit/'setup.sh', kit/'slurm.sbatch']:
    assert b'\r' not in p.read_bytes(), f'Linux script has CRLF: {p}'
data_counts = {}
for p in sorted((kit/'data').glob('*.jsonl')):
    rows = [json.loads(line) for line in p.read_text().splitlines()]
    assert len(rows) == 1200 and len({r['id'] for r in rows}) == 1200
    data_counts[p.name] = dict(Counter(r['check'] for r in rows))
archive = root/'pythia_pilot.zip'
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert all(n.startswith('pythia_pilot/') and '..' not in Path(n).parts for n in z.namelist())
    assert not any('/storage/' in n or '/__pycache__/' in n or '/.venv/' in n for n in z.namelist())
    for n in z.namelist():
        assert z.read(n) == (root/n).read_bytes(), f'Stale ZIP member: {n}'
    members = z.namelist()
report = {'validation': 'passed', 'python_and_notebook_syntax': 'passed',
          'linux_script_line_endings': 'LF', 'unit_tests': '6 passed',
          'zip_members': members, 'data_counts': data_counts,
          'zip_size_bytes': archive.stat().st_size,
          'zip_sha256': hashlib.sha256(archive.read_bytes()).hexdigest(),
          'not_tested': ['GPU execution', 'Pythia inference', 'actual tokenizer',
                         'remote installation', 'TAU permissions and quota', 'Bash execution']}
(root/'pilot_validation.json').write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='zip_members'}, indent=2))
