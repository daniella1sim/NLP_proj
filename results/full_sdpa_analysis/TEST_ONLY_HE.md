# שאלות המבחן בלבד — ללא חזרה על ההדגמות

כל שאלה מוצגת פעם אחת, עם התשובות משתי ההרצות. 100 משפחות, 12 בדיקות בכל משפחה. בביקורת נמצאו 1,200 שאלות שונות ללא כפילויות טקסטואליות בתוך כל הרצה.

## 000/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are wugs.
All korvas are tufas.
Question: Does it follow that all tufas are wugs?
Answer:
```

## 000/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are wugs.
All korvas are tufas.
Question: Does it follow that all wugs are tufas?
Answer:
```

## 000/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are wugs.
All korvas are tufas.
Question: Does it follow that all korvas are wugs?
Answer:
```

## 000/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are wugs.
All korvas are tufas.
Question: Does it follow that all wugs are korvas?
Answer:
```

## 000/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are wugs.
All korvas are grivaks.
Question: Does it follow that all korvas are wugs?
Answer:
```

## 000/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are wugs.
All korvas are tufas.
Question: Does it follow that all korvas are wugs?
Answer:
```

## 000/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tufas.
All tufas are wugs.
Question: Does it follow that all korvas are wugs?
Answer:
```

## 000/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tufas.
All tufas are wugs.
Question: Does it follow that all wugs are korvas?
Answer:
```

## 000/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tufas.
All grivaks are oskets.
All oskets are murdles.
All tufas are wugs.
Question: Does it follow that all korvas are wugs?
Answer:
```

## 000/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tufas.
All grivaks are oskets.
All oskets are murdles.
All tufas are wugs.
Question: Does it follow that all wugs are korvas?
Answer:
```

## 000/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are lomits.
All daxes are jastles.
Question: Does it follow that all daxes are lomits?
Answer:
```

## 000/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are lomits.
All daxes are jastles.
Question: Does it follow that all lomits are daxes?
Answer:
```

## 001/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are helpons.
All oskets are ruspins.
Question: Does it follow that all oskets are ruspins?
Answer:
```

## 001/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are helpons.
All oskets are ruspins.
Question: Does it follow that all ruspins are oskets?
Answer:
```

## 001/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are helpons.
All oskets are ruspins.
Question: Does it follow that all oskets are helpons?
Answer:
```

## 001/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are helpons.
All oskets are ruspins.
Question: Does it follow that all helpons are oskets?
Answer:
```

## 001/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are helpons.
All oskets are blickets.
Question: Does it follow that all oskets are helpons?
Answer:
```

## 001/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are helpons.
All oskets are ruspins.
Question: Does it follow that all oskets are helpons?
Answer:
```

## 001/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are ruspins.
All ruspins are helpons.
Question: Does it follow that all oskets are helpons?
Answer:
```

## 001/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are ruspins.
All ruspins are helpons.
Question: Does it follow that all helpons are oskets?
Answer:
```

## 001/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are helpons.
All blickets are wugs.
All wugs are sprocks.
All oskets are ruspins.
Question: Does it follow that all oskets are helpons?
Answer:
```

## 001/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are helpons.
All blickets are wugs.
All wugs are sprocks.
All oskets are ruspins.
Question: Does it follow that all helpons are oskets?
Answer:
```

## 001/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are ulvets.
All daxes are korvas.
Question: Does it follow that all daxes are ulvets?
Answer:
```

## 001/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are ulvets.
All daxes are korvas.
Question: Does it follow that all ulvets are daxes?
Answer:
```

## 002/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are shalds.
All ruspins are vibbles.
Question: Does it follow that all vibbles are shalds?
Answer:
```

## 002/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are shalds.
All ruspins are vibbles.
Question: Does it follow that all shalds are vibbles?
Answer:
```

## 002/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are shalds.
All ruspins are vibbles.
Question: Does it follow that all ruspins are shalds?
Answer:
```

## 002/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are shalds.
All ruspins are vibbles.
Question: Does it follow that all shalds are ruspins?
Answer:
```

## 002/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are shalds.
All ruspins are plinets.
Question: Does it follow that all ruspins are shalds?
Answer:
```

## 002/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are shalds.
All ruspins are vibbles.
Question: Does it follow that all ruspins are shalds?
Answer:
```

## 002/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are vibbles.
All vibbles are shalds.
Question: Does it follow that all ruspins are shalds?
Answer:
```

## 002/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are vibbles.
All vibbles are shalds.
Question: Does it follow that all shalds are ruspins?
Answer:
```

## 002/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All ruspins are vibbles.
All vibbles are shalds.
All oskets are zemples.
All plinets are oskets.
Question: Does it follow that all ruspins are shalds?
Answer:
```

## 002/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All ruspins are vibbles.
All vibbles are shalds.
All oskets are zemples.
All plinets are oskets.
Question: Does it follow that all shalds are ruspins?
Answer:
```

## 002/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are prandils.
All helpons are tivaks.
Question: Does it follow that all helpons are prandils?
Answer:
```

## 002/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are prandils.
All helpons are tivaks.
Question: Does it follow that all prandils are helpons?
Answer:
```

## 003/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are nufrons.
All brovets are prandils.
Question: Does it follow that all brovets are prandils?
Answer:
```

## 003/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are nufrons.
All brovets are prandils.
Question: Does it follow that all prandils are brovets?
Answer:
```

## 003/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are nufrons.
All brovets are prandils.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 003/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are nufrons.
All brovets are prandils.
Question: Does it follow that all nufrons are brovets?
Answer:
```

## 003/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are nufrons.
All brovets are oskets.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 003/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All brovets are prandils.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 003/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are prandils.
All prandils are nufrons.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 003/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are prandils.
All prandils are nufrons.
Question: Does it follow that all nufrons are brovets?
Answer:
```

## 003/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are korvas.
All oskets are zemples.
All prandils are nufrons.
All brovets are prandils.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 003/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are korvas.
All oskets are zemples.
All prandils are nufrons.
All brovets are prandils.
Question: Does it follow that all nufrons are brovets?
Answer:
```

## 003/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are grivaks.
All vromps are quavels.
Question: Does it follow that all vromps are grivaks?
Answer:
```

## 003/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are grivaks.
All vromps are quavels.
Question: Does it follow that all grivaks are vromps?
Answer:
```

## 004/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are oskets.
All oskets are kelbrins.
Question: Does it follow that all oskets are kelbrins?
Answer:
```

## 004/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are oskets.
All oskets are kelbrins.
Question: Does it follow that all kelbrins are oskets?
Answer:
```

## 004/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are oskets.
All oskets are kelbrins.
Question: Does it follow that all flomps are kelbrins?
Answer:
```

## 004/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are oskets.
All oskets are kelbrins.
Question: Does it follow that all kelbrins are flomps?
Answer:
```

## 004/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are quavels.
All oskets are kelbrins.
Question: Does it follow that all flomps are kelbrins?
Answer:
```

## 004/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are oskets.
All quavels are kelbrins.
Question: Does it follow that all flomps are kelbrins?
Answer:
```

## 004/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are kelbrins.
All flomps are oskets.
Question: Does it follow that all flomps are kelbrins?
Answer:
```

## 004/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are kelbrins.
All flomps are oskets.
Question: Does it follow that all kelbrins are flomps?
Answer:
```

## 004/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All oskets are kelbrins.
All daxes are prandils.
All flomps are oskets.
All quavels are daxes.
Question: Does it follow that all flomps are kelbrins?
Answer:
```

## 004/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are kelbrins.
All daxes are prandils.
All flomps are oskets.
All quavels are daxes.
Question: Does it follow that all kelbrins are flomps?
Answer:
```

## 004/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are blickets.
All blickets are ruspins.
Question: Does it follow that all nerps are ruspins?
Answer:
```

## 004/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are blickets.
All blickets are ruspins.
Question: Does it follow that all ruspins are nerps?
Answer:
```

## 005/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are brovets.
All brovets are lomits.
Question: Does it follow that all korvas are brovets?
Answer:
```

## 005/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are brovets.
All brovets are lomits.
Question: Does it follow that all brovets are korvas?
Answer:
```

## 005/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are brovets.
All brovets are lomits.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 005/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are brovets.
All brovets are lomits.
Question: Does it follow that all lomits are korvas?
Answer:
```

## 005/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are grivaks.
All brovets are lomits.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 005/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are brovets.
All grivaks are lomits.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 005/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are lomits.
All korvas are brovets.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 005/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are lomits.
All korvas are brovets.
Question: Does it follow that all lomits are korvas?
Answer:
```

## 005/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are lomits.
All ruspins are zemples.
All grivaks are ruspins.
All korvas are brovets.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 005/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are lomits.
All ruspins are zemples.
All grivaks are ruspins.
All korvas are brovets.
Question: Does it follow that all lomits are korvas?
Answer:
```

## 005/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are shalds.
All shalds are helpons.
Question: Does it follow that all daxes are helpons?
Answer:
```

## 005/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are shalds.
All shalds are helpons.
Question: Does it follow that all helpons are daxes?
Answer:
```

## 006/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are oskets.
All oskets are vibbles.
Question: Does it follow that all blickets are oskets?
Answer:
```

## 006/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are oskets.
All oskets are vibbles.
Question: Does it follow that all oskets are blickets?
Answer:
```

## 006/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are oskets.
All oskets are vibbles.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 006/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are oskets.
All oskets are vibbles.
Question: Does it follow that all vibbles are blickets?
Answer:
```

## 006/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are lomits.
All oskets are vibbles.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 006/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are oskets.
All lomits are vibbles.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 006/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vibbles.
All blickets are oskets.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 006/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vibbles.
All blickets are oskets.
Question: Does it follow that all vibbles are blickets?
Answer:
```

## 006/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are zemples.
All blickets are oskets.
All zemples are ruspins.
All oskets are vibbles.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 006/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are zemples.
All blickets are oskets.
All zemples are ruspins.
All oskets are vibbles.
Question: Does it follow that all vibbles are blickets?
Answer:
```

## 006/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are tivaks.
All tivaks are tufas.
Question: Does it follow that all daxes are tufas?
Answer:
```

## 006/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are tivaks.
All tivaks are tufas.
Question: Does it follow that all tufas are daxes?
Answer:
```

## 007/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are daxes.
All daxes are xandles.
Question: Does it follow that all nerps are daxes?
Answer:
```

## 007/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are daxes.
All daxes are xandles.
Question: Does it follow that all daxes are nerps?
Answer:
```

## 007/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are daxes.
All daxes are xandles.
Question: Does it follow that all nerps are xandles?
Answer:
```

## 007/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are daxes.
All daxes are xandles.
Question: Does it follow that all xandles are nerps?
Answer:
```

## 007/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are zorks.
All daxes are xandles.
Question: Does it follow that all nerps are xandles?
Answer:
```

## 007/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are daxes.
All zorks are xandles.
Question: Does it follow that all nerps are xandles?
Answer:
```

## 007/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are xandles.
All nerps are daxes.
Question: Does it follow that all nerps are xandles?
Answer:
```

## 007/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are xandles.
All nerps are daxes.
Question: Does it follow that all xandles are nerps?
Answer:
```

## 007/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are daxes.
All zorks are zemples.
All zemples are shalds.
All daxes are xandles.
Question: Does it follow that all nerps are xandles?
Answer:
```

## 007/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are daxes.
All zorks are zemples.
All zemples are shalds.
All daxes are xandles.
Question: Does it follow that all xandles are nerps?
Answer:
```

## 007/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are ruspins.
All ruspins are kelbrins.
Question: Does it follow that all vibbles are kelbrins?
Answer:
```

## 007/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are ruspins.
All ruspins are kelbrins.
Question: Does it follow that all kelbrins are vibbles?
Answer:
```

## 008/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are welbins.
All nerps are zemples.
Question: Does it follow that all zemples are welbins?
Answer:
```

## 008/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are welbins.
All nerps are zemples.
Question: Does it follow that all welbins are zemples?
Answer:
```

## 008/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are welbins.
All nerps are zemples.
Question: Does it follow that all nerps are welbins?
Answer:
```

## 008/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are welbins.
All nerps are zemples.
Question: Does it follow that all welbins are nerps?
Answer:
```

## 008/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are welbins.
All nerps are crundles.
Question: Does it follow that all nerps are welbins?
Answer:
```

## 008/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are welbins.
All nerps are zemples.
Question: Does it follow that all nerps are welbins?
Answer:
```

## 008/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are zemples.
All zemples are welbins.
Question: Does it follow that all nerps are welbins?
Answer:
```

## 008/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are zemples.
All zemples are welbins.
Question: Does it follow that all welbins are nerps?
Answer:
```

## 008/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are zemples.
All oskets are quavels.
All crundles are oskets.
All zemples are welbins.
Question: Does it follow that all nerps are welbins?
Answer:
```

## 008/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are zemples.
All oskets are quavels.
All crundles are oskets.
All zemples are welbins.
Question: Does it follow that all welbins are nerps?
Answer:
```

## 008/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are zeltrons.
All vibbles are sprocks.
Question: Does it follow that all vibbles are zeltrons?
Answer:
```

## 008/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are zeltrons.
All vibbles are sprocks.
Question: Does it follow that all zeltrons are vibbles?
Answer:
```

## 009/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All zemples are quavels.
Question: Does it follow that all zemples are quavels?
Answer:
```

## 009/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All zemples are quavels.
Question: Does it follow that all quavels are zemples?
Answer:
```

## 009/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All zemples are quavels.
Question: Does it follow that all vromps are quavels?
Answer:
```

## 009/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All zemples are quavels.
Question: Does it follow that all quavels are vromps?
Answer:
```

## 009/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are snorps.
All zemples are quavels.
Question: Does it follow that all vromps are quavels?
Answer:
```

## 009/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All snorps are quavels.
Question: Does it follow that all vromps are quavels?
Answer:
```

## 009/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are quavels.
All vromps are zemples.
Question: Does it follow that all vromps are quavels?
Answer:
```

## 009/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are quavels.
All vromps are zemples.
Question: Does it follow that all quavels are vromps?
Answer:
```

## 009/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are quavels.
All snorps are brovets.
All vromps are zemples.
All brovets are shalds.
Question: Does it follow that all vromps are quavels?
Answer:
```

## 009/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are quavels.
All snorps are brovets.
All vromps are zemples.
All brovets are shalds.
Question: Does it follow that all quavels are vromps?
Answer:
```

## 009/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are lomits.
All lomits are daxes.
Question: Does it follow that all blickets are daxes?
Answer:
```

## 009/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are lomits.
All lomits are daxes.
Question: Does it follow that all daxes are blickets?
Answer:
```

## 010/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are tivaks.
All daxes are zeltrons.
Question: Does it follow that all daxes are zeltrons?
Answer:
```

## 010/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are tivaks.
All daxes are zeltrons.
Question: Does it follow that all zeltrons are daxes?
Answer:
```

## 010/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are tivaks.
All daxes are zeltrons.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 010/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are tivaks.
All daxes are zeltrons.
Question: Does it follow that all tivaks are daxes?
Answer:
```

## 010/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are tivaks.
All daxes are korvas.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 010/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tivaks.
All daxes are zeltrons.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 010/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are zeltrons.
All zeltrons are tivaks.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 010/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are zeltrons.
All zeltrons are tivaks.
Question: Does it follow that all tivaks are daxes?
Answer:
```

## 010/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All daxes are zeltrons.
All plinets are murdles.
All korvas are plinets.
All zeltrons are tivaks.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 010/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All daxes are zeltrons.
All plinets are murdles.
All korvas are plinets.
All zeltrons are tivaks.
Question: Does it follow that all tivaks are daxes?
Answer:
```

## 010/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vibbles.
All ruspins are oskets.
Question: Does it follow that all ruspins are vibbles?
Answer:
```

## 010/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vibbles.
All ruspins are oskets.
Question: Does it follow that all vibbles are ruspins?
Answer:
```

## 011/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are oskets.
All crundles are korvas.
Question: Does it follow that all crundles are korvas?
Answer:
```

## 011/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are oskets.
All crundles are korvas.
Question: Does it follow that all korvas are crundles?
Answer:
```

## 011/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are oskets.
All crundles are korvas.
Question: Does it follow that all crundles are oskets?
Answer:
```

## 011/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are oskets.
All crundles are korvas.
Question: Does it follow that all oskets are crundles?
Answer:
```

## 011/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are oskets.
All crundles are tufas.
Question: Does it follow that all crundles are oskets?
Answer:
```

## 011/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are oskets.
All crundles are korvas.
Question: Does it follow that all crundles are oskets?
Answer:
```

## 011/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are korvas.
All korvas are oskets.
Question: Does it follow that all crundles are oskets?
Answer:
```

## 011/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are korvas.
All korvas are oskets.
Question: Does it follow that all oskets are crundles?
Answer:
```

## 011/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are oskets.
All crundles are korvas.
All tufas are sprocks.
All sprocks are plinets.
Question: Does it follow that all crundles are oskets?
Answer:
```

## 011/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are oskets.
All crundles are korvas.
All tufas are sprocks.
All sprocks are plinets.
Question: Does it follow that all oskets are crundles?
Answer:
```

## 011/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are wugs.
All lomits are zeltrons.
Question: Does it follow that all lomits are wugs?
Answer:
```

## 011/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are wugs.
All lomits are zeltrons.
Question: Does it follow that all wugs are lomits?
Answer:
```

## 012/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are ruspins.
All jastles are nerps.
Question: Does it follow that all jastles are nerps?
Answer:
```

## 012/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are ruspins.
All jastles are nerps.
Question: Does it follow that all nerps are jastles?
Answer:
```

## 012/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are ruspins.
All jastles are nerps.
Question: Does it follow that all jastles are ruspins?
Answer:
```

## 012/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are ruspins.
All jastles are nerps.
Question: Does it follow that all ruspins are jastles?
Answer:
```

## 012/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are ruspins.
All jastles are helpons.
Question: Does it follow that all jastles are ruspins?
Answer:
```

## 012/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are ruspins.
All jastles are nerps.
Question: Does it follow that all jastles are ruspins?
Answer:
```

## 012/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are nerps.
All nerps are ruspins.
Question: Does it follow that all jastles are ruspins?
Answer:
```

## 012/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are nerps.
All nerps are ruspins.
Question: Does it follow that all ruspins are jastles?
Answer:
```

## 012/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are korvas.
All korvas are crundles.
All nerps are ruspins.
All jastles are nerps.
Question: Does it follow that all jastles are ruspins?
Answer:
```

## 012/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are korvas.
All korvas are crundles.
All nerps are ruspins.
All jastles are nerps.
Question: Does it follow that all ruspins are jastles?
Answer:
```

