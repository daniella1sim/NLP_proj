import json
from pathlib import Path
import tempfile
import unittest
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import pilot


class PilotTests(unittest.TestCase):
    def test_graph_proof(self):
        self.assertEqual(pilot.proof([('a','b'),('b','c')], ('a','c')), ['a','b','c'])
        self.assertIsNone(pilot.proof([('a','b'),('b','c')], ('c','a')))
        self.assertEqual(pilot.proof([('a','b'),('b','c'),('a','c')], ('a','c')), ['a','c'])

    def test_all_families_and_controls(self):
        rows = pilot.make_data()
        self.assertEqual(len(rows), 1200)
        self.assertEqual(len({r['id'] for r in rows}), 1200)
        for r in rows:
            path = pilot.proof(r['edges'], r['query'])
            self.assertEqual(r['gold'], 'Yes' if path else 'No')
            self.assertTrue(r['prompt'].endswith('Answer:'))
            self.assertEqual(len(r['edges']), 4 if r['variant']=='distractors' else 2)
            if r['gold']=='Yes':
                self.assertEqual(r['hops'], 1 if r['check']=='direct' else 2)
            for span in r['entity_spans']:
                self.assertEqual(r['prompt'][span['start']:span['end']], span['entity'])
        for i in range(100):
            family = [r for r in rows if r['family']==i]
            clean = next(r for r in family if r['check']=='twohop' and r['gold']=='Yes')
            for r in family:
                if r['check']=='broken':
                    self.assertEqual(r['query'], clean['query'])
                    self.assertEqual(r['gold'], 'No')
                    self.assertEqual(sum(x!=y for e,f in zip(r['edges'],clean['edges'])
                                         for x,y in zip(e,f)), 1)
                if r['variant']=='reorder':
                    self.assertEqual(r['edges'], list(reversed(clean['edges'])))

    def test_determinism_and_shots(self):
        self.assertEqual(pilot.make_data(3), pilot.make_data(3))
        self.assertNotEqual(pilot.make_data(3), pilot.make_data(3, seed=9))
        for a,b in zip(pilot.make_data(3,shots=0),pilot.make_data(3,shots=4)):
            self.assertEqual(a['edges'], b['edges'])
            self.assertEqual(a['gold'], b['gold'])
            self.assertEqual(a['prompt'].count('Question:'), 1)
            self.assertEqual(b['prompt'].count('Question:'), 5)

    def test_answer_boundary_and_multitoken(self):
        class CharTokenizer:
            def encode(self, text, **kwargs): return list(map(ord, text))
        base, tail = pilot.label_tokens(CharTokenizer(), 'Answer:', ' Yes')
        self.assertEqual(tail, list(map(ord, ' Yes')))
        self.assertEqual(base, list(map(ord, 'Answer:')))
        class BadTokenizer:
            def encode(self, text, **kwargs): return [len(text)]
        with self.assertRaises(ValueError):
            pilot.label_tokens(BadTokenizer(), 'Answer:', ' Yes')

    def test_interrupted_result_recovery(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)/'results.jsonl'
            p.write_bytes(b'{"id":"ok"}\n{"id":')
            self.assertEqual(pilot.read_results(p, repair=True), [{'id':'ok'}])
            self.assertEqual(p.read_bytes(), b'{"id":"ok"}\n')
            p.write_bytes(b'{"id":"ok"}')
            pilot.read_results(p, repair=True)
            self.assertTrue(p.read_bytes().endswith(b'\n'))
            p.write_bytes(b'broken\n{"id":"ok"}\n')
            with self.assertRaises(ValueError): pilot.read_results(p, repair=True)

    def test_reports_known_answers(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d)
            rows = pilot.make_data(3)
            for r in rows:
                r.update(predicted=r['gold'], correct=True, format_ok=True, free_correct=True,
                         yes_minus_no=2 if r['gold']=='Yes' else -2)
            (out/'results.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in rows))
            pilot.summarize(out)
            paired = json.loads((out/'paired_metrics.json').read_text())
            self.assertEqual(paired['clean_and_broken_correct_first']['rate'], 1)
            self.assertEqual(paired['both_correct_rename_positive']['n_families'], 3)
            self.assertTrue((out/'summary.csv').exists())


if __name__ == '__main__': unittest.main()
