import unittest
from parallel import gpu_groups, merge_rows


class ParallelTests(unittest.TestCase):
    def test_even_and_odd_gpu_counts(self):
        for n in range(2,17):
            devices=[str(i) for i in range(n)]
            groups=gpu_groups(devices)
            self.assertEqual([d for g in groups for d in g],devices)
            self.assertTrue(all(len(g)>=2 for g in groups))
            self.assertEqual(len(groups),n//2)
        self.assertEqual(gpu_groups(['GPU-a','GPU-b','GPU-c','GPU-d','GPU-e']),
                         [['GPU-a','GPU-b','GPU-c'],['GPU-d','GPU-e']])

    def test_large_gpu_and_small_smoke(self):
        self.assertEqual(gpu_groups(['GPU-a'],minimum=1),[['GPU-a']])
        self.assertEqual(len(gpu_groups(list('abcdefgh'),max_workers=2)),2)
        with self.assertRaises(ValueError): gpu_groups(['0'])
        with self.assertRaises(ValueError): gpu_groups(['0','0'])

    def test_full_family_partition_and_merge(self):
        expected=[dict(id=f'{f}/{v}',family=f,gold='Yes',prompt=f'question {f} {v}')
                  for f in range(100) for v in range(12)]
        for count in range(1,9):
            shards=[[dict(r,predicted='Yes') for r in reversed(expected) if r['family']%count==i]
                    for i in range(count)]
            result=merge_rows(expected,shards)
            self.assertEqual([r['id'] for r in result],[r['id'] for r in expected])

    def test_rejects_missing_duplicate_foreign_and_wrong_data(self):
        expected=[dict(id='a',family=0,prompt='a'),dict(id='b',family=1,prompt='b')]
        for shards in ([[expected[0]],[]],
                       [[expected[0],expected[0]],[expected[1]]],
                       [[dict(id='foreign',family=0,prompt='a')],[expected[1]]],
                       [[dict(expected[0],prompt='changed')],[expected[1]]],
                       [[expected[1]],[expected[0]]]):
            with self.assertRaises(ValueError): merge_rows(expected,shards)


if __name__=='__main__': unittest.main()