## 012/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are ulvets.
All prandils are zorks.
Question: Does it follow that all prandils are ulvets?
Answer:
```

## 012/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are ulvets.
All prandils are zorks.
Question: Does it follow that all ulvets are prandils?
Answer:
```

## 013/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are tufas.
All tufas are zorks.
Question: Does it follow that all tufas are zorks?
Answer:
```

## 013/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are tufas.
All tufas are zorks.
Question: Does it follow that all zorks are tufas?
Answer:
```

## 013/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are tufas.
All tufas are zorks.
Question: Does it follow that all ruspins are zorks?
Answer:
```

## 013/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are tufas.
All tufas are zorks.
Question: Does it follow that all zorks are ruspins?
Answer:
```

## 013/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are yorbits.
All tufas are zorks.
Question: Does it follow that all ruspins are zorks?
Answer:
```

## 013/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are tufas.
All yorbits are zorks.
Question: Does it follow that all ruspins are zorks?
Answer:
```

## 013/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are zorks.
All ruspins are tufas.
Question: Does it follow that all ruspins are zorks?
Answer:
```

## 013/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are zorks.
All ruspins are tufas.
Question: Does it follow that all zorks are ruspins?
Answer:
```

## 013/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are tufas.
All yorbits are sprocks.
All tufas are zorks.
All sprocks are snorps.
Question: Does it follow that all ruspins are zorks?
Answer:
```

## 013/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are tufas.
All yorbits are sprocks.
All tufas are zorks.
All sprocks are snorps.
Question: Does it follow that all zorks are ruspins?
Answer:
```

## 013/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are helpons.
All helpons are kelbrins.
Question: Does it follow that all jastles are kelbrins?
Answer:
```

## 013/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are helpons.
All helpons are kelbrins.
Question: Does it follow that all kelbrins are jastles?
Answer:
```

## 014/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are sprocks.
All sprocks are korvas.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 014/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are sprocks.
All sprocks are korvas.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 014/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are sprocks.
All sprocks are korvas.
Question: Does it follow that all zemples are korvas?
Answer:
```

## 014/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are sprocks.
All sprocks are korvas.
Question: Does it follow that all korvas are zemples?
Answer:
```

## 014/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are ruspins.
All sprocks are korvas.
Question: Does it follow that all zemples are korvas?
Answer:
```

## 014/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are sprocks.
All ruspins are korvas.
Question: Does it follow that all zemples are korvas?
Answer:
```

## 014/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are korvas.
All zemples are sprocks.
Question: Does it follow that all zemples are korvas?
Answer:
```

## 014/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are korvas.
All zemples are sprocks.
Question: Does it follow that all korvas are zemples?
Answer:
```

## 014/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are nufrons.
All sprocks are korvas.
All nufrons are tufas.
All zemples are sprocks.
Question: Does it follow that all zemples are korvas?
Answer:
```

## 014/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are nufrons.
All sprocks are korvas.
All nufrons are tufas.
All zemples are sprocks.
Question: Does it follow that all korvas are zemples?
Answer:
```

## 014/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are prandils.
All prandils are flomps.
Question: Does it follow that all nerps are flomps?
Answer:
```

## 014/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are prandils.
All prandils are flomps.
Question: Does it follow that all flomps are nerps?
Answer:
```

## 015/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are jastles.
All jastles are sprocks.
Question: Does it follow that all jastles are sprocks?
Answer:
```

## 015/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are jastles.
All jastles are sprocks.
Question: Does it follow that all sprocks are jastles?
Answer:
```

## 015/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are jastles.
All jastles are sprocks.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 015/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are jastles.
All jastles are sprocks.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 015/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are vromps.
All jastles are sprocks.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 015/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are jastles.
All vromps are sprocks.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 015/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are sprocks.
All korvas are jastles.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 015/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are sprocks.
All korvas are jastles.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 015/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are welbins.
All korvas are jastles.
All jastles are sprocks.
All welbins are prandils.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 015/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are welbins.
All korvas are jastles.
All jastles are sprocks.
All welbins are prandils.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 015/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are daxes.
All daxes are oskets.
Question: Does it follow that all brovets are oskets?
Answer:
```

## 015/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are daxes.
All daxes are oskets.
Question: Does it follow that all oskets are brovets?
Answer:
```

## 016/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are crundles.
All wugs are zorks.
Question: Does it follow that all zorks are crundles?
Answer:
```

## 016/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are crundles.
All wugs are zorks.
Question: Does it follow that all crundles are zorks?
Answer:
```

## 016/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are crundles.
All wugs are zorks.
Question: Does it follow that all wugs are crundles?
Answer:
```

## 016/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are crundles.
All wugs are zorks.
Question: Does it follow that all crundles are wugs?
Answer:
```

## 016/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are crundles.
All wugs are korvas.
Question: Does it follow that all wugs are crundles?
Answer:
```

## 016/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are crundles.
All wugs are zorks.
Question: Does it follow that all wugs are crundles?
Answer:
```

## 016/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are zorks.
All zorks are crundles.
Question: Does it follow that all wugs are crundles?
Answer:
```

## 016/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are zorks.
All zorks are crundles.
Question: Does it follow that all crundles are wugs?
Answer:
```

## 016/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are crundles.
All korvas are jastles.
All jastles are welbins.
All wugs are zorks.
Question: Does it follow that all wugs are crundles?
Answer:
```

## 016/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are crundles.
All korvas are jastles.
All jastles are welbins.
All wugs are zorks.
Question: Does it follow that all crundles are wugs?
Answer:
```

## 016/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are nufrons.
All zeltrons are tivaks.
Question: Does it follow that all zeltrons are nufrons?
Answer:
```

## 016/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are nufrons.
All zeltrons are tivaks.
Question: Does it follow that all nufrons are zeltrons?
Answer:
```

## 017/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are shalds.
All blickets are kelbrins.
Question: Does it follow that all kelbrins are shalds?
Answer:
```

## 017/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are shalds.
All blickets are kelbrins.
Question: Does it follow that all shalds are kelbrins?
Answer:
```

## 017/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are shalds.
All blickets are kelbrins.
Question: Does it follow that all blickets are shalds?
Answer:
```

## 017/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are shalds.
All blickets are kelbrins.
Question: Does it follow that all shalds are blickets?
Answer:
```

## 017/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are shalds.
All blickets are korvas.
Question: Does it follow that all blickets are shalds?
Answer:
```

## 017/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are shalds.
All blickets are kelbrins.
Question: Does it follow that all blickets are shalds?
Answer:
```

## 017/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are kelbrins.
All kelbrins are shalds.
Question: Does it follow that all blickets are shalds?
Answer:
```

## 017/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are kelbrins.
All kelbrins are shalds.
Question: Does it follow that all shalds are blickets?
Answer:
```

## 017/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are vromps.
All kelbrins are shalds.
All blickets are kelbrins.
All korvas are prandils.
Question: Does it follow that all blickets are shalds?
Answer:
```

## 017/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are vromps.
All kelbrins are shalds.
All blickets are kelbrins.
All korvas are prandils.
Question: Does it follow that all shalds are blickets?
Answer:
```

## 017/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are murdles.
All wugs are daxes.
Question: Does it follow that all wugs are murdles?
Answer:
```

## 017/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are murdles.
All wugs are daxes.
Question: Does it follow that all murdles are wugs?
Answer:
```

## 018/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are jastles.
All kelbrins are wugs.
Question: Does it follow that all wugs are jastles?
Answer:
```

## 018/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are jastles.
All kelbrins are wugs.
Question: Does it follow that all jastles are wugs?
Answer:
```

## 018/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are jastles.
All kelbrins are wugs.
Question: Does it follow that all kelbrins are jastles?
Answer:
```

## 018/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are jastles.
All kelbrins are wugs.
Question: Does it follow that all jastles are kelbrins?
Answer:
```

## 018/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are jastles.
All kelbrins are flomps.
Question: Does it follow that all kelbrins are jastles?
Answer:
```

## 018/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are jastles.
All kelbrins are wugs.
Question: Does it follow that all kelbrins are jastles?
Answer:
```

## 018/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are wugs.
All wugs are jastles.
Question: Does it follow that all kelbrins are jastles?
Answer:
```

## 018/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are wugs.
All wugs are jastles.
Question: Does it follow that all jastles are kelbrins?
Answer:
```

## 018/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All kelbrins are wugs.
All murdles are snorps.
All wugs are jastles.
All flomps are murdles.
Question: Does it follow that all kelbrins are jastles?
Answer:
```

## 018/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All kelbrins are wugs.
All murdles are snorps.
All wugs are jastles.
All flomps are murdles.
Question: Does it follow that all jastles are kelbrins?
Answer:
```

## 018/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are grivaks.
All korvas are brovets.
Question: Does it follow that all korvas are grivaks?
Answer:
```

## 018/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are grivaks.
All korvas are brovets.
Question: Does it follow that all grivaks are korvas?
Answer:
```

## 019/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are zemples.
All zemples are tufas.
Question: Does it follow that all zemples are tufas?
Answer:
```

## 019/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are zemples.
All zemples are tufas.
Question: Does it follow that all tufas are zemples?
Answer:
```

## 019/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are zemples.
All zemples are tufas.
Question: Does it follow that all quavels are tufas?
Answer:
```

## 019/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are zemples.
All zemples are tufas.
Question: Does it follow that all tufas are quavels?
Answer:
```

## 019/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are prandils.
All zemples are tufas.
Question: Does it follow that all quavels are tufas?
Answer:
```

## 019/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are zemples.
All prandils are tufas.
Question: Does it follow that all quavels are tufas?
Answer:
```

## 019/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are tufas.
All quavels are zemples.
Question: Does it follow that all quavels are tufas?
Answer:
```

## 019/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are tufas.
All quavels are zemples.
Question: Does it follow that all tufas are quavels?
Answer:
```

## 019/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are zemples.
All zorks are oskets.
All prandils are zorks.
All zemples are tufas.
Question: Does it follow that all quavels are tufas?
Answer:
```

## 019/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are zemples.
All zorks are oskets.
All prandils are zorks.
All zemples are tufas.
Question: Does it follow that all tufas are quavels?
Answer:
```

## 019/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are vibbles.
All vibbles are brovets.
Question: Does it follow that all murdles are brovets?
Answer:
```

## 019/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are vibbles.
All vibbles are brovets.
Question: Does it follow that all brovets are murdles?
Answer:
```

## 020/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are wugs.
All blickets are korvas.
Question: Does it follow that all korvas are wugs?
Answer:
```

## 020/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are wugs.
All blickets are korvas.
Question: Does it follow that all wugs are korvas?
Answer:
```

## 020/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are wugs.
All blickets are korvas.
Question: Does it follow that all blickets are wugs?
Answer:
```

## 020/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are wugs.
All blickets are korvas.
Question: Does it follow that all wugs are blickets?
Answer:
```

## 020/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are wugs.
All blickets are zemples.
Question: Does it follow that all blickets are wugs?
Answer:
```

## 020/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are wugs.
All blickets are korvas.
Question: Does it follow that all blickets are wugs?
Answer:
```

## 020/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are korvas.
All korvas are wugs.
Question: Does it follow that all blickets are wugs?
Answer:
```

## 020/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are korvas.
All korvas are wugs.
Question: Does it follow that all wugs are blickets?
Answer:
```

## 020/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All blickets are korvas.
All korvas are wugs.
All vibbles are shalds.
All zemples are vibbles.
Question: Does it follow that all blickets are wugs?
Answer:
```

## 020/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All blickets are korvas.
All korvas are wugs.
All vibbles are shalds.
All zemples are vibbles.
Question: Does it follow that all wugs are blickets?
Answer:
```

## 020/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are nerps.
All quavels are yorbits.
Question: Does it follow that all quavels are nerps?
Answer:
```

## 020/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are nerps.
All quavels are yorbits.
Question: Does it follow that all nerps are quavels?
Answer:
```

## 021/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are helpons.
All snorps are crundles.
Question: Does it follow that all snorps are crundles?
Answer:
```

## 021/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are helpons.
All snorps are crundles.
Question: Does it follow that all crundles are snorps?
Answer:
```

## 021/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are helpons.
All snorps are crundles.
Question: Does it follow that all snorps are helpons?
Answer:
```

## 021/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are helpons.
All snorps are crundles.
Question: Does it follow that all helpons are snorps?
Answer:
```

## 021/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are helpons.
All snorps are daxes.
Question: Does it follow that all snorps are helpons?
Answer:
```

## 021/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are helpons.
All snorps are crundles.
Question: Does it follow that all snorps are helpons?
Answer:
```

## 021/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are crundles.
All crundles are helpons.
Question: Does it follow that all snorps are helpons?
Answer:
```

## 021/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are crundles.
All crundles are helpons.
Question: Does it follow that all helpons are snorps?
Answer:
```

## 021/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are nufrons.
All daxes are sprocks.
All snorps are crundles.
All crundles are helpons.
Question: Does it follow that all snorps are helpons?
Answer:
```

## 021/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are nufrons.
All daxes are sprocks.
All snorps are crundles.
All crundles are helpons.
Question: Does it follow that all helpons are snorps?
Answer:
```

## 021/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are zorks.
All oskets are lomits.
Question: Does it follow that all oskets are zorks?
Answer:
```

## 021/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are zorks.
All oskets are lomits.
Question: Does it follow that all zorks are oskets?
Answer:
```

## 022/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are vibbles.
All vibbles are kelbrins.
Question: Does it follow that all nufrons are vibbles?
Answer:
```

## 022/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are vibbles.
All vibbles are kelbrins.
Question: Does it follow that all vibbles are nufrons?
Answer:
```

## 022/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are vibbles.
All vibbles are kelbrins.
Question: Does it follow that all nufrons are kelbrins?
Answer:
```

## 022/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are vibbles.
All vibbles are kelbrins.
Question: Does it follow that all kelbrins are nufrons?
Answer:
```

## 022/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are ruspins.
All vibbles are kelbrins.
Question: Does it follow that all nufrons are kelbrins?
Answer:
```

## 022/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are vibbles.
All ruspins are kelbrins.
Question: Does it follow that all nufrons are kelbrins?
Answer:
```

## 022/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are kelbrins.
All nufrons are vibbles.
Question: Does it follow that all nufrons are kelbrins?
Answer:
```

## 022/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are kelbrins.
All nufrons are vibbles.
Question: Does it follow that all kelbrins are nufrons?
Answer:
```

## 022/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are vibbles.
All oskets are quavels.
All ruspins are oskets.
All vibbles are kelbrins.
Question: Does it follow that all nufrons are kelbrins?
Answer:
```

## 022/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All nufrons are vibbles.
All oskets are quavels.
All ruspins are oskets.
All vibbles are kelbrins.
Question: Does it follow that all kelbrins are nufrons?
Answer:
```

## 022/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are sprocks.
All sprocks are flomps.
Question: Does it follow that all brovets are flomps?
Answer:
```

## 022/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are sprocks.
All sprocks are flomps.
Question: Does it follow that all flomps are brovets?
Answer:
```

## 023/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are wugs.
All oskets are kelbrins.
Question: Does it follow that all oskets are kelbrins?
Answer:
```

## 023/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are wugs.
All oskets are kelbrins.
Question: Does it follow that all kelbrins are oskets?
Answer:
```

## 023/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are wugs.
All oskets are kelbrins.
Question: Does it follow that all oskets are wugs?
Answer:
```

## 023/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are wugs.
All oskets are kelbrins.
Question: Does it follow that all wugs are oskets?
Answer:
```

## 023/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are wugs.
All oskets are ruspins.
Question: Does it follow that all oskets are wugs?
Answer:
```

## 023/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are wugs.
All oskets are kelbrins.
Question: Does it follow that all oskets are wugs?
Answer:
```

## 023/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are kelbrins.
All kelbrins are wugs.
Question: Does it follow that all oskets are wugs?
Answer:
```

## 023/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are kelbrins.
All kelbrins are wugs.
Question: Does it follow that all wugs are oskets?
Answer:
```

## 023/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are nerps.
All oskets are kelbrins.
All kelbrins are wugs.
All ruspins are sprocks.
Question: Does it follow that all oskets are wugs?
Answer:
```

## 023/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are nerps.
All oskets are kelbrins.
All kelbrins are wugs.
All ruspins are sprocks.
Question: Does it follow that all wugs are oskets?
Answer:
```

## 023/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are flomps.
All prandils are tufas.
Question: Does it follow that all prandils are flomps?
Answer:
```

## 023/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are flomps.
All prandils are tufas.
Question: Does it follow that all flomps are prandils?
Answer:
```

## 024/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are tufas.
All tufas are ulvets.
Question: Does it follow that all tufas are ulvets?
Answer:
```

## 024/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are tufas.
All tufas are ulvets.
Question: Does it follow that all ulvets are tufas?
Answer:
```

## 024/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are tufas.
All tufas are ulvets.
Question: Does it follow that all murdles are ulvets?
Answer:
```

## 024/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are tufas.
All tufas are ulvets.
Question: Does it follow that all ulvets are murdles?
Answer:
```

## 024/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are oskets.
All tufas are ulvets.
Question: Does it follow that all murdles are ulvets?
Answer:
```

## 024/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are tufas.
All oskets are ulvets.
Question: Does it follow that all murdles are ulvets?
Answer:
```

## 024/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are ulvets.
All murdles are tufas.
Question: Does it follow that all murdles are ulvets?
Answer:
```

## 024/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are ulvets.
All murdles are tufas.
Question: Does it follow that all ulvets are murdles?
Answer:
```

## 024/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are wugs.
All murdles are tufas.
All tufas are ulvets.
All wugs are sprocks.
Question: Does it follow that all murdles are ulvets?
Answer:
```

## 024/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are wugs.
All murdles are tufas.
All tufas are ulvets.
All wugs are sprocks.
Question: Does it follow that all ulvets are murdles?
Answer:
```

## 024/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are tivaks.
All tivaks are snorps.
Question: Does it follow that all vibbles are snorps?
Answer:
```

## 024/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are tivaks.
All tivaks are snorps.
Question: Does it follow that all snorps are vibbles?
Answer:
```

## 025/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are vromps.
All vromps are zorks.
Question: Does it follow that all murdles are vromps?
Answer:
```

## 025/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are vromps.
All vromps are zorks.
Question: Does it follow that all vromps are murdles?
Answer:
```

## 025/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are vromps.
All vromps are zorks.
Question: Does it follow that all murdles are zorks?
Answer:
```

## 025/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are vromps.
All vromps are zorks.
Question: Does it follow that all zorks are murdles?
Answer:
```

## 025/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are tivaks.
All vromps are zorks.
Question: Does it follow that all murdles are zorks?
Answer:
```

## 025/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are vromps.
All tivaks are zorks.
Question: Does it follow that all murdles are zorks?
Answer:
```

