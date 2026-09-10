#!/usr/bin/env python3
"""Tokenizer-compatibility audit for name-completion datasets.

For every row of every given jsonl file, checks under the given tokenizer:
  1. pair length  : len(tok(' '+gold)) == len(tok(' '+distractor))
  2. boundary     : tok(prompt) is a strict prefix of tok(prompt+' '+cand+'.')
                    for BOTH candidates (the exact property completion_evaluation.py
                    asserts at run time).
Works with either a raw tokenizers-json file (--tokenizer-json) or a HF
snapshot/model dir (--hf-tokenizer, needs transformers). Exit code 1 if any
check fails; writes a JSON report.

Usage:
  python audit_tokenizer.py --tokenizer-json dolma2.json --out report.json data/*.jsonl
  python audit_tokenizer.py --hf-tokenizer /path/to/snapshot --out report.json data/*.jsonl
"""
import argparse, collections, json, sys
from pathlib import Path


def load_tokenizer(args):
    if args.tokenizer_json:
        from tokenizers import Tokenizer
        t = Tokenizer.from_file(args.tokenizer_json)
        return (lambda s: t.encode(s, add_special_tokens=False).ids), f'json:{args.tokenizer_json}'
    from transformers import AutoTokenizer
    t = AutoTokenizer.from_pretrained(args.hf_tokenizer, local_files_only=Path(args.hf_tokenizer).exists())
    return (lambda s: t.encode(s, add_special_tokens=False)), f'hf:{args.hf_tokenizer}'


def audit_file(path, enc):
    broken_pairs, broken_boundary = [], []
    n = skipped = 0
    name_len = {}

    for line in Path(path).open(encoding='utf-8'):
        row = json.loads(line)
        n += 1

        gold = row['gold']
        others = [c for c in row['candidates'] if c != gold]
        assert len(others) == 1, f'{row["id"]}: expected exactly 2 candidates'
        distractor = others[0]

        prompt = row['prompt']
        base = enc(prompt)

        def get_tail(candidate):
            full = enc(prompt + ' ' + candidate + '.')
            # The candidate must append cleanly after the prompt.
            if full[:len(base)] != base or len(full) == len(base):
                return None
            # tokens scored by completion_evaluation.py.
            return full[len(base):]

        gold_tail = get_tail(gold)
        distractor_tail = get_tail(distractor)
        # Check answer-boundary stability.
        if gold_tail is None:
            broken_boundary.append(dict(id=row['id'], candidate=gold))
        if distractor_tail is None:
            broken_boundary.append(dict(id=row['id'], candidate=distractor))
        # Some control examples are intentionally unmatched.
        if row.get('length_matched') is False:
            skipped += 1
        elif gold_tail is not None and distractor_tail is not None:
            lg = len(gold_tail)
            ld = len(distractor_tail)

            name_len[gold] = lg
            name_len[distractor] = ld

            if lg != ld:
                broken_pairs.append(dict(id=row['id'], family=row['family'], world=row['world'], gold=gold, len_gold=lg, distractor=distractor, len_distractor=ld,))

    return dict(file=str(path), rows=n, skipped_unmatched=skipped, broken_pairs=broken_pairs, broken_boundary=broken_boundary, length_histogram=dict(collections.Counter(name_len.values())),)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+')
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument('--tokenizer-json')
    g.add_argument('--hf-tokenizer')
    ap.add_argument('--out', required=True)
    args = ap.parse_args()
    enc, label = load_tokenizer(args)
    reports = [audit_file(f, enc) for f in args.files]
    families = sorted({(b['family'], b['world']) for r in reports for b in r['broken_pairs']})
    total_broken = sum(len(r['broken_pairs']) for r in reports)
    total_boundary = sum(len(r['broken_boundary']) for r in reports)
    summary = dict(tokenizer=label, files=len(reports),
                   rows=sum(r['rows'] for r in reports),
                   broken_pair_rows=total_broken, broken_boundary_rows=total_boundary,
                   affected_families=[list(f) for f in families], reports=reports)
    Path(args.out).write_text(json.dumps(summary, indent=1), encoding='utf-8')
    print(f'{label}: {summary["rows"]} rows | broken pairs: {total_broken} '
          f'({len(families)} families) | boundary violations: {total_boundary}')
    for r in reports:
        print(f'  {Path(r["file"]).name}: {len(r["broken_pairs"])} broken pairs, '
              f'{len(r["broken_boundary"])} boundary, name-length hist {r["length_histogram"]}')
    sys.exit(1 if total_broken or total_boundary else 0)


if __name__ == '__main__':
    main()
