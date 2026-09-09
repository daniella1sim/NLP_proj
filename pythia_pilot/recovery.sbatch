#!/usr/bin/env bash
#SBATCH --job-name=pythia-recovery
#SBATCH --partition=studentkillable
#SBATCH --account=gpu-students
#SBATCH --constraint=geforce_rtx_2080
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err
set -euo pipefail
cd "${SLURM_SUBMIT_DIR:?Submit from pythia_pilot}"
unset PYTHONPATH PYTHONHOME
export PYTHONNOUSERSITE=1
source env.sh
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-4}"
export TRITON_CACHE_DIR="$PILOT_STORAGE/triton-cache-recovery"
srun "$PWD/.venv_recovery/bin/python" -u recovery_run.py "$@"
