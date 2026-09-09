#!/usr/bin/env bash
# Separate environment; preserves existing packages, model files and running jobs.
set -euo pipefail
cd -- "$(dirname -- "$0")"
unset PYTHONPATH PYTHONHOME
export PYTHONNOUSERSITE=1
source env.sh
export VIRTUALENV_OVERRIDE_APP_DATA="$PILOT_STORAGE/virtualenv-cache"
mkdir -p "$PILOT_STORAGE/bootstrap"
if [[ ! -f "$PILOT_STORAGE/bootstrap/virtualenv.pyz" ]]; then
  python3 -I -c 'import sys, urllib.request; urllib.request.urlretrieve("https://bootstrap.pypa.io/virtualenv.pyz", sys.argv[1])' "$PILOT_STORAGE/bootstrap/virtualenv.pyz"
fi
if [[ ! -x .venv_recovery/bin/python ]]; then
  python3 -I "$PILOT_STORAGE/bootstrap/virtualenv.pyz" --no-periodic-update .venv_recovery
fi
PY="$PWD/.venv_recovery/bin/python"
"$PY" -I -m pip install 'torch==2.6.0+cu118' --index-url https://download.pytorch.org/whl/cu118
"$PY" -I -m pip install 'torch==2.6.0+cu118' 'numpy==1.26.4' -r requirements.txt
"$PY" -I -m pip check
"$PY" -I -c 'import torch, transformers; print("Torch:", torch.__version__, torch.__file__); print("Transformers:", transformers.__version__); assert torch.__version__ == "2.6.0+cu118"'
"$PY" -I -m pip freeze > "$PILOT_STORAGE/recovery-environment.txt"
echo 'RECOVERY SETUP OK. Existing model weights will be reused; submit recovery.sbatch next.'
