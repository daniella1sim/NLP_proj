"""No GPU required: check actual tokenizer, graph controls and name parsing."""
import json
from pathlib import Path
import sys
import unittest
from collections import Counter
from completion_evaluation import answer_ids, parse_name, winner, summarize
import pilot
import build_data as b
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'tmp/tokenizer_audit_deps'))
from tokenizers import Tokenizer

class TokenizerAdapter:
    def __init__(self): self.t=Tokenizer.from_file(str(ROOT/'tokenizer_source/tokenizer.json'))
    def encode(self,s,add_special_tokens=False): return self.t.encode(s,add_special_tokens=add_special_tokens).ids

class CompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data={n:[json.loads(s) for s in (ROOT/f'data/completion_{n}shot.jsonl').read_text().splitlines()] for n in (0,4,12)}

    def test_exact_name_not_partial_or_explanation(self):
        for text in (' wugs.','\nwugs\n',' wugs and daxes'):
            self.assertEqual(parse_name(text),'wugs')
        self.assertIsNone(parse_name(' wu'))
        self.assertEqual(parse_name(' wugs',eos=True),'wugs')
        self.assertNotEqual(parse_name(' The answer is wugs.'),'wugs')
        self.assertEqual(winner({'wugs':-2,'daxes':-2}),'Tie')

    def test_shots_change_only_demonstrations(self):
        for rs in zip(self.data[0],self.data[4],self.data[12]):
            for r in rs[1:]:
                for k in ('id','edges','query_source','candidates','gold','proof','hops'):
                    self.assertEqual(r[k],rs[0][k])
                self.assertEqual(r['prompt'].rsplit('\n\n',1)[1],rs[0]['prompt'].rsplit('\n\n',1)[1])
            self.assertEqual(rs[1]['demo_ids'],rs[2]['demo_ids'][:4])
            self.assertEqual(rs[0]['demo_ids'],[])

    def test_unique_answers_and_one_fact_counterfactual(self):
        rows=self.data[0]; by_id={r['id']:r for r in rows}
        self.assertEqual(len(by_id),1200)
        for r in rows:
            valid=[c for c in r['candidates'] if b.path(r['edges'],[r['query_source'],c])]
            self.assertEqual(valid,[r['gold']])
            if r['check']=='broken':
                base=by_id[r['paired_base_id']]
                self.assertEqual(base['candidates'],r['candidates'])
                self.assertEqual(base['query_source'],r['query_source'])
                self.assertEqual(sum(a!=c for a,c in zip(base['edges'],r['edges'])),1)
                self.assertNotEqual(base['gold'],r['gold'])
            if r['check']=='robustness':
                base=by_id[r['paired_base_id']]
                gold=r.get('rename_mapping',{}).get(base['gold'],base['gold'])
                self.assertEqual(gold,r['gold'])

    def test_full_name_tokenization_and_period(self):
        tok=TokenizerAdapter()
        for r in self.data[0]:
            for name in r['candidates']:
                p,a=answer_ids(tok,r['prompt'],name)
                self.assertEqual(tok.t.decode(p+a),r['prompt']+' '+name+'.')
                self.assertGreaterEqual(len(a),3)
                self.assertLessEqual(len(a),5)

    def test_completion_path_and_old_default(self):
        self.assertEqual(pilot.dataset_path(0,'completion').name,'completion_0shot.jsonl')
        self.assertEqual(pilot.dataset_path(4,'v3').name,'pilot_4shot_prompt_v3.jsonl')
        with self.assertRaises(ValueError): pilot.dataset_path(0,'v2')

if __name__=='__main__': unittest.main()