## 025/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zorks.
All murdles are vromps.
Question: Does it follow that all murdles are zorks?
Answer:
```

## 025/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zorks.
All murdles are vromps.
Question: Does it follow that all zorks are murdles?
Answer:
```

## 025/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are lomits.
All vromps are zorks.
All lomits are sprocks.
All murdles are vromps.
Question: Does it follow that all murdles are zorks?
Answer:
```

## 025/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are lomits.
All vromps are zorks.
All lomits are sprocks.
All murdles are vromps.
Question: Does it follow that all zorks are murdles?
Answer:
```

## 025/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are vibbles.
All vibbles are kelbrins.
Question: Does it follow that all zemples are kelbrins?
Answer:
```

## 025/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are vibbles.
All vibbles are kelbrins.
Question: Does it follow that all kelbrins are zemples?
Answer:
```

## 026/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are yorbits.
All ruspins are zemples.
Question: Does it follow that all ruspins are zemples?
Answer:
```

## 026/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are yorbits.
All ruspins are zemples.
Question: Does it follow that all zemples are ruspins?
Answer:
```

## 026/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are yorbits.
All ruspins are zemples.
Question: Does it follow that all ruspins are yorbits?
Answer:
```

## 026/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are yorbits.
All ruspins are zemples.
Question: Does it follow that all yorbits are ruspins?
Answer:
```

## 026/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are yorbits.
All ruspins are daxes.
Question: Does it follow that all ruspins are yorbits?
Answer:
```

## 026/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are yorbits.
All ruspins are zemples.
Question: Does it follow that all ruspins are yorbits?
Answer:
```

## 026/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are zemples.
All zemples are yorbits.
Question: Does it follow that all ruspins are yorbits?
Answer:
```

## 026/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are zemples.
All zemples are yorbits.
Question: Does it follow that all yorbits are ruspins?
Answer:
```

## 026/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are nufrons.
All zemples are yorbits.
All ruspins are zemples.
All nufrons are quavels.
Question: Does it follow that all ruspins are yorbits?
Answer:
```

## 026/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are nufrons.
All zemples are yorbits.
All ruspins are zemples.
All nufrons are quavels.
Question: Does it follow that all yorbits are ruspins?
Answer:
```

## 026/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are blickets.
All welbins are flomps.
Question: Does it follow that all welbins are blickets?
Answer:
```

## 026/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are blickets.
All welbins are flomps.
Question: Does it follow that all blickets are welbins?
Answer:
```

## 027/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are ruspins.
All ruspins are nerps.
Question: Does it follow that all crundles are ruspins?
Answer:
```

## 027/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are ruspins.
All ruspins are nerps.
Question: Does it follow that all ruspins are crundles?
Answer:
```

## 027/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are ruspins.
All ruspins are nerps.
Question: Does it follow that all crundles are nerps?
Answer:
```

## 027/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are ruspins.
All ruspins are nerps.
Question: Does it follow that all nerps are crundles?
Answer:
```

## 027/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are flomps.
All ruspins are nerps.
Question: Does it follow that all crundles are nerps?
Answer:
```

## 027/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are ruspins.
All flomps are nerps.
Question: Does it follow that all crundles are nerps?
Answer:
```

## 027/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are nerps.
All crundles are ruspins.
Question: Does it follow that all crundles are nerps?
Answer:
```

## 027/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are nerps.
All crundles are ruspins.
Question: Does it follow that all nerps are crundles?
Answer:
```

## 027/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All crundles are ruspins.
All ruspins are nerps.
All flomps are ulvets.
All ulvets are prandils.
Question: Does it follow that all crundles are nerps?
Answer:
```

## 027/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All crundles are ruspins.
All ruspins are nerps.
All flomps are ulvets.
All ulvets are prandils.
Question: Does it follow that all nerps are crundles?
Answer:
```

## 027/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are blickets.
All blickets are kelbrins.
Question: Does it follow that all oskets are kelbrins?
Answer:
```

## 027/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are blickets.
All blickets are kelbrins.
Question: Does it follow that all kelbrins are oskets?
Answer:
```

## 028/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are prandils.
All daxes are snorps.
Question: Does it follow that all snorps are prandils?
Answer:
```

## 028/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are prandils.
All daxes are snorps.
Question: Does it follow that all prandils are snorps?
Answer:
```

## 028/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are prandils.
All daxes are snorps.
Question: Does it follow that all daxes are prandils?
Answer:
```

## 028/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are prandils.
All daxes are snorps.
Question: Does it follow that all prandils are daxes?
Answer:
```

## 028/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are prandils.
All daxes are brovets.
Question: Does it follow that all daxes are prandils?
Answer:
```

## 028/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are prandils.
All daxes are snorps.
Question: Does it follow that all daxes are prandils?
Answer:
```

## 028/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are snorps.
All snorps are prandils.
Question: Does it follow that all daxes are prandils?
Answer:
```

## 028/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are snorps.
All snorps are prandils.
Question: Does it follow that all prandils are daxes?
Answer:
```

## 028/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All snorps are prandils.
All korvas are shalds.
All daxes are snorps.
All brovets are korvas.
Question: Does it follow that all daxes are prandils?
Answer:
```

## 028/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are prandils.
All korvas are shalds.
All daxes are snorps.
All brovets are korvas.
Question: Does it follow that all prandils are daxes?
Answer:
```

## 028/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are jastles.
All zorks are nufrons.
Question: Does it follow that all zorks are jastles?
Answer:
```

## 028/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are jastles.
All zorks are nufrons.
Question: Does it follow that all jastles are zorks?
Answer:
```

## 029/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All daxes are vibbles.
Question: Does it follow that all daxes are vibbles?
Answer:
```

## 029/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All daxes are vibbles.
Question: Does it follow that all vibbles are daxes?
Answer:
```

## 029/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All daxes are vibbles.
Question: Does it follow that all tivaks are vibbles?
Answer:
```

## 029/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All daxes are vibbles.
Question: Does it follow that all vibbles are tivaks?
Answer:
```

## 029/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are zemples.
All daxes are vibbles.
Question: Does it follow that all tivaks are vibbles?
Answer:
```

## 029/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All zemples are vibbles.
Question: Does it follow that all tivaks are vibbles?
Answer:
```

## 029/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are vibbles.
All tivaks are daxes.
Question: Does it follow that all tivaks are vibbles?
Answer:
```

## 029/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are vibbles.
All tivaks are daxes.
Question: Does it follow that all vibbles are tivaks?
Answer:
```

## 029/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are vibbles.
All oskets are jastles.
All tivaks are daxes.
All zemples are oskets.
Question: Does it follow that all tivaks are vibbles?
Answer:
```

## 029/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are vibbles.
All oskets are jastles.
All tivaks are daxes.
All zemples are oskets.
Question: Does it follow that all vibbles are tivaks?
Answer:
```

## 029/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are kelbrins.
All kelbrins are tufas.
Question: Does it follow that all sprocks are tufas?
Answer:
```

## 029/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are kelbrins.
All kelbrins are tufas.
Question: Does it follow that all tufas are sprocks?
Answer:
```

## 030/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are nufrons.
All nufrons are crundles.
Question: Does it follow that all vibbles are nufrons?
Answer:
```

## 030/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are nufrons.
All nufrons are crundles.
Question: Does it follow that all nufrons are vibbles?
Answer:
```

## 030/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are nufrons.
All nufrons are crundles.
Question: Does it follow that all vibbles are crundles?
Answer:
```

## 030/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are nufrons.
All nufrons are crundles.
Question: Does it follow that all crundles are vibbles?
Answer:
```

## 030/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are helpons.
All nufrons are crundles.
Question: Does it follow that all vibbles are crundles?
Answer:
```

## 030/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are nufrons.
All helpons are crundles.
Question: Does it follow that all vibbles are crundles?
Answer:
```

## 030/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are crundles.
All vibbles are nufrons.
Question: Does it follow that all vibbles are crundles?
Answer:
```

## 030/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are crundles.
All vibbles are nufrons.
Question: Does it follow that all crundles are vibbles?
Answer:
```

## 030/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are crundles.
All helpons are sprocks.
All vibbles are nufrons.
All sprocks are tivaks.
Question: Does it follow that all vibbles are crundles?
Answer:
```

## 030/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are crundles.
All helpons are sprocks.
All vibbles are nufrons.
All sprocks are tivaks.
Question: Does it follow that all crundles are vibbles?
Answer:
```

## 030/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are brovets.
All brovets are wugs.
Question: Does it follow that all flomps are wugs?
Answer:
```

## 030/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are brovets.
All brovets are wugs.
Question: Does it follow that all wugs are flomps?
Answer:
```

## 031/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are wugs.
All grivaks are vibbles.
Question: Does it follow that all vibbles are wugs?
Answer:
```

## 031/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are wugs.
All grivaks are vibbles.
Question: Does it follow that all wugs are vibbles?
Answer:
```

## 031/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are wugs.
All grivaks are vibbles.
Question: Does it follow that all grivaks are wugs?
Answer:
```

## 031/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are wugs.
All grivaks are vibbles.
Question: Does it follow that all wugs are grivaks?
Answer:
```

## 031/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are wugs.
All grivaks are flomps.
Question: Does it follow that all grivaks are wugs?
Answer:
```

## 031/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are wugs.
All grivaks are vibbles.
Question: Does it follow that all grivaks are wugs?
Answer:
```

## 031/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are vibbles.
All vibbles are wugs.
Question: Does it follow that all grivaks are wugs?
Answer:
```

## 031/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are vibbles.
All vibbles are wugs.
Question: Does it follow that all wugs are grivaks?
Answer:
```

## 031/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are jastles.
All grivaks are vibbles.
All vibbles are wugs.
All flomps are welbins.
Question: Does it follow that all grivaks are wugs?
Answer:
```

## 031/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are jastles.
All grivaks are vibbles.
All vibbles are wugs.
All flomps are welbins.
Question: Does it follow that all wugs are grivaks?
Answer:
```

## 031/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are crundles.
All nufrons are plinets.
Question: Does it follow that all nufrons are crundles?
Answer:
```

## 031/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are crundles.
All nufrons are plinets.
Question: Does it follow that all crundles are nufrons?
Answer:
```

## 032/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are nufrons.
All brovets are sprocks.
Question: Does it follow that all brovets are sprocks?
Answer:
```

## 032/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are nufrons.
All brovets are sprocks.
Question: Does it follow that all sprocks are brovets?
Answer:
```

## 032/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are nufrons.
All brovets are sprocks.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 032/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are nufrons.
All brovets are sprocks.
Question: Does it follow that all nufrons are brovets?
Answer:
```

## 032/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are nufrons.
All brovets are crundles.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 032/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are nufrons.
All brovets are sprocks.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 032/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are sprocks.
All sprocks are nufrons.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 032/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are sprocks.
All sprocks are nufrons.
Question: Does it follow that all nufrons are brovets?
Answer:
```

## 032/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All sprocks are nufrons.
All brovets are sprocks.
All crundles are wugs.
All wugs are lomits.
Question: Does it follow that all brovets are nufrons?
Answer:
```

## 032/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All sprocks are nufrons.
All brovets are sprocks.
All crundles are wugs.
All wugs are lomits.
Question: Does it follow that all nufrons are brovets?
Answer:
```

## 032/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are daxes.
All tufas are welbins.
Question: Does it follow that all tufas are daxes?
Answer:
```

## 032/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are daxes.
All tufas are welbins.
Question: Does it follow that all daxes are tufas?
Answer:
```

## 033/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are flomps.
All flomps are korvas.
Question: Does it follow that all kelbrins are flomps?
Answer:
```

## 033/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are flomps.
All flomps are korvas.
Question: Does it follow that all flomps are kelbrins?
Answer:
```

## 033/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are flomps.
All flomps are korvas.
Question: Does it follow that all kelbrins are korvas?
Answer:
```

## 033/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are flomps.
All flomps are korvas.
Question: Does it follow that all korvas are kelbrins?
Answer:
```

## 033/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are oskets.
All flomps are korvas.
Question: Does it follow that all kelbrins are korvas?
Answer:
```

## 033/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are flomps.
All oskets are korvas.
Question: Does it follow that all kelbrins are korvas?
Answer:
```

## 033/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are korvas.
All kelbrins are flomps.
Question: Does it follow that all kelbrins are korvas?
Answer:
```

## 033/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are korvas.
All kelbrins are flomps.
Question: Does it follow that all korvas are kelbrins?
Answer:
```

## 033/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are flomps.
All jastles are quavels.
All flomps are korvas.
All oskets are jastles.
Question: Does it follow that all kelbrins are korvas?
Answer:
```

## 033/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All kelbrins are flomps.
All jastles are quavels.
All flomps are korvas.
All oskets are jastles.
Question: Does it follow that all korvas are kelbrins?
Answer:
```

## 033/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are snorps.
All snorps are lomits.
Question: Does it follow that all zorks are lomits?
Answer:
```

## 033/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are snorps.
All snorps are lomits.
Question: Does it follow that all lomits are zorks?
Answer:
```

## 034/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are zemples.
All zemples are sprocks.
Question: Does it follow that all zemples are sprocks?
Answer:
```

## 034/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are zemples.
All zemples are sprocks.
Question: Does it follow that all sprocks are zemples?
Answer:
```

## 034/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are zemples.
All zemples are sprocks.
Question: Does it follow that all tufas are sprocks?
Answer:
```

## 034/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are zemples.
All zemples are sprocks.
Question: Does it follow that all sprocks are tufas?
Answer:
```

## 034/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are ruspins.
All zemples are sprocks.
Question: Does it follow that all tufas are sprocks?
Answer:
```

## 034/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are zemples.
All ruspins are sprocks.
Question: Does it follow that all tufas are sprocks?
Answer:
```

## 034/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are sprocks.
All tufas are zemples.
Question: Does it follow that all tufas are sprocks?
Answer:
```

## 034/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are sprocks.
All tufas are zemples.
Question: Does it follow that all sprocks are tufas?
Answer:
```

## 034/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are oskets.
All zemples are sprocks.
All ruspins are kelbrins.
All tufas are zemples.
Question: Does it follow that all tufas are sprocks?
Answer:
```

## 034/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are oskets.
All zemples are sprocks.
All ruspins are kelbrins.
All tufas are zemples.
Question: Does it follow that all sprocks are tufas?
Answer:
```

## 034/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are quavels.
All quavels are yorbits.
Question: Does it follow that all jastles are yorbits?
Answer:
```

## 034/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are quavels.
All quavels are yorbits.
Question: Does it follow that all yorbits are jastles?
Answer:
```

## 035/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are nerps.
All nerps are lomits.
Question: Does it follow that all nerps are lomits?
Answer:
```

## 035/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are nerps.
All nerps are lomits.
Question: Does it follow that all lomits are nerps?
Answer:
```

## 035/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are nerps.
All nerps are lomits.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 035/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are nerps.
All nerps are lomits.
Question: Does it follow that all lomits are korvas?
Answer:
```

## 035/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are zorks.
All nerps are lomits.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 035/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are nerps.
All zorks are lomits.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 035/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are lomits.
All korvas are nerps.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 035/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are lomits.
All korvas are nerps.
Question: Does it follow that all lomits are korvas?
Answer:
```

## 035/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are sprocks.
All nerps are lomits.
All korvas are nerps.
All zorks are wugs.
Question: Does it follow that all korvas are lomits?
Answer:
```

## 035/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are sprocks.
All nerps are lomits.
All korvas are nerps.
All zorks are wugs.
Question: Does it follow that all lomits are korvas?
Answer:
```

## 035/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are prandils.
All prandils are crundles.
Question: Does it follow that all grivaks are crundles?
Answer:
```

## 035/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are prandils.
All prandils are crundles.
Question: Does it follow that all crundles are grivaks?
Answer:
```

## 036/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are shalds.
All snorps are wugs.
Question: Does it follow that all snorps are wugs?
Answer:
```

## 036/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are shalds.
All snorps are wugs.
Question: Does it follow that all wugs are snorps?
Answer:
```

## 036/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are shalds.
All snorps are wugs.
Question: Does it follow that all snorps are shalds?
Answer:
```

## 036/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are shalds.
All snorps are wugs.
Question: Does it follow that all shalds are snorps?
Answer:
```

## 036/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are shalds.
All snorps are murdles.
Question: Does it follow that all snorps are shalds?
Answer:
```

## 036/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are shalds.
All snorps are wugs.
Question: Does it follow that all snorps are shalds?
Answer:
```

## 036/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are wugs.
All wugs are shalds.
Question: Does it follow that all snorps are shalds?
Answer:
```

## 036/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are wugs.
All wugs are shalds.
Question: Does it follow that all shalds are snorps?
Answer:
```

## 036/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are yorbits.
All murdles are oskets.
All wugs are shalds.
All snorps are wugs.
Question: Does it follow that all snorps are shalds?
Answer:
```

## 036/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are yorbits.
All murdles are oskets.
All wugs are shalds.
All snorps are wugs.
Question: Does it follow that all shalds are snorps?
Answer:
```

## 036/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are vromps.
All helpons are vibbles.
Question: Does it follow that all helpons are vromps?
Answer:
```

## 036/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are vromps.
All helpons are vibbles.
Question: Does it follow that all vromps are helpons?
Answer:
```

## 037/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are helpons.
All helpons are brovets.
Question: Does it follow that all helpons are brovets?
Answer:
```

## 037/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are helpons.
All helpons are brovets.
Question: Does it follow that all brovets are helpons?
Answer:
```

## 037/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are helpons.
All helpons are brovets.
Question: Does it follow that all daxes are brovets?
Answer:
```

## 037/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are helpons.
All helpons are brovets.
Question: Does it follow that all brovets are daxes?
Answer:
```

## 037/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are murdles.
All helpons are brovets.
Question: Does it follow that all daxes are brovets?
Answer:
```

## 037/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are helpons.
All murdles are brovets.
Question: Does it follow that all daxes are brovets?
Answer:
```

## 037/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are brovets.
All daxes are helpons.
Question: Does it follow that all daxes are brovets?
Answer:
```

## 037/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are brovets.
All daxes are helpons.
Question: Does it follow that all brovets are daxes?
Answer:
```

## 037/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All murdles are korvas.
All helpons are brovets.
All korvas are vromps.
All daxes are helpons.
Question: Does it follow that all daxes are brovets?
Answer:
```

## 037/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are korvas.
All helpons are brovets.
All korvas are vromps.
All daxes are helpons.
Question: Does it follow that all brovets are daxes?
Answer:
```

## 037/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are zemples.
All zemples are oskets.
Question: Does it follow that all tivaks are oskets?
Answer:
```

## 037/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are zemples.
All zemples are oskets.
Question: Does it follow that all oskets are tivaks?
Answer:
```

