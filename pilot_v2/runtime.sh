#!/usr/bin/env bash
# Source this inside bash. Reuse the exact package directories that worked on s-004.
V2_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
V1_RUNTIME="${PILOT_V1_RUNTIME:-$(dirname -- "$V2_ROOT")/pythia_pilot}"
unset PYTHONHOME
export PYTHONNOUSERSITE=1
export PYTHONPATH="$V1_RUNTIME/torch_cu126:$V1_RUNTIME/python_packages"
export PILOT_STORAGE="$V2_ROOT/storage"
export PILOT_RUNS="$PILOT_STORAGE/runs"
export HF_HOME="$PILOT_STORAGE/hf"
export TMPDIR="$PILOT_STORAGE/tmp"
export TRITON_CACHE_DIR="$PILOT_STORAGE/triton-cache"
export TOKENIZERS_PARALLELISM=false
mkdir -p "$TMPDIR" "$TRITON_CACHE_DIR" "$V2_ROOT/logs"
