#!/usr/bin/env bash
set -euo pipefail
cd -- "$(dirname -- "$0")"
source env.sh
python3 -c 'import sys; assert (3,10) <= sys.version_info[:2] <= (3,12), "Use Python 3.10, 3.11 or 3.12"'
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
# CUDA runtime wheels; no CUDA compiler installation required for this pilot.
python -m pip install torch==2.6.0 --index-url https://download.pytorch.org/whl/cu118
python -m pip install -r requirements.txt
python -m pip check
python -m unittest discover -s tests -v
python -m pip freeze > "$PILOT_STORAGE/environment-installed.txt"
echo 'Setup complete. Next: source .venv/bin/activate; python pilot.py download'
