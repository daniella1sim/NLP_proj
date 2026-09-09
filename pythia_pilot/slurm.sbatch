#!/usr/bin/env bash
#SBATCH --job-name=pythia-pilot
#SBATCH --partition=studentkillable
#SBATCH --account=gpu-students
#SBATCH --constraint=geforce_rtx_3090
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=03:00:00
#SBATCH --output=logs/%x-%j.out
#SBATCH --error=logs/%x-%j.err
set -euo pipefail
cd "${SLURM_SUBMIT_DIR:?Submit from the pythia_pilot directory}"
source env.sh
source .venv/bin/activate
export HF_HUB_OFFLINE=1
export TRANSFORMERS_OFFLINE=1
export OMP_NUM_THREADS="${SLURM_CPUS_PER_TASK:-4}"
nvidia-smi
srun python -u pilot.py run "$@"
