# NLP Final Project — Semantic Induction Circuits (SICs) for Multi-hop Reasoning

Behavioral pilot phase: measuring whether Pythia-6.9B resolves 1-hop and 2-hop
semantic relations in-context, as groundwork for mechanistic circuit analysis
(Relation Index, activation/path patching, faithfulness) across training checkpoints.

## Repository layout

- `pilot_v2/` — runner code (Slurm + HF Transformers) and datasets v1/v2.
  - `pilot.py`, `parallel.py` — evaluation runner (candidate log-prob scoring + free generation), multi-GPU worker launcher.
  - `completion_evaluation.py` — name-completion scoring (multi-token candidates).
  - `data/` — question files per prompt format and shot count (0/4/12).
- `pilot_v3/` — current dataset generator and data (`build_data_v3.py`, `data/`).
  Natural-language multi-hop with a named composed relation (mother→grandmother),
  three content worlds, mention-balanced candidates, no options line.
  See `pilot_v3/README_HE.md` for the full design rationale.
- `results/` — per-run metrics, audits and reports (raw `results.jsonl` files are
  git-ignored for size; they are kept on OneDrive and on the cluster).
- `data_pipeline_plan.tex` — end-to-end pipeline plan (Overleaf).

## Dataset versions — status

- **v1 (`completion_*`)** — syllogistic completion ("Therefore, all X are").
  Strong 1-hop signal (80–91%), but 2-hop confounded by a mention-frequency
  shortcut and an options-line position bias. Frozen.
- **v2 (`completion_v2_*`)** — graph-navigation phrasing ("shortest chain of
  exactly K steps"). Collapsed to chance on all checks, including 1-hop:
  base LMs are highly sensitive to unnatural, meta-linguistic prompt formats.
  **Frozen deliberately as a documented negative result** (format-sensitivity
  evidence for the report); not developed further.
- **v3 (`completion_v3_*`)** — current. Natural language, named composed
  relation, balanced mentions (frequency baseline = exactly 50%), candidate
  scoring without an options line, token-length-matched candidate pairs,
  pipeline-control questions in a separate file.

## Running (Slurm)

```bash
bash submit.sh 2 --name completion_v3_12shot_v1 --shots 12 --prompt-version completion_v3
# or, avoiding a specific node / GPU type:
sbatch --gres=gpu:2 --cpus-per-task=4 --mem=32G --exclude=s-002 slurm_flex.sbatch \
  --gpus 2 --name completion_v3_12shot_v1 --shots 12 --prompt-version completion_v3
```

Model: EleutherAI/pythia-6.9b (fp16, sharded across 2 GPUs via device_map;
revision pinned in `pilot_v2/model_lock.json`).
