#!/usr/bin/env bash
# Source this file; all generated storage stays below the chosen pilot directory.
PILOT_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
export PILOT_STORAGE="${PILOT_STORAGE:-$PILOT_ROOT/storage}"
export HF_HOME="$PILOT_STORAGE/hf"
export PIP_CACHE_DIR="$PILOT_STORAGE/pip-cache"
export TMPDIR="$PILOT_STORAGE/tmp"
export TOKENIZERS_PARALLELISM=false
mkdir -p "$PILOT_STORAGE" "$HF_HOME" "$PIP_CACHE_DIR" "$TMPDIR" "$PILOT_ROOT/logs"