## 038/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are shalds.
All shalds are tivaks.
Question: Does it follow that all zemples are shalds?
Answer:
```

## 038/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are shalds.
All shalds are tivaks.
Question: Does it follow that all shalds are zemples?
Answer:
```

## 038/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are shalds.
All shalds are tivaks.
Question: Does it follow that all zemples are tivaks?
Answer:
```

## 038/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are shalds.
All shalds are tivaks.
Question: Does it follow that all tivaks are zemples?
Answer:
```

## 038/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are oskets.
All shalds are tivaks.
Question: Does it follow that all zemples are tivaks?
Answer:
```

## 038/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are shalds.
All oskets are tivaks.
Question: Does it follow that all zemples are tivaks?
Answer:
```

## 038/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are tivaks.
All zemples are shalds.
Question: Does it follow that all zemples are tivaks?
Answer:
```

## 038/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are tivaks.
All zemples are shalds.
Question: Does it follow that all tivaks are zemples?
Answer:
```

## 038/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are shalds.
All tufas are korvas.
All oskets are tufas.
All shalds are tivaks.
Question: Does it follow that all zemples are tivaks?
Answer:
```

## 038/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All zemples are shalds.
All tufas are korvas.
All oskets are tufas.
All shalds are tivaks.
Question: Does it follow that all tivaks are zemples?
Answer:
```

## 038/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are nerps.
All nerps are lomits.
Question: Does it follow that all blickets are lomits?
Answer:
```

## 038/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are nerps.
All nerps are lomits.
Question: Does it follow that all lomits are blickets?
Answer:
```

## 039/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are zemples.
All helpons are prandils.
Question: Does it follow that all helpons are prandils?
Answer:
```

## 039/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are zemples.
All helpons are prandils.
Question: Does it follow that all prandils are helpons?
Answer:
```

## 039/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are zemples.
All helpons are prandils.
Question: Does it follow that all helpons are zemples?
Answer:
```

## 039/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are zemples.
All helpons are prandils.
Question: Does it follow that all zemples are helpons?
Answer:
```

## 039/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are zemples.
All helpons are yorbits.
Question: Does it follow that all helpons are zemples?
Answer:
```

## 039/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are zemples.
All helpons are prandils.
Question: Does it follow that all helpons are zemples?
Answer:
```

## 039/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are prandils.
All prandils are zemples.
Question: Does it follow that all helpons are zemples?
Answer:
```

## 039/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are prandils.
All prandils are zemples.
Question: Does it follow that all zemples are helpons?
Answer:
```

## 039/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are zemples.
All helpons are prandils.
All yorbits are kelbrins.
All kelbrins are tufas.
Question: Does it follow that all helpons are zemples?
Answer:
```

## 039/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are zemples.
All helpons are prandils.
All yorbits are kelbrins.
All kelbrins are tufas.
Question: Does it follow that all zemples are helpons?
Answer:
```

## 039/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are vibbles.
All wugs are sprocks.
Question: Does it follow that all wugs are vibbles?
Answer:
```

## 039/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are vibbles.
All wugs are sprocks.
Question: Does it follow that all vibbles are wugs?
Answer:
```

## 040/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are kelbrins.
All kelbrins are snorps.
Question: Does it follow that all tivaks are kelbrins?
Answer:
```

## 040/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are kelbrins.
All kelbrins are snorps.
Question: Does it follow that all kelbrins are tivaks?
Answer:
```

## 040/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are kelbrins.
All kelbrins are snorps.
Question: Does it follow that all tivaks are snorps?
Answer:
```

## 040/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are kelbrins.
All kelbrins are snorps.
Question: Does it follow that all snorps are tivaks?
Answer:
```

## 040/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are zemples.
All kelbrins are snorps.
Question: Does it follow that all tivaks are snorps?
Answer:
```

## 040/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are kelbrins.
All zemples are snorps.
Question: Does it follow that all tivaks are snorps?
Answer:
```

## 040/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are snorps.
All tivaks are kelbrins.
Question: Does it follow that all tivaks are snorps?
Answer:
```

## 040/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are snorps.
All tivaks are kelbrins.
Question: Does it follow that all snorps are tivaks?
Answer:
```

## 040/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are kelbrins.
All zemples are korvas.
All kelbrins are snorps.
All korvas are yorbits.
Question: Does it follow that all tivaks are snorps?
Answer:
```

## 040/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are kelbrins.
All zemples are korvas.
All kelbrins are snorps.
All korvas are yorbits.
Question: Does it follow that all snorps are tivaks?
Answer:
```

## 040/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are brovets.
All brovets are wugs.
Question: Does it follow that all quavels are wugs?
Answer:
```

## 040/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are brovets.
All brovets are wugs.
Question: Does it follow that all wugs are quavels?
Answer:
```

## 041/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are ruspins.
All ruspins are snorps.
Question: Does it follow that all brovets are ruspins?
Answer:
```

## 041/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are ruspins.
All ruspins are snorps.
Question: Does it follow that all ruspins are brovets?
Answer:
```

## 041/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are ruspins.
All ruspins are snorps.
Question: Does it follow that all brovets are snorps?
Answer:
```

## 041/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are ruspins.
All ruspins are snorps.
Question: Does it follow that all snorps are brovets?
Answer:
```

## 041/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are blickets.
All ruspins are snorps.
Question: Does it follow that all brovets are snorps?
Answer:
```

## 041/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are ruspins.
All blickets are snorps.
Question: Does it follow that all brovets are snorps?
Answer:
```

## 041/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are snorps.
All brovets are ruspins.
Question: Does it follow that all brovets are snorps?
Answer:
```

## 041/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are snorps.
All brovets are ruspins.
Question: Does it follow that all snorps are brovets?
Answer:
```

## 041/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All ruspins are snorps.
All blickets are prandils.
All prandils are sprocks.
All brovets are ruspins.
Question: Does it follow that all brovets are snorps?
Answer:
```

## 041/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are snorps.
All blickets are prandils.
All prandils are sprocks.
All brovets are ruspins.
Question: Does it follow that all snorps are brovets?
Answer:
```

## 041/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are crundles.
All crundles are zorks.
Question: Does it follow that all daxes are zorks?
Answer:
```

## 041/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are crundles.
All crundles are zorks.
Question: Does it follow that all zorks are daxes?
Answer:
```

## 042/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are tivaks.
All daxes are shalds.
Question: Does it follow that all daxes are shalds?
Answer:
```

## 042/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are tivaks.
All daxes are shalds.
Question: Does it follow that all shalds are daxes?
Answer:
```

## 042/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are tivaks.
All daxes are shalds.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 042/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are tivaks.
All daxes are shalds.
Question: Does it follow that all tivaks are daxes?
Answer:
```

## 042/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are tivaks.
All daxes are tufas.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 042/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are tivaks.
All daxes are shalds.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 042/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are shalds.
All shalds are tivaks.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 042/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are shalds.
All shalds are tivaks.
Question: Does it follow that all tivaks are daxes?
Answer:
```

## 042/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are shalds.
All lomits are korvas.
All shalds are tivaks.
All tufas are lomits.
Question: Does it follow that all daxes are tivaks?
Answer:
```

## 042/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are shalds.
All lomits are korvas.
All shalds are tivaks.
All tufas are lomits.
Question: Does it follow that all tivaks are daxes?
Answer:
```

## 042/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are murdles.
All snorps are jastles.
Question: Does it follow that all snorps are murdles?
Answer:
```

## 042/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are murdles.
All snorps are jastles.
Question: Does it follow that all murdles are snorps?
Answer:
```

## 043/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are vibbles.
All ruspins are kelbrins.
Question: Does it follow that all kelbrins are vibbles?
Answer:
```

## 043/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are vibbles.
All ruspins are kelbrins.
Question: Does it follow that all vibbles are kelbrins?
Answer:
```

## 043/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are vibbles.
All ruspins are kelbrins.
Question: Does it follow that all ruspins are vibbles?
Answer:
```

## 043/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are vibbles.
All ruspins are kelbrins.
Question: Does it follow that all vibbles are ruspins?
Answer:
```

## 043/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are vibbles.
All ruspins are prandils.
Question: Does it follow that all ruspins are vibbles?
Answer:
```

## 043/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are vibbles.
All ruspins are kelbrins.
Question: Does it follow that all ruspins are vibbles?
Answer:
```

## 043/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are kelbrins.
All kelbrins are vibbles.
Question: Does it follow that all ruspins are vibbles?
Answer:
```

## 043/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are kelbrins.
All kelbrins are vibbles.
Question: Does it follow that all vibbles are ruspins?
Answer:
```

## 043/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are vibbles.
All ruspins are kelbrins.
All sprocks are nufrons.
All prandils are sprocks.
Question: Does it follow that all ruspins are vibbles?
Answer:
```

## 043/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are vibbles.
All ruspins are kelbrins.
All sprocks are nufrons.
All prandils are sprocks.
Question: Does it follow that all vibbles are ruspins?
Answer:
```

## 043/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are helpons.
All oskets are jastles.
Question: Does it follow that all oskets are helpons?
Answer:
```

## 043/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are helpons.
All oskets are jastles.
Question: Does it follow that all helpons are oskets?
Answer:
```

## 044/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are plinets.
All tufas are snorps.
Question: Does it follow that all tufas are snorps?
Answer:
```

## 044/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are plinets.
All tufas are snorps.
Question: Does it follow that all snorps are tufas?
Answer:
```

## 044/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are plinets.
All tufas are snorps.
Question: Does it follow that all tufas are plinets?
Answer:
```

## 044/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are plinets.
All tufas are snorps.
Question: Does it follow that all plinets are tufas?
Answer:
```

## 044/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are plinets.
All tufas are prandils.
Question: Does it follow that all tufas are plinets?
Answer:
```

## 044/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are plinets.
All tufas are snorps.
Question: Does it follow that all tufas are plinets?
Answer:
```

## 044/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are snorps.
All snorps are plinets.
Question: Does it follow that all tufas are plinets?
Answer:
```

## 044/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are snorps.
All snorps are plinets.
Question: Does it follow that all plinets are tufas?
Answer:
```

## 044/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are kelbrins.
All snorps are plinets.
All kelbrins are zemples.
All tufas are snorps.
Question: Does it follow that all tufas are plinets?
Answer:
```

## 044/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are kelbrins.
All snorps are plinets.
All kelbrins are zemples.
All tufas are snorps.
Question: Does it follow that all plinets are tufas?
Answer:
```

## 044/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are grivaks.
All crundles are korvas.
Question: Does it follow that all crundles are grivaks?
Answer:
```

## 044/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are grivaks.
All crundles are korvas.
Question: Does it follow that all grivaks are crundles?
Answer:
```

## 045/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are kelbrins.
All crundles are helpons.
Question: Does it follow that all helpons are kelbrins?
Answer:
```

## 045/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are kelbrins.
All crundles are helpons.
Question: Does it follow that all kelbrins are helpons?
Answer:
```

## 045/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are kelbrins.
All crundles are helpons.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 045/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are kelbrins.
All crundles are helpons.
Question: Does it follow that all kelbrins are crundles?
Answer:
```

## 045/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are kelbrins.
All crundles are wugs.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 045/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are kelbrins.
All crundles are helpons.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 045/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are helpons.
All helpons are kelbrins.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 045/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are helpons.
All helpons are kelbrins.
Question: Does it follow that all kelbrins are crundles?
Answer:
```

## 045/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are tivaks.
All helpons are kelbrins.
All wugs are zorks.
All crundles are helpons.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 045/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are tivaks.
All helpons are kelbrins.
All wugs are zorks.
All crundles are helpons.
Question: Does it follow that all kelbrins are crundles?
Answer:
```

## 045/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are oskets.
All vromps are zemples.
Question: Does it follow that all vromps are oskets?
Answer:
```

## 045/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are oskets.
All vromps are zemples.
Question: Does it follow that all oskets are vromps?
Answer:
```

## 046/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are crundles.
All nerps are zeltrons.
Question: Does it follow that all nerps are zeltrons?
Answer:
```

## 046/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are crundles.
All nerps are zeltrons.
Question: Does it follow that all zeltrons are nerps?
Answer:
```

## 046/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are crundles.
All nerps are zeltrons.
Question: Does it follow that all nerps are crundles?
Answer:
```

## 046/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are crundles.
All nerps are zeltrons.
Question: Does it follow that all crundles are nerps?
Answer:
```

## 046/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are crundles.
All nerps are plinets.
Question: Does it follow that all nerps are crundles?
Answer:
```

## 046/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are crundles.
All nerps are zeltrons.
Question: Does it follow that all nerps are crundles?
Answer:
```

## 046/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are zeltrons.
All zeltrons are crundles.
Question: Does it follow that all nerps are crundles?
Answer:
```

## 046/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are zeltrons.
All zeltrons are crundles.
Question: Does it follow that all crundles are nerps?
Answer:
```

## 046/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All zeltrons are crundles.
All brovets are jastles.
All nerps are zeltrons.
All plinets are brovets.
Question: Does it follow that all nerps are crundles?
Answer:
```

## 046/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All zeltrons are crundles.
All brovets are jastles.
All nerps are zeltrons.
All plinets are brovets.
Question: Does it follow that all crundles are nerps?
Answer:
```

## 046/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are lomits.
All quavels are ruspins.
Question: Does it follow that all quavels are lomits?
Answer:
```

## 046/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are lomits.
All quavels are ruspins.
Question: Does it follow that all lomits are quavels?
Answer:
```

## 047/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are helpons.
All helpons are kelbrins.
Question: Does it follow that all helpons are kelbrins?
Answer:
```

## 047/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are helpons.
All helpons are kelbrins.
Question: Does it follow that all kelbrins are helpons?
Answer:
```

## 047/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are helpons.
All helpons are kelbrins.
Question: Does it follow that all brovets are kelbrins?
Answer:
```

## 047/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are helpons.
All helpons are kelbrins.
Question: Does it follow that all kelbrins are brovets?
Answer:
```

## 047/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are tufas.
All helpons are kelbrins.
Question: Does it follow that all brovets are kelbrins?
Answer:
```

## 047/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are helpons.
All tufas are kelbrins.
Question: Does it follow that all brovets are kelbrins?
Answer:
```

## 047/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are kelbrins.
All brovets are helpons.
Question: Does it follow that all brovets are kelbrins?
Answer:
```

## 047/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are kelbrins.
All brovets are helpons.
Question: Does it follow that all kelbrins are brovets?
Answer:
```

## 047/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are helpons.
All daxes are tivaks.
All tufas are daxes.
All helpons are kelbrins.
Question: Does it follow that all brovets are kelbrins?
Answer:
```

## 047/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All brovets are helpons.
All daxes are tivaks.
All tufas are daxes.
All helpons are kelbrins.
Question: Does it follow that all kelbrins are brovets?
Answer:
```

## 047/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are lomits.
All lomits are ruspins.
Question: Does it follow that all oskets are ruspins?
Answer:
```

## 047/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are lomits.
All lomits are ruspins.
Question: Does it follow that all ruspins are oskets?
Answer:
```

## 048/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are grivaks.
All shalds are blickets.
Question: Does it follow that all shalds are blickets?
Answer:
```

## 048/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are grivaks.
All shalds are blickets.
Question: Does it follow that all blickets are shalds?
Answer:
```

## 048/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are grivaks.
All shalds are blickets.
Question: Does it follow that all shalds are grivaks?
Answer:
```

## 048/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are grivaks.
All shalds are blickets.
Question: Does it follow that all grivaks are shalds?
Answer:
```

## 048/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are grivaks.
All shalds are xandles.
Question: Does it follow that all shalds are grivaks?
Answer:
```

## 048/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are grivaks.
All shalds are blickets.
Question: Does it follow that all shalds are grivaks?
Answer:
```

## 048/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are blickets.
All blickets are grivaks.
Question: Does it follow that all shalds are grivaks?
Answer:
```

## 048/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are blickets.
All blickets are grivaks.
Question: Does it follow that all grivaks are shalds?
Answer:
```

## 048/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All shalds are blickets.
All daxes are prandils.
All xandles are daxes.
All blickets are grivaks.
Question: Does it follow that all shalds are grivaks?
Answer:
```

## 048/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All shalds are blickets.
All daxes are prandils.
All xandles are daxes.
All blickets are grivaks.
Question: Does it follow that all grivaks are shalds?
Answer:
```

## 048/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ulvets are tufas.
All nufrons are ulvets.
Question: Does it follow that all nufrons are tufas?
Answer:
```

## 048/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ulvets are tufas.
All nufrons are ulvets.
Question: Does it follow that all tufas are nufrons?
Answer:
```

## 049/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are brovets.
All brovets are zorks.
Question: Does it follow that all crundles are brovets?
Answer:
```

## 049/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are brovets.
All brovets are zorks.
Question: Does it follow that all brovets are crundles?
Answer:
```

## 049/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are brovets.
All brovets are zorks.
Question: Does it follow that all crundles are zorks?
Answer:
```

## 049/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are brovets.
All brovets are zorks.
Question: Does it follow that all zorks are crundles?
Answer:
```

## 049/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are quavels.
All brovets are zorks.
Question: Does it follow that all crundles are zorks?
Answer:
```

## 049/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are brovets.
All quavels are zorks.
Question: Does it follow that all crundles are zorks?
Answer:
```

## 049/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are zorks.
All crundles are brovets.
Question: Does it follow that all crundles are zorks?
Answer:
```

## 049/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are zorks.
All crundles are brovets.
Question: Does it follow that all zorks are crundles?
Answer:
```

## 049/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are nufrons.
All quavels are snorps.
All brovets are zorks.
All crundles are brovets.
Question: Does it follow that all crundles are zorks?
Answer:
```

## 049/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are nufrons.
All quavels are snorps.
All brovets are zorks.
All crundles are brovets.
Question: Does it follow that all zorks are crundles?
Answer:
```

## 049/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are lomits.
All lomits are prandils.
Question: Does it follow that all helpons are prandils?
Answer:
```

## 049/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are lomits.
All lomits are prandils.
Question: Does it follow that all prandils are helpons?
Answer:
```

## 050/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All ruspins are oskets.
Question: Does it follow that all oskets are nufrons?
Answer:
```

## 050/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All ruspins are oskets.
Question: Does it follow that all nufrons are oskets?
Answer:
```

## 050/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All ruspins are oskets.
Question: Does it follow that all ruspins are nufrons?
Answer:
```

## 050/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All ruspins are oskets.
Question: Does it follow that all nufrons are ruspins?
Answer:
```

## 050/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All ruspins are kelbrins.
Question: Does it follow that all ruspins are nufrons?
Answer:
```

