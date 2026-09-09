# OLMo-2-7B comparison run — operating notes

Goal: run the SAME v3.1 behavioral battery on `allenai/OLMo-2-1124-7B` (base,
not Instruct) and compare against Pythia-6.9B. Decision metrics were fixed in
advance — see "Decision rule" below.

## Why a separate data variant

v3.1 candidate pairs were token-length matched under Pythia's tokenizer.
Under OLMo-2's tokenizer (dolma2, ~100K vocab) 1,450/3,640 rows broke.
`pilot_v3/adapt_data_olmo2.py` renamed 81 entities in 60 families (anchored on
the two-hop gold) so every pair is matched under BOTH tokenizers; demos, ids,
question structure and mention balance are unchanged. Verbatim controls keep
demo-name candidates and are marked `length_matched: false` (excluded from
length matching by design). All outputs pass `audit_tokenizer.py` under both
tokenizers and `verify_logic.py` (0 errors, 3,600 rows + 19,200 demo blocks).

`pilot.py` now refuses any model/dataset combination that was not audited
together (`matched_tokenizers` field; legacy files = Pythia only).

## One-time setup on the cluster

```bash
cd ~/pilot_v2
tar xzf completion_v3_olmo2_update.tar.gz          # code + data/ files
python3 -c "from transformers import Olmo2ForCausalLM"   # must succeed; else: pip install -U transformers
python3 pilot.py download --model olmo2-7b         # ~15 GB; pins model_lock_olmo2.json
python3 preflight_olmo2.py                         # must print PREFLIGHT PASSED
```

Copy `model_lock_olmo2.json` back into the repo after the download pins it.

## Smoke, then full runs

```bash
# smoke: 2 families, 4-shot
sbatch --gres=gpu:2 --cpus-per-task=4 --mem=32G --exclude=s-002,s-005 slurm.sbatch \
  --gpus 2 --name olmo2_smoke --model olmo2-7b --shots 4 --prompt-version completion_v3_olmo2 --limit-families 2

# full runs (submit all three; also the controls file)
for S in 0 4 12; do
  sbatch --gres=gpu:2 --cpus-per-task=4 --mem=32G --exclude=s-002,s-005 slurm.sbatch \
    --gpus 2 --name olmo2_7b_v3_1_${S}shot --model olmo2-7b --shots $S --prompt-version completion_v3_olmo2
done
sbatch --gres=gpu:2 --cpus-per-task=4 --mem=32G --exclude=s-002,s-005 slurm.sbatch \
  --gpus 2 --name olmo2_7b_v3_1_controls --model olmo2-7b --shots 4 --prompt-version completion_v3_olmo2_controls
```

Results land in `~/storage/runs/<name>/` as before (summary.csv,
option_order_metrics.json, paired_metrics.json).

## Decision rule (pre-registered before seeing any OLMo number)

OLMo-2-7B is chosen as the checkpoint-sweep platform if, at 4- and 12-shot,
on candidate accuracy with both-orders-correct as the primary form:

1. direct and twohop/base are at least at Pythia's level (twohop both-orders
   >= ~72%), and
2. broken/first is no longer systematically wrong (accuracy above 50% both
   orders; Pythia: 0-18%), and
3. broken/second stays high (>= Pythia's 68-100%).

Secondary pre-registered metric: robustness/reorder above chance (Wilson 95%
CI excluding 25% both-orders / 50% per-order; Pythia: at chance). Reorder
improving without broken/first improving (or vice versa) is reported as a
partial result, not silently collapsed into "better".

If OLMo fails 1, neither model supports the task robustly -> revisit task
design before any mechanistic work. If OLMo passes 1 but not 2-3, it matches
Pythia's layout-bound regime -> the mechanistic story is about layout
heuristics on either platform; pick by checkpoint availability.
