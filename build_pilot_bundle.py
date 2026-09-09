"""Build the portable notebook and ZIP from the local pilot sources."""
from pathlib import Path
import json
import zipfile

ROOT = Path(__file__).resolve().parent
KIT = ROOT / 'pythia_pilot'


def md(text):
    return {'cell_type': 'markdown', 'metadata': {}, 'source': text.splitlines(keepends=True)}


def code(text):
    return {'cell_type': 'code', 'metadata': {}, 'execution_count': None, 'outputs': [],
            'source': text.splitlines(keepends=True)}


cells = [
    md('''# Pythia-1B pilot — Colab
בחר Runtime → Change runtime type → GPU. הרץ את התאים לפי הסדר.
העלה את החבילה `pythia_pilot.zip` שהוכנה בפרויקט.
המשקולות זמניות; תוצאות נשמרות ב־Drive אחרי כל דוגמה.
לא בוצע אימון. בתחילה מריצים רק 24 פרומפטים לבדיקת תקינות.
'''),
    code('''from google.colab import files, drive
from pathlib import Path
import os, zipfile, sys, subprocess, shutil

drive.mount('/content/drive')
uploaded = files.upload()
if 'pythia_pilot.zip' not in uploaded:
    raise ValueError('Upload pythia_pilot.zip')
with zipfile.ZipFile('pythia_pilot.zip') as archive:
    for name in archive.namelist():
        target = (Path('/content') / name).resolve()
        if not target.is_relative_to(Path('/content/pythia_pilot')):
            raise ValueError('Unexpected ZIP path: ' + name)
    archive.extractall('/content')
os.chdir('/content/pythia_pilot')
os.environ['PILOT_STORAGE'] = '/content/pythia_pilot/storage'
os.environ['PILOT_RUNS'] = '/content/drive/MyDrive/pythia_pilot_runs'
os.environ['HF_HOME'] = '/content/pythia_pilot/storage/hf'
print('Results:', os.environ['PILOT_RUNS'])
'''),
    code('''subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], check=True)
subprocess.run([sys.executable, '-m', 'unittest', 'discover', '-s', 'tests', '-v'], check=True)
subprocess.run([sys.executable, '-c', 'import torch; print(torch.__version__); assert torch.cuda.is_available(), "Select a GPU runtime"; print(torch.cuda.get_device_name(0))'], check=True)
'''),
    code('''subprocess.run([sys.executable, 'pilot.py', 'download'], check=True)
'''),
    md('''## הרצה קצרה
אם שינית גרסאות/קוד, בחר שם חדש. חזרה עם אותן הגדרות ממשיכה ריצה חלקית.
'''),
    code('''RUN_TAG = 'colab_v1'
subprocess.run([sys.executable, '-u', 'pilot.py', 'run', '--name', RUN_TAG + '_smoke', '--limit-families', '2'], check=True)
print(Path(os.environ['PILOT_RUNS'], RUN_TAG + '_smoke', 'summary.csv').read_text())
'''),
    md('''## הפיילוט המלא: ארבע הבדיקות, עם ארבע דוגמאות
הרץ לאחר שההרצה הקצרה הסתיימה בהצלחה ובדקת את התוצאות והזמן שלה.
'''),
    code('''subprocess.run([sys.executable, '-u', 'pilot.py', 'run', '--name', RUN_TAG + '_4shot'], check=True)
'''),
    md('''## השוואת 0-shot — אופציונלי, לאחר קריאת התוצאות
אותם מקרים, ללא הדוגמאות שבפרומפט.
'''),
    code('''subprocess.run([sys.executable, '-u', 'pilot.py', 'run', '--name', RUN_TAG + '_0shot', '--shots', '0'], check=True)
'''),
    md('''## הורדת תוצאות למחשב
אפשר להריץ גם אחרי שעצרת ריצה. התוצאות שכבר נכתבו נשמרות ב־Drive.
שמור את ZIP המקומי תחת `final proj/project`.
'''),
    code('''archive_path = shutil.make_archive('/content/pythia_results', 'zip', os.environ['PILOT_RUNS'])
files.download(archive_path)
'''),
]
notebook = {'nbformat': 4, 'nbformat_minor': 5,
            'metadata': {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'},
                         'language_info': {'name': 'python'}, 'accelerator': 'GPU'}, 'cells': cells}
for i, cell in enumerate(cells):
    cell['id'] = f'pilot-{i:02d}'
(KIT / 'colab.ipynb').write_text(json.dumps(notebook, ensure_ascii=False, indent=2), encoding='utf-8')
excluded = {'__pycache__', '.venv', 'storage', 'logs', '.git'}
with zipfile.ZipFile(ROOT / 'pythia_pilot.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
    for path in sorted(KIT.rglob('*')):
        if path.is_file() and not any(part in excluded for part in path.relative_to(KIT).parts):
            archive.write(path, path.relative_to(ROOT).as_posix())
print(ROOT / 'pythia_pilot.zip')