## 050/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are nufrons.
All ruspins are oskets.
Question: Does it follow that all ruspins are nufrons?
Answer:
```

## 050/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are oskets.
All oskets are nufrons.
Question: Does it follow that all ruspins are nufrons?
Answer:
```

## 050/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are oskets.
All oskets are nufrons.
Question: Does it follow that all nufrons are ruspins?
Answer:
```

## 050/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are oskets.
All kelbrins are crundles.
All crundles are prandils.
All oskets are nufrons.
Question: Does it follow that all ruspins are nufrons?
Answer:
```

## 050/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are oskets.
All kelbrins are crundles.
All crundles are prandils.
All oskets are nufrons.
Question: Does it follow that all nufrons are ruspins?
Answer:
```

## 050/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are quavels.
All jastles are tufas.
Question: Does it follow that all jastles are quavels?
Answer:
```

## 050/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are quavels.
All jastles are tufas.
Question: Does it follow that all quavels are jastles?
Answer:
```

## 051/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All flomps are blickets.
Question: Does it follow that all flomps are blickets?
Answer:
```

## 051/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All flomps are blickets.
Question: Does it follow that all blickets are flomps?
Answer:
```

## 051/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All flomps are blickets.
Question: Does it follow that all tivaks are blickets?
Answer:
```

## 051/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All flomps are blickets.
Question: Does it follow that all blickets are tivaks?
Answer:
```

## 051/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are welbins.
All flomps are blickets.
Question: Does it follow that all tivaks are blickets?
Answer:
```

## 051/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All welbins are blickets.
Question: Does it follow that all tivaks are blickets?
Answer:
```

## 051/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are blickets.
All tivaks are flomps.
Question: Does it follow that all tivaks are blickets?
Answer:
```

## 051/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are blickets.
All tivaks are flomps.
Question: Does it follow that all blickets are tivaks?
Answer:
```

## 051/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are blickets.
All tivaks are flomps.
All zeltrons are zorks.
All welbins are zeltrons.
Question: Does it follow that all tivaks are blickets?
Answer:
```

## 051/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All flomps are blickets.
All tivaks are flomps.
All zeltrons are zorks.
All welbins are zeltrons.
Question: Does it follow that all blickets are tivaks?
Answer:
```

## 051/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are nerps.
All nerps are lomits.
Question: Does it follow that all nufrons are lomits?
Answer:
```

## 051/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are nerps.
All nerps are lomits.
Question: Does it follow that all lomits are nufrons?
Answer:
```

## 052/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are blickets.
All blickets are xandles.
Question: Does it follow that all blickets are xandles?
Answer:
```

## 052/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are blickets.
All blickets are xandles.
Question: Does it follow that all xandles are blickets?
Answer:
```

## 052/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are blickets.
All blickets are xandles.
Question: Does it follow that all shalds are xandles?
Answer:
```

## 052/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are blickets.
All blickets are xandles.
Question: Does it follow that all xandles are shalds?
Answer:
```

## 052/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are zorks.
All blickets are xandles.
Question: Does it follow that all shalds are xandles?
Answer:
```

## 052/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are blickets.
All zorks are xandles.
Question: Does it follow that all shalds are xandles?
Answer:
```

## 052/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are xandles.
All shalds are blickets.
Question: Does it follow that all shalds are xandles?
Answer:
```

## 052/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are xandles.
All shalds are blickets.
Question: Does it follow that all xandles are shalds?
Answer:
```

## 052/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are oskets.
All shalds are blickets.
All blickets are xandles.
All zorks are vibbles.
Question: Does it follow that all shalds are xandles?
Answer:
```

## 052/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are oskets.
All shalds are blickets.
All blickets are xandles.
All zorks are vibbles.
Question: Does it follow that all xandles are shalds?
Answer:
```

## 052/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are yorbits.
All yorbits are brovets.
Question: Does it follow that all vromps are brovets?
Answer:
```

## 052/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are yorbits.
All yorbits are brovets.
Question: Does it follow that all brovets are vromps?
Answer:
```

## 053/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All flomps are korvas.
Question: Does it follow that all flomps are korvas?
Answer:
```

## 053/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All flomps are korvas.
Question: Does it follow that all korvas are flomps?
Answer:
```

## 053/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All flomps are korvas.
Question: Does it follow that all tivaks are korvas?
Answer:
```

## 053/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All flomps are korvas.
Question: Does it follow that all korvas are tivaks?
Answer:
```

## 053/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are quavels.
All flomps are korvas.
Question: Does it follow that all tivaks are korvas?
Answer:
```

## 053/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are flomps.
All quavels are korvas.
Question: Does it follow that all tivaks are korvas?
Answer:
```

## 053/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are korvas.
All tivaks are flomps.
Question: Does it follow that all tivaks are korvas?
Answer:
```

## 053/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are korvas.
All tivaks are flomps.
Question: Does it follow that all korvas are tivaks?
Answer:
```

## 053/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are korvas.
All lomits are vibbles.
All tivaks are flomps.
All quavels are lomits.
Question: Does it follow that all tivaks are korvas?
Answer:
```

## 053/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are korvas.
All lomits are vibbles.
All tivaks are flomps.
All quavels are lomits.
Question: Does it follow that all korvas are tivaks?
Answer:
```

## 053/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are zorks.
All zorks are jastles.
Question: Does it follow that all shalds are jastles?
Answer:
```

## 053/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are zorks.
All zorks are jastles.
Question: Does it follow that all jastles are shalds?
Answer:
```

## 054/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are zeltrons.
All zeltrons are jastles.
Question: Does it follow that all blickets are zeltrons?
Answer:
```

## 054/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are zeltrons.
All zeltrons are jastles.
Question: Does it follow that all zeltrons are blickets?
Answer:
```

## 054/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are zeltrons.
All zeltrons are jastles.
Question: Does it follow that all blickets are jastles?
Answer:
```

## 054/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are zeltrons.
All zeltrons are jastles.
Question: Does it follow that all jastles are blickets?
Answer:
```

## 054/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are prandils.
All zeltrons are jastles.
Question: Does it follow that all blickets are jastles?
Answer:
```

## 054/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are zeltrons.
All prandils are jastles.
Question: Does it follow that all blickets are jastles?
Answer:
```

## 054/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are jastles.
All blickets are zeltrons.
Question: Does it follow that all blickets are jastles?
Answer:
```

## 054/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are jastles.
All blickets are zeltrons.
Question: Does it follow that all jastles are blickets?
Answer:
```

## 054/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All prandils are grivaks.
All zeltrons are jastles.
All grivaks are sprocks.
All blickets are zeltrons.
Question: Does it follow that all blickets are jastles?
Answer:
```

## 054/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All prandils are grivaks.
All zeltrons are jastles.
All grivaks are sprocks.
All blickets are zeltrons.
Question: Does it follow that all jastles are blickets?
Answer:
```

## 054/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are crundles.
All crundles are snorps.
Question: Does it follow that all daxes are snorps?
Answer:
```

## 054/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are crundles.
All crundles are snorps.
Question: Does it follow that all snorps are daxes?
Answer:
```

## 055/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are lomits.
All grivaks are crundles.
Question: Does it follow that all grivaks are crundles?
Answer:
```

## 055/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are lomits.
All grivaks are crundles.
Question: Does it follow that all crundles are grivaks?
Answer:
```

## 055/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are lomits.
All grivaks are crundles.
Question: Does it follow that all grivaks are lomits?
Answer:
```

## 055/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are lomits.
All grivaks are crundles.
Question: Does it follow that all lomits are grivaks?
Answer:
```

## 055/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are lomits.
All grivaks are plinets.
Question: Does it follow that all grivaks are lomits?
Answer:
```

## 055/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are lomits.
All grivaks are crundles.
Question: Does it follow that all grivaks are lomits?
Answer:
```

## 055/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are crundles.
All crundles are lomits.
Question: Does it follow that all grivaks are lomits?
Answer:
```

## 055/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are crundles.
All crundles are lomits.
Question: Does it follow that all lomits are grivaks?
Answer:
```

## 055/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are crundles.
All plinets are daxes.
All daxes are shalds.
All crundles are lomits.
Question: Does it follow that all grivaks are lomits?
Answer:
```

## 055/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are crundles.
All plinets are daxes.
All daxes are shalds.
All crundles are lomits.
Question: Does it follow that all lomits are grivaks?
Answer:
```

## 055/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are nufrons.
All zeltrons are flomps.
Question: Does it follow that all zeltrons are nufrons?
Answer:
```

## 055/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are nufrons.
All zeltrons are flomps.
Question: Does it follow that all nufrons are zeltrons?
Answer:
```

## 056/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are grivaks.
All ruspins are zemples.
Question: Does it follow that all zemples are grivaks?
Answer:
```

## 056/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are grivaks.
All ruspins are zemples.
Question: Does it follow that all grivaks are zemples?
Answer:
```

## 056/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are grivaks.
All ruspins are zemples.
Question: Does it follow that all ruspins are grivaks?
Answer:
```

## 056/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are grivaks.
All ruspins are zemples.
Question: Does it follow that all grivaks are ruspins?
Answer:
```

## 056/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are grivaks.
All ruspins are zeltrons.
Question: Does it follow that all ruspins are grivaks?
Answer:
```

## 056/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are grivaks.
All ruspins are zemples.
Question: Does it follow that all ruspins are grivaks?
Answer:
```

## 056/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are zemples.
All zemples are grivaks.
Question: Does it follow that all ruspins are grivaks?
Answer:
```

## 056/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are zemples.
All zemples are grivaks.
Question: Does it follow that all grivaks are ruspins?
Answer:
```

## 056/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All quavels are nerps.
All zemples are grivaks.
All zeltrons are quavels.
All ruspins are zemples.
Question: Does it follow that all ruspins are grivaks?
Answer:
```

## 056/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All quavels are nerps.
All zemples are grivaks.
All zeltrons are quavels.
All ruspins are zemples.
Question: Does it follow that all grivaks are ruspins?
Answer:
```

## 056/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are blickets.
All vromps are jastles.
Question: Does it follow that all vromps are blickets?
Answer:
```

## 056/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are blickets.
All vromps are jastles.
Question: Does it follow that all blickets are vromps?
Answer:
```

## 057/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are nerps.
All nerps are ruspins.
Question: Does it follow that all nerps are ruspins?
Answer:
```

## 057/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are nerps.
All nerps are ruspins.
Question: Does it follow that all ruspins are nerps?
Answer:
```

## 057/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are nerps.
All nerps are ruspins.
Question: Does it follow that all flomps are ruspins?
Answer:
```

## 057/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are nerps.
All nerps are ruspins.
Question: Does it follow that all ruspins are flomps?
Answer:
```

## 057/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are prandils.
All nerps are ruspins.
Question: Does it follow that all flomps are ruspins?
Answer:
```

## 057/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are nerps.
All prandils are ruspins.
Question: Does it follow that all flomps are ruspins?
Answer:
```

## 057/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are ruspins.
All flomps are nerps.
Question: Does it follow that all flomps are ruspins?
Answer:
```

## 057/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are ruspins.
All flomps are nerps.
Question: Does it follow that all ruspins are flomps?
Answer:
```

## 057/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are oskets.
All flomps are nerps.
All oskets are nufrons.
All nerps are ruspins.
Question: Does it follow that all flomps are ruspins?
Answer:
```

## 057/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are oskets.
All flomps are nerps.
All oskets are nufrons.
All nerps are ruspins.
Question: Does it follow that all ruspins are flomps?
Answer:
```

## 057/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are helpons.
All helpons are crundles.
Question: Does it follow that all tufas are crundles?
Answer:
```

## 057/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are helpons.
All helpons are crundles.
Question: Does it follow that all crundles are tufas?
Answer:
```

## 058/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are snorps.
All snorps are vibbles.
Question: Does it follow that all grivaks are snorps?
Answer:
```

## 058/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are snorps.
All snorps are vibbles.
Question: Does it follow that all snorps are grivaks?
Answer:
```

## 058/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are snorps.
All snorps are vibbles.
Question: Does it follow that all grivaks are vibbles?
Answer:
```

## 058/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are snorps.
All snorps are vibbles.
Question: Does it follow that all vibbles are grivaks?
Answer:
```

## 058/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are nufrons.
All snorps are vibbles.
Question: Does it follow that all grivaks are vibbles?
Answer:
```

## 058/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are snorps.
All nufrons are vibbles.
Question: Does it follow that all grivaks are vibbles?
Answer:
```

## 058/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are vibbles.
All grivaks are snorps.
Question: Does it follow that all grivaks are vibbles?
Answer:
```

## 058/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are vibbles.
All grivaks are snorps.
Question: Does it follow that all vibbles are grivaks?
Answer:
```

## 058/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are vibbles.
All nufrons are korvas.
All grivaks are snorps.
All korvas are jastles.
Question: Does it follow that all grivaks are vibbles?
Answer:
```

## 058/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are vibbles.
All nufrons are korvas.
All grivaks are snorps.
All korvas are jastles.
Question: Does it follow that all vibbles are grivaks?
Answer:
```

## 058/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are flomps.
All flomps are zorks.
Question: Does it follow that all oskets are zorks?
Answer:
```

## 058/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are flomps.
All flomps are zorks.
Question: Does it follow that all zorks are oskets?
Answer:
```

## 059/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are prandils.
All prandils are brovets.
Question: Does it follow that all prandils are brovets?
Answer:
```

## 059/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are prandils.
All prandils are brovets.
Question: Does it follow that all brovets are prandils?
Answer:
```

## 059/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are prandils.
All prandils are brovets.
Question: Does it follow that all tufas are brovets?
Answer:
```

## 059/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are prandils.
All prandils are brovets.
Question: Does it follow that all brovets are tufas?
Answer:
```

## 059/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are kelbrins.
All prandils are brovets.
Question: Does it follow that all tufas are brovets?
Answer:
```

## 059/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are prandils.
All kelbrins are brovets.
Question: Does it follow that all tufas are brovets?
Answer:
```

## 059/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are brovets.
All tufas are prandils.
Question: Does it follow that all tufas are brovets?
Answer:
```

## 059/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are brovets.
All tufas are prandils.
Question: Does it follow that all brovets are tufas?
Answer:
```

## 059/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are prandils.
All kelbrins are vibbles.
All vibbles are zorks.
All prandils are brovets.
Question: Does it follow that all tufas are brovets?
Answer:
```

## 059/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All tufas are prandils.
All kelbrins are vibbles.
All vibbles are zorks.
All prandils are brovets.
Question: Does it follow that all brovets are tufas?
Answer:
```

## 059/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are shalds.
All shalds are grivaks.
Question: Does it follow that all plinets are grivaks?
Answer:
```

## 059/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are shalds.
All shalds are grivaks.
Question: Does it follow that all grivaks are plinets?
Answer:
```

## 060/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are vibbles.
All vibbles are blickets.
Question: Does it follow that all xandles are vibbles?
Answer:
```

## 060/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are vibbles.
All vibbles are blickets.
Question: Does it follow that all vibbles are xandles?
Answer:
```

## 060/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are vibbles.
All vibbles are blickets.
Question: Does it follow that all xandles are blickets?
Answer:
```

## 060/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are vibbles.
All vibbles are blickets.
Question: Does it follow that all blickets are xandles?
Answer:
```

## 060/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are prandils.
All vibbles are blickets.
Question: Does it follow that all xandles are blickets?
Answer:
```

## 060/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are vibbles.
All prandils are blickets.
Question: Does it follow that all xandles are blickets?
Answer:
```

## 060/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are blickets.
All xandles are vibbles.
Question: Does it follow that all xandles are blickets?
Answer:
```

## 060/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are blickets.
All xandles are vibbles.
Question: Does it follow that all blickets are xandles?
Answer:
```

## 060/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are vibbles.
All ruspins are ulvets.
All prandils are ruspins.
All vibbles are blickets.
Question: Does it follow that all xandles are blickets?
Answer:
```

## 060/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All xandles are vibbles.
All ruspins are ulvets.
All prandils are ruspins.
All vibbles are blickets.
Question: Does it follow that all blickets are xandles?
Answer:
```

## 060/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are grivaks.
All grivaks are kelbrins.
Question: Does it follow that all lomits are kelbrins?
Answer:
```

## 060/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are grivaks.
All grivaks are kelbrins.
Question: Does it follow that all kelbrins are lomits?
Answer:
```

## 061/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are kelbrins.
All jastles are blickets.
Question: Does it follow that all blickets are kelbrins?
Answer:
```

## 061/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are kelbrins.
All jastles are blickets.
Question: Does it follow that all kelbrins are blickets?
Answer:
```

## 061/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are kelbrins.
All jastles are blickets.
Question: Does it follow that all jastles are kelbrins?
Answer:
```

## 061/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are kelbrins.
All jastles are blickets.
Question: Does it follow that all kelbrins are jastles?
Answer:
```

## 061/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are kelbrins.
All jastles are vromps.
Question: Does it follow that all jastles are kelbrins?
Answer:
```

## 061/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are kelbrins.
All jastles are blickets.
Question: Does it follow that all jastles are kelbrins?
Answer:
```

## 061/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are blickets.
All blickets are kelbrins.
Question: Does it follow that all jastles are kelbrins?
Answer:
```

## 061/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are blickets.
All blickets are kelbrins.
Question: Does it follow that all kelbrins are jastles?
Answer:
```

## 061/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All vromps are crundles.
All jastles are blickets.
All blickets are kelbrins.
All crundles are grivaks.
Question: Does it follow that all jastles are kelbrins?
Answer:
```

## 061/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All vromps are crundles.
All jastles are blickets.
All blickets are kelbrins.
All crundles are grivaks.
Question: Does it follow that all kelbrins are jastles?
Answer:
```

## 061/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are snorps.
All wugs are quavels.
Question: Does it follow that all wugs are snorps?
Answer:
```

## 061/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are snorps.
All wugs are quavels.
Question: Does it follow that all snorps are wugs?
Answer:
```

## 062/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are lomits.
All lomits are oskets.
Question: Does it follow that all lomits are oskets?
Answer:
```

## 062/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are lomits.
All lomits are oskets.
Question: Does it follow that all oskets are lomits?
Answer:
```

## 062/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are lomits.
All lomits are oskets.
Question: Does it follow that all vromps are oskets?
Answer:
```

## 062/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are lomits.
All lomits are oskets.
Question: Does it follow that all oskets are vromps?
Answer:
```

## 062/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are korvas.
All lomits are oskets.
Question: Does it follow that all vromps are oskets?
Answer:
```

## 062/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are lomits.
All korvas are oskets.
Question: Does it follow that all vromps are oskets?
Answer:
```

## 062/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are oskets.
All vromps are lomits.
Question: Does it follow that all vromps are oskets?
Answer:
```

