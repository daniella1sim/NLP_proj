#!/usr/bin/env bash
#SBATCH --job-name=pythia-numeric
#SBATCH --partition=studentkillable
#SBATCH --account=gpu-students
#SBATCH --constraint=geforce_rtx_2080
#SBATCH --exclude=s-005
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --gres=gpu:2
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --time=01:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err
set -euo pipefail
cd "${SLURM_SUBMIT_DIR:?Submit from pilot_v2}"
source runtime.sh
unset TORCH_DISABLE_NATIVE_JIT
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-4}"
PY=/home/yandex/DLWorkShop2025b/maximg/envs/pythia312/bin/python
test -x "$PY"
echo 'Diagnostics only: three short forward passes per attention mode, no generation or full evaluation.'
# Run both diagnostics even if eager fails. Each subprocess releases its model before the next.
first_status=0
srun "$PY" -u numeric_probe.py --attention eager "$@" || first_status=$?
second_status=0
srun "$PY" -u numeric_probe.py --attention sdpa_math "$@" || second_status=$?
echo "Diagnostic exit codes: eager=$first_status sdpa_math=$second_status; inspect diagnostics/*.json"
if (( first_status != 0 || second_status != 0 )); then exit 1; fi
