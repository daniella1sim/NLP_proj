#!/usr/bin/env bash
# Usage: bash submit.sh 4 --name full_12shot --shots 12
set -euo pipefail
cd -- "$(dirname -- "$0")"
GPUS="${1:?First argument must be the number of GPUs}"
if [[ ! "$GPUS" =~ ^[1-9][0-9]*$ ]]; then
  echo 'GPU count must be a positive integer.' >&2
  exit 2
fi
shift
mkdir -p logs
sbatch --gres="gpu:$GPUS" --cpus-per-task="$((GPUS * 2))" --mem="$((GPUS * 16))G" slurm.sbatch --gpus "$GPUS" "$@"