## 062/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are oskets.
All vromps are lomits.
Question: Does it follow that all oskets are vromps?
Answer:
```

## 062/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are oskets.
All zorks are prandils.
All korvas are zorks.
All vromps are lomits.
Question: Does it follow that all vromps are oskets?
Answer:
```

## 062/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are oskets.
All zorks are prandils.
All korvas are zorks.
All vromps are lomits.
Question: Does it follow that all oskets are vromps?
Answer:
```

## 062/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are snorps.
All snorps are vibbles.
Question: Does it follow that all helpons are vibbles?
Answer:
```

## 062/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are snorps.
All snorps are vibbles.
Question: Does it follow that all vibbles are helpons?
Answer:
```

## 063/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vromps.
All vromps are quavels.
Question: Does it follow that all oskets are vromps?
Answer:
```

## 063/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vromps.
All vromps are quavels.
Question: Does it follow that all vromps are oskets?
Answer:
```

## 063/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vromps.
All vromps are quavels.
Question: Does it follow that all oskets are quavels?
Answer:
```

## 063/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vromps.
All vromps are quavels.
Question: Does it follow that all quavels are oskets?
Answer:
```

## 063/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are prandils.
All vromps are quavels.
Question: Does it follow that all oskets are quavels?
Answer:
```

## 063/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vromps.
All prandils are quavels.
Question: Does it follow that all oskets are quavels?
Answer:
```

## 063/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are quavels.
All oskets are vromps.
Question: Does it follow that all oskets are quavels?
Answer:
```

## 063/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are quavels.
All oskets are vromps.
Question: Does it follow that all quavels are oskets?
Answer:
```

## 063/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are vromps.
All prandils are daxes.
All vromps are quavels.
All daxes are tivaks.
Question: Does it follow that all oskets are quavels?
Answer:
```

## 063/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All oskets are vromps.
All prandils are daxes.
All vromps are quavels.
All daxes are tivaks.
Question: Does it follow that all quavels are oskets?
Answer:
```

## 063/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are yorbits.
All yorbits are ruspins.
Question: Does it follow that all murdles are ruspins?
Answer:
```

## 063/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are yorbits.
All yorbits are ruspins.
Question: Does it follow that all ruspins are murdles?
Answer:
```

## 064/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are vibbles.
All blickets are ruspins.
Question: Does it follow that all ruspins are vibbles?
Answer:
```

## 064/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are vibbles.
All blickets are ruspins.
Question: Does it follow that all vibbles are ruspins?
Answer:
```

## 064/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are vibbles.
All blickets are ruspins.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 064/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are vibbles.
All blickets are ruspins.
Question: Does it follow that all vibbles are blickets?
Answer:
```

## 064/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are vibbles.
All blickets are helpons.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 064/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are vibbles.
All blickets are ruspins.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 064/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are ruspins.
All ruspins are vibbles.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 064/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are ruspins.
All ruspins are vibbles.
Question: Does it follow that all vibbles are blickets?
Answer:
```

## 064/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All blickets are ruspins.
All helpons are jastles.
All ruspins are vibbles.
All jastles are murdles.
Question: Does it follow that all blickets are vibbles?
Answer:
```

## 064/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All blickets are ruspins.
All helpons are jastles.
All ruspins are vibbles.
All jastles are murdles.
Question: Does it follow that all vibbles are blickets?
Answer:
```

## 064/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are kelbrins.
All brovets are daxes.
Question: Does it follow that all brovets are kelbrins?
Answer:
```

## 064/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are kelbrins.
All brovets are daxes.
Question: Does it follow that all kelbrins are brovets?
Answer:
```

## 065/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are vibbles.
All vibbles are grivaks.
Question: Does it follow that all sprocks are vibbles?
Answer:
```

## 065/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are vibbles.
All vibbles are grivaks.
Question: Does it follow that all vibbles are sprocks?
Answer:
```

## 065/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are vibbles.
All vibbles are grivaks.
Question: Does it follow that all sprocks are grivaks?
Answer:
```

## 065/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are vibbles.
All vibbles are grivaks.
Question: Does it follow that all grivaks are sprocks?
Answer:
```

## 065/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are ruspins.
All vibbles are grivaks.
Question: Does it follow that all sprocks are grivaks?
Answer:
```

## 065/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are vibbles.
All ruspins are grivaks.
Question: Does it follow that all sprocks are grivaks?
Answer:
```

## 065/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are grivaks.
All sprocks are vibbles.
Question: Does it follow that all sprocks are grivaks?
Answer:
```

## 065/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are grivaks.
All sprocks are vibbles.
Question: Does it follow that all grivaks are sprocks?
Answer:
```

## 065/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are vibbles.
All ruspins are vromps.
All vromps are crundles.
All vibbles are grivaks.
Question: Does it follow that all sprocks are grivaks?
Answer:
```

## 065/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are vibbles.
All ruspins are vromps.
All vromps are crundles.
All vibbles are grivaks.
Question: Does it follow that all grivaks are sprocks?
Answer:
```

## 065/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are zemples.
All zemples are shalds.
Question: Does it follow that all brovets are shalds?
Answer:
```

## 065/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are zemples.
All zemples are shalds.
Question: Does it follow that all shalds are brovets?
Answer:
```

## 066/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are yorbits.
All yorbits are korvas.
Question: Does it follow that all yorbits are korvas?
Answer:
```

## 066/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are yorbits.
All yorbits are korvas.
Question: Does it follow that all korvas are yorbits?
Answer:
```

## 066/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are yorbits.
All yorbits are korvas.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 066/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are yorbits.
All yorbits are korvas.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 066/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are zemples.
All yorbits are korvas.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 066/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are yorbits.
All zemples are korvas.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 066/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are korvas.
All sprocks are yorbits.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 066/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are korvas.
All sprocks are yorbits.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 066/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are yorbits.
All vibbles are murdles.
All yorbits are korvas.
All zemples are vibbles.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 066/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are yorbits.
All vibbles are murdles.
All yorbits are korvas.
All zemples are vibbles.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 066/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are tufas.
All tufas are ruspins.
Question: Does it follow that all daxes are ruspins?
Answer:
```

## 066/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are tufas.
All tufas are ruspins.
Question: Does it follow that all ruspins are daxes?
Answer:
```

## 067/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are wugs.
All jastles are sprocks.
Question: Does it follow that all sprocks are wugs?
Answer:
```

## 067/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are wugs.
All jastles are sprocks.
Question: Does it follow that all wugs are sprocks?
Answer:
```

## 067/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are wugs.
All jastles are sprocks.
Question: Does it follow that all jastles are wugs?
Answer:
```

## 067/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are wugs.
All jastles are sprocks.
Question: Does it follow that all wugs are jastles?
Answer:
```

## 067/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are wugs.
All jastles are prandils.
Question: Does it follow that all jastles are wugs?
Answer:
```

## 067/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are wugs.
All jastles are sprocks.
Question: Does it follow that all jastles are wugs?
Answer:
```

## 067/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are sprocks.
All sprocks are wugs.
Question: Does it follow that all jastles are wugs?
Answer:
```

## 067/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are sprocks.
All sprocks are wugs.
Question: Does it follow that all wugs are jastles?
Answer:
```

## 067/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are vibbles.
All jastles are sprocks.
All vibbles are tufas.
All sprocks are wugs.
Question: Does it follow that all jastles are wugs?
Answer:
```

## 067/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are vibbles.
All jastles are sprocks.
All vibbles are tufas.
All sprocks are wugs.
Question: Does it follow that all wugs are jastles?
Answer:
```

## 067/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are nerps.
All blickets are vromps.
Question: Does it follow that all blickets are nerps?
Answer:
```

## 067/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are nerps.
All blickets are vromps.
Question: Does it follow that all nerps are blickets?
Answer:
```

## 068/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zorks.
All daxes are vromps.
Question: Does it follow that all vromps are zorks?
Answer:
```

## 068/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zorks.
All daxes are vromps.
Question: Does it follow that all zorks are vromps?
Answer:
```

## 068/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zorks.
All daxes are vromps.
Question: Does it follow that all daxes are zorks?
Answer:
```

## 068/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zorks.
All daxes are vromps.
Question: Does it follow that all zorks are daxes?
Answer:
```

## 068/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zorks.
All daxes are shalds.
Question: Does it follow that all daxes are zorks?
Answer:
```

## 068/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are zorks.
All daxes are vromps.
Question: Does it follow that all daxes are zorks?
Answer:
```

## 068/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are vromps.
All vromps are zorks.
Question: Does it follow that all daxes are zorks?
Answer:
```

## 068/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are vromps.
All vromps are zorks.
Question: Does it follow that all zorks are daxes?
Answer:
```

## 068/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are ulvets.
All daxes are vromps.
All ulvets are jastles.
All vromps are zorks.
Question: Does it follow that all daxes are zorks?
Answer:
```

## 068/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are ulvets.
All daxes are vromps.
All ulvets are jastles.
All vromps are zorks.
Question: Does it follow that all zorks are daxes?
Answer:
```

## 068/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are wugs.
All nufrons are blickets.
Question: Does it follow that all nufrons are wugs?
Answer:
```

## 068/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are wugs.
All nufrons are blickets.
Question: Does it follow that all wugs are nufrons?
Answer:
```

## 069/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are sprocks.
All lomits are oskets.
Question: Does it follow that all oskets are sprocks?
Answer:
```

## 069/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are sprocks.
All lomits are oskets.
Question: Does it follow that all sprocks are oskets?
Answer:
```

## 069/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are sprocks.
All lomits are oskets.
Question: Does it follow that all lomits are sprocks?
Answer:
```

## 069/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are sprocks.
All lomits are oskets.
Question: Does it follow that all sprocks are lomits?
Answer:
```

## 069/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are sprocks.
All lomits are helpons.
Question: Does it follow that all lomits are sprocks?
Answer:
```

## 069/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are sprocks.
All lomits are oskets.
Question: Does it follow that all lomits are sprocks?
Answer:
```

## 069/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are oskets.
All oskets are sprocks.
Question: Does it follow that all lomits are sprocks?
Answer:
```

## 069/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are oskets.
All oskets are sprocks.
Question: Does it follow that all sprocks are lomits?
Answer:
```

## 069/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are oskets.
All helpons are wugs.
All oskets are sprocks.
All wugs are xandles.
Question: Does it follow that all lomits are sprocks?
Answer:
```

## 069/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All lomits are oskets.
All helpons are wugs.
All oskets are sprocks.
All wugs are xandles.
Question: Does it follow that all sprocks are lomits?
Answer:
```

## 069/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are prandils.
All brovets are quavels.
Question: Does it follow that all brovets are prandils?
Answer:
```

## 069/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are prandils.
All brovets are quavels.
Question: Does it follow that all prandils are brovets?
Answer:
```

## 070/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are ruspins.
All ulvets are yorbits.
Question: Does it follow that all yorbits are ruspins?
Answer:
```

## 070/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are ruspins.
All ulvets are yorbits.
Question: Does it follow that all ruspins are yorbits?
Answer:
```

## 070/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are ruspins.
All ulvets are yorbits.
Question: Does it follow that all ulvets are ruspins?
Answer:
```

## 070/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are ruspins.
All ulvets are yorbits.
Question: Does it follow that all ruspins are ulvets?
Answer:
```

## 070/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are ruspins.
All ulvets are snorps.
Question: Does it follow that all ulvets are ruspins?
Answer:
```

## 070/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are ruspins.
All ulvets are yorbits.
Question: Does it follow that all ulvets are ruspins?
Answer:
```

## 070/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ulvets are yorbits.
All yorbits are ruspins.
Question: Does it follow that all ulvets are ruspins?
Answer:
```

## 070/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ulvets are yorbits.
All yorbits are ruspins.
Question: Does it follow that all ruspins are ulvets?
Answer:
```

## 070/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are shalds.
All snorps are grivaks.
All ulvets are yorbits.
All yorbits are ruspins.
Question: Does it follow that all ulvets are ruspins?
Answer:
```

## 070/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are shalds.
All snorps are grivaks.
All ulvets are yorbits.
All yorbits are ruspins.
Question: Does it follow that all ruspins are ulvets?
Answer:
```

## 070/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are kelbrins.
All zemples are zorks.
Question: Does it follow that all zemples are kelbrins?
Answer:
```

## 070/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are kelbrins.
All zemples are zorks.
Question: Does it follow that all kelbrins are zemples?
Answer:
```

## 071/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are daxes.
All daxes are wugs.
Question: Does it follow that all shalds are daxes?
Answer:
```

## 071/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are daxes.
All daxes are wugs.
Question: Does it follow that all daxes are shalds?
Answer:
```

## 071/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are daxes.
All daxes are wugs.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 071/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are daxes.
All daxes are wugs.
Question: Does it follow that all wugs are shalds?
Answer:
```

## 071/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are crundles.
All daxes are wugs.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 071/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are daxes.
All crundles are wugs.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 071/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are wugs.
All shalds are daxes.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 071/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are wugs.
All shalds are daxes.
Question: Does it follow that all wugs are shalds?
Answer:
```

## 071/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are wugs.
All shalds are daxes.
All zemples are tufas.
All crundles are zemples.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 071/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are wugs.
All shalds are daxes.
All zemples are tufas.
All crundles are zemples.
Question: Does it follow that all wugs are shalds?
Answer:
```

## 071/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are vromps.
All vromps are ulvets.
Question: Does it follow that all prandils are ulvets?
Answer:
```

## 071/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are vromps.
All vromps are ulvets.
Question: Does it follow that all ulvets are prandils?
Answer:
```

## 072/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are tivaks.
All murdles are zemples.
Question: Does it follow that all murdles are zemples?
Answer:
```

## 072/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are tivaks.
All murdles are zemples.
Question: Does it follow that all zemples are murdles?
Answer:
```

## 072/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are tivaks.
All murdles are zemples.
Question: Does it follow that all murdles are tivaks?
Answer:
```

## 072/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are tivaks.
All murdles are zemples.
Question: Does it follow that all tivaks are murdles?
Answer:
```

## 072/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are tivaks.
All murdles are shalds.
Question: Does it follow that all murdles are tivaks?
Answer:
```

## 072/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are tivaks.
All murdles are zemples.
Question: Does it follow that all murdles are tivaks?
Answer:
```

## 072/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are zemples.
All zemples are tivaks.
Question: Does it follow that all murdles are tivaks?
Answer:
```

## 072/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are zemples.
All zemples are tivaks.
Question: Does it follow that all tivaks are murdles?
Answer:
```

## 072/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are vromps.
All zemples are tivaks.
All murdles are zemples.
All shalds are quavels.
Question: Does it follow that all murdles are tivaks?
Answer:
```

## 072/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are vromps.
All zemples are tivaks.
All murdles are zemples.
All shalds are quavels.
Question: Does it follow that all tivaks are murdles?
Answer:
```

## 072/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are oskets.
All zeltrons are korvas.
Question: Does it follow that all zeltrons are oskets?
Answer:
```

## 072/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are oskets.
All zeltrons are korvas.
Question: Does it follow that all oskets are zeltrons?
Answer:
```

## 073/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are sprocks.
All snorps are murdles.
Question: Does it follow that all snorps are murdles?
Answer:
```

## 073/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are sprocks.
All snorps are murdles.
Question: Does it follow that all murdles are snorps?
Answer:
```

## 073/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are sprocks.
All snorps are murdles.
Question: Does it follow that all snorps are sprocks?
Answer:
```

## 073/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are sprocks.
All snorps are murdles.
Question: Does it follow that all sprocks are snorps?
Answer:
```

## 073/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are sprocks.
All snorps are yorbits.
Question: Does it follow that all snorps are sprocks?
Answer:
```

## 073/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are sprocks.
All snorps are murdles.
Question: Does it follow that all snorps are sprocks?
Answer:
```

## 073/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are murdles.
All murdles are sprocks.
Question: Does it follow that all snorps are sprocks?
Answer:
```

## 073/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are murdles.
All murdles are sprocks.
Question: Does it follow that all sprocks are snorps?
Answer:
```

## 073/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are sprocks.
All snorps are murdles.
All yorbits are kelbrins.
All kelbrins are plinets.
Question: Does it follow that all snorps are sprocks?
Answer:
```

## 073/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All murdles are sprocks.
All snorps are murdles.
All yorbits are kelbrins.
All kelbrins are plinets.
Question: Does it follow that all sprocks are snorps?
Answer:
```

## 073/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are brovets.
All prandils are quavels.
Question: Does it follow that all prandils are brovets?
Answer:
```

## 073/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are brovets.
All prandils are quavels.
Question: Does it follow that all brovets are prandils?
Answer:
```

## 074/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are blickets.
All nerps are crundles.
Question: Does it follow that all nerps are crundles?
Answer:
```

## 074/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are blickets.
All nerps are crundles.
Question: Does it follow that all crundles are nerps?
Answer:
```

## 074/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are blickets.
All nerps are crundles.
Question: Does it follow that all nerps are blickets?
Answer:
```

## 074/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are blickets.
All nerps are crundles.
Question: Does it follow that all blickets are nerps?
Answer:
```

## 074/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are blickets.
All nerps are prandils.
Question: Does it follow that all nerps are blickets?
Answer:
```

## 074/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are blickets.
All nerps are crundles.
Question: Does it follow that all nerps are blickets?
Answer:
```

## 074/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are crundles.
All crundles are blickets.
Question: Does it follow that all nerps are blickets?
Answer:
```

## 074/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are crundles.
All crundles are blickets.
Question: Does it follow that all blickets are nerps?
Answer:
```

## 074/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are wugs.
All crundles are blickets.
All wugs are shalds.
All nerps are crundles.
Question: Does it follow that all nerps are blickets?
Answer:
```

## 074/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are wugs.
All crundles are blickets.
All wugs are shalds.
All nerps are crundles.
Question: Does it follow that all blickets are nerps?
Answer:
```

## 074/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are oskets.
All tufas are welbins.
Question: Does it follow that all tufas are oskets?
Answer:
```

## 074/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are oskets.
All tufas are welbins.
Question: Does it follow that all oskets are tufas?
Answer:
```

## 075/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are quavels.
All quavels are shalds.
Question: Does it follow that all quavels are shalds?
Answer:
```

## 075/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are quavels.
All quavels are shalds.
Question: Does it follow that all shalds are quavels?
Answer:
```

## 075/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are quavels.
All quavels are shalds.
Question: Does it follow that all zeltrons are shalds?
Answer:
```

## 075/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are quavels.
All quavels are shalds.
Question: Does it follow that all shalds are zeltrons?
Answer:
```

## 075/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are grivaks.
All quavels are shalds.
Question: Does it follow that all zeltrons are shalds?
Answer:
```

## 075/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are quavels.
All grivaks are shalds.
Question: Does it follow that all zeltrons are shalds?
Answer:
```

