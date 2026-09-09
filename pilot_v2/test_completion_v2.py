"""Validate the experimental controls independently of model inference."""
import copy
import json
from pathlib import Path
from collections import Counter
import tempfile
import unittest
import build_completion_v2_data as gen
import completion_evaluation as ev
import pilot

ROOT=Path(__file__).resolve().parent

class ControlledCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data={s:[json.loads(x) for x in (ROOT/f'data/completion_v2_{s}shot.jsonl').read_text().splitlines()] for s in (0,4,12)}

    def test_graph_depth_frequency_and_counterfactual(self):
        rows=self.data[0]; ix={x['id']:x for x in rows}
        self.assertEqual(len(ix),1200)
        self.assertEqual(len({x['question_id'] for x in rows}),600)
        for r in rows:
            gen.check(r)
            if r['check']=='broken':
                base=ix[r['paired_base_id']]
                self.assertNotEqual(base['gold'],r['gold'])
                self.assertEqual(base['candidates'],r['candidates'])
                self.assertEqual(sum(a!=b for a,b in zip(base['edges'],r['edges'])),2)
                for col in (0,1):
                    self.assertEqual(Counter(e[col] for e in base['edges']),Counter(e[col] for e in r['edges']))

    def test_order_pairs_and_shot_conditions(self):
        for shot,rows in self.data.items():
            ix={x['id']:x for x in rows}
            for r in rows:
                other=ix[r['option_pair_id']]
                for key in ('gold','edges','proof','query_source','demo_ids','hops'):
                    self.assertEqual(r[key],other[key])
                self.assertEqual(r['candidates'],other['candidates'][::-1])
                self.assertEqual(r['prompt'].replace(' or '.join(r['candidates']),'OPTIONS'),other['prompt'].replace(' or '.join(other['candidates']),'OPTIONS'))
                self.assertEqual(len(r['demo_ids']),shot)
        for a,b,c in zip(*self.data.values()):
            for key in ('id','edges','candidates','gold','proof'):
                self.assertEqual(a[key],b[key]); self.assertEqual(b[key],c[key])
            self.assertEqual(b['demo_ids'],c['demo_ids'][:4])
        self.assertEqual(pilot.dataset_path(12,'completion_v2').name,'completion_v2_12shot.jsonl')

    def test_paired_summary_accounts_for_renaming_and_order(self):
        selected=[copy.deepcopy(r) for r in self.data[0] if r['family']==0]
        for r in selected:
            r.update(free_label=r['gold'],predicted=r['gold'],free_correct=True,correct=True,format_ok=True,
                     gold_minus_best_other=1.,mean_score_predicted=r['gold'])
        with tempfile.TemporaryDirectory() as folder:
            ev.summarize(Path(folder),selected)
            paired=json.loads((Path(folder)/'paired_metrics.json').read_text())
            order=json.loads((Path(folder)/'option_order_metrics.json').read_text())
            self.assertEqual(paired['robustness/rename']['free_answer_changed'],0)
            self.assertEqual(paired['broken/first']['free_answer_changed'],1)
            self.assertTrue(all(v['both_candidate_correct']==1 and v['candidate_same_name']==1 for v in order.values()))

if __name__=='__main__': unittest.main()