## 075/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are shalds.
All zeltrons are quavels.
Question: Does it follow that all zeltrons are shalds?
Answer:
```

## 075/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are shalds.
All zeltrons are quavels.
Question: Does it follow that all shalds are zeltrons?
Answer:
```

## 075/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are oskets.
All zeltrons are quavels.
All grivaks are daxes.
All quavels are shalds.
Question: Does it follow that all zeltrons are shalds?
Answer:
```

## 075/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are oskets.
All zeltrons are quavels.
All grivaks are daxes.
All quavels are shalds.
Question: Does it follow that all shalds are zeltrons?
Answer:
```

## 075/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are zorks.
All zorks are snorps.
Question: Does it follow that all wugs are snorps?
Answer:
```

## 075/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are zorks.
All zorks are snorps.
Question: Does it follow that all snorps are wugs?
Answer:
```

## 076/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are plinets.
All plinets are quavels.
Question: Does it follow that all plinets are quavels?
Answer:
```

## 076/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are plinets.
All plinets are quavels.
Question: Does it follow that all quavels are plinets?
Answer:
```

## 076/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are plinets.
All plinets are quavels.
Question: Does it follow that all shalds are quavels?
Answer:
```

## 076/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are plinets.
All plinets are quavels.
Question: Does it follow that all quavels are shalds?
Answer:
```

## 076/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are prandils.
All plinets are quavels.
Question: Does it follow that all shalds are quavels?
Answer:
```

## 076/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are plinets.
All prandils are quavels.
Question: Does it follow that all shalds are quavels?
Answer:
```

## 076/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are quavels.
All shalds are plinets.
Question: Does it follow that all shalds are quavels?
Answer:
```

## 076/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are quavels.
All shalds are plinets.
Question: Does it follow that all quavels are shalds?
Answer:
```

## 076/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are tufas.
All plinets are quavels.
All tufas are ruspins.
All shalds are plinets.
Question: Does it follow that all shalds are quavels?
Answer:
```

## 076/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are tufas.
All plinets are quavels.
All tufas are ruspins.
All shalds are plinets.
Question: Does it follow that all quavels are shalds?
Answer:
```

## 076/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are sprocks.
All sprocks are brovets.
Question: Does it follow that all welbins are brovets?
Answer:
```

## 076/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are sprocks.
All sprocks are brovets.
Question: Does it follow that all brovets are welbins?
Answer:
```

## 077/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are flomps.
All yorbits are jastles.
Question: Does it follow that all jastles are flomps?
Answer:
```

## 077/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are flomps.
All yorbits are jastles.
Question: Does it follow that all flomps are jastles?
Answer:
```

## 077/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are flomps.
All yorbits are jastles.
Question: Does it follow that all yorbits are flomps?
Answer:
```

## 077/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are flomps.
All yorbits are jastles.
Question: Does it follow that all flomps are yorbits?
Answer:
```

## 077/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are flomps.
All yorbits are daxes.
Question: Does it follow that all yorbits are flomps?
Answer:
```

## 077/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are flomps.
All yorbits are jastles.
Question: Does it follow that all yorbits are flomps?
Answer:
```

## 077/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are jastles.
All jastles are flomps.
Question: Does it follow that all yorbits are flomps?
Answer:
```

## 077/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are jastles.
All jastles are flomps.
Question: Does it follow that all flomps are yorbits?
Answer:
```

## 077/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All jastles are flomps.
All daxes are kelbrins.
All kelbrins are plinets.
All yorbits are jastles.
Question: Does it follow that all yorbits are flomps?
Answer:
```

## 077/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All jastles are flomps.
All daxes are kelbrins.
All kelbrins are plinets.
All yorbits are jastles.
Question: Does it follow that all flomps are yorbits?
Answer:
```

## 077/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are prandils.
All zemples are shalds.
Question: Does it follow that all zemples are prandils?
Answer:
```

## 077/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are prandils.
All zemples are shalds.
Question: Does it follow that all prandils are zemples?
Answer:
```

## 078/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are yorbits.
All yorbits are blickets.
Question: Does it follow that all ruspins are yorbits?
Answer:
```

## 078/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are yorbits.
All yorbits are blickets.
Question: Does it follow that all yorbits are ruspins?
Answer:
```

## 078/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are yorbits.
All yorbits are blickets.
Question: Does it follow that all ruspins are blickets?
Answer:
```

## 078/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are yorbits.
All yorbits are blickets.
Question: Does it follow that all blickets are ruspins?
Answer:
```

## 078/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are prandils.
All yorbits are blickets.
Question: Does it follow that all ruspins are blickets?
Answer:
```

## 078/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are yorbits.
All prandils are blickets.
Question: Does it follow that all ruspins are blickets?
Answer:
```

## 078/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are blickets.
All ruspins are yorbits.
Question: Does it follow that all ruspins are blickets?
Answer:
```

## 078/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are blickets.
All ruspins are yorbits.
Question: Does it follow that all blickets are ruspins?
Answer:
```

## 078/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are vromps.
All yorbits are blickets.
All prandils are nufrons.
All ruspins are yorbits.
Question: Does it follow that all ruspins are blickets?
Answer:
```

## 078/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are vromps.
All yorbits are blickets.
All prandils are nufrons.
All ruspins are yorbits.
Question: Does it follow that all blickets are ruspins?
Answer:
```

## 078/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are zemples.
All zemples are zeltrons.
Question: Does it follow that all tufas are zeltrons?
Answer:
```

## 078/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are zemples.
All zemples are zeltrons.
Question: Does it follow that all zeltrons are tufas?
Answer:
```

## 079/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are shalds.
All shalds are prandils.
Question: Does it follow that all shalds are prandils?
Answer:
```

## 079/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are shalds.
All shalds are prandils.
Question: Does it follow that all prandils are shalds?
Answer:
```

## 079/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are shalds.
All shalds are prandils.
Question: Does it follow that all blickets are prandils?
Answer:
```

## 079/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are shalds.
All shalds are prandils.
Question: Does it follow that all prandils are blickets?
Answer:
```

## 079/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are zorks.
All shalds are prandils.
Question: Does it follow that all blickets are prandils?
Answer:
```

## 079/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are shalds.
All zorks are prandils.
Question: Does it follow that all blickets are prandils?
Answer:
```

## 079/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are prandils.
All blickets are shalds.
Question: Does it follow that all blickets are prandils?
Answer:
```

## 079/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are prandils.
All blickets are shalds.
Question: Does it follow that all prandils are blickets?
Answer:
```

## 079/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All wugs are zemples.
All zorks are wugs.
All blickets are shalds.
All shalds are prandils.
Question: Does it follow that all blickets are prandils?
Answer:
```

## 079/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are zemples.
All zorks are wugs.
All blickets are shalds.
All shalds are prandils.
Question: Does it follow that all prandils are blickets?
Answer:
```

## 079/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are ruspins.
All ruspins are oskets.
Question: Does it follow that all yorbits are oskets?
Answer:
```

## 079/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are ruspins.
All ruspins are oskets.
Question: Does it follow that all oskets are yorbits?
Answer:
```

## 080/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All helpons are tivaks.
Question: Does it follow that all helpons are tivaks?
Answer:
```

## 080/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All helpons are tivaks.
Question: Does it follow that all tivaks are helpons?
Answer:
```

## 080/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All helpons are tivaks.
Question: Does it follow that all helpons are daxes?
Answer:
```

## 080/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All helpons are tivaks.
Question: Does it follow that all daxes are helpons?
Answer:
```

## 080/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are daxes.
All helpons are oskets.
Question: Does it follow that all helpons are daxes?
Answer:
```

## 080/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are daxes.
All helpons are tivaks.
Question: Does it follow that all helpons are daxes?
Answer:
```

## 080/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are tivaks.
All tivaks are daxes.
Question: Does it follow that all helpons are daxes?
Answer:
```

## 080/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are tivaks.
All tivaks are daxes.
Question: Does it follow that all daxes are helpons?
Answer:
```

## 080/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are brovets.
All oskets are kelbrins.
All tivaks are daxes.
All helpons are tivaks.
Question: Does it follow that all helpons are daxes?
Answer:
```

## 080/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are brovets.
All oskets are kelbrins.
All tivaks are daxes.
All helpons are tivaks.
Question: Does it follow that all daxes are helpons?
Answer:
```

## 080/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are snorps.
All lomits are ruspins.
Question: Does it follow that all lomits are snorps?
Answer:
```

## 080/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are snorps.
All lomits are ruspins.
Question: Does it follow that all snorps are lomits?
Answer:
```

## 081/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are zorks.
All zorks are zemples.
Question: Does it follow that all welbins are zorks?
Answer:
```

## 081/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are zorks.
All zorks are zemples.
Question: Does it follow that all zorks are welbins?
Answer:
```

## 081/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are zorks.
All zorks are zemples.
Question: Does it follow that all welbins are zemples?
Answer:
```

## 081/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are zorks.
All zorks are zemples.
Question: Does it follow that all zemples are welbins?
Answer:
```

## 081/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are vibbles.
All zorks are zemples.
Question: Does it follow that all welbins are zemples?
Answer:
```

## 081/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are zorks.
All vibbles are zemples.
Question: Does it follow that all welbins are zemples?
Answer:
```

## 081/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are zemples.
All welbins are zorks.
Question: Does it follow that all welbins are zemples?
Answer:
```

## 081/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are zemples.
All welbins are zorks.
Question: Does it follow that all zemples are welbins?
Answer:
```

## 081/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are zorks.
All vibbles are prandils.
All prandils are nufrons.
All zorks are zemples.
Question: Does it follow that all welbins are zemples?
Answer:
```

## 081/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are zorks.
All vibbles are prandils.
All prandils are nufrons.
All zorks are zemples.
Question: Does it follow that all zemples are welbins?
Answer:
```

## 081/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tivaks.
All tivaks are nerps.
Question: Does it follow that all korvas are nerps?
Answer:
```

## 081/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tivaks.
All tivaks are nerps.
Question: Does it follow that all nerps are korvas?
Answer:
```

## 082/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are daxes.
All nerps are oskets.
Question: Does it follow that all nerps are oskets?
Answer:
```

## 082/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are daxes.
All nerps are oskets.
Question: Does it follow that all oskets are nerps?
Answer:
```

## 082/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are daxes.
All nerps are oskets.
Question: Does it follow that all nerps are daxes?
Answer:
```

## 082/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are daxes.
All nerps are oskets.
Question: Does it follow that all daxes are nerps?
Answer:
```

## 082/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are daxes.
All nerps are welbins.
Question: Does it follow that all nerps are daxes?
Answer:
```

## 082/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are daxes.
All nerps are oskets.
Question: Does it follow that all nerps are daxes?
Answer:
```

## 082/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are oskets.
All oskets are daxes.
Question: Does it follow that all nerps are daxes?
Answer:
```

## 082/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are oskets.
All oskets are daxes.
Question: Does it follow that all daxes are nerps?
Answer:
```

## 082/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are oskets.
All crundles are zemples.
All oskets are daxes.
All welbins are crundles.
Question: Does it follow that all nerps are daxes?
Answer:
```

## 082/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are oskets.
All crundles are zemples.
All oskets are daxes.
All welbins are crundles.
Question: Does it follow that all daxes are nerps?
Answer:
```

## 082/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are wugs.
All ulvets are grivaks.
Question: Does it follow that all ulvets are wugs?
Answer:
```

## 082/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are wugs.
All ulvets are grivaks.
Question: Does it follow that all wugs are ulvets?
Answer:
```

## 083/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are prandils.
All prandils are kelbrins.
Question: Does it follow that all crundles are prandils?
Answer:
```

## 083/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are prandils.
All prandils are kelbrins.
Question: Does it follow that all prandils are crundles?
Answer:
```

## 083/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are prandils.
All prandils are kelbrins.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 083/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are prandils.
All prandils are kelbrins.
Question: Does it follow that all kelbrins are crundles?
Answer:
```

## 083/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are oskets.
All prandils are kelbrins.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 083/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are prandils.
All oskets are kelbrins.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 083/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are kelbrins.
All crundles are prandils.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 083/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are kelbrins.
All crundles are prandils.
Question: Does it follow that all kelbrins are crundles?
Answer:
```

## 083/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All crundles are prandils.
All prandils are kelbrins.
All oskets are lomits.
All lomits are quavels.
Question: Does it follow that all crundles are kelbrins?
Answer:
```

## 083/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All crundles are prandils.
All prandils are kelbrins.
All oskets are lomits.
All lomits are quavels.
Question: Does it follow that all kelbrins are crundles?
Answer:
```

## 083/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are vibbles.
All vibbles are korvas.
Question: Does it follow that all flomps are korvas?
Answer:
```

## 083/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are vibbles.
All vibbles are korvas.
Question: Does it follow that all korvas are flomps?
Answer:
```

## 084/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are sprocks.
All crundles are daxes.
Question: Does it follow that all daxes are sprocks?
Answer:
```

## 084/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are sprocks.
All crundles are daxes.
Question: Does it follow that all sprocks are daxes?
Answer:
```

## 084/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are sprocks.
All crundles are daxes.
Question: Does it follow that all crundles are sprocks?
Answer:
```

## 084/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are sprocks.
All crundles are daxes.
Question: Does it follow that all sprocks are crundles?
Answer:
```

## 084/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are sprocks.
All crundles are wugs.
Question: Does it follow that all crundles are sprocks?
Answer:
```

## 084/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are sprocks.
All crundles are daxes.
Question: Does it follow that all crundles are sprocks?
Answer:
```

## 084/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are daxes.
All daxes are sprocks.
Question: Does it follow that all crundles are sprocks?
Answer:
```

## 084/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are daxes.
All daxes are sprocks.
Question: Does it follow that all sprocks are crundles?
Answer:
```

## 084/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are daxes.
All quavels are zeltrons.
All wugs are quavels.
All daxes are sprocks.
Question: Does it follow that all crundles are sprocks?
Answer:
```

## 084/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All crundles are daxes.
All quavels are zeltrons.
All wugs are quavels.
All daxes are sprocks.
Question: Does it follow that all sprocks are crundles?
Answer:
```

## 084/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are blickets.
All snorps are brovets.
Question: Does it follow that all snorps are blickets?
Answer:
```

## 084/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are blickets.
All snorps are brovets.
Question: Does it follow that all blickets are snorps?
Answer:
```

## 085/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are nerps.
All grivaks are tufas.
Question: Does it follow that all tufas are nerps?
Answer:
```

## 085/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are nerps.
All grivaks are tufas.
Question: Does it follow that all nerps are tufas?
Answer:
```

## 085/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are nerps.
All grivaks are tufas.
Question: Does it follow that all grivaks are nerps?
Answer:
```

## 085/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are nerps.
All grivaks are tufas.
Question: Does it follow that all nerps are grivaks?
Answer:
```

## 085/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tufas are nerps.
All grivaks are blickets.
Question: Does it follow that all grivaks are nerps?
Answer:
```

## 085/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are nerps.
All grivaks are tufas.
Question: Does it follow that all grivaks are nerps?
Answer:
```

## 085/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are tufas.
All tufas are nerps.
Question: Does it follow that all grivaks are nerps?
Answer:
```

## 085/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All grivaks are tufas.
All tufas are nerps.
Question: Does it follow that all nerps are grivaks?
Answer:
```

## 085/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are sprocks.
All blickets are zorks.
All tufas are nerps.
All grivaks are tufas.
Question: Does it follow that all grivaks are nerps?
Answer:
```

## 085/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are sprocks.
All blickets are zorks.
All tufas are nerps.
All grivaks are tufas.
Question: Does it follow that all nerps are grivaks?
Answer:
```

## 085/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are shalds.
All yorbits are brovets.
Question: Does it follow that all yorbits are shalds?
Answer:
```

## 085/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are shalds.
All yorbits are brovets.
Question: Does it follow that all shalds are yorbits?
Answer:
```

## 086/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are flomps.
All flomps are wugs.
Question: Does it follow that all welbins are flomps?
Answer:
```

## 086/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are flomps.
All flomps are wugs.
Question: Does it follow that all flomps are welbins?
Answer:
```

## 086/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are flomps.
All flomps are wugs.
Question: Does it follow that all welbins are wugs?
Answer:
```

## 086/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are flomps.
All flomps are wugs.
Question: Does it follow that all wugs are welbins?
Answer:
```

## 086/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are plinets.
All flomps are wugs.
Question: Does it follow that all welbins are wugs?
Answer:
```

## 086/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are flomps.
All plinets are wugs.
Question: Does it follow that all welbins are wugs?
Answer:
```

## 086/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are wugs.
All welbins are flomps.
Question: Does it follow that all welbins are wugs?
Answer:
```

## 086/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are wugs.
All welbins are flomps.
Question: Does it follow that all wugs are welbins?
Answer:
```

## 086/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are prandils.
All flomps are wugs.
All welbins are flomps.
All prandils are lomits.
Question: Does it follow that all welbins are wugs?
Answer:
```

## 086/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are prandils.
All flomps are wugs.
All welbins are flomps.
All prandils are lomits.
Question: Does it follow that all wugs are welbins?
Answer:
```

## 086/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are xandles.
All xandles are sprocks.
Question: Does it follow that all zemples are sprocks?
Answer:
```

## 086/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zemples are xandles.
All xandles are sprocks.
Question: Does it follow that all sprocks are zemples?
Answer:
```

## 087/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All snorps are vromps.
Question: Does it follow that all vromps are zemples?
Answer:
```

## 087/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All snorps are vromps.
Question: Does it follow that all zemples are vromps?
Answer:
```

## 087/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All snorps are vromps.
Question: Does it follow that all snorps are zemples?
Answer:
```

## 087/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All snorps are vromps.
Question: Does it follow that all zemples are snorps?
Answer:
```

## 087/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are zemples.
All snorps are yorbits.
Question: Does it follow that all snorps are zemples?
Answer:
```

## 087/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are zemples.
All snorps are vromps.
Question: Does it follow that all snorps are zemples?
Answer:
```

## 087/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are vromps.
All vromps are zemples.
Question: Does it follow that all snorps are zemples?
Answer:
```

## 087/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All snorps are vromps.
All vromps are zemples.
Question: Does it follow that all zemples are snorps?
Answer:
```

## 087/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are zorks.
All vromps are zemples.
All yorbits are korvas.
All snorps are vromps.
Question: Does it follow that all snorps are zemples?
Answer:
```

## 087/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are zorks.
All vromps are zemples.
All yorbits are korvas.
All snorps are vromps.
Question: Does it follow that all zemples are snorps?
Answer:
```

## 087/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are welbins.
All plinets are shalds.
Question: Does it follow that all plinets are welbins?
Answer:
```

## 087/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are welbins.
All plinets are shalds.
Question: Does it follow that all welbins are plinets?
Answer:
```

## 088/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are plinets.
All plinets are sprocks.
Question: Does it follow that all plinets are sprocks?
Answer:
```

## 088/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are plinets.
All plinets are sprocks.
Question: Does it follow that all sprocks are plinets?
Answer:
```

## 088/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are plinets.
All plinets are sprocks.
Question: Does it follow that all kelbrins are sprocks?
Answer:
```

## 088/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are plinets.
All plinets are sprocks.
Question: Does it follow that all sprocks are kelbrins?
Answer:
```

## 088/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are jastles.
All plinets are sprocks.
Question: Does it follow that all kelbrins are sprocks?
Answer:
```

## 088/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All kelbrins are plinets.
All jastles are sprocks.
Question: Does it follow that all kelbrins are sprocks?
Answer:
```

## 088/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are sprocks.
All kelbrins are plinets.
Question: Does it follow that all kelbrins are sprocks?
Answer:
```

## 088/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are sprocks.
All kelbrins are plinets.
Question: Does it follow that all sprocks are kelbrins?
Answer:
```

## 088/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All plinets are sprocks.
All jastles are prandils.
All prandils are helpons.
All kelbrins are plinets.
Question: Does it follow that all kelbrins are sprocks?
Answer:
```

## 088/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are sprocks.
All jastles are prandils.
All prandils are helpons.
All kelbrins are plinets.
Question: Does it follow that all sprocks are kelbrins?
Answer:
```

## 088/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are zemples.
All zemples are snorps.
Question: Does it follow that all shalds are snorps?
Answer:
```

## 088/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are zemples.
All zemples are snorps.
Question: Does it follow that all snorps are shalds?
Answer:
```

## 089/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are ruspins.
All nufrons are plinets.
Question: Does it follow that all plinets are ruspins?
Answer:
```

## 089/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are ruspins.
All nufrons are plinets.
Question: Does it follow that all ruspins are plinets?
Answer:
```

## 089/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are ruspins.
All nufrons are plinets.
Question: Does it follow that all nufrons are ruspins?
Answer:
```

## 089/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are ruspins.
All nufrons are plinets.
Question: Does it follow that all ruspins are nufrons?
Answer:
```

## 089/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are ruspins.
All nufrons are vibbles.
Question: Does it follow that all nufrons are ruspins?
Answer:
```

## 089/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are ruspins.
All nufrons are plinets.
Question: Does it follow that all nufrons are ruspins?
Answer:
```

## 089/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are plinets.
All plinets are ruspins.
Question: Does it follow that all nufrons are ruspins?
Answer:
```

## 089/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are plinets.
All plinets are ruspins.
Question: Does it follow that all ruspins are nufrons?
Answer:
```

## 089/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All nufrons are plinets.
All plinets are ruspins.
All vibbles are wugs.
All wugs are kelbrins.
Question: Does it follow that all nufrons are ruspins?
Answer:
```

## 089/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All nufrons are plinets.
All plinets are ruspins.
All vibbles are wugs.
All wugs are kelbrins.
Question: Does it follow that all ruspins are nufrons?
Answer:
```

## 089/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are helpons.
All oskets are flomps.
Question: Does it follow that all oskets are helpons?
Answer:
```

## 089/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are helpons.
All oskets are flomps.
Question: Does it follow that all helpons are oskets?
Answer:
```

## 090/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are flomps.
All vibbles are zorks.
Question: Does it follow that all zorks are flomps?
Answer:
```

## 090/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are flomps.
All vibbles are zorks.
Question: Does it follow that all flomps are zorks?
Answer:
```

## 090/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are flomps.
All vibbles are zorks.
Question: Does it follow that all vibbles are flomps?
Answer:
```

## 090/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are flomps.
All vibbles are zorks.
Question: Does it follow that all flomps are vibbles?
Answer:
```

## 090/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are flomps.
All vibbles are shalds.
Question: Does it follow that all vibbles are flomps?
Answer:
```

## 090/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are flomps.
All vibbles are zorks.
Question: Does it follow that all vibbles are flomps?
Answer:
```

## 090/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are zorks.
All zorks are flomps.
Question: Does it follow that all vibbles are flomps?
Answer:
```

## 090/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are zorks.
All zorks are flomps.
Question: Does it follow that all flomps are vibbles?
Answer:
```

## 090/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are zorks.
All shalds are welbins.
All zorks are flomps.
All welbins are zeltrons.
Question: Does it follow that all vibbles are flomps?
Answer:
```

## 090/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are zorks.
All shalds are welbins.
All zorks are flomps.
All welbins are zeltrons.
Question: Does it follow that all flomps are vibbles?
Answer:
```

## 090/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are crundles.
All blickets are nerps.
Question: Does it follow that all blickets are crundles?
Answer:
```

## 090/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nerps are crundles.
All blickets are nerps.
Question: Does it follow that all crundles are blickets?
Answer:
```

## 091/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ulvets are nufrons.
All vromps are ulvets.
Question: Does it follow that all vromps are ulvets?
Answer:
```

## 091/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ulvets are nufrons.
All vromps are ulvets.
Question: Does it follow that all ulvets are vromps?
Answer:
```

## 091/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ulvets are nufrons.
All vromps are ulvets.
Question: Does it follow that all vromps are nufrons?
Answer:
```

## 091/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ulvets are nufrons.
All vromps are ulvets.
Question: Does it follow that all nufrons are vromps?
Answer:
```

## 091/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ulvets are nufrons.
All vromps are blickets.
Question: Does it follow that all vromps are nufrons?
Answer:
```

## 091/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are nufrons.
All vromps are ulvets.
Question: Does it follow that all vromps are nufrons?
Answer:
```

## 091/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are ulvets.
All ulvets are nufrons.
Question: Does it follow that all vromps are nufrons?
Answer:
```

## 091/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are ulvets.
All ulvets are nufrons.
Question: Does it follow that all nufrons are vromps?
Answer:
```

## 091/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are shalds.
All blickets are xandles.
All vromps are ulvets.
All ulvets are nufrons.
Question: Does it follow that all vromps are nufrons?
Answer:
```

## 091/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are shalds.
All blickets are xandles.
All vromps are ulvets.
All ulvets are nufrons.
Question: Does it follow that all nufrons are vromps?
Answer:
```

## 091/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are tufas.
All korvas are ruspins.
Question: Does it follow that all korvas are tufas?
Answer:
```

## 091/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are tufas.
All korvas are ruspins.
Question: Does it follow that all tufas are korvas?
Answer:
```

## 092/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are helpons.
All helpons are korvas.
Question: Does it follow that all helpons are korvas?
Answer:
```

## 092/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are helpons.
All helpons are korvas.
Question: Does it follow that all korvas are helpons?
Answer:
```

## 092/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are helpons.
All helpons are korvas.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 092/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are helpons.
All helpons are korvas.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 092/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are yorbits.
All helpons are korvas.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 092/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are helpons.
All yorbits are korvas.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 092/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are korvas.
All sprocks are helpons.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 092/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All helpons are korvas.
All sprocks are helpons.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 092/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are tufas.
All helpons are korvas.
All sprocks are helpons.
All yorbits are plinets.
Question: Does it follow that all sprocks are korvas?
Answer:
```

## 092/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All plinets are tufas.
All helpons are korvas.
All sprocks are helpons.
All yorbits are plinets.
Question: Does it follow that all korvas are sprocks?
Answer:
```

## 092/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are nufrons.
All nufrons are grivaks.
Question: Does it follow that all vibbles are grivaks?
Answer:
```

## 092/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vibbles are nufrons.
All nufrons are grivaks.
Question: Does it follow that all grivaks are vibbles?
Answer:
```

## 093/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are zorks.
All zorks are shalds.
Question: Does it follow that all zorks are shalds?
Answer:
```

## 093/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are zorks.
All zorks are shalds.
Question: Does it follow that all shalds are zorks?
Answer:
```

## 093/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are zorks.
All zorks are shalds.
Question: Does it follow that all korvas are shalds?
Answer:
```

## 093/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are zorks.
All zorks are shalds.
Question: Does it follow that all shalds are korvas?
Answer:
```

## 093/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tufas.
All zorks are shalds.
Question: Does it follow that all korvas are shalds?
Answer:
```

## 093/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are zorks.
All tufas are shalds.
Question: Does it follow that all korvas are shalds?
Answer:
```

## 093/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are shalds.
All korvas are zorks.
Question: Does it follow that all korvas are shalds?
Answer:
```

## 093/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zorks are shalds.
All korvas are zorks.
Question: Does it follow that all shalds are korvas?
Answer:
```

## 093/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are welbins.
All tufas are quavels.
All korvas are zorks.
All zorks are shalds.
Question: Does it follow that all korvas are shalds?
Answer:
```

## 093/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are welbins.
All tufas are quavels.
All korvas are zorks.
All zorks are shalds.
Question: Does it follow that all shalds are korvas?
Answer:
```

## 093/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are zemples.
All zemples are crundles.
Question: Does it follow that all tivaks are crundles?
Answer:
```

## 093/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All tivaks are zemples.
All zemples are crundles.
Question: Does it follow that all crundles are tivaks?
Answer:
```

## 094/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All nufrons are zemples.
Question: Does it follow that all nufrons are zemples?
Answer:
```

## 094/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All nufrons are zemples.
Question: Does it follow that all zemples are nufrons?
Answer:
```

## 094/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All nufrons are zemples.
Question: Does it follow that all oskets are zemples?
Answer:
```

## 094/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All nufrons are zemples.
Question: Does it follow that all zemples are oskets?
Answer:
```

## 094/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are korvas.
All nufrons are zemples.
Question: Does it follow that all oskets are zemples?
Answer:
```

## 094/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All korvas are zemples.
Question: Does it follow that all oskets are zemples?
Answer:
```

## 094/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are zemples.
All oskets are nufrons.
Question: Does it follow that all oskets are zemples?
Answer:
```

## 094/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All nufrons are zemples.
All oskets are nufrons.
Question: Does it follow that all zemples are oskets?
Answer:
```

## 094/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All zeltrons are lomits.
All nufrons are zemples.
All korvas are zeltrons.
Question: Does it follow that all oskets are zemples?
Answer:
```

## 094/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All oskets are nufrons.
All zeltrons are lomits.
All nufrons are zemples.
All korvas are zeltrons.
Question: Does it follow that all zemples are oskets?
Answer:
```

## 094/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are zorks.
All zorks are tivaks.
Question: Does it follow that all prandils are tivaks?
Answer:
```

## 094/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All prandils are zorks.
All zorks are tivaks.
Question: Does it follow that all tivaks are prandils?
Answer:
```

## 095/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are zeltrons.
All brovets are daxes.
Question: Does it follow that all brovets are daxes?
Answer:
```

## 095/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are zeltrons.
All brovets are daxes.
Question: Does it follow that all daxes are brovets?
Answer:
```

## 095/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are zeltrons.
All brovets are daxes.
Question: Does it follow that all brovets are zeltrons?
Answer:
```

## 095/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are zeltrons.
All brovets are daxes.
Question: Does it follow that all zeltrons are brovets?
Answer:
```

## 095/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All daxes are zeltrons.
All brovets are sprocks.
Question: Does it follow that all brovets are zeltrons?
Answer:
```

## 095/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All sprocks are zeltrons.
All brovets are daxes.
Question: Does it follow that all brovets are zeltrons?
Answer:
```

## 095/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are daxes.
All daxes are zeltrons.
Question: Does it follow that all brovets are zeltrons?
Answer:
```

## 095/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are daxes.
All daxes are zeltrons.
Question: Does it follow that all zeltrons are brovets?
Answer:
```

## 095/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are daxes.
All ruspins are oskets.
All daxes are zeltrons.
All sprocks are ruspins.
Question: Does it follow that all brovets are zeltrons?
Answer:
```

## 095/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All brovets are daxes.
All ruspins are oskets.
All daxes are zeltrons.
All sprocks are ruspins.
Question: Does it follow that all zeltrons are brovets?
Answer:
```

## 095/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are jastles.
All vromps are quavels.
Question: Does it follow that all vromps are jastles?
Answer:
```

## 095/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are jastles.
All vromps are quavels.
Question: Does it follow that all jastles are vromps?
Answer:
```

## 096/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are daxes.
All welbins are wugs.
Question: Does it follow that all welbins are wugs?
Answer:
```

## 096/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are daxes.
All welbins are wugs.
Question: Does it follow that all wugs are welbins?
Answer:
```

## 096/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are daxes.
All welbins are wugs.
Question: Does it follow that all welbins are daxes?
Answer:
```

## 096/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are daxes.
All welbins are wugs.
Question: Does it follow that all daxes are welbins?
Answer:
```

## 096/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are daxes.
All welbins are yorbits.
Question: Does it follow that all welbins are daxes?
Answer:
```

## 096/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are daxes.
All welbins are wugs.
Question: Does it follow that all welbins are daxes?
Answer:
```

## 096/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are wugs.
All wugs are daxes.
Question: Does it follow that all welbins are daxes?
Answer:
```

## 096/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All welbins are wugs.
All wugs are daxes.
Question: Does it follow that all daxes are welbins?
Answer:
```

## 096/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are flomps.
All yorbits are ruspins.
All welbins are wugs.
All wugs are daxes.
Question: Does it follow that all welbins are daxes?
Answer:
```

## 096/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are flomps.
All yorbits are ruspins.
All welbins are wugs.
All wugs are daxes.
Question: Does it follow that all daxes are welbins?
Answer:
```

## 096/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are sprocks.
All oskets are xandles.
Question: Does it follow that all oskets are sprocks?
Answer:
```

## 096/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All xandles are sprocks.
All oskets are xandles.
Question: Does it follow that all sprocks are oskets?
Answer:
```

## 097/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are brovets.
All brovets are wugs.
Question: Does it follow that all shalds are brovets?
Answer:
```

## 097/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are brovets.
All brovets are wugs.
Question: Does it follow that all brovets are shalds?
Answer:
```

## 097/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are brovets.
All brovets are wugs.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 097/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are brovets.
All brovets are wugs.
Question: Does it follow that all wugs are shalds?
Answer:
```

## 097/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are korvas.
All brovets are wugs.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 097/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All shalds are brovets.
All korvas are wugs.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 097/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are wugs.
All shalds are brovets.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 097/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All brovets are wugs.
All shalds are brovets.
Question: Does it follow that all wugs are shalds?
Answer:
```

## 097/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tufas.
All brovets are wugs.
All tufas are daxes.
All shalds are brovets.
Question: Does it follow that all shalds are wugs?
Answer:
```

## 097/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All korvas are tufas.
All brovets are wugs.
All tufas are daxes.
All shalds are brovets.
Question: Does it follow that all wugs are shalds?
Answer:
```

## 097/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are sprocks.
All sprocks are zorks.
Question: Does it follow that all flomps are zorks?
Answer:
```

## 097/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are sprocks.
All sprocks are zorks.
Question: Does it follow that all zorks are flomps?
Answer:
```

## 098/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are jastles.
All zeltrons are vromps.
Question: Does it follow that all vromps are jastles?
Answer:
```

## 098/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are jastles.
All zeltrons are vromps.
Question: Does it follow that all jastles are vromps?
Answer:
```

## 098/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are jastles.
All zeltrons are vromps.
Question: Does it follow that all zeltrons are jastles?
Answer:
```

## 098/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are jastles.
All zeltrons are vromps.
Question: Does it follow that all jastles are zeltrons?
Answer:
```

## 098/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All vromps are jastles.
All zeltrons are quavels.
Question: Does it follow that all zeltrons are jastles?
Answer:
```

## 098/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All quavels are jastles.
All zeltrons are vromps.
Question: Does it follow that all zeltrons are jastles?
Answer:
```

## 098/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are vromps.
All vromps are jastles.
Question: Does it follow that all zeltrons are jastles?
Answer:
```

## 098/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All zeltrons are vromps.
All vromps are jastles.
Question: Does it follow that all jastles are zeltrons?
Answer:
```

## 098/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **Yes**.

```text
All zeltrons are vromps.
All brovets are nufrons.
All vromps are jastles.
All quavels are brovets.
Question: Does it follow that all zeltrons are jastles?
Answer:
```

## 098/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **Yes**.

```text
All zeltrons are vromps.
All brovets are nufrons.
All vromps are jastles.
All quavels are brovets.
Question: Does it follow that all jastles are zeltrons?
Answer:
```

## 098/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are vibbles.
All yorbits are wugs.
Question: Does it follow that all yorbits are vibbles?
Answer:
```

## 098/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All wugs are vibbles.
All yorbits are wugs.
Question: Does it follow that all vibbles are yorbits?
Answer:
```

## 099/direct/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are vibbles.
All yorbits are blickets.
Question: Does it follow that all yorbits are blickets?
Answer:
```

## 099/direct/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are vibbles.
All yorbits are blickets.
Question: Does it follow that all blickets are yorbits?
Answer:
```

## 099/twohop/base/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are vibbles.
All yorbits are blickets.
Question: Does it follow that all yorbits are vibbles?
Answer:
```

## 099/twohop/base/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are vibbles.
All yorbits are blickets.
Question: Does it follow that all vibbles are yorbits?
Answer:
```

## 099/broken/first/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All blickets are vibbles.
All yorbits are flomps.
Question: Does it follow that all yorbits are vibbles?
Answer:
```

## 099/broken/second/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are vibbles.
All yorbits are blickets.
Question: Does it follow that all yorbits are vibbles?
Answer:
```

## 099/robustness/reorder/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are blickets.
All blickets are vibbles.
Question: Does it follow that all yorbits are vibbles?
Answer:
```

## 099/robustness/reorder/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All yorbits are blickets.
All blickets are vibbles.
Question: Does it follow that all vibbles are yorbits?
Answer:
```

## 099/robustness/distractors/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are snorps.
All snorps are oskets.
All blickets are vibbles.
All yorbits are blickets.
Question: Does it follow that all yorbits are vibbles?
Answer:
```

## 099/robustness/distractors/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All flomps are snorps.
All snorps are oskets.
All blickets are vibbles.
All yorbits are blickets.
Question: Does it follow that all vibbles are yorbits?
Answer:
```

## 099/robustness/rename/positive

אמת: **Yes**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are murdles.
All welbins are ruspins.
Question: Does it follow that all welbins are murdles?
Answer:
```

## 099/robustness/rename/negative

אמת: **No**; 4-shot: **No**; 12-shot: **No**.

```text
All ruspins are murdles.
All welbins are ruspins.
Question: Does it follow that all murdles are welbins?
Answer:
```
