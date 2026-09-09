# כל שאלות ההשלמה — השוואת 0/4/12 הדגמות

## 000/direct/base/0

```text
All sprocks are korvas.
All vibbles are sprocks.
All lomits are korvas.
All grivaks are quavels.
Possible completions: sprocks or quavels.
Therefore, all vibbles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 000/direct/base/1

```text
All sprocks are korvas.
All vibbles are sprocks.
All lomits are korvas.
All grivaks are quavels.
Possible completions: quavels or korvas.
Therefore, all sprocks are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | korvas | correct_target |
| 4 | " korvas." | korvas | korvas | correct_target |
| 12 | " korvas." | korvas | korvas | correct_target |
## 000/twohop/base/0

```text
All sprocks are korvas.
All vibbles are sprocks.
All lomits are korvas.
All grivaks are quavels.
Possible completions: korvas or quavels.
Therefore, all vibbles are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | korvas | reachable_one_hop |
| 4 | " sprocks." | sprocks | korvas | reachable_one_hop |
| 12 | " sprocks." | sprocks | korvas | reachable_one_hop |
## 000/twohop/base/1

```text
All korvas are sprocks.
All lomits are vibbles.
All grivaks are quavels.
All sprocks are vibbles.
Possible completions: quavels or vibbles.
Therefore, all korvas are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | vibbles | reachable_one_hop |
| 4 | " sprocks." | sprocks | vibbles | reachable_one_hop |
| 12 | " sprocks." | sprocks | vibbles | reachable_one_hop |
## 000/broken/first/0

```text
All sprocks are korvas.
All vibbles are grivaks.
All lomits are korvas.
All grivaks are quavels.
Possible completions: korvas or quavels.
Therefore, all vibbles are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | korvas | reachable_one_hop |
| 4 | " grivaks." | grivaks | quavels | reachable_one_hop |
| 12 | " grivaks." | grivaks | korvas | reachable_one_hop |
## 000/broken/second/1

```text
All sprocks are quavels.
All vibbles are sprocks.
All lomits are korvas.
All grivaks are quavels.
Possible completions: korvas or quavels.
Therefore, all vibbles are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 4 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 12 | " quavels." | quavels | quavels | correct_target |
## 000/robustness/reorder/0

```text
All lomits are korvas.
All sprocks are korvas.
All vibbles are sprocks.
All grivaks are quavels.
Possible completions: korvas or quavels.
Therefore, all vibbles are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | korvas | unreachable_fact_name |
| 4 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 12 | " sprocks." | sprocks | quavels | reachable_one_hop |
## 000/robustness/reorder/1

```text
All korvas are sprocks.
All grivaks are quavels.
All sprocks are vibbles.
All lomits are vibbles.
Possible completions: quavels or vibbles.
Therefore, all korvas are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | vibbles | reachable_one_hop |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 000/robustness/distractors/0

```text
All lomits are korvas.
All crundles are daxes.
All sprocks are korvas.
All vibbles are sprocks.
All grivaks are quavels.
All daxes are quavels.
Possible completions: korvas or quavels.
Therefore, all vibbles are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | quavels | unreachable_fact_name |
| 4 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 12 | " quavels." | quavels | quavels | wrong_candidate |
## 000/robustness/distractors/1

```text
All grivaks are quavels.
All korvas are sprocks.
All daxes are quavels.
All lomits are vibbles.
All crundles are daxes.
All sprocks are vibbles.
Possible completions: quavels or vibbles.
Therefore, all korvas are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 4 | " sprocks." | sprocks | vibbles | reachable_one_hop |
| 12 | " sprocks." | sprocks | vibbles | reachable_one_hop |
## 000/robustness/rename/0

```text
All jastles are wugs.
All shalds are jastles.
All nerps are wugs.
All zemples are yorbits.
Possible completions: wugs or yorbits.
Therefore, all shalds are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | wugs | reachable_one_hop |
| 4 | " jastles." | jastles | wugs | reachable_one_hop |
| 12 | " wugs." | wugs | wugs | correct_target |
## 000/robustness/rename/1

```text
All xandles are blickets.
All ulvets are zeltrons.
All wugs are tufas.
All blickets are zeltrons.
Possible completions: tufas or zeltrons.
Therefore, all xandles are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | tufas | reachable_one_hop |
| 4 | " blickets." | blickets | zeltrons | reachable_one_hop |
| 12 | " blickets." | blickets | zeltrons | reachable_one_hop |
## 001/direct/base/0

```text
All murdles are zemples.
All vromps are yorbits.
All nerps are yorbits.
All vibbles are vromps.
Possible completions: zemples or vromps.
Therefore, all vibbles are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " vromps." | vromps | vromps | correct_target |
| 12 | " vromps." | vromps | vromps | correct_target |
## 001/direct/base/1

```text
All murdles are zemples.
All vromps are yorbits.
All nerps are yorbits.
All vibbles are vromps.
Possible completions: yorbits or zemples.
Therefore, all vromps are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " vibbles." | vibbles | yorbits | unreachable_fact_name |
| 12 | " vibbles." | vibbles | zemples | unreachable_fact_name |
## 001/twohop/base/0

```text
All murdles are zemples.
All vromps are yorbits.
All nerps are yorbits.
All vibbles are vromps.
Possible completions: zemples or yorbits.
Therefore, all vibbles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " vromps." | vromps | yorbits | reachable_one_hop |
| 12 | " vromps." | vromps | yorbits | reachable_one_hop |
## 001/twohop/base/1

```text
All vromps are vibbles.
All murdles are zemples.
All nerps are vibbles.
All yorbits are vromps.
Possible completions: vibbles or zemples.
Therefore, all yorbits are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 001/broken/first/0

```text
All murdles are zemples.
All vromps are yorbits.
All nerps are yorbits.
All vibbles are murdles.
Possible completions: zemples or yorbits.
Therefore, all vibbles are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " murdles." | murdles | zemples | reachable_one_hop |
| 12 | " murdles." | murdles | yorbits | reachable_one_hop |
## 001/broken/second/1

```text
All murdles are zemples.
All vromps are zemples.
All nerps are yorbits.
All vibbles are vromps.
Possible completions: zemples or yorbits.
Therefore, all vibbles are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " vromps." | vromps | zemples | reachable_one_hop |
| 12 | " vromps." | vromps | zemples | reachable_one_hop |
## 001/robustness/reorder/0

```text
All vromps are yorbits.
All murdles are zemples.
All nerps are yorbits.
All vibbles are vromps.
Possible completions: zemples or yorbits.
Therefore, all vibbles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " vromps." | vromps | yorbits | reachable_one_hop |
| 12 | " vromps." | vromps | yorbits | reachable_one_hop |
## 001/robustness/reorder/1

```text
All murdles are zemples.
All nerps are vibbles.
All yorbits are vromps.
All vromps are vibbles.
Possible completions: vibbles or zemples.
Therefore, all yorbits are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | zemples | reachable_one_hop |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 001/robustness/distractors/0

```text
All murdles are zemples.
All nerps are yorbits.
All vibbles are vromps.
All kelbrins are zemples.
All quavels are kelbrins.
All vromps are yorbits.
Possible completions: zemples or yorbits.
Therefore, all vibbles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | zemples | reachable_one_hop |
| 4 | " vromps." | vromps | zemples | reachable_one_hop |
| 12 | " vromps." | vromps | zemples | reachable_one_hop |
## 001/robustness/distractors/1

```text
All nerps are vibbles.
All murdles are zemples.
All vromps are vibbles.
All yorbits are vromps.
All quavels are kelbrins.
All kelbrins are zemples.
Possible completions: vibbles or zemples.
Therefore, all yorbits are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | zemples | correct_target |
## 001/robustness/rename/0

```text
All flomps are shalds.
All korvas are kelbrins.
All snorps are kelbrins.
All grivaks are korvas.
Possible completions: shalds or kelbrins.
Therefore, all grivaks are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | wrong_candidate |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " korvas." | korvas | kelbrins | reachable_one_hop |
## 001/robustness/rename/1

```text
All oskets are welbins.
All lomits are ulvets.
All tufas are welbins.
All zorks are oskets.
Possible completions: welbins or ulvets.
Therefore, all zorks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | welbins | reachable_one_hop |
| 4 | " oskets." | oskets | welbins | reachable_one_hop |
| 12 | " oskets." | oskets | ulvets | reachable_one_hop |
## 002/direct/base/0

```text
All grivaks are shalds.
All yorbits are daxes.
All helpons are yorbits.
All jastles are daxes.
Possible completions: yorbits or shalds.
Therefore, all helpons are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | yorbits | unreachable_fact_name |
| 4 | " daxes." | daxes | yorbits | other_reachable |
| 12 | " daxes." | daxes | yorbits | other_reachable |
## 002/direct/base/1

```text
All grivaks are shalds.
All yorbits are daxes.
All helpons are yorbits.
All jastles are daxes.
Possible completions: shalds or daxes.
Therefore, all yorbits are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | daxes | unreachable_fact_name |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 002/twohop/base/0

```text
All grivaks are shalds.
All yorbits are daxes.
All helpons are yorbits.
All jastles are daxes.
Possible completions: daxes or shalds.
Therefore, all helpons are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | daxes | unreachable_fact_name |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 002/twohop/base/1

```text
All yorbits are helpons.
All jastles are helpons.
All grivaks are shalds.
All daxes are yorbits.
Possible completions: shalds or helpons.
Therefore, all daxes are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | helpons | reachable_one_hop |
| 4 | " yorbits." | yorbits | helpons | reachable_one_hop |
| 12 | " yorbits." | yorbits | helpons | reachable_one_hop |
## 002/broken/first/0

```text
All grivaks are shalds.
All yorbits are daxes.
All helpons are grivaks.
All jastles are daxes.
Possible completions: daxes or shalds.
Therefore, all helpons are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | daxes | reachable_one_hop |
| 4 | " grivaks." | grivaks | daxes | reachable_one_hop |
| 12 | " grivaks." | grivaks | daxes | reachable_one_hop |
## 002/broken/second/1

```text
All grivaks are shalds.
All yorbits are shalds.
All helpons are yorbits.
All jastles are daxes.
Possible completions: daxes or shalds.
Therefore, all helpons are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | daxes | unreachable_fact_name |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 002/robustness/reorder/0

```text
All helpons are yorbits.
All grivaks are shalds.
All jastles are daxes.
All yorbits are daxes.
Possible completions: daxes or shalds.
Therefore, all helpons are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | correct_target |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 002/robustness/reorder/1

```text
All daxes are yorbits.
All jastles are helpons.
All yorbits are helpons.
All grivaks are shalds.
Possible completions: shalds or helpons.
Therefore, all daxes are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | helpons | correct_target |
| 4 | " helpons." | helpons | helpons | correct_target |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 002/robustness/distractors/0

```text
All oskets are tufas.
All jastles are daxes.
All tufas are shalds.
All grivaks are shalds.
All yorbits are daxes.
All helpons are yorbits.
Possible completions: daxes or shalds.
Therefore, all helpons are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | correct_target |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 002/robustness/distractors/1

```text
All grivaks are shalds.
All jastles are helpons.
All tufas are shalds.
All oskets are tufas.
All daxes are yorbits.
All yorbits are helpons.
Possible completions: shalds or helpons.
Therefore, all daxes are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | shalds | reachable_one_hop |
| 4 | " yorbits." | yorbits | helpons | reachable_one_hop |
| 12 | " helpons." | helpons | helpons | correct_target |
## 002/robustness/rename/0

```text
All snorps are xandles.
All korvas are lomits.
All plinets are korvas.
All prandils are lomits.
Possible completions: lomits or xandles.
Therefore, all plinets are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | correct_target |
| 4 | " korvas." | korvas | lomits | reachable_one_hop |
| 12 | " xandles." | xandles | xandles | wrong_candidate |
## 002/robustness/rename/1

```text
All nufrons are korvas.
All quavels are korvas.
All brovets are zemples.
All zeltrons are nufrons.
Possible completions: zemples or korvas.
Therefore, all zeltrons are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | korvas | reachable_one_hop |
| 4 | " nufrons." | nufrons | korvas | reachable_one_hop |
| 12 | " nufrons." | nufrons | korvas | reachable_one_hop |
## 003/direct/base/0

```text
All tivaks are snorps.
All vromps are ruspins.
All jastles are kelbrins.
All ruspins are kelbrins.
Possible completions: snorps or ruspins.
Therefore, all vromps are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | ruspins | other_reachable |
| 4 | " kelbrins." | kelbrins | ruspins | other_reachable |
| 12 | " kelbrins." | kelbrins | ruspins | other_reachable |
## 003/direct/base/1

```text
All tivaks are snorps.
All vromps are ruspins.
All jastles are kelbrins.
All ruspins are kelbrins.
Possible completions: kelbrins or snorps.
Therefore, all ruspins are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 003/twohop/base/0

```text
All tivaks are snorps.
All vromps are ruspins.
All jastles are kelbrins.
All ruspins are kelbrins.
Possible completions: snorps or kelbrins.
Therefore, all vromps are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 003/twohop/base/1

```text
All tivaks are snorps.
All ruspins are vromps.
All jastles are vromps.
All kelbrins are ruspins.
Possible completions: vromps or snorps.
Therefore, all kelbrins are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | vromps | reachable_one_hop |
| 4 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 12 | " ruspins." | ruspins | snorps | reachable_one_hop |
## 003/broken/first/0

```text
All tivaks are snorps.
All vromps are tivaks.
All jastles are kelbrins.
All ruspins are kelbrins.
Possible completions: snorps or kelbrins.
Therefore, all vromps are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | snorps | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 12 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
## 003/broken/second/1

```text
All tivaks are snorps.
All vromps are ruspins.
All jastles are kelbrins.
All ruspins are snorps.
Possible completions: snorps or kelbrins.
Therefore, all vromps are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 003/robustness/reorder/0

```text
All ruspins are kelbrins.
All jastles are kelbrins.
All tivaks are snorps.
All vromps are ruspins.
Possible completions: snorps or kelbrins.
Therefore, all vromps are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | wrong_candidate |
| 4 | " ruspins." | ruspins | kelbrins | reachable_one_hop |
| 12 | " ruspins." | ruspins | kelbrins | reachable_one_hop |
## 003/robustness/reorder/1

```text
All ruspins are vromps.
All tivaks are snorps.
All kelbrins are ruspins.
All jastles are vromps.
Possible completions: vromps or snorps.
Therefore, all kelbrins are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | vromps | reachable_one_hop |
| 4 | " ruspins." | ruspins | vromps | reachable_one_hop |
| 12 | " ruspins." | ruspins | snorps | reachable_one_hop |
## 003/robustness/distractors/0

```text
All vromps are ruspins.
All tivaks are snorps.
All zorks are yorbits.
All yorbits are snorps.
All ruspins are kelbrins.
All jastles are kelbrins.
Possible completions: snorps or kelbrins.
Therefore, all vromps are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 4 | " ruspins." | ruspins | kelbrins | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 003/robustness/distractors/1

```text
All ruspins are vromps.
All jastles are vromps.
All zorks are yorbits.
All yorbits are snorps.
All tivaks are snorps.
All kelbrins are ruspins.
Possible completions: vromps or snorps.
Therefore, all kelbrins are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | vromps | reachable_one_hop |
| 4 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 12 | " ruspins." | ruspins | snorps | reachable_one_hop |
## 003/robustness/rename/0

```text
All nufrons are yorbits.
All brovets are shalds.
All plinets are tufas.
All shalds are tufas.
Possible completions: yorbits or tufas.
Therefore, all brovets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | yorbits | reachable_one_hop |
| 4 | " shalds." | shalds | tufas | reachable_one_hop |
| 12 | " shalds." | shalds | tufas | reachable_one_hop |
## 003/robustness/rename/1

```text
All plinets are wugs.
All sprocks are quavels.
All zorks are quavels.
All zemples are sprocks.
Possible completions: quavels or wugs.
Therefore, all zemples are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | wugs | reachable_one_hop |
| 4 | " sprocks." | sprocks | wugs | reachable_one_hop |
| 12 | " sprocks." | sprocks | wugs | reachable_one_hop |
## 004/direct/base/0

```text
All lomits are helpons.
All grivaks are helpons.
All wugs are grivaks.
All ruspins are sprocks.
Possible completions: grivaks or sprocks.
Therefore, all wugs are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | grivaks | unreachable_fact_name |
| 4 | " grivaks." | grivaks | grivaks | correct_target |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 004/direct/base/1

```text
All lomits are helpons.
All grivaks are helpons.
All wugs are grivaks.
All ruspins are sprocks.
Possible completions: sprocks or helpons.
Therefore, all grivaks are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " helpons." | helpons | helpons | correct_target |
| 12 | " helpons." | helpons | helpons | correct_target |
## 004/twohop/base/0

```text
All lomits are helpons.
All grivaks are helpons.
All wugs are grivaks.
All ruspins are sprocks.
Possible completions: helpons or sprocks.
Therefore, all wugs are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | helpons | unreachable_fact_name |
| 4 | " grivaks." | grivaks | sprocks | reachable_one_hop |
| 12 | " grivaks." | grivaks | sprocks | reachable_one_hop |
## 004/twohop/base/1

```text
All ruspins are sprocks.
All lomits are wugs.
All helpons are grivaks.
All grivaks are wugs.
Possible completions: sprocks or wugs.
Therefore, all helpons are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | wugs | reachable_one_hop |
| 4 | " grivaks." | grivaks | wugs | reachable_one_hop |
| 12 | " grivaks." | grivaks | wugs | reachable_one_hop |
## 004/broken/first/0

```text
All lomits are helpons.
All grivaks are helpons.
All wugs are ruspins.
All ruspins are sprocks.
Possible completions: helpons or sprocks.
Therefore, all wugs are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | helpons | reachable_one_hop |
| 4 | " ruspins." | ruspins | sprocks | reachable_one_hop |
| 12 | " ruspins." | ruspins | sprocks | reachable_one_hop |
## 004/broken/second/1

```text
All lomits are helpons.
All grivaks are sprocks.
All wugs are grivaks.
All ruspins are sprocks.
Possible completions: helpons or sprocks.
Therefore, all wugs are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | helpons | unreachable_fact_name |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 004/robustness/reorder/0

```text
All wugs are grivaks.
All lomits are helpons.
All grivaks are helpons.
All ruspins are sprocks.
Possible completions: helpons or sprocks.
Therefore, all wugs are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | sprocks | reachable_one_hop |
| 4 | " grivaks." | grivaks | sprocks | reachable_one_hop |
| 12 | " grivaks." | grivaks | sprocks | reachable_one_hop |
## 004/robustness/reorder/1

```text
All ruspins are sprocks.
All grivaks are wugs.
All lomits are wugs.
All helpons are grivaks.
Possible completions: sprocks or wugs.
Therefore, all helpons are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | wugs | reachable_one_hop |
| 4 | " grivaks." | grivaks | wugs | reachable_one_hop |
| 12 | " grivaks." | grivaks | wugs | reachable_one_hop |
## 004/robustness/distractors/0

```text
All ruspins are sprocks.
All wugs are grivaks.
All zorks are sprocks.
All daxes are zorks.
All grivaks are helpons.
All lomits are helpons.
Possible completions: helpons or sprocks.
Therefore, all wugs are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | helpons | correct_target |
| 4 | " grivaks." | grivaks | sprocks | reachable_one_hop |
| 12 | " grivaks." | grivaks | helpons | reachable_one_hop |
## 004/robustness/distractors/1

```text
All lomits are wugs.
All zorks are sprocks.
All daxes are zorks.
All ruspins are sprocks.
All helpons are grivaks.
All grivaks are wugs.
Possible completions: sprocks or wugs.
Therefore, all helpons are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 004/robustness/rename/0

```text
All zemples are oskets.
All vromps are oskets.
All shalds are vromps.
All plinets are brovets.
Possible completions: oskets or brovets.
Therefore, all shalds are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | oskets | unreachable_fact_name |
| 4 | " vromps." | vromps | oskets | reachable_one_hop |
| 12 | " vromps." | vromps | brovets | reachable_one_hop |
## 004/robustness/rename/1

```text
All nufrons are ulvets.
All zeltrons are vibbles.
All jastles are nerps.
All nerps are vibbles.
Possible completions: ulvets or vibbles.
Therefore, all jastles are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | vibbles | reachable_one_hop |
| 4 | " nerps." | nerps | vibbles | reachable_one_hop |
| 12 | " nerps." | nerps | vibbles | reachable_one_hop |
## 005/direct/base/0

```text
All oskets are tufas.
All nufrons are oskets.
All prandils are nerps.
All ruspins are tufas.
Possible completions: nerps or oskets.
Therefore, all nufrons are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | oskets | unreachable_fact_name |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " tufas." | tufas | oskets | other_reachable |
## 005/direct/base/1

```text
All oskets are tufas.
All nufrons are oskets.
All prandils are nerps.
All ruspins are tufas.
Possible completions: tufas or nerps.
Therefore, all oskets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 005/twohop/base/0

```text
All oskets are tufas.
All nufrons are oskets.
All prandils are nerps.
All ruspins are tufas.
Possible completions: nerps or tufas.
Therefore, all nufrons are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | nerps | unreachable_fact_name |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 005/twohop/base/1

```text
All ruspins are nufrons.
All oskets are nufrons.
All prandils are nerps.
All tufas are oskets.
Possible completions: nufrons or nerps.
Therefore, all tufas are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | nufrons | reachable_one_hop |
| 4 | " oskets." | oskets | nerps | reachable_one_hop |
| 12 | " oskets." | oskets | nufrons | reachable_one_hop |
## 005/broken/first/0

```text
All oskets are tufas.
All nufrons are prandils.
All prandils are nerps.
All ruspins are tufas.
Possible completions: nerps or tufas.
Therefore, all nufrons are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | tufas | unreachable_fact_name |
| 4 | " prandils." | prandils | tufas | reachable_one_hop |
| 12 | " tufas." | tufas | tufas | wrong_candidate |
## 005/broken/second/1

```text
All oskets are nerps.
All nufrons are oskets.
All prandils are nerps.
All ruspins are tufas.
Possible completions: nerps or tufas.
Therefore, all nufrons are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | nerps | unreachable_fact_name |
| 4 | " ruspins." | ruspins | tufas | unreachable_fact_name |
| 12 | " tufas." | tufas | tufas | wrong_candidate |
## 005/robustness/reorder/0

```text
All nufrons are oskets.
All prandils are nerps.
All oskets are tufas.
All ruspins are tufas.
Possible completions: nerps or tufas.
Therefore, all nufrons are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | nerps | reachable_one_hop |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 005/robustness/reorder/1

```text
All ruspins are nufrons.
All oskets are nufrons.
All tufas are oskets.
All prandils are nerps.
Possible completions: nufrons or nerps.
Therefore, all tufas are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | nufrons | unreachable_fact_name |
| 4 | " oskets." | oskets | nerps | reachable_one_hop |
| 12 | " oskets." | oskets | nerps | reachable_one_hop |
## 005/robustness/distractors/0

```text
All ruspins are tufas.
All nufrons are oskets.
All oskets are tufas.
All prandils are nerps.
All shalds are nerps.
All vibbles are shalds.
Possible completions: nerps or tufas.
Therefore, all nufrons are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | tufas | reachable_one_hop |
| 4 | " oskets." | oskets | tufas | reachable_one_hop |
| 12 | " tufas." | tufas | tufas | correct_target |
## 005/robustness/distractors/1

```text
All shalds are nerps.
All oskets are nufrons.
All ruspins are nufrons.
All tufas are oskets.
All prandils are nerps.
All vibbles are shalds.
Possible completions: nufrons or nerps.
Therefore, all tufas are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | nufrons | unreachable_fact_name |
| 4 | " oskets." | oskets | nerps | reachable_one_hop |
| 12 | " shalds." | shalds | nerps | unreachable_fact_name |
## 005/robustness/rename/0

```text
All blickets are kelbrins.
All sprocks are blickets.
All korvas are lomits.
All helpons are kelbrins.
Possible completions: lomits or kelbrins.
Therefore, all sprocks are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | wrong_candidate |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 005/robustness/rename/1

```text
All quavels are murdles.
All wugs are murdles.
All zemples are zeltrons.
All grivaks are wugs.
Possible completions: murdles or zeltrons.
Therefore, all grivaks are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | murdles | correct_target |
| 4 | " wugs." | wugs | zeltrons | reachable_one_hop |
| 12 | " wugs." | wugs | zeltrons | reachable_one_hop |
## 006/direct/base/0

```text
All helpons are flomps.
All blickets are xandles.
All yorbits are helpons.
All tivaks are flomps.
Possible completions: helpons or xandles.
Therefore, all yorbits are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | helpons | correct_target |
| 4 | " flomps." | flomps | helpons | other_reachable |
| 12 | " flomps." | flomps | helpons | other_reachable |
## 006/direct/base/1

```text
All helpons are flomps.
All blickets are xandles.
All yorbits are helpons.
All tivaks are flomps.
Possible completions: xandles or flomps.
Therefore, all helpons are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | flomps | correct_target |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " flomps." | flomps | flomps | correct_target |
## 006/twohop/base/0

```text
All helpons are flomps.
All blickets are xandles.
All yorbits are helpons.
All tivaks are flomps.
Possible completions: flomps or xandles.
Therefore, all yorbits are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | flomps | reachable_one_hop |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " flomps." | flomps | flomps | correct_target |
## 006/twohop/base/1

```text
All tivaks are yorbits.
All flomps are helpons.
All blickets are xandles.
All helpons are yorbits.
Possible completions: xandles or yorbits.
Therefore, all flomps are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | xandles | reachable_one_hop |
| 4 | " helpons." | helpons | yorbits | reachable_one_hop |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 006/broken/first/0

```text
All helpons are flomps.
All blickets are xandles.
All yorbits are blickets.
All tivaks are flomps.
Possible completions: flomps or xandles.
Therefore, all yorbits are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | flomps | wrong_candidate |
| 4 | " flomps." | flomps | flomps | wrong_candidate |
| 12 | " flomps." | flomps | flomps | wrong_candidate |
## 006/broken/second/1

```text
All helpons are xandles.
All blickets are xandles.
All yorbits are helpons.
All tivaks are flomps.
Possible completions: flomps or xandles.
Therefore, all yorbits are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | xandles | correct_target |
| 4 | " flomps." | flomps | flomps | wrong_candidate |
| 12 | " helpons." | helpons | xandles | reachable_one_hop |
## 006/robustness/reorder/0

```text
All helpons are flomps.
All yorbits are helpons.
All blickets are xandles.
All tivaks are flomps.
Possible completions: flomps or xandles.
Therefore, all yorbits are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | flomps | correct_target |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " flomps." | flomps | flomps | correct_target |
## 006/robustness/reorder/1

```text
All tivaks are yorbits.
All helpons are yorbits.
All blickets are xandles.
All flomps are helpons.
Possible completions: xandles or yorbits.
Therefore, all flomps are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " helpons." | helpons | xandles | reachable_one_hop |
| 12 | " helpons." | helpons | yorbits | reachable_one_hop |
## 006/robustness/distractors/0

```text
All yorbits are helpons.
All ulvets are korvas.
All tivaks are flomps.
All korvas are xandles.
All helpons are flomps.
All blickets are xandles.
Possible completions: flomps or xandles.
Therefore, all yorbits are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | flomps | reachable_one_hop |
| 4 | " helpons." | helpons | flomps | reachable_one_hop |
| 12 | " helpons." | helpons | xandles | reachable_one_hop |
## 006/robustness/distractors/1

```text
All flomps are helpons.
All ulvets are korvas.
All helpons are yorbits.
All korvas are xandles.
All tivaks are yorbits.
All blickets are xandles.
Possible completions: xandles or yorbits.
Therefore, all flomps are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | yorbits | reachable_one_hop |
| 4 | " yorbits." | yorbits | yorbits | correct_target |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 006/robustness/rename/0

```text
All murdles are sprocks.
All prandils are tufas.
All zeltrons are murdles.
All vibbles are sprocks.
Possible completions: sprocks or tufas.
Therefore, all zeltrons are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | sprocks | unreachable_fact_name |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " murdles." | murdles | tufas | reachable_one_hop |
## 006/robustness/rename/1

```text
All tufas are grivaks.
All jastles are zemples.
All wugs are zorks.
All zemples are grivaks.
Possible completions: zorks or grivaks.
Therefore, all jastles are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | grivaks | reachable_one_hop |
| 4 | " zemples." | zemples | grivaks | reachable_one_hop |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 007/direct/base/0

```text
All oskets are zorks.
All wugs are korvas.
All brovets are kelbrins.
All zorks are korvas.
Possible completions: kelbrins or zorks.
Therefore, all oskets are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " korvas." | korvas | zorks | other_reachable |
| 12 | " korvas." | korvas | zorks | other_reachable |
## 007/direct/base/1

```text
All oskets are zorks.
All wugs are korvas.
All brovets are kelbrins.
All zorks are korvas.
Possible completions: korvas or kelbrins.
Therefore, all zorks are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | korvas | correct_target |
| 4 | " korvas." | korvas | korvas | correct_target |
| 12 | " korvas." | korvas | korvas | correct_target |
## 007/twohop/base/0

```text
All oskets are zorks.
All wugs are korvas.
All brovets are kelbrins.
All zorks are korvas.
Possible completions: kelbrins or korvas.
Therefore, all oskets are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 4 | " korvas." | korvas | korvas | correct_target |
| 12 | " korvas." | korvas | korvas | correct_target |
## 007/twohop/base/1

```text
All zorks are oskets.
All wugs are oskets.
All brovets are kelbrins.
All korvas are zorks.
Possible completions: oskets or kelbrins.
Therefore, all korvas are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | oskets | reachable_one_hop |
| 4 | " zorks." | zorks | oskets | reachable_one_hop |
| 12 | " zorks." | zorks | kelbrins | reachable_one_hop |
## 007/broken/first/0

```text
All oskets are brovets.
All wugs are korvas.
All brovets are kelbrins.
All zorks are korvas.
Possible completions: kelbrins or korvas.
Therefore, all oskets are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | kelbrins | reachable_one_hop |
| 4 | " brovets." | brovets | korvas | reachable_one_hop |
| 12 | " korvas." | korvas | korvas | wrong_candidate |
## 007/broken/second/1

```text
All oskets are zorks.
All wugs are korvas.
All brovets are kelbrins.
All zorks are kelbrins.
Possible completions: kelbrins or korvas.
Therefore, all oskets are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 007/robustness/reorder/0

```text
All zorks are korvas.
All brovets are kelbrins.
All oskets are zorks.
All wugs are korvas.
Possible completions: kelbrins or korvas.
Therefore, all oskets are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | kelbrins | reachable_one_hop |
| 4 | " zorks." | zorks | kelbrins | reachable_one_hop |
| 12 | " zorks." | zorks | korvas | reachable_one_hop |
## 007/robustness/reorder/1

```text
All zorks are oskets.
All brovets are kelbrins.
All wugs are oskets.
All korvas are zorks.
Possible completions: oskets or kelbrins.
Therefore, all korvas are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | oskets | reachable_one_hop |
| 4 | " zorks." | zorks | oskets | reachable_one_hop |
| 12 | " zorks." | zorks | kelbrins | reachable_one_hop |
## 007/robustness/distractors/0

```text
All wugs are korvas.
All zorks are korvas.
All jastles are kelbrins.
All oskets are zorks.
All brovets are kelbrins.
All tufas are jastles.
Possible completions: kelbrins or korvas.
Therefore, all oskets are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | kelbrins | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 12 | " zorks." | zorks | kelbrins | reachable_one_hop |
## 007/robustness/distractors/1

```text
All brovets are kelbrins.
All zorks are oskets.
All jastles are kelbrins.
All korvas are zorks.
All wugs are oskets.
All tufas are jastles.
Possible completions: oskets or kelbrins.
Therefore, all korvas are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | oskets | reachable_one_hop |
| 4 | " zorks." | zorks | kelbrins | reachable_one_hop |
| 12 | " jastles." | jastles | kelbrins | unreachable_fact_name |
## 007/robustness/rename/0

```text
All ulvets are blickets.
All jastles are snorps.
All ruspins are sprocks.
All blickets are snorps.
Possible completions: sprocks or snorps.
Therefore, all ulvets are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | sprocks | reachable_one_hop |
| 4 | " blickets." | blickets | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | correct_target |
## 007/robustness/rename/1

```text
All daxes are ulvets.
All crundles are ulvets.
All zeltrons are vromps.
All nufrons are daxes.
Possible completions: ulvets or vromps.
Therefore, all nufrons are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | ulvets | reachable_one_hop |
| 4 | " daxes." | daxes | ulvets | reachable_one_hop |
| 12 | " daxes." | daxes | ulvets | reachable_one_hop |
## 008/direct/base/0

```text
All tivaks are zorks.
All lomits are nerps.
All korvas are zemples.
All zorks are nerps.
Possible completions: zorks or zemples.
Therefore, all tivaks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " nerps." | nerps | zorks | other_reachable |
| 12 | " nerps." | nerps | zorks | other_reachable |
## 008/direct/base/1

```text
All tivaks are zorks.
All lomits are nerps.
All korvas are zemples.
All zorks are nerps.
Possible completions: zemples or nerps.
Therefore, all zorks are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 008/twohop/base/0

```text
All tivaks are zorks.
All lomits are nerps.
All korvas are zemples.
All zorks are nerps.
Possible completions: nerps or zemples.
Therefore, all tivaks are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | nerps | reachable_one_hop |
| 4 | " zorks." | zorks | nerps | reachable_one_hop |
| 12 | " nerps." | nerps | nerps | correct_target |
## 008/twohop/base/1

```text
All zorks are tivaks.
All korvas are zemples.
All nerps are zorks.
All lomits are tivaks.
Possible completions: zemples or tivaks.
Therefore, all nerps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zemples | reachable_one_hop |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " zorks." | zorks | tivaks | reachable_one_hop |
## 008/broken/first/0

```text
All tivaks are korvas.
All lomits are nerps.
All korvas are zemples.
All zorks are nerps.
Possible completions: nerps or zemples.
Therefore, all tivaks are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | nerps | unreachable_fact_name |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 008/broken/second/1

```text
All tivaks are zorks.
All lomits are nerps.
All korvas are zemples.
All zorks are zemples.
Possible completions: nerps or zemples.
Therefore, all tivaks are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | nerps | reachable_one_hop |
| 4 | " zorks." | zorks | zemples | reachable_one_hop |
| 12 | " zorks." | zorks | zemples | reachable_one_hop |
## 008/robustness/reorder/0

```text
All korvas are zemples.
All tivaks are zorks.
All zorks are nerps.
All lomits are nerps.
Possible completions: nerps or zemples.
Therefore, all tivaks are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | nerps | reachable_one_hop |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 008/robustness/reorder/1

```text
All lomits are tivaks.
All korvas are zemples.
All nerps are zorks.
All zorks are tivaks.
Possible completions: zemples or tivaks.
Therefore, all nerps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | tivaks | reachable_one_hop |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 008/robustness/distractors/0

```text
All tivaks are zorks.
All zeltrons are zemples.
All korvas are zemples.
All lomits are nerps.
All ruspins are zeltrons.
All zorks are nerps.
Possible completions: nerps or zemples.
Therefore, all tivaks are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 008/robustness/distractors/1

```text
All nerps are zorks.
All lomits are tivaks.
All ruspins are zeltrons.
All korvas are zemples.
All zorks are tivaks.
All zeltrons are zemples.
Possible completions: zemples or tivaks.
Therefore, all nerps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | tivaks | reachable_one_hop |
| 4 | " zorks." | zorks | tivaks | reachable_one_hop |
| 12 | " zorks." | zorks | tivaks | reachable_one_hop |
## 008/robustness/rename/0

```text
All ruspins are nufrons.
All sprocks are xandles.
All shalds are vromps.
All nufrons are xandles.
Possible completions: xandles or vromps.
Therefore, all ruspins are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | xandles | correct_target |
| 4 | " vromps." | vromps | vromps | wrong_candidate |
| 12 | " shalds." | shalds | vromps | unreachable_fact_name |
## 008/robustness/rename/1

```text
All ruspins are zeltrons.
All oskets are brovets.
All shalds are ruspins.
All vibbles are zeltrons.
Possible completions: brovets or zeltrons.
Therefore, all shalds are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | brovets | reachable_one_hop |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 009/direct/base/0

```text
All blickets are vibbles.
All tufas are vibbles.
All ruspins are zeltrons.
All yorbits are blickets.
Possible completions: zeltrons or blickets.
Therefore, all yorbits are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | correct_target |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 009/direct/base/1

```text
All blickets are vibbles.
All tufas are vibbles.
All ruspins are zeltrons.
All yorbits are blickets.
Possible completions: vibbles or zeltrons.
Therefore, all blickets are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 009/twohop/base/0

```text
All blickets are vibbles.
All tufas are vibbles.
All ruspins are zeltrons.
All yorbits are blickets.
Possible completions: zeltrons or vibbles.
Therefore, all yorbits are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | vibbles | reachable_one_hop |
| 4 | " blickets." | blickets | vibbles | reachable_one_hop |
| 12 | " blickets." | blickets | vibbles | reachable_one_hop |
## 009/twohop/base/1

```text
All vibbles are blickets.
All tufas are yorbits.
All ruspins are zeltrons.
All blickets are yorbits.
Possible completions: yorbits or zeltrons.
Therefore, all vibbles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " blickets." | blickets | yorbits | reachable_one_hop |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 009/broken/first/0

```text
All blickets are vibbles.
All tufas are vibbles.
All ruspins are zeltrons.
All yorbits are ruspins.
Possible completions: zeltrons or vibbles.
Therefore, all yorbits are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " ruspins." | ruspins | vibbles | reachable_one_hop |
| 12 | " ruspins." | ruspins | vibbles | reachable_one_hop |
## 009/broken/second/1

```text
All blickets are zeltrons.
All tufas are vibbles.
All ruspins are zeltrons.
All yorbits are blickets.
Possible completions: zeltrons or vibbles.
Therefore, all yorbits are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | zeltrons | reachable_one_hop |
| 4 | " blickets." | blickets | zeltrons | reachable_one_hop |
| 12 | " blickets." | blickets | zeltrons | reachable_one_hop |
## 009/robustness/reorder/0

```text
All ruspins are zeltrons.
All yorbits are blickets.
All blickets are vibbles.
All tufas are vibbles.
Possible completions: zeltrons or vibbles.
Therefore, all yorbits are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | vibbles | reachable_one_hop |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 009/robustness/reorder/1

```text
All vibbles are blickets.
All blickets are yorbits.
All ruspins are zeltrons.
All tufas are yorbits.
Possible completions: yorbits or zeltrons.
Therefore, all vibbles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 009/robustness/distractors/0

```text
All tufas are vibbles.
All ruspins are zeltrons.
All sprocks are tivaks.
All tivaks are zeltrons.
All yorbits are blickets.
All blickets are vibbles.
Possible completions: zeltrons or vibbles.
Therefore, all yorbits are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | vibbles | reachable_one_hop |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 009/robustness/distractors/1

```text
All vibbles are blickets.
All blickets are yorbits.
All tufas are yorbits.
All sprocks are tivaks.
All ruspins are zeltrons.
All tivaks are zeltrons.
Possible completions: yorbits or zeltrons.
Therefore, all vibbles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | zeltrons | reachable_one_hop |
| 4 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 009/robustness/rename/0

```text
All grivaks are oskets.
All welbins are oskets.
All prandils are daxes.
All ulvets are grivaks.
Possible completions: daxes or oskets.
Therefore, all ulvets are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | daxes | reachable_one_hop |
| 4 | " grivaks." | grivaks | oskets | reachable_one_hop |
| 12 | " grivaks." | grivaks | daxes | reachable_one_hop |
## 009/robustness/rename/1

```text
All zorks are nufrons.
All nerps are helpons.
All grivaks are crundles.
All nufrons are helpons.
Possible completions: helpons or crundles.
Therefore, all zorks are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | helpons | correct_target |
| 4 | " nufrons." | nufrons | crundles | reachable_one_hop |
| 12 | " crundles." | crundles | crundles | wrong_candidate |
## 010/direct/base/0

```text
All grivaks are kelbrins.
All kelbrins are helpons.
All daxes are oskets.
All nufrons are helpons.
Possible completions: kelbrins or oskets.
Therefore, all grivaks are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 4 | " helpons." | helpons | oskets | other_reachable |
| 12 | " helpons." | helpons | oskets | other_reachable |
## 010/direct/base/1

```text
All grivaks are kelbrins.
All kelbrins are helpons.
All daxes are oskets.
All nufrons are helpons.
Possible completions: oskets or helpons.
Therefore, all kelbrins are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " helpons." | helpons | helpons | correct_target |
| 12 | " helpons." | helpons | helpons | correct_target |
## 010/twohop/base/0

```text
All grivaks are kelbrins.
All kelbrins are helpons.
All daxes are oskets.
All nufrons are helpons.
Possible completions: helpons or oskets.
Therefore, all grivaks are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | helpons | correct_target |
| 4 | " oskets." | oskets | oskets | wrong_candidate |
| 12 | " helpons." | helpons | helpons | correct_target |
## 010/twohop/base/1

```text
All nufrons are grivaks.
All daxes are oskets.
All kelbrins are grivaks.
All helpons are kelbrins.
Possible completions: oskets or grivaks.
Therefore, all helpons are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " kelbrins." | kelbrins | grivaks | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | grivaks | reachable_one_hop |
## 010/broken/first/0

```text
All grivaks are daxes.
All kelbrins are helpons.
All daxes are oskets.
All nufrons are helpons.
Possible completions: helpons or oskets.
Therefore, all grivaks are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | helpons | reachable_one_hop |
| 4 | " daxes." | daxes | oskets | reachable_one_hop |
| 12 | " oskets." | oskets | oskets | correct_target |
## 010/broken/second/1

```text
All grivaks are kelbrins.
All kelbrins are oskets.
All daxes are oskets.
All nufrons are helpons.
Possible completions: helpons or oskets.
Therefore, all grivaks are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | helpons | wrong_candidate |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " oskets." | oskets | oskets | correct_target |
## 010/robustness/reorder/0

```text
All daxes are oskets.
All kelbrins are helpons.
All grivaks are kelbrins.
All nufrons are helpons.
Possible completions: helpons or oskets.
Therefore, all grivaks are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | helpons | unreachable_fact_name |
| 4 | " helpons." | helpons | helpons | correct_target |
| 12 | " kelbrins." | kelbrins | helpons | reachable_one_hop |
## 010/robustness/reorder/1

```text
All helpons are kelbrins.
All daxes are oskets.
All nufrons are grivaks.
All kelbrins are grivaks.
Possible completions: oskets or grivaks.
Therefore, all helpons are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | oskets | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | grivaks | reachable_one_hop |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 010/robustness/distractors/0

```text
All snorps are oskets.
All kelbrins are helpons.
All nufrons are helpons.
All jastles are snorps.
All daxes are oskets.
All grivaks are kelbrins.
Possible completions: helpons or oskets.
Therefore, all grivaks are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | helpons | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | oskets | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | helpons | reachable_one_hop |
## 010/robustness/distractors/1

```text
All helpons are kelbrins.
All snorps are oskets.
All jastles are snorps.
All nufrons are grivaks.
All kelbrins are grivaks.
All daxes are oskets.
Possible completions: oskets or grivaks.
Therefore, all helpons are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | grivaks | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | grivaks | reachable_one_hop |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 010/robustness/rename/0

```text
All prandils are jastles.
All jastles are lomits.
All nerps are wugs.
All sprocks are lomits.
Possible completions: lomits or wugs.
Therefore, all prandils are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | correct_target |
| 4 | " wugs." | wugs | wugs | wrong_candidate |
| 12 | " wugs." | wugs | wugs | wrong_candidate |
## 010/robustness/rename/1

```text
All quavels are korvas.
All tivaks are zemples.
All flomps are korvas.
All zeltrons are flomps.
Possible completions: zemples or korvas.
Therefore, all zeltrons are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " flomps." | flomps | korvas | reachable_one_hop |
| 12 | " flomps." | flomps | korvas | reachable_one_hop |
## 011/direct/base/0

```text
All brovets are sprocks.
All zeltrons are xandles.
All vibbles are lomits.
All xandles are sprocks.
Possible completions: lomits or xandles.
Therefore, all zeltrons are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | xandles | correct_target |
| 4 | " sprocks." | sprocks | xandles | other_reachable |
| 12 | " sprocks." | sprocks | xandles | other_reachable |
## 011/direct/base/1

```text
All brovets are sprocks.
All zeltrons are xandles.
All vibbles are lomits.
All xandles are sprocks.
Possible completions: sprocks or lomits.
Therefore, all xandles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 011/twohop/base/0

```text
All brovets are sprocks.
All zeltrons are xandles.
All vibbles are lomits.
All xandles are sprocks.
Possible completions: lomits or sprocks.
Therefore, all zeltrons are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | lomits | reachable_one_hop |
| 4 | " xandles." | xandles | sprocks | reachable_one_hop |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 011/twohop/base/1

```text
All brovets are zeltrons.
All sprocks are xandles.
All xandles are zeltrons.
All vibbles are lomits.
Possible completions: zeltrons or lomits.
Therefore, all sprocks are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " lomits." | lomits | lomits | wrong_candidate |
## 011/broken/first/0

```text
All brovets are sprocks.
All zeltrons are vibbles.
All vibbles are lomits.
All xandles are sprocks.
Possible completions: lomits or sprocks.
Therefore, all zeltrons are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | lomits | unreachable_fact_name |
| 4 | " vibbles." | vibbles | sprocks | reachable_one_hop |
| 12 | " vibbles." | vibbles | sprocks | reachable_one_hop |
## 011/broken/second/1

```text
All brovets are sprocks.
All zeltrons are xandles.
All vibbles are lomits.
All xandles are lomits.
Possible completions: lomits or sprocks.
Therefore, all zeltrons are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | sprocks | reachable_one_hop |
| 4 | " xandles." | xandles | sprocks | reachable_one_hop |
| 12 | " sprocks." | sprocks | sprocks | wrong_candidate |
## 011/robustness/reorder/0

```text
All xandles are sprocks.
All zeltrons are xandles.
All vibbles are lomits.
All brovets are sprocks.
Possible completions: lomits or sprocks.
Therefore, all zeltrons are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | wrong_candidate |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 011/robustness/reorder/1

```text
All xandles are zeltrons.
All vibbles are lomits.
All sprocks are xandles.
All brovets are zeltrons.
Possible completions: zeltrons or lomits.
Therefore, all sprocks are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | lomits | reachable_one_hop |
| 4 | " xandles." | xandles | zeltrons | reachable_one_hop |
| 12 | " xandles." | xandles | zeltrons | reachable_one_hop |
## 011/robustness/distractors/0

```text
All zeltrons are xandles.
All xandles are sprocks.
All vibbles are lomits.
All welbins are zemples.
All zemples are lomits.
All brovets are sprocks.
Possible completions: lomits or sprocks.
Therefore, all zeltrons are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | wrong_candidate |
| 4 | " lomits." | lomits | lomits | wrong_candidate |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 011/robustness/distractors/1

```text
All sprocks are xandles.
All zemples are lomits.
All welbins are zemples.
All xandles are zeltrons.
All brovets are zeltrons.
All vibbles are lomits.
Possible completions: zeltrons or lomits.
Therefore, all sprocks are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | lomits | reachable_one_hop |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " lomits." | lomits | lomits | wrong_candidate |
## 011/robustness/rename/0

```text
All crundles are nerps.
All welbins are plinets.
All quavels are flomps.
All plinets are nerps.
Possible completions: flomps or nerps.
Therefore, all welbins are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " crundles." | crundles | flomps | unreachable_fact_name |
| 4 | " plinets." | plinets | nerps | reachable_one_hop |
| 12 | " plinets." | plinets | nerps | reachable_one_hop |
## 011/robustness/rename/1

```text
All zemples are ulvets.
All kelbrins are snorps.
All snorps are ulvets.
All prandils are zorks.
Possible completions: ulvets or zorks.
Therefore, all kelbrins are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | ulvets | unreachable_fact_name |
| 4 | " snorps." | snorps | ulvets | reachable_one_hop |
| 12 | " snorps." | snorps | zorks | reachable_one_hop |
## 012/direct/base/0

```text
All lomits are quavels.
All tufas are flomps.
All quavels are flomps.
All crundles are oskets.
Possible completions: quavels or oskets.
Therefore, all lomits are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | correct_target |
| 4 | " crundles." | crundles | quavels | unreachable_fact_name |
| 12 | " oskets." | oskets | oskets | wrong_candidate |
## 012/direct/base/1

```text
All lomits are quavels.
All tufas are flomps.
All quavels are flomps.
All crundles are oskets.
Possible completions: oskets or flomps.
Therefore, all quavels are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " crundles." | crundles | oskets | unreachable_fact_name |
| 4 | " crundles." | crundles | flomps | unreachable_fact_name |
| 12 | " flomps." | flomps | flomps | correct_target |
## 012/twohop/base/0

```text
All lomits are quavels.
All tufas are flomps.
All quavels are flomps.
All crundles are oskets.
Possible completions: flomps or oskets.
Therefore, all lomits are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | oskets | reachable_one_hop |
| 4 | " crundles." | crundles | oskets | unreachable_fact_name |
| 12 | " oskets." | oskets | oskets | wrong_candidate |
## 012/twohop/base/1

```text
All flomps are quavels.
All crundles are oskets.
All tufas are lomits.
All quavels are lomits.
Possible completions: oskets or lomits.
Therefore, all flomps are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | oskets | reachable_one_hop |
| 4 | " lomits." | lomits | lomits | correct_target |
| 12 | " lomits." | lomits | lomits | correct_target |
## 012/broken/first/0

```text
All lomits are crundles.
All tufas are flomps.
All quavels are flomps.
All crundles are oskets.
Possible completions: flomps or oskets.
Therefore, all lomits are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " crundles." | crundles | oskets | reachable_one_hop |
| 4 | " crundles." | crundles | oskets | reachable_one_hop |
| 12 | " oskets." | oskets | oskets | correct_target |
## 012/broken/second/1

```text
All lomits are quavels.
All tufas are flomps.
All quavels are oskets.
All crundles are oskets.
Possible completions: flomps or oskets.
Therefore, all lomits are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | flomps | reachable_one_hop |
| 4 | " quavels." | quavels | oskets | reachable_one_hop |
| 12 | " oskets." | oskets | oskets | correct_target |
## 012/robustness/reorder/0

```text
All tufas are flomps.
All crundles are oskets.
All quavels are flomps.
All lomits are quavels.
Possible completions: flomps or oskets.
Therefore, all lomits are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | flomps | reachable_one_hop |
| 4 | " quavels." | quavels | flomps | reachable_one_hop |
| 12 | " quavels." | quavels | flomps | reachable_one_hop |
## 012/robustness/reorder/1

```text
All crundles are oskets.
All quavels are lomits.
All flomps are quavels.
All tufas are lomits.
Possible completions: oskets or lomits.
Therefore, all flomps are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | oskets | unreachable_fact_name |
| 4 | " tufas." | tufas | lomits | unreachable_fact_name |
| 12 | " lomits." | lomits | lomits | correct_target |
## 012/robustness/distractors/0

```text
All quavels are flomps.
All helpons are jastles.
All lomits are quavels.
All jastles are oskets.
All tufas are flomps.
All crundles are oskets.
Possible completions: flomps or oskets.
Therefore, all lomits are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | flomps | reachable_one_hop |
| 4 | " tufas." | tufas | flomps | unreachable_fact_name |
| 12 | " tufas." | tufas | oskets | unreachable_fact_name |
## 012/robustness/distractors/1

```text
All flomps are quavels.
All jastles are oskets.
All crundles are oskets.
All helpons are jastles.
All tufas are lomits.
All quavels are lomits.
Possible completions: oskets or lomits.
Therefore, all flomps are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | lomits | reachable_one_hop |
| 4 | " lomits." | lomits | lomits | correct_target |
| 12 | " lomits." | lomits | lomits | correct_target |
## 012/robustness/rename/0

```text
All vromps are sprocks.
All korvas are ruspins.
All sprocks are ruspins.
All brovets are prandils.
Possible completions: ruspins or prandils.
Therefore, all vromps are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | ruspins | reachable_one_hop |
| 4 | " prandils." | prandils | prandils | wrong_candidate |
| 12 | " prandils." | prandils | prandils | wrong_candidate |
## 012/robustness/rename/1

```text
All plinets are yorbits.
All sprocks are helpons.
All murdles are vromps.
All yorbits are vromps.
Possible completions: helpons or vromps.
Therefore, all plinets are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | helpons | wrong_candidate |
| 4 | " vromps." | vromps | vromps | correct_target |
| 12 | " vromps." | vromps | vromps | correct_target |
## 013/direct/base/0

```text
All murdles are tufas.
All nufrons are shalds.
All brovets are sprocks.
All tufas are shalds.
Possible completions: sprocks or tufas.
Therefore, all murdles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " shalds." | shalds | tufas | other_reachable |
## 013/direct/base/1

```text
All murdles are tufas.
All nufrons are shalds.
All brovets are sprocks.
All tufas are shalds.
Possible completions: shalds or sprocks.
Therefore, all tufas are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | correct_target |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 013/twohop/base/0

```text
All murdles are tufas.
All nufrons are shalds.
All brovets are sprocks.
All tufas are shalds.
Possible completions: sprocks or shalds.
Therefore, all murdles are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 013/twohop/base/1

```text
All shalds are tufas.
All brovets are sprocks.
All tufas are murdles.
All nufrons are murdles.
Possible completions: murdles or sprocks.
Therefore, all shalds are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | sprocks | reachable_one_hop |
| 4 | " tufas." | tufas | sprocks | reachable_one_hop |
| 12 | " tufas." | tufas | murdles | reachable_one_hop |
## 013/broken/first/0

```text
All murdles are brovets.
All nufrons are shalds.
All brovets are sprocks.
All tufas are shalds.
Possible completions: sprocks or shalds.
Therefore, all murdles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | sprocks | reachable_one_hop |
| 4 | " shalds." | shalds | shalds | wrong_candidate |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 013/broken/second/1

```text
All murdles are tufas.
All nufrons are shalds.
All brovets are sprocks.
All tufas are sprocks.
Possible completions: sprocks or shalds.
Therefore, all murdles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " shalds." | shalds | shalds | wrong_candidate |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 013/robustness/reorder/0

```text
All tufas are shalds.
All brovets are sprocks.
All nufrons are shalds.
All murdles are tufas.
Possible completions: sprocks or shalds.
Therefore, all murdles are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | sprocks | reachable_one_hop |
| 4 | " tufas." | tufas | shalds | reachable_one_hop |
| 12 | " tufas." | tufas | shalds | reachable_one_hop |
## 013/robustness/reorder/1

```text
All shalds are tufas.
All nufrons are murdles.
All brovets are sprocks.
All tufas are murdles.
Possible completions: murdles or sprocks.
Therefore, all shalds are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | murdles | reachable_one_hop |
| 4 | " tufas." | tufas | murdles | reachable_one_hop |
| 12 | " tufas." | tufas | sprocks | reachable_one_hop |
## 013/robustness/distractors/0

```text
All kelbrins are korvas.
All murdles are tufas.
All korvas are sprocks.
All brovets are sprocks.
All tufas are shalds.
All nufrons are shalds.
Possible completions: sprocks or shalds.
Therefore, all murdles are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | sprocks | reachable_one_hop |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 013/robustness/distractors/1

```text
All korvas are sprocks.
All kelbrins are korvas.
All nufrons are murdles.
All tufas are murdles.
All shalds are tufas.
All brovets are sprocks.
Possible completions: murdles or sprocks.
Therefore, all shalds are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | sprocks | unreachable_fact_name |
| 4 | " tufas." | tufas | sprocks | reachable_one_hop |
| 12 | " sprocks." | sprocks | sprocks | wrong_candidate |
## 013/robustness/rename/0

```text
All grivaks are oskets.
All welbins are nerps.
All plinets are zeltrons.
All oskets are nerps.
Possible completions: zeltrons or nerps.
Therefore, all grivaks are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | zeltrons | reachable_one_hop |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 013/robustness/rename/1

```text
All vromps are zorks.
All xandles are zemples.
All zorks are nerps.
All plinets are nerps.
Possible completions: nerps or zemples.
Therefore, all vromps are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | nerps | reachable_one_hop |
| 4 | " zorks." | zorks | nerps | reachable_one_hop |
| 12 | " nerps." | nerps | nerps | correct_target |
## 014/direct/base/0

```text
All oskets are quavels.
All sprocks are zemples.
All kelbrins are zemples.
All blickets are sprocks.
Possible completions: sprocks or quavels.
Therefore, all blickets are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | wrong_candidate |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 014/direct/base/1

```text
All oskets are quavels.
All sprocks are zemples.
All kelbrins are zemples.
All blickets are sprocks.
Possible completions: quavels or zemples.
Therefore, all sprocks are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | quavels | unreachable_fact_name |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 014/twohop/base/0

```text
All oskets are quavels.
All sprocks are zemples.
All kelbrins are zemples.
All blickets are sprocks.
Possible completions: zemples or quavels.
Therefore, all blickets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | wrong_candidate |
| 4 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 12 | " sprocks." | sprocks | quavels | reachable_one_hop |
## 014/twohop/base/1

```text
All oskets are quavels.
All sprocks are blickets.
All kelbrins are blickets.
All zemples are sprocks.
Possible completions: quavels or blickets.
Therefore, all zemples are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 4 | " sprocks." | sprocks | blickets | reachable_one_hop |
| 12 | " sprocks." | sprocks | blickets | reachable_one_hop |
## 014/broken/first/0

```text
All oskets are quavels.
All sprocks are zemples.
All kelbrins are zemples.
All blickets are oskets.
Possible completions: zemples or quavels.
Therefore, all blickets are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | quavels | reachable_one_hop |
| 4 | " oskets." | oskets | quavels | reachable_one_hop |
| 12 | " oskets." | oskets | quavels | reachable_one_hop |
## 014/broken/second/1

```text
All oskets are quavels.
All sprocks are quavels.
All kelbrins are zemples.
All blickets are sprocks.
Possible completions: zemples or quavels.
Therefore, all blickets are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 12 | " sprocks." | sprocks | quavels | reachable_one_hop |
## 014/robustness/reorder/0

```text
All kelbrins are zemples.
All blickets are sprocks.
All sprocks are zemples.
All oskets are quavels.
Possible completions: zemples or quavels.
Therefore, all blickets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | zemples | unreachable_fact_name |
| 4 | " sprocks." | sprocks | zemples | reachable_one_hop |
| 12 | " quavels." | quavels | quavels | wrong_candidate |
## 014/robustness/reorder/1

```text
All oskets are quavels.
All kelbrins are blickets.
All sprocks are blickets.
All zemples are sprocks.
Possible completions: quavels or blickets.
Therefore, all zemples are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 4 | " sprocks." | sprocks | blickets | reachable_one_hop |
| 12 | " sprocks." | sprocks | blickets | reachable_one_hop |
## 014/robustness/distractors/0

```text
All jastles are ruspins.
All oskets are quavels.
All blickets are sprocks.
All ruspins are quavels.
All kelbrins are zemples.
All sprocks are zemples.
Possible completions: zemples or quavels.
Therefore, all blickets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | zemples | reachable_one_hop |
| 4 | " sprocks." | sprocks | zemples | reachable_one_hop |
| 12 | " sprocks." | sprocks | zemples | reachable_one_hop |
## 014/robustness/distractors/1

```text
All sprocks are blickets.
All ruspins are quavels.
All oskets are quavels.
All jastles are ruspins.
All zemples are sprocks.
All kelbrins are blickets.
Possible completions: quavels or blickets.
Therefore, all zemples are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | blickets | reachable_one_hop |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 014/robustness/rename/0

```text
All nufrons are grivaks.
All ulvets are tufas.
All helpons are tufas.
All jastles are ulvets.
Possible completions: tufas or grivaks.
Therefore, all jastles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | grivaks | reachable_one_hop |
| 4 | " ulvets." | ulvets | tufas | reachable_one_hop |
| 12 | " ulvets." | ulvets | tufas | reachable_one_hop |
## 014/robustness/rename/1

```text
All yorbits are xandles.
All tufas are helpons.
All daxes are helpons.
All tivaks are tufas.
Possible completions: xandles or helpons.
Therefore, all tivaks are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | xandles | reachable_one_hop |
| 4 | " tufas." | tufas | xandles | reachable_one_hop |
| 12 | " tufas." | tufas | helpons | reachable_one_hop |
## 015/direct/base/0

```text
All kelbrins are nufrons.
All lomits are sprocks.
All grivaks are nufrons.
All xandles are grivaks.
Possible completions: sprocks or grivaks.
Therefore, all xandles are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " grivaks." | grivaks | grivaks | correct_target |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 015/direct/base/1

```text
All kelbrins are nufrons.
All lomits are sprocks.
All grivaks are nufrons.
All xandles are grivaks.
Possible completions: nufrons or sprocks.
Therefore, all grivaks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 015/twohop/base/0

```text
All kelbrins are nufrons.
All lomits are sprocks.
All grivaks are nufrons.
All xandles are grivaks.
Possible completions: sprocks or nufrons.
Therefore, all xandles are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " grivaks." | grivaks | nufrons | reachable_one_hop |
| 12 | " grivaks." | grivaks | nufrons | reachable_one_hop |
## 015/twohop/base/1

```text
All grivaks are xandles.
All nufrons are grivaks.
All kelbrins are xandles.
All lomits are sprocks.
Possible completions: xandles or sprocks.
Therefore, all nufrons are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | sprocks | unreachable_fact_name |
| 4 | " grivaks." | grivaks | xandles | reachable_one_hop |
| 12 | " sprocks." | sprocks | sprocks | wrong_candidate |
## 015/broken/first/0

```text
All kelbrins are nufrons.
All lomits are sprocks.
All grivaks are nufrons.
All xandles are lomits.
Possible completions: sprocks or nufrons.
Therefore, all xandles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " lomits." | lomits | sprocks | reachable_one_hop |
| 12 | " lomits." | lomits | sprocks | reachable_one_hop |
## 015/broken/second/1

```text
All kelbrins are nufrons.
All lomits are sprocks.
All grivaks are sprocks.
All xandles are grivaks.
Possible completions: sprocks or nufrons.
Therefore, all xandles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " grivaks." | grivaks | sprocks | reachable_one_hop |
| 12 | " grivaks." | grivaks | nufrons | reachable_one_hop |
## 015/robustness/reorder/0

```text
All grivaks are nufrons.
All lomits are sprocks.
All xandles are grivaks.
All kelbrins are nufrons.
Possible completions: sprocks or nufrons.
Therefore, all xandles are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " grivaks." | grivaks | sprocks | reachable_one_hop |
| 12 | " grivaks." | grivaks | nufrons | reachable_one_hop |
## 015/robustness/reorder/1

```text
All kelbrins are xandles.
All lomits are sprocks.
All nufrons are grivaks.
All grivaks are xandles.
Possible completions: xandles or sprocks.
Therefore, all nufrons are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | xandles | correct_target |
| 4 | " grivaks." | grivaks | xandles | reachable_one_hop |
| 12 | " grivaks." | grivaks | xandles | reachable_one_hop |
## 015/robustness/distractors/0

```text
All grivaks are nufrons.
All vibbles are snorps.
All kelbrins are nufrons.
All lomits are sprocks.
All snorps are sprocks.
All xandles are grivaks.
Possible completions: sprocks or nufrons.
Therefore, all xandles are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | nufrons | reachable_one_hop |
| 4 | " grivaks." | grivaks | nufrons | reachable_one_hop |
| 12 | " grivaks." | grivaks | nufrons | reachable_one_hop |
## 015/robustness/distractors/1

```text
All snorps are sprocks.
All lomits are sprocks.
All vibbles are snorps.
All nufrons are grivaks.
All kelbrins are xandles.
All grivaks are xandles.
Possible completions: xandles or sprocks.
Therefore, all nufrons are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | xandles | reachable_one_hop |
| 4 | " grivaks." | grivaks | xandles | reachable_one_hop |
| 12 | " grivaks." | grivaks | sprocks | reachable_one_hop |
## 015/robustness/rename/0

```text
All crundles are korvas.
All yorbits are vromps.
All plinets are korvas.
All oskets are plinets.
Possible completions: vromps or korvas.
Therefore, all oskets are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | vromps | reachable_one_hop |
| 4 | " plinets." | plinets | vromps | reachable_one_hop |
| 12 | " plinets." | plinets | korvas | reachable_one_hop |
## 015/robustness/rename/1

```text
All shalds are zeltrons.
All ruspins are shalds.
All prandils are zeltrons.
All brovets are jastles.
Possible completions: zeltrons or jastles.
Therefore, all ruspins are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | jastles | reachable_one_hop |
| 4 | " shalds." | shalds | zeltrons | reachable_one_hop |
| 12 | " shalds." | shalds | jastles | reachable_one_hop |
## 016/direct/base/0

```text
All shalds are welbins.
All grivaks are welbins.
All prandils are grivaks.
All quavels are ruspins.
Possible completions: grivaks or ruspins.
Therefore, all prandils are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | grivaks | unreachable_fact_name |
| 4 | " grivaks." | grivaks | grivaks | correct_target |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 016/direct/base/1

```text
All shalds are welbins.
All grivaks are welbins.
All prandils are grivaks.
All quavels are ruspins.
Possible completions: ruspins or welbins.
Therefore, all grivaks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " welbins." | welbins | welbins | correct_target |
| 12 | " welbins." | welbins | welbins | correct_target |
## 016/twohop/base/0

```text
All shalds are welbins.
All grivaks are welbins.
All prandils are grivaks.
All quavels are ruspins.
Possible completions: welbins or ruspins.
Therefore, all prandils are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | welbins | unreachable_fact_name |
| 4 | " grivaks." | grivaks | ruspins | reachable_one_hop |
| 12 | " grivaks." | grivaks | ruspins | reachable_one_hop |
## 016/twohop/base/1

```text
All shalds are prandils.
All quavels are ruspins.
All grivaks are prandils.
All welbins are grivaks.
Possible completions: ruspins or prandils.
Therefore, all welbins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | correct_target |
| 4 | " grivaks." | grivaks | ruspins | reachable_one_hop |
| 12 | " grivaks." | grivaks | prandils | reachable_one_hop |
## 016/broken/first/0

```text
All shalds are welbins.
All grivaks are welbins.
All prandils are quavels.
All quavels are ruspins.
Possible completions: welbins or ruspins.
Therefore, all prandils are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | ruspins | reachable_one_hop |
| 4 | " quavels." | quavels | ruspins | reachable_one_hop |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 016/broken/second/1

```text
All shalds are welbins.
All grivaks are ruspins.
All prandils are grivaks.
All quavels are ruspins.
Possible completions: welbins or ruspins.
Therefore, all prandils are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | ruspins | reachable_one_hop |
| 4 | " grivaks." | grivaks | ruspins | reachable_one_hop |
| 12 | " grivaks." | grivaks | ruspins | reachable_one_hop |
## 016/robustness/reorder/0

```text
All prandils are grivaks.
All quavels are ruspins.
All grivaks are welbins.
All shalds are welbins.
Possible completions: welbins or ruspins.
Therefore, all prandils are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " grivaks." | grivaks | ruspins | reachable_one_hop |
| 12 | " grivaks." | grivaks | ruspins | reachable_one_hop |
## 016/robustness/reorder/1

```text
All quavels are ruspins.
All shalds are prandils.
All grivaks are prandils.
All welbins are grivaks.
Possible completions: ruspins or prandils.
Therefore, all welbins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | ruspins | reachable_one_hop |
| 4 | " grivaks." | grivaks | ruspins | reachable_one_hop |
| 12 | " grivaks." | grivaks | prandils | reachable_one_hop |
## 016/robustness/distractors/0

```text
All grivaks are welbins.
All prandils are grivaks.
All snorps are wugs.
All wugs are ruspins.
All quavels are ruspins.
All shalds are welbins.
Possible completions: welbins or ruspins.
Therefore, all prandils are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | welbins | reachable_one_hop |
| 4 | " grivaks." | grivaks | ruspins | reachable_one_hop |
| 12 | " grivaks." | grivaks | ruspins | reachable_one_hop |
## 016/robustness/distractors/1

```text
All snorps are wugs.
All welbins are grivaks.
All wugs are ruspins.
All shalds are prandils.
All quavels are ruspins.
All grivaks are prandils.
Possible completions: ruspins or prandils.
Therefore, all welbins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | ruspins | reachable_one_hop |
| 4 | " grivaks." | grivaks | prandils | reachable_one_hop |
| 12 | " grivaks." | grivaks | prandils | reachable_one_hop |
## 016/robustness/rename/0

```text
All wugs are zorks.
All jastles are zorks.
All korvas are jastles.
All tivaks are zeltrons.
Possible completions: zorks or zeltrons.
Therefore, all korvas are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | zeltrons | unreachable_fact_name |
| 4 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 016/robustness/rename/1

```text
All snorps are nufrons.
All tufas are yorbits.
All tivaks are nufrons.
All sprocks are tivaks.
Possible completions: yorbits or nufrons.
Therefore, all sprocks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " tivaks." | tivaks | nufrons | reachable_one_hop |
| 12 | " tivaks." | tivaks | nufrons | reachable_one_hop |
## 017/direct/base/0

```text
All prandils are zorks.
All jastles are ruspins.
All helpons are yorbits.
All zorks are ruspins.
Possible completions: yorbits or zorks.
Therefore, all prandils are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " zorks." | zorks | zorks | correct_target |
## 017/direct/base/1

```text
All prandils are zorks.
All jastles are ruspins.
All helpons are yorbits.
All zorks are ruspins.
Possible completions: ruspins or yorbits.
Therefore, all zorks are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 017/twohop/base/0

```text
All prandils are zorks.
All jastles are ruspins.
All helpons are yorbits.
All zorks are ruspins.
Possible completions: yorbits or ruspins.
Therefore, all prandils are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 017/twohop/base/1

```text
All helpons are yorbits.
All ruspins are zorks.
All jastles are prandils.
All zorks are prandils.
Possible completions: prandils or yorbits.
Therefore, all ruspins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | prandils | reachable_one_hop |
| 4 | " zorks." | zorks | yorbits | reachable_one_hop |
| 12 | " zorks." | zorks | prandils | reachable_one_hop |
## 017/broken/first/0

```text
All prandils are helpons.
All jastles are ruspins.
All helpons are yorbits.
All zorks are ruspins.
Possible completions: yorbits or ruspins.
Therefore, all prandils are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " helpons." | helpons | ruspins | reachable_one_hop |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 017/broken/second/1

```text
All prandils are zorks.
All jastles are ruspins.
All helpons are yorbits.
All zorks are yorbits.
Possible completions: yorbits or ruspins.
Therefore, all prandils are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 017/robustness/reorder/0

```text
All helpons are yorbits.
All jastles are ruspins.
All zorks are ruspins.
All prandils are zorks.
Possible completions: yorbits or ruspins.
Therefore, all prandils are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | yorbits | reachable_one_hop |
| 4 | " zorks." | zorks | ruspins | reachable_one_hop |
| 12 | " zorks." | zorks | ruspins | reachable_one_hop |
## 017/robustness/reorder/1

```text
All zorks are prandils.
All ruspins are zorks.
All helpons are yorbits.
All jastles are prandils.
Possible completions: prandils or yorbits.
Therefore, all ruspins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | prandils | reachable_one_hop |
| 4 | " zorks." | zorks | prandils | reachable_one_hop |
| 12 | " zorks." | zorks | prandils | reachable_one_hop |
## 017/robustness/distractors/0

```text
All zorks are ruspins.
All prandils are zorks.
All quavels are yorbits.
All helpons are yorbits.
All jastles are ruspins.
All tivaks are quavels.
Possible completions: yorbits or ruspins.
Therefore, all prandils are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | yorbits | reachable_one_hop |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 017/robustness/distractors/1

```text
All tivaks are quavels.
All ruspins are zorks.
All helpons are yorbits.
All quavels are yorbits.
All jastles are prandils.
All zorks are prandils.
Possible completions: prandils or yorbits.
Therefore, all ruspins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | prandils | reachable_one_hop |
| 4 | " zorks." | zorks | prandils | reachable_one_hop |
| 12 | " prandils." | prandils | prandils | correct_target |
## 017/robustness/rename/0

```text
All nerps are vibbles.
All flomps are wugs.
All sprocks are murdles.
All vibbles are wugs.
Possible completions: murdles or wugs.
Therefore, all nerps are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | wugs | reachable_one_hop |
| 4 | " vibbles." | vibbles | wugs | reachable_one_hop |
| 12 | " wugs." | wugs | wugs | correct_target |
## 017/robustness/rename/1

```text
All flomps are wugs.
All brovets are nufrons.
All kelbrins are zemples.
All nufrons are zemples.
Possible completions: zemples or wugs.
Therefore, all brovets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | wugs | reachable_one_hop |
| 4 | " wugs." | wugs | wugs | wrong_candidate |
| 12 | " wugs." | wugs | wugs | wrong_candidate |
## 018/direct/base/0

```text
All jastles are ruspins.
All daxes are yorbits.
All brovets are oskets.
All ruspins are oskets.
Possible completions: ruspins or yorbits.
Therefore, all jastles are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " oskets." | oskets | ruspins | other_reachable |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 018/direct/base/1

```text
All jastles are ruspins.
All daxes are yorbits.
All brovets are oskets.
All ruspins are oskets.
Possible completions: yorbits or oskets.
Therefore, all ruspins are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | correct_target |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " oskets." | oskets | oskets | correct_target |
## 018/twohop/base/0

```text
All jastles are ruspins.
All daxes are yorbits.
All brovets are oskets.
All ruspins are oskets.
Possible completions: oskets or yorbits.
Therefore, all jastles are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | correct_target |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " ruspins." | ruspins | oskets | reachable_one_hop |
## 018/twohop/base/1

```text
All oskets are ruspins.
All brovets are jastles.
All ruspins are jastles.
All daxes are yorbits.
Possible completions: yorbits or jastles.
Therefore, all oskets are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 018/broken/first/0

```text
All jastles are daxes.
All daxes are yorbits.
All brovets are oskets.
All ruspins are oskets.
Possible completions: oskets or yorbits.
Therefore, all jastles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " oskets." | oskets | oskets | wrong_candidate |
| 12 | " oskets." | oskets | oskets | wrong_candidate |
## 018/broken/second/1

```text
All jastles are ruspins.
All daxes are yorbits.
All brovets are oskets.
All ruspins are yorbits.
Possible completions: oskets or yorbits.
Therefore, all jastles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | oskets | reachable_one_hop |
| 4 | " ruspins." | ruspins | yorbits | reachable_one_hop |
| 12 | " ruspins." | ruspins | yorbits | reachable_one_hop |
## 018/robustness/reorder/0

```text
All daxes are yorbits.
All brovets are oskets.
All ruspins are oskets.
All jastles are ruspins.
Possible completions: oskets or yorbits.
Therefore, all jastles are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | correct_target |
| 4 | " ruspins." | ruspins | oskets | reachable_one_hop |
| 12 | " ruspins." | ruspins | oskets | reachable_one_hop |
## 018/robustness/reorder/1

```text
All oskets are ruspins.
All daxes are yorbits.
All ruspins are jastles.
All brovets are jastles.
Possible completions: yorbits or jastles.
Therefore, all oskets are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 018/robustness/distractors/0

```text
All jastles are ruspins.
All ruspins are oskets.
All daxes are yorbits.
All brovets are oskets.
All flomps are yorbits.
All sprocks are flomps.
Possible completions: oskets or yorbits.
Therefore, all jastles are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | oskets | reachable_one_hop |
| 4 | " flomps." | flomps | yorbits | unreachable_fact_name |
| 12 | " flomps." | flomps | yorbits | unreachable_fact_name |
## 018/robustness/distractors/1

```text
All oskets are ruspins.
All brovets are jastles.
All sprocks are flomps.
All ruspins are jastles.
All daxes are yorbits.
All flomps are yorbits.
Possible completions: yorbits or jastles.
Therefore, all oskets are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | jastles | reachable_one_hop |
| 4 | " ruspins." | ruspins | jastles | reachable_one_hop |
| 12 | " jastles." | jastles | jastles | correct_target |
## 018/robustness/rename/0

```text
All lomits are quavels.
All murdles are sprocks.
All welbins are vibbles.
All quavels are vibbles.
Possible completions: vibbles or sprocks.
Therefore, all lomits are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | vibbles | reachable_one_hop |
| 4 | " quavels." | quavels | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 018/robustness/rename/1

```text
All kelbrins are wugs.
All ulvets are helpons.
All wugs are helpons.
All xandles are vibbles.
Possible completions: vibbles or helpons.
Therefore, all kelbrins are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " wugs." | wugs | vibbles | reachable_one_hop |
## 019/direct/base/0

```text
All tivaks are nerps.
All oskets are nerps.
All vromps are quavels.
All zemples are oskets.
Possible completions: quavels or oskets.
Therefore, all zemples are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | quavels | other_reachable |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " oskets." | oskets | oskets | correct_target |
## 019/direct/base/1

```text
All tivaks are nerps.
All oskets are nerps.
All vromps are quavels.
All zemples are oskets.
Possible completions: nerps or quavels.
Therefore, all oskets are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 019/twohop/base/0

```text
All tivaks are nerps.
All oskets are nerps.
All vromps are quavels.
All zemples are oskets.
Possible completions: quavels or nerps.
Therefore, all zemples are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " oskets." | oskets | nerps | reachable_one_hop |
| 12 | " oskets." | oskets | nerps | reachable_one_hop |
## 019/twohop/base/1

```text
All oskets are zemples.
All nerps are oskets.
All vromps are quavels.
All tivaks are zemples.
Possible completions: zemples or quavels.
Therefore, all nerps are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 019/broken/first/0

```text
All tivaks are nerps.
All oskets are nerps.
All vromps are quavels.
All zemples are vromps.
Possible completions: quavels or nerps.
Therefore, all zemples are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | wrong_candidate |
| 4 | " vromps." | vromps | nerps | reachable_one_hop |
| 12 | " vromps." | vromps | nerps | reachable_one_hop |
## 019/broken/second/1

```text
All tivaks are nerps.
All oskets are quavels.
All vromps are quavels.
All zemples are oskets.
Possible completions: quavels or nerps.
Therefore, all zemples are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | nerps | reachable_one_hop |
| 4 | " oskets." | oskets | nerps | reachable_one_hop |
| 12 | " oskets." | oskets | nerps | reachable_one_hop |
## 019/robustness/reorder/0

```text
All tivaks are nerps.
All vromps are quavels.
All zemples are oskets.
All oskets are nerps.
Possible completions: quavels or nerps.
Therefore, all zemples are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 019/robustness/reorder/1

```text
All tivaks are zemples.
All vromps are quavels.
All oskets are zemples.
All nerps are oskets.
Possible completions: zemples or quavels.
Therefore, all nerps are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " oskets." | oskets | zemples | reachable_one_hop |
| 12 | " oskets." | oskets | zemples | reachable_one_hop |
## 019/robustness/distractors/0

```text
All oskets are nerps.
All lomits are korvas.
All vromps are quavels.
All zemples are oskets.
All tivaks are nerps.
All korvas are quavels.
Possible completions: quavels or nerps.
Therefore, all zemples are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | quavels | reachable_one_hop |
| 4 | " tivaks." | tivaks | nerps | unreachable_fact_name |
| 12 | " oskets." | oskets | nerps | reachable_one_hop |
## 019/robustness/distractors/1

```text
All tivaks are zemples.
All lomits are korvas.
All korvas are quavels.
All nerps are oskets.
All vromps are quavels.
All oskets are zemples.
Possible completions: zemples or quavels.
Therefore, all nerps are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 019/robustness/rename/0

```text
All wugs are yorbits.
All tufas are yorbits.
All flomps are zeltrons.
All ulvets are tufas.
Possible completions: zeltrons or yorbits.
Therefore, all ulvets are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 4 | " tufas." | tufas | zeltrons | reachable_one_hop |
| 12 | " tufas." | tufas | yorbits | reachable_one_hop |
## 019/robustness/rename/1

```text
All wugs are zorks.
All grivaks are wugs.
All flomps are jastles.
All prandils are zorks.
Possible completions: zorks or jastles.
Therefore, all grivaks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | zorks | reachable_one_hop |
| 4 | " wugs." | wugs | zorks | reachable_one_hop |
| 12 | " zorks." | zorks | zorks | correct_target |
## 020/direct/base/0

```text
All oskets are zemples.
All zemples are quavels.
All sprocks are ruspins.
All crundles are quavels.
Possible completions: zemples or ruspins.
Therefore, all oskets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 020/direct/base/1

```text
All oskets are zemples.
All zemples are quavels.
All sprocks are ruspins.
All crundles are quavels.
Possible completions: ruspins or quavels.
Therefore, all zemples are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 4 | " quavels." | quavels | quavels | correct_target |
| 12 | " quavels." | quavels | quavels | correct_target |
## 020/twohop/base/0

```text
All oskets are zemples.
All zemples are quavels.
All sprocks are ruspins.
All crundles are quavels.
Possible completions: quavels or ruspins.
Therefore, all oskets are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 020/twohop/base/1

```text
All sprocks are ruspins.
All crundles are oskets.
All quavels are zemples.
All zemples are oskets.
Possible completions: ruspins or oskets.
Therefore, all quavels are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | oskets | reachable_one_hop |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " oskets." | oskets | oskets | correct_target |
## 020/broken/first/0

```text
All oskets are sprocks.
All zemples are quavels.
All sprocks are ruspins.
All crundles are quavels.
Possible completions: quavels or ruspins.
Therefore, all oskets are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 020/broken/second/1

```text
All oskets are zemples.
All zemples are ruspins.
All sprocks are ruspins.
All crundles are quavels.
Possible completions: quavels or ruspins.
Therefore, all oskets are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 020/robustness/reorder/0

```text
All zemples are quavels.
All crundles are quavels.
All sprocks are ruspins.
All oskets are zemples.
Possible completions: quavels or ruspins.
Therefore, all oskets are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | correct_target |
| 4 | " zemples." | zemples | ruspins | reachable_one_hop |
| 12 | " zemples." | zemples | ruspins | reachable_one_hop |
## 020/robustness/reorder/1

```text
All crundles are oskets.
All zemples are oskets.
All sprocks are ruspins.
All quavels are zemples.
Possible completions: ruspins or oskets.
Therefore, all quavels are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 4 | " zemples." | zemples | oskets | reachable_one_hop |
| 12 | " zemples." | zemples | oskets | reachable_one_hop |
## 020/robustness/distractors/0

```text
All sprocks are ruspins.
All zemples are quavels.
All crundles are quavels.
All brovets are helpons.
All helpons are ruspins.
All oskets are zemples.
Possible completions: quavels or ruspins.
Therefore, all oskets are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | ruspins | reachable_one_hop |
| 4 | " zemples." | zemples | ruspins | reachable_one_hop |
| 12 | " zemples." | zemples | ruspins | reachable_one_hop |
## 020/robustness/distractors/1

```text
All crundles are oskets.
All brovets are helpons.
All sprocks are ruspins.
All quavels are zemples.
All zemples are oskets.
All helpons are ruspins.
Possible completions: ruspins or oskets.
Therefore, all quavels are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | oskets | reachable_one_hop |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " oskets." | oskets | oskets | correct_target |
## 020/robustness/rename/0

```text
All wugs are nufrons.
All nufrons are flomps.
All helpons are yorbits.
All zorks are flomps.
Possible completions: flomps or yorbits.
Therefore, all wugs are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " zorks." | zorks | yorbits | unreachable_fact_name |
## 020/robustness/rename/1

```text
All blickets are tivaks.
All welbins are vromps.
All daxes are brovets.
All brovets are vromps.
Possible completions: tivaks or vromps.
Therefore, all daxes are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | tivaks | reachable_one_hop |
| 4 | " brovets." | brovets | vromps | reachable_one_hop |
| 12 | " vromps." | vromps | vromps | correct_target |
## 021/direct/base/0

```text
All ulvets are nufrons.
All prandils are zorks.
All shalds are oskets.
All zorks are nufrons.
Possible completions: oskets or zorks.
Therefore, all prandils are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | zorks | other_reachable |
| 4 | " nufrons." | nufrons | zorks | other_reachable |
| 12 | " nufrons." | nufrons | zorks | other_reachable |
## 021/direct/base/1

```text
All ulvets are nufrons.
All prandils are zorks.
All shalds are oskets.
All zorks are nufrons.
Possible completions: nufrons or oskets.
Therefore, all zorks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 021/twohop/base/0

```text
All ulvets are nufrons.
All prandils are zorks.
All shalds are oskets.
All zorks are nufrons.
Possible completions: oskets or nufrons.
Therefore, all prandils are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | oskets | unreachable_fact_name |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 021/twohop/base/1

```text
All nufrons are zorks.
All shalds are oskets.
All ulvets are prandils.
All zorks are prandils.
Possible completions: prandils or oskets.
Therefore, all nufrons are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | oskets | reachable_one_hop |
| 4 | " zorks." | zorks | prandils | reachable_one_hop |
| 12 | " zorks." | zorks | oskets | reachable_one_hop |
## 021/broken/first/0

```text
All ulvets are nufrons.
All prandils are shalds.
All shalds are oskets.
All zorks are nufrons.
Possible completions: oskets or nufrons.
Therefore, all prandils are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | oskets | reachable_one_hop |
| 4 | " shalds." | shalds | nufrons | reachable_one_hop |
| 12 | " nufrons." | nufrons | nufrons | wrong_candidate |
## 021/broken/second/1

```text
All ulvets are nufrons.
All prandils are zorks.
All shalds are oskets.
All zorks are oskets.
Possible completions: oskets or nufrons.
Therefore, all prandils are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | nufrons | unreachable_fact_name |
| 4 | " zorks." | zorks | oskets | reachable_one_hop |
| 12 | " nufrons." | nufrons | nufrons | wrong_candidate |
## 021/robustness/reorder/0

```text
All prandils are zorks.
All zorks are nufrons.
All ulvets are nufrons.
All shalds are oskets.
Possible completions: oskets or nufrons.
Therefore, all prandils are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " shalds." | shalds | nufrons | unreachable_fact_name |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 021/robustness/reorder/1

```text
All nufrons are zorks.
All ulvets are prandils.
All shalds are oskets.
All zorks are prandils.
Possible completions: prandils or oskets.
Therefore, all nufrons are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | prandils | reachable_one_hop |
| 4 | " prandils." | prandils | prandils | correct_target |
| 12 | " prandils." | prandils | prandils | correct_target |
## 021/robustness/distractors/0

```text
All shalds are oskets.
All ulvets are nufrons.
All lomits are wugs.
All zorks are nufrons.
All prandils are zorks.
All wugs are oskets.
Possible completions: oskets or nufrons.
Therefore, all prandils are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | oskets | unreachable_fact_name |
| 4 | " zorks." | zorks | oskets | reachable_one_hop |
| 12 | " zorks." | zorks | nufrons | reachable_one_hop |
## 021/robustness/distractors/1

```text
All lomits are wugs.
All wugs are oskets.
All ulvets are prandils.
All zorks are prandils.
All shalds are oskets.
All nufrons are zorks.
Possible completions: prandils or oskets.
Therefore, all nufrons are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | prandils | reachable_one_hop |
| 4 | " zorks." | zorks | oskets | reachable_one_hop |
| 12 | " zorks." | zorks | oskets | reachable_one_hop |
## 021/robustness/rename/0

```text
All welbins are zeltrons.
All grivaks are vibbles.
All wugs are murdles.
All vibbles are zeltrons.
Possible completions: murdles or zeltrons.
Therefore, all grivaks are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | zeltrons | reachable_one_hop |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 021/robustness/rename/1

```text
All snorps are welbins.
All yorbits are blickets.
All tufas are murdles.
All welbins are murdles.
Possible completions: murdles or blickets.
Therefore, all snorps are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | blickets | reachable_one_hop |
| 4 | " blickets." | blickets | blickets | wrong_candidate |
| 12 | " blickets." | blickets | blickets | wrong_candidate |
## 022/direct/base/0

```text
All tivaks are tufas.
All nufrons are zemples.
All ruspins are tufas.
All jastles are ruspins.
Possible completions: ruspins or zemples.
Therefore, all jastles are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 022/direct/base/1

```text
All tivaks are tufas.
All nufrons are zemples.
All ruspins are tufas.
All jastles are ruspins.
Possible completions: zemples or tufas.
Therefore, all ruspins are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | zemples | unreachable_fact_name |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 022/twohop/base/0

```text
All tivaks are tufas.
All nufrons are zemples.
All ruspins are tufas.
All jastles are ruspins.
Possible completions: tufas or zemples.
Therefore, all jastles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " ruspins." | ruspins | tufas | reachable_one_hop |
| 12 | " ruspins." | ruspins | tufas | reachable_one_hop |
## 022/twohop/base/1

```text
All ruspins are jastles.
All tufas are ruspins.
All nufrons are zemples.
All tivaks are jastles.
Possible completions: zemples or jastles.
Therefore, all tufas are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 022/broken/first/0

```text
All tivaks are tufas.
All nufrons are zemples.
All ruspins are tufas.
All jastles are nufrons.
Possible completions: tufas or zemples.
Therefore, all jastles are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | wrong_candidate |
| 4 | " nufrons." | nufrons | zemples | reachable_one_hop |
| 12 | " nufrons." | nufrons | tufas | reachable_one_hop |
## 022/broken/second/1

```text
All tivaks are tufas.
All nufrons are zemples.
All ruspins are zemples.
All jastles are ruspins.
Possible completions: tufas or zemples.
Therefore, all jastles are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | tufas | reachable_one_hop |
| 4 | " ruspins." | ruspins | zemples | reachable_one_hop |
| 12 | " ruspins." | ruspins | tufas | reachable_one_hop |
## 022/robustness/reorder/0

```text
All tivaks are tufas.
All jastles are ruspins.
All ruspins are tufas.
All nufrons are zemples.
Possible completions: tufas or zemples.
Therefore, all jastles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " ruspins." | ruspins | zemples | reachable_one_hop |
| 12 | " ruspins." | ruspins | zemples | reachable_one_hop |
## 022/robustness/reorder/1

```text
All nufrons are zemples.
All tivaks are jastles.
All tufas are ruspins.
All ruspins are jastles.
Possible completions: zemples or jastles.
Therefore, all tufas are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | jastles | reachable_one_hop |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 022/robustness/distractors/0

```text
All ruspins are tufas.
All nerps are ulvets.
All nufrons are zemples.
All ulvets are zemples.
All jastles are ruspins.
All tivaks are tufas.
Possible completions: tufas or zemples.
Therefore, all jastles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | tufas | reachable_one_hop |
| 4 | " ruspins." | ruspins | tufas | reachable_one_hop |
| 12 | " ruspins." | ruspins | tufas | reachable_one_hop |
## 022/robustness/distractors/1

```text
All tivaks are jastles.
All nufrons are zemples.
All ruspins are jastles.
All tufas are ruspins.
All nerps are ulvets.
All ulvets are zemples.
Possible completions: zemples or jastles.
Therefore, all tufas are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " ruspins." | ruspins | jastles | reachable_one_hop |
| 12 | " jastles." | jastles | jastles | correct_target |
## 022/robustness/rename/0

```text
All zeltrons are lomits.
All snorps are flomps.
All daxes are lomits.
All oskets are daxes.
Possible completions: lomits or flomps.
Therefore, all oskets are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | lomits | reachable_one_hop |
| 4 | " daxes." | daxes | flomps | reachable_one_hop |
| 12 | " daxes." | daxes | lomits | reachable_one_hop |
## 022/robustness/rename/1

```text
All kelbrins are murdles.
All quavels are kelbrins.
All flomps are zorks.
All wugs are murdles.
Possible completions: zorks or murdles.
Therefore, all quavels are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | zorks | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | murdles | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | murdles | reachable_one_hop |
## 023/direct/base/0

```text
All helpons are ruspins.
All murdles are kelbrins.
All ruspins are kelbrins.
All daxes are flomps.
Possible completions: flomps or ruspins.
Therefore, all helpons are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 023/direct/base/1

```text
All helpons are ruspins.
All murdles are kelbrins.
All ruspins are kelbrins.
All daxes are flomps.
Possible completions: kelbrins or flomps.
Therefore, all ruspins are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 023/twohop/base/0

```text
All helpons are ruspins.
All murdles are kelbrins.
All ruspins are kelbrins.
All daxes are flomps.
Possible completions: flomps or kelbrins.
Therefore, all helpons are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | kelbrins | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 023/twohop/base/1

```text
All kelbrins are ruspins.
All ruspins are helpons.
All murdles are helpons.
All daxes are flomps.
Possible completions: helpons or flomps.
Therefore, all kelbrins are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | flomps | wrong_candidate |
| 4 | " ruspins." | ruspins | flomps | reachable_one_hop |
| 12 | " flomps." | flomps | flomps | wrong_candidate |
## 023/broken/first/0

```text
All helpons are daxes.
All murdles are kelbrins.
All ruspins are kelbrins.
All daxes are flomps.
Possible completions: flomps or kelbrins.
Therefore, all helpons are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | flomps | reachable_one_hop |
| 4 | " daxes." | daxes | kelbrins | reachable_one_hop |
| 12 | " daxes." | daxes | kelbrins | reachable_one_hop |
## 023/broken/second/1

```text
All helpons are ruspins.
All murdles are kelbrins.
All ruspins are flomps.
All daxes are flomps.
Possible completions: flomps or kelbrins.
Therefore, all helpons are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | kelbrins | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 12 | " flomps." | flomps | flomps | correct_target |
## 023/robustness/reorder/0

```text
All daxes are flomps.
All helpons are ruspins.
All ruspins are kelbrins.
All murdles are kelbrins.
Possible completions: flomps or kelbrins.
Therefore, all helpons are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | flomps | reachable_one_hop |
| 4 | " ruspins." | ruspins | kelbrins | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 023/robustness/reorder/1

```text
All kelbrins are ruspins.
All ruspins are helpons.
All daxes are flomps.
All murdles are helpons.
Possible completions: helpons or flomps.
Therefore, all kelbrins are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | flomps | wrong_candidate |
| 4 | " flomps." | flomps | flomps | wrong_candidate |
| 12 | " flomps." | flomps | flomps | wrong_candidate |
## 023/robustness/distractors/0

```text
All murdles are kelbrins.
All ruspins are kelbrins.
All daxes are flomps.
All vibbles are brovets.
All brovets are flomps.
All helpons are ruspins.
Possible completions: flomps or kelbrins.
Therefore, all helpons are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | flomps | reachable_one_hop |
| 4 | " ruspins." | ruspins | kelbrins | reachable_one_hop |
| 12 | " ruspins." | ruspins | flomps | reachable_one_hop |
## 023/robustness/distractors/1

```text
All murdles are helpons.
All daxes are flomps.
All ruspins are helpons.
All brovets are flomps.
All vibbles are brovets.
All kelbrins are ruspins.
Possible completions: helpons or flomps.
Therefore, all kelbrins are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | helpons | reachable_one_hop |
| 4 | " ruspins." | ruspins | flomps | reachable_one_hop |
| 12 | " ruspins." | ruspins | flomps | reachable_one_hop |
## 023/robustness/rename/0

```text
All shalds are blickets.
All nerps are crundles.
All blickets are crundles.
All tufas are zemples.
Possible completions: zemples or crundles.
Therefore, all shalds are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | zemples | reachable_one_hop |
| 4 | " blickets." | blickets | crundles | reachable_one_hop |
| 12 | " crundles." | crundles | crundles | correct_target |
## 023/robustness/rename/1

```text
All tivaks are sprocks.
All sprocks are plinets.
All vromps are plinets.
All yorbits are nufrons.
Possible completions: plinets or nufrons.
Therefore, all tivaks are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | correct_target |
| 4 | " sprocks." | sprocks | nufrons | reachable_one_hop |
| 12 | " sprocks." | sprocks | plinets | reachable_one_hop |
## 024/direct/base/0

```text
All nerps are ruspins.
All vromps are ruspins.
All prandils are vromps.
All tivaks are lomits.
Possible completions: vromps or lomits.
Therefore, all prandils are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | vromps | unreachable_fact_name |
| 4 | " vromps." | vromps | vromps | correct_target |
| 12 | " vromps." | vromps | vromps | correct_target |
## 024/direct/base/1

```text
All nerps are ruspins.
All vromps are ruspins.
All prandils are vromps.
All tivaks are lomits.
Possible completions: lomits or ruspins.
Therefore, all vromps are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 024/twohop/base/0

```text
All nerps are ruspins.
All vromps are ruspins.
All prandils are vromps.
All tivaks are lomits.
Possible completions: ruspins or lomits.
Therefore, all prandils are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | ruspins | unreachable_fact_name |
| 4 | " tivaks." | tivaks | lomits | unreachable_fact_name |
| 12 | " vromps." | vromps | lomits | reachable_one_hop |
## 024/twohop/base/1

```text
All vromps are prandils.
All tivaks are lomits.
All ruspins are vromps.
All nerps are prandils.
Possible completions: lomits or prandils.
Therefore, all ruspins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | wrong_candidate |
| 4 | " prandils." | prandils | prandils | correct_target |
| 12 | " prandils." | prandils | prandils | correct_target |
## 024/broken/first/0

```text
All nerps are ruspins.
All vromps are ruspins.
All prandils are tivaks.
All tivaks are lomits.
Possible completions: ruspins or lomits.
Therefore, all prandils are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | ruspins | reachable_one_hop |
| 4 | " tivaks." | tivaks | lomits | reachable_one_hop |
| 12 | " tivaks." | tivaks | lomits | reachable_one_hop |
## 024/broken/second/1

```text
All nerps are ruspins.
All vromps are lomits.
All prandils are vromps.
All tivaks are lomits.
Possible completions: ruspins or lomits.
Therefore, all prandils are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | ruspins | unreachable_fact_name |
| 4 | " lomits." | lomits | lomits | correct_target |
| 12 | " vromps." | vromps | lomits | reachable_one_hop |
## 024/robustness/reorder/0

```text
All prandils are vromps.
All vromps are ruspins.
All tivaks are lomits.
All nerps are ruspins.
Possible completions: ruspins or lomits.
Therefore, all prandils are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | lomits | unreachable_fact_name |
| 4 | " lomits." | lomits | lomits | wrong_candidate |
| 12 | " lomits." | lomits | lomits | wrong_candidate |
## 024/robustness/reorder/1

```text
All vromps are prandils.
All ruspins are vromps.
All nerps are prandils.
All tivaks are lomits.
Possible completions: lomits or prandils.
Therefore, all ruspins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | wrong_candidate |
| 4 | " prandils." | prandils | prandils | correct_target |
| 12 | " prandils." | prandils | prandils | correct_target |
## 024/robustness/distractors/0

```text
All prandils are vromps.
All nerps are ruspins.
All ulvets are sprocks.
All tivaks are lomits.
All sprocks are lomits.
All vromps are ruspins.
Possible completions: ruspins or lomits.
Therefore, all prandils are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | lomits | reachable_one_hop |
| 4 | " lomits." | lomits | lomits | wrong_candidate |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 024/robustness/distractors/1

```text
All sprocks are lomits.
All ulvets are sprocks.
All ruspins are vromps.
All nerps are prandils.
All tivaks are lomits.
All vromps are prandils.
Possible completions: lomits or prandils.
Therefore, all ruspins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | lomits | unreachable_fact_name |
| 4 | " lomits." | lomits | lomits | wrong_candidate |
| 12 | " prandils." | prandils | prandils | correct_target |
## 024/robustness/rename/0

```text
All welbins are korvas.
All zorks are korvas.
All blickets are zorks.
All quavels are crundles.
Possible completions: korvas or crundles.
Therefore, all blickets are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | korvas | unreachable_fact_name |
| 4 | " zorks." | zorks | crundles | reachable_one_hop |
| 12 | " crundles." | crundles | crundles | wrong_candidate |
## 024/robustness/rename/1

```text
All korvas are flomps.
All murdles are yorbits.
All welbins are korvas.
All quavels are flomps.
Possible completions: yorbits or flomps.
Therefore, all welbins are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | yorbits | reachable_one_hop |
| 4 | " quavels." | quavels | flomps | unreachable_fact_name |
| 12 | " flomps." | flomps | flomps | correct_target |
## 025/direct/base/0

```text
All crundles are flomps.
All shalds are wugs.
All grivaks are brovets.
All brovets are flomps.
Possible completions: wugs or brovets.
Therefore, all grivaks are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | brovets | other_reachable |
| 4 | " flomps." | flomps | brovets | other_reachable |
| 12 | " flomps." | flomps | brovets | other_reachable |
## 025/direct/base/1

```text
All crundles are flomps.
All shalds are wugs.
All grivaks are brovets.
All brovets are flomps.
Possible completions: flomps or wugs.
Therefore, all brovets are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | flomps | correct_target |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " flomps." | flomps | flomps | correct_target |
## 025/twohop/base/0

```text
All crundles are flomps.
All shalds are wugs.
All grivaks are brovets.
All brovets are flomps.
Possible completions: wugs or flomps.
Therefore, all grivaks are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | flomps | reachable_one_hop |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " flomps." | flomps | flomps | correct_target |
## 025/twohop/base/1

```text
All crundles are grivaks.
All shalds are wugs.
All flomps are brovets.
All brovets are grivaks.
Possible completions: grivaks or wugs.
Therefore, all flomps are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | correct_target |
| 4 | " grivaks." | grivaks | grivaks | correct_target |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 025/broken/first/0

```text
All crundles are flomps.
All shalds are wugs.
All grivaks are shalds.
All brovets are flomps.
Possible completions: wugs or flomps.
Therefore, all grivaks are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | wugs | reachable_one_hop |
| 4 | " flomps." | flomps | flomps | wrong_candidate |
| 12 | " shalds." | shalds | flomps | reachable_one_hop |
## 025/broken/second/1

```text
All crundles are flomps.
All shalds are wugs.
All grivaks are brovets.
All brovets are wugs.
Possible completions: wugs or flomps.
Therefore, all grivaks are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | wugs | reachable_one_hop |
| 4 | " brovets." | brovets | wugs | reachable_one_hop |
| 12 | " brovets." | brovets | wugs | reachable_one_hop |
## 025/robustness/reorder/0

```text
All shalds are wugs.
All crundles are flomps.
All grivaks are brovets.
All brovets are flomps.
Possible completions: wugs or flomps.
Therefore, all grivaks are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | wugs | reachable_one_hop |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " brovets." | brovets | flomps | reachable_one_hop |
## 025/robustness/reorder/1

```text
All crundles are grivaks.
All shalds are wugs.
All brovets are grivaks.
All flomps are brovets.
Possible completions: grivaks or wugs.
Therefore, all flomps are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | correct_target |
| 4 | " brovets." | brovets | grivaks | reachable_one_hop |
| 12 | " brovets." | brovets | grivaks | reachable_one_hop |
## 025/robustness/distractors/0

```text
All brovets are flomps.
All crundles are flomps.
All kelbrins are yorbits.
All grivaks are brovets.
All shalds are wugs.
All yorbits are wugs.
Possible completions: wugs or flomps.
Therefore, all grivaks are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | wugs | reachable_one_hop |
| 4 | " brovets." | brovets | flomps | reachable_one_hop |
| 12 | " brovets." | brovets | wugs | reachable_one_hop |
## 025/robustness/distractors/1

```text
All yorbits are wugs.
All brovets are grivaks.
All crundles are grivaks.
All shalds are wugs.
All flomps are brovets.
All kelbrins are yorbits.
Possible completions: grivaks or wugs.
Therefore, all flomps are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | grivaks | unreachable_fact_name |
| 4 | " wugs." | wugs | wugs | wrong_candidate |
| 12 | " wugs." | wugs | wugs | wrong_candidate |
## 025/robustness/rename/0

```text
All ruspins are nerps.
All oskets are tivaks.
All yorbits are vromps.
All vromps are nerps.
Possible completions: tivaks or nerps.
Therefore, all yorbits are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 025/robustness/rename/1

```text
All welbins are tivaks.
All daxes are vibbles.
All ulvets are lomits.
All lomits are tivaks.
Possible completions: tivaks or vibbles.
Therefore, all ulvets are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | tivaks | reachable_one_hop |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 026/direct/base/0

```text
All sprocks are plinets.
All shalds are flomps.
All zemples are flomps.
All nufrons are shalds.
Possible completions: shalds or plinets.
Therefore, all nufrons are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | correct_target |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 026/direct/base/1

```text
All sprocks are plinets.
All shalds are flomps.
All zemples are flomps.
All nufrons are shalds.
Possible completions: plinets or flomps.
Therefore, all shalds are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | flomps | correct_target |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " plinets." | plinets | plinets | wrong_candidate |
## 026/twohop/base/0

```text
All sprocks are plinets.
All shalds are flomps.
All zemples are flomps.
All nufrons are shalds.
Possible completions: flomps or plinets.
Therefore, all nufrons are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | plinets | reachable_one_hop |
| 4 | " shalds." | shalds | plinets | reachable_one_hop |
| 12 | " shalds." | shalds | plinets | reachable_one_hop |
## 026/twohop/base/1

```text
All shalds are nufrons.
All flomps are shalds.
All zemples are nufrons.
All sprocks are plinets.
Possible completions: plinets or nufrons.
Therefore, all flomps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | plinets | reachable_one_hop |
| 4 | " shalds." | shalds | nufrons | reachable_one_hop |
| 12 | " shalds." | shalds | nufrons | reachable_one_hop |
## 026/broken/first/0

```text
All sprocks are plinets.
All shalds are flomps.
All zemples are flomps.
All nufrons are sprocks.
Possible completions: flomps or plinets.
Therefore, all nufrons are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | plinets | reachable_one_hop |
| 4 | " sprocks." | sprocks | plinets | reachable_one_hop |
| 12 | " sprocks." | sprocks | plinets | reachable_one_hop |
## 026/broken/second/1

```text
All sprocks are plinets.
All shalds are plinets.
All zemples are flomps.
All nufrons are shalds.
Possible completions: flomps or plinets.
Therefore, all nufrons are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | plinets | reachable_one_hop |
| 4 | " shalds." | shalds | plinets | reachable_one_hop |
| 12 | " shalds." | shalds | plinets | reachable_one_hop |
## 026/robustness/reorder/0

```text
All nufrons are shalds.
All shalds are flomps.
All sprocks are plinets.
All zemples are flomps.
Possible completions: flomps or plinets.
Therefore, all nufrons are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | plinets | unreachable_fact_name |
| 4 | " shalds." | shalds | plinets | reachable_one_hop |
| 12 | " plinets." | plinets | plinets | wrong_candidate |
## 026/robustness/reorder/1

```text
All shalds are nufrons.
All flomps are shalds.
All sprocks are plinets.
All zemples are nufrons.
Possible completions: plinets or nufrons.
Therefore, all flomps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | plinets | unreachable_fact_name |
| 4 | " shalds." | shalds | plinets | reachable_one_hop |
| 12 | " shalds." | shalds | nufrons | reachable_one_hop |
## 026/robustness/distractors/0

```text
All shalds are flomps.
All ruspins are plinets.
All sprocks are plinets.
All nufrons are shalds.
All grivaks are ruspins.
All zemples are flomps.
Possible completions: flomps or plinets.
Therefore, all nufrons are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | plinets | reachable_one_hop |
| 4 | " shalds." | shalds | flomps | reachable_one_hop |
| 12 | " shalds." | shalds | plinets | reachable_one_hop |
## 026/robustness/distractors/1

```text
All zemples are nufrons.
All grivaks are ruspins.
All sprocks are plinets.
All shalds are nufrons.
All flomps are shalds.
All ruspins are plinets.
Possible completions: plinets or nufrons.
Therefore, all flomps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | plinets | reachable_one_hop |
| 4 | " shalds." | shalds | plinets | reachable_one_hop |
| 12 | " shalds." | shalds | plinets | reachable_one_hop |
## 026/robustness/rename/0

```text
All kelbrins are oskets.
All brovets are ruspins.
All crundles are ruspins.
All quavels are brovets.
Possible completions: ruspins or oskets.
Therefore, all quavels are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | ruspins | reachable_one_hop |
| 4 | " brovets." | brovets | ruspins | reachable_one_hop |
| 12 | " brovets." | brovets | ruspins | reachable_one_hop |
## 026/robustness/rename/1

```text
All korvas are murdles.
All prandils are korvas.
All tufas are murdles.
All welbins are blickets.
Possible completions: blickets or murdles.
Therefore, all prandils are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | blickets | reachable_one_hop |
| 4 | " murdles." | murdles | murdles | correct_target |
| 12 | " murdles." | murdles | murdles | correct_target |
## 027/direct/base/0

```text
All sprocks are kelbrins.
All kelbrins are zorks.
All grivaks are zorks.
All brovets are lomits.
Possible completions: lomits or kelbrins.
Therefore, all sprocks are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | wrong_candidate |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 027/direct/base/1

```text
All sprocks are kelbrins.
All kelbrins are zorks.
All grivaks are zorks.
All brovets are lomits.
Possible completions: zorks or lomits.
Therefore, all kelbrins are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " lomits." | lomits | lomits | wrong_candidate |
## 027/twohop/base/0

```text
All sprocks are kelbrins.
All kelbrins are zorks.
All grivaks are zorks.
All brovets are lomits.
Possible completions: lomits or zorks.
Therefore, all sprocks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | wrong_candidate |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " zorks." | zorks | zorks | correct_target |
## 027/twohop/base/1

```text
All grivaks are sprocks.
All zorks are kelbrins.
All brovets are lomits.
All kelbrins are sprocks.
Possible completions: sprocks or lomits.
Therefore, all zorks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | sprocks | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | lomits | reachable_one_hop |
| 12 | " lomits." | lomits | lomits | wrong_candidate |
## 027/broken/first/0

```text
All sprocks are brovets.
All kelbrins are zorks.
All grivaks are zorks.
All brovets are lomits.
Possible completions: lomits or zorks.
Therefore, all sprocks are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | lomits | reachable_one_hop |
| 4 | " zorks." | zorks | zorks | wrong_candidate |
| 12 | " zorks." | zorks | zorks | wrong_candidate |
## 027/broken/second/1

```text
All sprocks are kelbrins.
All kelbrins are lomits.
All grivaks are zorks.
All brovets are lomits.
Possible completions: lomits or zorks.
Therefore, all sprocks are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | lomits | reachable_one_hop |
| 4 | " zorks." | zorks | zorks | wrong_candidate |
| 12 | " zorks." | zorks | zorks | wrong_candidate |
## 027/robustness/reorder/0

```text
All brovets are lomits.
All sprocks are kelbrins.
All grivaks are zorks.
All kelbrins are zorks.
Possible completions: lomits or zorks.
Therefore, all sprocks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | lomits | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | zorks | reachable_one_hop |
| 12 | " zorks." | zorks | zorks | correct_target |
## 027/robustness/reorder/1

```text
All grivaks are sprocks.
All brovets are lomits.
All kelbrins are sprocks.
All zorks are kelbrins.
Possible completions: sprocks or lomits.
Therefore, all zorks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | sprocks | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | lomits | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | lomits | reachable_one_hop |
## 027/robustness/distractors/0

```text
All xandles are shalds.
All sprocks are kelbrins.
All brovets are lomits.
All grivaks are zorks.
All shalds are lomits.
All kelbrins are zorks.
Possible completions: lomits or zorks.
Therefore, all sprocks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | lomits | reachable_one_hop |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " zorks." | zorks | zorks | correct_target |
## 027/robustness/distractors/1

```text
All shalds are lomits.
All grivaks are sprocks.
All zorks are kelbrins.
All brovets are lomits.
All xandles are shalds.
All kelbrins are sprocks.
Possible completions: sprocks or lomits.
Therefore, all zorks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | lomits | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | lomits | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | lomits | reachable_one_hop |
## 027/robustness/rename/0

```text
All prandils are jastles.
All jastles are daxes.
All snorps are daxes.
All zeltrons are tivaks.
Possible completions: tivaks or daxes.
Therefore, all prandils are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | tivaks | unreachable_fact_name |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 027/robustness/rename/1

```text
All jastles are yorbits.
All zemples are welbins.
All shalds are blickets.
All welbins are yorbits.
Possible completions: yorbits or blickets.
Therefore, all zemples are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | yorbits | reachable_one_hop |
| 4 | " yorbits." | yorbits | yorbits | correct_target |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 028/direct/base/0

```text
All tufas are jastles.
All murdles are tufas.
All kelbrins are tivaks.
All vibbles are jastles.
Possible completions: tufas or tivaks.
Therefore, all murdles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 028/direct/base/1

```text
All tufas are jastles.
All murdles are tufas.
All kelbrins are tivaks.
All vibbles are jastles.
Possible completions: tivaks or jastles.
Therefore, all tufas are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 028/twohop/base/0

```text
All tufas are jastles.
All murdles are tufas.
All kelbrins are tivaks.
All vibbles are jastles.
Possible completions: jastles or tivaks.
Therefore, all murdles are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " tufas." | tufas | jastles | reachable_one_hop |
| 12 | " tufas." | tufas | tivaks | reachable_one_hop |
## 028/twohop/base/1

```text
All jastles are tufas.
All kelbrins are tivaks.
All vibbles are murdles.
All tufas are murdles.
Possible completions: tivaks or murdles.
Therefore, all jastles are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | tivaks | wrong_candidate |
| 4 | " tufas." | tufas | tivaks | reachable_one_hop |
| 12 | " tufas." | tufas | murdles | reachable_one_hop |
## 028/broken/first/0

```text
All tufas are jastles.
All murdles are kelbrins.
All kelbrins are tivaks.
All vibbles are jastles.
Possible completions: jastles or tivaks.
Therefore, all murdles are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | wrong_candidate |
| 4 | " kelbrins." | kelbrins | tivaks | reachable_one_hop |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 028/broken/second/1

```text
All tufas are tivaks.
All murdles are tufas.
All kelbrins are tivaks.
All vibbles are jastles.
Possible completions: jastles or tivaks.
Therefore, all murdles are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | wrong_candidate |
| 4 | " tufas." | tufas | jastles | reachable_one_hop |
| 12 | " tufas." | tufas | tivaks | reachable_one_hop |
## 028/robustness/reorder/0

```text
All murdles are tufas.
All vibbles are jastles.
All kelbrins are tivaks.
All tufas are jastles.
Possible completions: jastles or tivaks.
Therefore, all murdles are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " tufas." | tufas | jastles | reachable_one_hop |
| 12 | " tufas." | tufas | tivaks | reachable_one_hop |
## 028/robustness/reorder/1

```text
All kelbrins are tivaks.
All tufas are murdles.
All jastles are tufas.
All vibbles are murdles.
Possible completions: tivaks or murdles.
Therefore, all jastles are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tivaks | reachable_one_hop |
| 4 | " tufas." | tufas | murdles | reachable_one_hop |
| 12 | " tufas." | tufas | tivaks | reachable_one_hop |
## 028/robustness/distractors/0

```text
All vibbles are jastles.
All tufas are jastles.
All kelbrins are tivaks.
All nerps are tivaks.
All murdles are tufas.
All plinets are nerps.
Possible completions: jastles or tivaks.
Therefore, all murdles are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " tufas." | tufas | tivaks | reachable_one_hop |
| 12 | " tufas." | tufas | tivaks | reachable_one_hop |
## 028/robustness/distractors/1

```text
All plinets are nerps.
All vibbles are murdles.
All nerps are tivaks.
All jastles are tufas.
All kelbrins are tivaks.
All tufas are murdles.
Possible completions: tivaks or murdles.
Therefore, all jastles are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | murdles | reachable_one_hop |
| 4 | " tufas." | tufas | murdles | reachable_one_hop |
| 12 | " tufas." | tufas | murdles | reachable_one_hop |
## 028/robustness/rename/0

```text
All shalds are zeltrons.
All korvas are shalds.
All nerps are xandles.
All prandils are zeltrons.
Possible completions: zeltrons or xandles.
Therefore, all korvas are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | zeltrons | reachable_one_hop |
| 4 | " shalds." | shalds | zeltrons | reachable_one_hop |
| 12 | " shalds." | shalds | zeltrons | reachable_one_hop |
## 028/robustness/rename/1

```text
All korvas are nerps.
All sprocks are prandils.
All blickets are quavels.
All nerps are quavels.
Possible completions: prandils or quavels.
Therefore, all korvas are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | quavels | reachable_one_hop |
| 4 | " nerps." | nerps | prandils | reachable_one_hop |
| 12 | " prandils." | prandils | prandils | wrong_candidate |
## 029/direct/base/0

```text
All nufrons are welbins.
All zemples are oskets.
All vromps are nufrons.
All tufas are welbins.
Possible completions: oskets or nufrons.
Therefore, all vromps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 029/direct/base/1

```text
All nufrons are welbins.
All zemples are oskets.
All vromps are nufrons.
All tufas are welbins.
Possible completions: welbins or oskets.
Therefore, all nufrons are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " welbins." | welbins | welbins | correct_target |
| 12 | " welbins." | welbins | welbins | correct_target |
## 029/twohop/base/0

```text
All nufrons are welbins.
All zemples are oskets.
All vromps are nufrons.
All tufas are welbins.
Possible completions: oskets or welbins.
Therefore, all vromps are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 4 | " nufrons." | nufrons | welbins | reachable_one_hop |
| 12 | " nufrons." | nufrons | welbins | reachable_one_hop |
## 029/twohop/base/1

```text
All welbins are nufrons.
All nufrons are vromps.
All zemples are oskets.
All tufas are vromps.
Possible completions: vromps or oskets.
Therefore, all welbins are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | vromps | correct_target |
| 4 | " nufrons." | nufrons | vromps | reachable_one_hop |
| 12 | " vromps." | vromps | vromps | correct_target |
## 029/broken/first/0

```text
All nufrons are welbins.
All zemples are oskets.
All vromps are zemples.
All tufas are welbins.
Possible completions: oskets or welbins.
Therefore, all vromps are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | oskets | unreachable_fact_name |
| 4 | " welbins." | welbins | welbins | wrong_candidate |
| 12 | " zemples." | zemples | welbins | reachable_one_hop |
## 029/broken/second/1

```text
All nufrons are oskets.
All zemples are oskets.
All vromps are nufrons.
All tufas are welbins.
Possible completions: oskets or welbins.
Therefore, all vromps are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | correct_target |
| 4 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 12 | " nufrons." | nufrons | oskets | reachable_one_hop |
## 029/robustness/reorder/0

```text
All vromps are nufrons.
All zemples are oskets.
All nufrons are welbins.
All tufas are welbins.
Possible completions: oskets or welbins.
Therefore, all vromps are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 4 | " nufrons." | nufrons | welbins | reachable_one_hop |
| 12 | " nufrons." | nufrons | welbins | reachable_one_hop |
## 029/robustness/reorder/1

```text
All zemples are oskets.
All welbins are nufrons.
All tufas are vromps.
All nufrons are vromps.
Possible completions: vromps or oskets.
Therefore, all welbins are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | vromps | reachable_one_hop |
| 4 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 12 | " nufrons." | nufrons | oskets | reachable_one_hop |
## 029/robustness/distractors/0

```text
All nufrons are welbins.
All zemples are oskets.
All tufas are welbins.
All plinets are oskets.
All vromps are nufrons.
All brovets are plinets.
Possible completions: oskets or welbins.
Therefore, all vromps are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 4 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 12 | " nufrons." | nufrons | welbins | reachable_one_hop |
## 029/robustness/distractors/1

```text
All nufrons are vromps.
All zemples are oskets.
All welbins are nufrons.
All tufas are vromps.
All plinets are oskets.
All brovets are plinets.
Possible completions: vromps or oskets.
Therefore, all welbins are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | vromps | reachable_one_hop |
| 4 | " nufrons." | nufrons | vromps | reachable_one_hop |
| 12 | " nufrons." | nufrons | vromps | reachable_one_hop |
## 029/robustness/rename/0

```text
All korvas are helpons.
All nerps are blickets.
All jastles are korvas.
All kelbrins are helpons.
Possible completions: blickets or helpons.
Therefore, all jastles are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | wrong_candidate |
| 4 | " korvas." | korvas | blickets | reachable_one_hop |
| 12 | " korvas." | korvas | helpons | reachable_one_hop |
## 029/robustness/rename/1

```text
All nerps are ruspins.
All ruspins are daxes.
All shalds are sprocks.
All ulvets are daxes.
Possible completions: daxes or sprocks.
Therefore, all nerps are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | daxes | reachable_one_hop |
| 4 | " ruspins." | ruspins | daxes | reachable_one_hop |
| 12 | " daxes." | daxes | daxes | correct_target |
## 030/direct/base/0

```text
All quavels are korvas.
All plinets are korvas.
All daxes are plinets.
All wugs are grivaks.
Possible completions: plinets or grivaks.
Therefore, all daxes are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | correct_target |
| 4 | " plinets." | plinets | plinets | correct_target |
| 12 | " plinets." | plinets | plinets | correct_target |
## 030/direct/base/1

```text
All quavels are korvas.
All plinets are korvas.
All daxes are plinets.
All wugs are grivaks.
Possible completions: grivaks or korvas.
Therefore, all plinets are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | wrong_candidate |
| 4 | " korvas." | korvas | korvas | correct_target |
| 12 | " korvas." | korvas | korvas | correct_target |
## 030/twohop/base/0

```text
All quavels are korvas.
All plinets are korvas.
All daxes are plinets.
All wugs are grivaks.
Possible completions: korvas or grivaks.
Therefore, all daxes are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | korvas | reachable_one_hop |
| 4 | " plinets." | plinets | grivaks | reachable_one_hop |
| 12 | " plinets." | plinets | grivaks | reachable_one_hop |
## 030/twohop/base/1

```text
All wugs are grivaks.
All plinets are daxes.
All korvas are plinets.
All quavels are daxes.
Possible completions: grivaks or daxes.
Therefore, all korvas are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | grivaks | reachable_one_hop |
| 4 | " plinets." | plinets | daxes | reachable_one_hop |
| 12 | " plinets." | plinets | daxes | reachable_one_hop |
## 030/broken/first/0

```text
All quavels are korvas.
All plinets are korvas.
All daxes are wugs.
All wugs are grivaks.
Possible completions: korvas or grivaks.
Therefore, all daxes are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | korvas | reachable_one_hop |
| 4 | " grivaks." | grivaks | grivaks | correct_target |
| 12 | " wugs." | wugs | grivaks | reachable_one_hop |
## 030/broken/second/1

```text
All quavels are korvas.
All plinets are grivaks.
All daxes are plinets.
All wugs are grivaks.
Possible completions: korvas or grivaks.
Therefore, all daxes are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | grivaks | reachable_one_hop |
| 4 | " plinets." | plinets | grivaks | reachable_one_hop |
| 12 | " plinets." | plinets | grivaks | reachable_one_hop |
## 030/robustness/reorder/0

```text
All wugs are grivaks.
All daxes are plinets.
All quavels are korvas.
All plinets are korvas.
Possible completions: korvas or grivaks.
Therefore, all daxes are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | grivaks | reachable_one_hop |
| 4 | " grivaks." | grivaks | grivaks | wrong_candidate |
| 12 | " grivaks." | grivaks | grivaks | wrong_candidate |
## 030/robustness/reorder/1

```text
All quavels are daxes.
All korvas are plinets.
All wugs are grivaks.
All plinets are daxes.
Possible completions: grivaks or daxes.
Therefore, all korvas are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | grivaks | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 030/robustness/distractors/0

```text
All quavels are korvas.
All tufas are grivaks.
All plinets are korvas.
All shalds are tufas.
All wugs are grivaks.
All daxes are plinets.
Possible completions: korvas or grivaks.
Therefore, all daxes are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | korvas | reachable_one_hop |
| 4 | " plinets." | plinets | grivaks | reachable_one_hop |
| 12 | " plinets." | plinets | grivaks | reachable_one_hop |
## 030/robustness/distractors/1

```text
All korvas are plinets.
All quavels are daxes.
All plinets are daxes.
All wugs are grivaks.
All tufas are grivaks.
All shalds are tufas.
Possible completions: grivaks or daxes.
Therefore, all korvas are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | grivaks | reachable_one_hop |
| 4 | " tufas." | tufas | grivaks | unreachable_fact_name |
| 12 | " tufas." | tufas | grivaks | unreachable_fact_name |
## 030/robustness/rename/0

```text
All yorbits are nerps.
All flomps are nerps.
All prandils are flomps.
All zemples are vibbles.
Possible completions: nerps or vibbles.
Therefore, all prandils are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | nerps | unreachable_fact_name |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " flomps." | flomps | vibbles | reachable_one_hop |
## 030/robustness/rename/1

```text
All xandles are lomits.
All nerps are blickets.
All ruspins are nerps.
All shalds are blickets.
Possible completions: lomits or blickets.
Therefore, all ruspins are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | lomits | unreachable_fact_name |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 031/direct/base/0

```text
All yorbits are sprocks.
All welbins are ruspins.
All ruspins are sprocks.
All korvas are snorps.
Possible completions: snorps or ruspins.
Therefore, all welbins are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | snorps | other_reachable |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 031/direct/base/1

```text
All yorbits are sprocks.
All welbins are ruspins.
All ruspins are sprocks.
All korvas are snorps.
Possible completions: sprocks or snorps.
Therefore, all ruspins are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " snorps." | snorps | snorps | wrong_candidate |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 031/twohop/base/0

```text
All yorbits are sprocks.
All welbins are ruspins.
All ruspins are sprocks.
All korvas are snorps.
Possible completions: snorps or sprocks.
Therefore, all welbins are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | wrong_candidate |
| 4 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 031/twohop/base/1

```text
All ruspins are welbins.
All sprocks are ruspins.
All korvas are snorps.
All yorbits are welbins.
Possible completions: welbins or snorps.
Therefore, all sprocks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | welbins | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | wrong_candidate |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 031/broken/first/0

```text
All yorbits are sprocks.
All welbins are korvas.
All ruspins are sprocks.
All korvas are snorps.
Possible completions: snorps or sprocks.
Therefore, all welbins are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | correct_target |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 031/broken/second/1

```text
All yorbits are sprocks.
All welbins are ruspins.
All ruspins are snorps.
All korvas are snorps.
Possible completions: snorps or sprocks.
Therefore, all welbins are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 4 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 12 | " ruspins." | ruspins | snorps | reachable_one_hop |
## 031/robustness/reorder/0

```text
All welbins are ruspins.
All ruspins are sprocks.
All yorbits are sprocks.
All korvas are snorps.
Possible completions: snorps or sprocks.
Therefore, all welbins are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | wrong_candidate |
| 4 | " snorps." | snorps | snorps | wrong_candidate |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 031/robustness/reorder/1

```text
All sprocks are ruspins.
All yorbits are welbins.
All korvas are snorps.
All ruspins are welbins.
Possible completions: welbins or snorps.
Therefore, all sprocks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | welbins | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | wrong_candidate |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 031/robustness/distractors/0

```text
All ruspins are sprocks.
All korvas are snorps.
All welbins are ruspins.
All ulvets are snorps.
All oskets are ulvets.
All yorbits are sprocks.
Possible completions: snorps or sprocks.
Therefore, all welbins are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 031/robustness/distractors/1

```text
All ruspins are welbins.
All korvas are snorps.
All oskets are ulvets.
All yorbits are welbins.
All sprocks are ruspins.
All ulvets are snorps.
Possible completions: welbins or snorps.
Therefore, all sprocks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | welbins | reachable_one_hop |
| 4 | " ruspins." | ruspins | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 031/robustness/rename/0

```text
All helpons are daxes.
All nufrons are wugs.
All wugs are daxes.
All jastles are prandils.
Possible completions: prandils or daxes.
Therefore, all nufrons are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | daxes | reachable_one_hop |
| 4 | " wugs." | wugs | daxes | reachable_one_hop |
| 12 | " daxes." | daxes | daxes | correct_target |
## 031/robustness/rename/1

```text
All shalds are kelbrins.
All daxes are shalds.
All jastles are blickets.
All wugs are kelbrins.
Possible completions: kelbrins or blickets.
Therefore, all daxes are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | kelbrins | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " shalds." | shalds | kelbrins | reachable_one_hop |
## 032/direct/base/0

```text
All shalds are vromps.
All kelbrins are vromps.
All nufrons are yorbits.
All tivaks are shalds.
Possible completions: shalds or yorbits.
Therefore, all tivaks are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | correct_target |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 032/direct/base/1

```text
All shalds are vromps.
All kelbrins are vromps.
All nufrons are yorbits.
All tivaks are shalds.
Possible completions: yorbits or vromps.
Therefore, all shalds are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " vromps." | vromps | vromps | correct_target |
| 12 | " vromps." | vromps | vromps | correct_target |
## 032/twohop/base/0

```text
All shalds are vromps.
All kelbrins are vromps.
All nufrons are yorbits.
All tivaks are shalds.
Possible completions: vromps or yorbits.
Therefore, all tivaks are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | vromps | reachable_one_hop |
| 4 | " shalds." | shalds | vromps | reachable_one_hop |
| 12 | " shalds." | shalds | vromps | reachable_one_hop |
## 032/twohop/base/1

```text
All nufrons are yorbits.
All vromps are shalds.
All kelbrins are tivaks.
All shalds are tivaks.
Possible completions: yorbits or tivaks.
Therefore, all vromps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | yorbits | reachable_one_hop |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " shalds." | shalds | tivaks | reachable_one_hop |
## 032/broken/first/0

```text
All shalds are vromps.
All kelbrins are vromps.
All nufrons are yorbits.
All tivaks are nufrons.
Possible completions: vromps or yorbits.
Therefore, all tivaks are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | vromps | reachable_one_hop |
| 4 | " nufrons." | nufrons | yorbits | reachable_one_hop |
| 12 | " nufrons." | nufrons | yorbits | reachable_one_hop |
## 032/broken/second/1

```text
All shalds are yorbits.
All kelbrins are vromps.
All nufrons are yorbits.
All tivaks are shalds.
Possible completions: vromps or yorbits.
Therefore, all tivaks are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | vromps | reachable_one_hop |
| 4 | " shalds." | shalds | yorbits | reachable_one_hop |
| 12 | " shalds." | shalds | yorbits | reachable_one_hop |
## 032/robustness/reorder/0

```text
All nufrons are yorbits.
All tivaks are shalds.
All shalds are vromps.
All kelbrins are vromps.
Possible completions: vromps or yorbits.
Therefore, all tivaks are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | yorbits | reachable_one_hop |
| 4 | " shalds." | shalds | vromps | reachable_one_hop |
| 12 | " shalds." | shalds | yorbits | reachable_one_hop |
## 032/robustness/reorder/1

```text
All vromps are shalds.
All nufrons are yorbits.
All kelbrins are tivaks.
All shalds are tivaks.
Possible completions: yorbits or tivaks.
Therefore, all vromps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | yorbits | reachable_one_hop |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " shalds." | shalds | tivaks | reachable_one_hop |
## 032/robustness/distractors/0

```text
All daxes are wugs.
All shalds are vromps.
All kelbrins are vromps.
All wugs are yorbits.
All nufrons are yorbits.
All tivaks are shalds.
Possible completions: vromps or yorbits.
Therefore, all tivaks are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | vromps | reachable_one_hop |
| 4 | " shalds." | shalds | yorbits | reachable_one_hop |
| 12 | " shalds." | shalds | yorbits | reachable_one_hop |
## 032/robustness/distractors/1

```text
All wugs are yorbits.
All vromps are shalds.
All daxes are wugs.
All kelbrins are tivaks.
All shalds are tivaks.
All nufrons are yorbits.
Possible completions: yorbits or tivaks.
Therefore, all vromps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | yorbits | reachable_one_hop |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " shalds." | shalds | tivaks | reachable_one_hop |
## 032/robustness/rename/0

```text
All zemples are blickets.
All lomits are blickets.
All sprocks are zorks.
All nerps are zemples.
Possible completions: blickets or zorks.
Therefore, all nerps are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | correct_target |
| 4 | " zemples." | zemples | blickets | reachable_one_hop |
| 12 | " zemples." | zemples | blickets | reachable_one_hop |
## 032/robustness/rename/1

```text
All sprocks are zemples.
All jastles are crundles.
All zorks are plinets.
All crundles are plinets.
Possible completions: zemples or plinets.
Therefore, all jastles are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " crundles." | crundles | zemples | reachable_one_hop |
| 4 | " plinets." | plinets | plinets | correct_target |
| 12 | " crundles." | crundles | plinets | reachable_one_hop |
## 033/direct/base/0

```text
All daxes are sprocks.
All tivaks are plinets.
All plinets are snorps.
All yorbits are snorps.
Possible completions: sprocks or plinets.
Therefore, all tivaks are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | sprocks | other_reachable |
| 4 | " plinets." | plinets | plinets | correct_target |
| 12 | " snorps." | snorps | plinets | other_reachable |
## 033/direct/base/1

```text
All daxes are sprocks.
All tivaks are plinets.
All plinets are snorps.
All yorbits are snorps.
Possible completions: snorps or sprocks.
Therefore, all plinets are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | correct_target |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 033/twohop/base/0

```text
All daxes are sprocks.
All tivaks are plinets.
All plinets are snorps.
All yorbits are snorps.
Possible completions: sprocks or snorps.
Therefore, all tivaks are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " plinets." | plinets | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | correct_target |
## 033/twohop/base/1

```text
All snorps are plinets.
All plinets are tivaks.
All daxes are sprocks.
All yorbits are tivaks.
Possible completions: tivaks or sprocks.
Therefore, all snorps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | tivaks | correct_target |
| 4 | " plinets." | plinets | tivaks | reachable_one_hop |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 033/broken/first/0

```text
All daxes are sprocks.
All tivaks are daxes.
All plinets are snorps.
All yorbits are snorps.
Possible completions: sprocks or snorps.
Therefore, all tivaks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | sprocks | reachable_one_hop |
| 4 | " daxes." | daxes | sprocks | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 033/broken/second/1

```text
All daxes are sprocks.
All tivaks are plinets.
All plinets are sprocks.
All yorbits are snorps.
Possible completions: sprocks or snorps.
Therefore, all tivaks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " plinets." | plinets | sprocks | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 033/robustness/reorder/0

```text
All tivaks are plinets.
All yorbits are snorps.
All plinets are snorps.
All daxes are sprocks.
Possible completions: sprocks or snorps.
Therefore, all tivaks are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " plinets." | plinets | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | correct_target |
## 033/robustness/reorder/1

```text
All snorps are plinets.
All yorbits are tivaks.
All plinets are tivaks.
All daxes are sprocks.
Possible completions: tivaks or sprocks.
Therefore, all snorps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | tivaks | reachable_one_hop |
| 4 | " plinets." | plinets | tivaks | reachable_one_hop |
| 12 | " sprocks." | sprocks | sprocks | wrong_candidate |
## 033/robustness/distractors/0

```text
All tufas are zorks.
All plinets are snorps.
All tivaks are plinets.
All zorks are sprocks.
All yorbits are snorps.
All daxes are sprocks.
Possible completions: sprocks or snorps.
Therefore, all tivaks are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 12 | " sprocks." | sprocks | sprocks | wrong_candidate |
## 033/robustness/distractors/1

```text
All snorps are plinets.
All yorbits are tivaks.
All daxes are sprocks.
All zorks are sprocks.
All tufas are zorks.
All plinets are tivaks.
Possible completions: tivaks or sprocks.
Therefore, all snorps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | tivaks | reachable_one_hop |
| 4 | " plinets." | plinets | tivaks | reachable_one_hop |
| 12 | " tivaks." | tivaks | sprocks | correct_target |
## 033/robustness/rename/0

```text
All lomits are brovets.
All tufas are wugs.
All wugs are nerps.
All flomps are nerps.
Possible completions: brovets or nerps.
Therefore, all tufas are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | brovets | reachable_one_hop |
| 4 | " wugs." | wugs | nerps | reachable_one_hop |
| 12 | " nerps." | nerps | nerps | correct_target |
## 033/robustness/rename/1

```text
All ruspins are vromps.
All vromps are vibbles.
All crundles are prandils.
All zorks are vibbles.
Possible completions: vibbles or prandils.
Therefore, all ruspins are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vromps." | vromps | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | prandils | correct_target |
## 034/direct/base/0

```text
All prandils are helpons.
All nufrons are prandils.
All flomps are yorbits.
All kelbrins are helpons.
Possible completions: prandils or yorbits.
Therefore, all nufrons are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | correct_target |
| 4 | " prandils." | prandils | prandils | correct_target |
| 12 | " prandils." | prandils | prandils | correct_target |
## 034/direct/base/1

```text
All prandils are helpons.
All nufrons are prandils.
All flomps are yorbits.
All kelbrins are helpons.
Possible completions: yorbits or helpons.
Therefore, all prandils are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " helpons." | helpons | helpons | correct_target |
| 12 | " helpons." | helpons | helpons | correct_target |
## 034/twohop/base/0

```text
All prandils are helpons.
All nufrons are prandils.
All flomps are yorbits.
All kelbrins are helpons.
Possible completions: helpons or yorbits.
Therefore, all nufrons are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | helpons | reachable_one_hop |
| 4 | " prandils." | prandils | helpons | reachable_one_hop |
| 12 | " prandils." | prandils | yorbits | reachable_one_hop |
## 034/twohop/base/1

```text
All helpons are prandils.
All kelbrins are nufrons.
All flomps are yorbits.
All prandils are nufrons.
Possible completions: yorbits or nufrons.
Therefore, all helpons are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | yorbits | reachable_one_hop |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 034/broken/first/0

```text
All prandils are helpons.
All nufrons are flomps.
All flomps are yorbits.
All kelbrins are helpons.
Possible completions: helpons or yorbits.
Therefore, all nufrons are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | helpons | unreachable_fact_name |
| 4 | " flomps." | flomps | yorbits | reachable_one_hop |
| 12 | " flomps." | flomps | yorbits | reachable_one_hop |
## 034/broken/second/1

```text
All prandils are yorbits.
All nufrons are prandils.
All flomps are yorbits.
All kelbrins are helpons.
Possible completions: helpons or yorbits.
Therefore, all nufrons are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | helpons | wrong_candidate |
| 4 | " yorbits." | yorbits | yorbits | correct_target |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 034/robustness/reorder/0

```text
All prandils are helpons.
All nufrons are prandils.
All kelbrins are helpons.
All flomps are yorbits.
Possible completions: helpons or yorbits.
Therefore, all nufrons are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | helpons | reachable_one_hop |
| 4 | " prandils." | prandils | yorbits | reachable_one_hop |
| 12 | " yorbits." | yorbits | yorbits | wrong_candidate |
## 034/robustness/reorder/1

```text
All flomps are yorbits.
All prandils are nufrons.
All helpons are prandils.
All kelbrins are nufrons.
Possible completions: yorbits or nufrons.
Therefore, all helpons are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | yorbits | reachable_one_hop |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 034/robustness/distractors/0

```text
All zemples are yorbits.
All prandils are helpons.
All nufrons are prandils.
All kelbrins are helpons.
All shalds are zemples.
All flomps are yorbits.
Possible completions: helpons or yorbits.
Therefore, all nufrons are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | helpons | unreachable_fact_name |
| 4 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 12 | " yorbits." | yorbits | yorbits | wrong_candidate |
## 034/robustness/distractors/1

```text
All kelbrins are nufrons.
All helpons are prandils.
All shalds are zemples.
All flomps are yorbits.
All zemples are yorbits.
All prandils are nufrons.
Possible completions: yorbits or nufrons.
Therefore, all helpons are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 034/robustness/rename/0

```text
All zemples are shalds.
All snorps are zemples.
All oskets are ulvets.
All blickets are shalds.
Possible completions: shalds or ulvets.
Therefore, all snorps are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | shalds | reachable_one_hop |
| 4 | " zemples." | zemples | shalds | reachable_one_hop |
| 12 | " zemples." | zemples | shalds | reachable_one_hop |
## 034/robustness/rename/1

```text
All sprocks are vromps.
All ruspins are shalds.
All tufas are daxes.
All vromps are shalds.
Possible completions: daxes or shalds.
Therefore, all sprocks are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | daxes | reachable_one_hop |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 035/direct/base/0

```text
All brovets are tufas.
All plinets are jastles.
All jastles are tufas.
All oskets are vibbles.
Possible completions: vibbles or jastles.
Therefore, all plinets are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 035/direct/base/1

```text
All brovets are tufas.
All plinets are jastles.
All jastles are tufas.
All oskets are vibbles.
Possible completions: tufas or vibbles.
Therefore, all jastles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 035/twohop/base/0

```text
All brovets are tufas.
All plinets are jastles.
All jastles are tufas.
All oskets are vibbles.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " jastles." | jastles | tufas | reachable_one_hop |
| 12 | " jastles." | jastles | tufas | reachable_one_hop |
## 035/twohop/base/1

```text
All brovets are plinets.
All jastles are plinets.
All tufas are jastles.
All oskets are vibbles.
Possible completions: plinets or vibbles.
Therefore, all tufas are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | vibbles | unreachable_fact_name |
| 4 | " jastles." | jastles | vibbles | reachable_one_hop |
| 12 | " jastles." | jastles | vibbles | reachable_one_hop |
## 035/broken/first/0

```text
All brovets are tufas.
All plinets are oskets.
All jastles are tufas.
All oskets are vibbles.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " tufas." | tufas | tufas | wrong_candidate |
| 12 | " tufas." | tufas | tufas | wrong_candidate |
## 035/broken/second/1

```text
All brovets are tufas.
All plinets are jastles.
All jastles are vibbles.
All oskets are vibbles.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | vibbles | unreachable_fact_name |
| 4 | " jastles." | jastles | tufas | reachable_one_hop |
| 12 | " jastles." | jastles | tufas | reachable_one_hop |
## 035/robustness/reorder/0

```text
All plinets are jastles.
All jastles are tufas.
All oskets are vibbles.
All brovets are tufas.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " jastles." | jastles | tufas | reachable_one_hop |
| 12 | " jastles." | jastles | tufas | reachable_one_hop |
## 035/robustness/reorder/1

```text
All oskets are vibbles.
All jastles are plinets.
All tufas are jastles.
All brovets are plinets.
Possible completions: plinets or vibbles.
Therefore, all tufas are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | plinets | reachable_one_hop |
| 4 | " jastles." | jastles | vibbles | reachable_one_hop |
| 12 | " jastles." | jastles | vibbles | reachable_one_hop |
## 035/robustness/distractors/0

```text
All jastles are tufas.
All oskets are vibbles.
All korvas are zorks.
All zorks are vibbles.
All plinets are jastles.
All brovets are tufas.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " jastles." | jastles | tufas | reachable_one_hop |
| 12 | " jastles." | jastles | tufas | reachable_one_hop |
## 035/robustness/distractors/1

```text
All jastles are plinets.
All brovets are plinets.
All tufas are jastles.
All zorks are vibbles.
All korvas are zorks.
All oskets are vibbles.
Possible completions: plinets or vibbles.
Therefore, all tufas are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | plinets | reachable_one_hop |
| 4 | " jastles." | jastles | vibbles | reachable_one_hop |
| 12 | " zorks." | zorks | vibbles | unreachable_fact_name |
## 035/robustness/rename/0

```text
All flomps are zeltrons.
All ulvets are wugs.
All wugs are zeltrons.
All shalds are crundles.
Possible completions: crundles or zeltrons.
Therefore, all ulvets are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | zeltrons | reachable_one_hop |
| 4 | " wugs." | wugs | zeltrons | reachable_one_hop |
| 12 | " wugs." | wugs | zeltrons | reachable_one_hop |
## 035/robustness/rename/1

```text
All xandles are zorks.
All nufrons are zorks.
All ruspins are nufrons.
All helpons are korvas.
Possible completions: zorks or korvas.
Therefore, all ruspins are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | zorks | reachable_one_hop |
| 4 | " nufrons." | nufrons | korvas | reachable_one_hop |
| 12 | " nufrons." | nufrons | korvas | reachable_one_hop |
## 036/direct/base/0

```text
All welbins are ruspins.
All snorps are ruspins.
All tivaks are sprocks.
All nufrons are welbins.
Possible completions: welbins or sprocks.
Therefore, all nufrons are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " welbins." | welbins | welbins | correct_target |
| 12 | " welbins." | welbins | welbins | correct_target |
## 036/direct/base/1

```text
All welbins are ruspins.
All snorps are ruspins.
All tivaks are sprocks.
All nufrons are welbins.
Possible completions: sprocks or ruspins.
Therefore, all welbins are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 036/twohop/base/0

```text
All welbins are ruspins.
All snorps are ruspins.
All tivaks are sprocks.
All nufrons are welbins.
Possible completions: ruspins or sprocks.
Therefore, all nufrons are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | ruspins | reachable_one_hop |
| 4 | " welbins." | welbins | ruspins | reachable_one_hop |
| 12 | " welbins." | welbins | ruspins | reachable_one_hop |
## 036/twohop/base/1

```text
All ruspins are welbins.
All welbins are nufrons.
All tivaks are sprocks.
All snorps are nufrons.
Possible completions: sprocks or nufrons.
Therefore, all ruspins are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | sprocks | unreachable_fact_name |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 036/broken/first/0

```text
All welbins are ruspins.
All snorps are ruspins.
All tivaks are sprocks.
All nufrons are tivaks.
Possible completions: ruspins or sprocks.
Therefore, all nufrons are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | ruspins | reachable_one_hop |
| 4 | " tivaks." | tivaks | ruspins | reachable_one_hop |
| 12 | " tivaks." | tivaks | ruspins | reachable_one_hop |
## 036/broken/second/1

```text
All welbins are sprocks.
All snorps are ruspins.
All tivaks are sprocks.
All nufrons are welbins.
Possible completions: ruspins or sprocks.
Therefore, all nufrons are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | sprocks | reachable_one_hop |
| 4 | " welbins." | welbins | sprocks | reachable_one_hop |
| 12 | " welbins." | welbins | sprocks | reachable_one_hop |
## 036/robustness/reorder/0

```text
All snorps are ruspins.
All nufrons are welbins.
All tivaks are sprocks.
All welbins are ruspins.
Possible completions: ruspins or sprocks.
Therefore, all nufrons are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | ruspins | reachable_one_hop |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 036/robustness/reorder/1

```text
All tivaks are sprocks.
All snorps are nufrons.
All welbins are nufrons.
All ruspins are welbins.
Possible completions: sprocks or nufrons.
Therefore, all ruspins are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " welbins." | welbins | nufrons | reachable_one_hop |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 036/robustness/distractors/0

```text
All yorbits are vromps.
All nufrons are welbins.
All welbins are ruspins.
All vromps are sprocks.
All tivaks are sprocks.
All snorps are ruspins.
Possible completions: ruspins or sprocks.
Therefore, all nufrons are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | ruspins | reachable_one_hop |
| 4 | " welbins." | welbins | ruspins | reachable_one_hop |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 036/robustness/distractors/1

```text
All vromps are sprocks.
All tivaks are sprocks.
All snorps are nufrons.
All welbins are nufrons.
All yorbits are vromps.
All ruspins are welbins.
Possible completions: sprocks or nufrons.
Therefore, all ruspins are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " welbins." | welbins | nufrons | reachable_one_hop |
| 12 | " welbins." | welbins | nufrons | reachable_one_hop |
## 036/robustness/rename/0

```text
All zeltrons are prandils.
All vromps are prandils.
All murdles are daxes.
All jastles are zeltrons.
Possible completions: prandils or daxes.
Therefore, all jastles are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | correct_target |
| 4 | " zeltrons." | zeltrons | prandils | reachable_one_hop |
| 12 | " zeltrons." | zeltrons | prandils | reachable_one_hop |
## 036/robustness/rename/1

```text
All wugs are ulvets.
All ulvets are oskets.
All blickets are zeltrons.
All zorks are oskets.
Possible completions: zeltrons or oskets.
Therefore, all wugs are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 4 | " ulvets." | ulvets | zeltrons | reachable_one_hop |
| 12 | " oskets." | oskets | oskets | correct_target |
## 037/direct/base/0

```text
All korvas are snorps.
All brovets are snorps.
All jastles are zemples.
All nufrons are brovets.
Possible completions: zemples or brovets.
Therefore, all nufrons are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " brovets." | brovets | brovets | correct_target |
| 12 | " brovets." | brovets | brovets | correct_target |
## 037/direct/base/1

```text
All korvas are snorps.
All brovets are snorps.
All jastles are zemples.
All nufrons are brovets.
Possible completions: snorps or zemples.
Therefore, all brovets are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | correct_target |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 037/twohop/base/0

```text
All korvas are snorps.
All brovets are snorps.
All jastles are zemples.
All nufrons are brovets.
Possible completions: zemples or snorps.
Therefore, all nufrons are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " brovets." | brovets | snorps | reachable_one_hop |
## 037/twohop/base/1

```text
All korvas are nufrons.
All snorps are brovets.
All brovets are nufrons.
All jastles are zemples.
Possible completions: nufrons or zemples.
Therefore, all snorps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | nufrons | unreachable_fact_name |
| 4 | " zemples." | zemples | zemples | wrong_candidate |
| 12 | " zemples." | zemples | zemples | wrong_candidate |
## 037/broken/first/0

```text
All korvas are snorps.
All brovets are snorps.
All jastles are zemples.
All nufrons are jastles.
Possible completions: zemples or snorps.
Therefore, all nufrons are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " jastles." | jastles | zemples | reachable_one_hop |
| 12 | " jastles." | jastles | snorps | reachable_one_hop |
## 037/broken/second/1

```text
All korvas are snorps.
All brovets are zemples.
All jastles are zemples.
All nufrons are brovets.
Possible completions: zemples or snorps.
Therefore, all nufrons are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | zemples | reachable_one_hop |
| 4 | " brovets." | brovets | snorps | reachable_one_hop |
| 12 | " brovets." | brovets | snorps | reachable_one_hop |
## 037/robustness/reorder/0

```text
All nufrons are brovets.
All korvas are snorps.
All jastles are zemples.
All brovets are snorps.
Possible completions: zemples or snorps.
Therefore, all nufrons are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | zemples | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 037/robustness/reorder/1

```text
All korvas are nufrons.
All brovets are nufrons.
All snorps are brovets.
All jastles are zemples.
Possible completions: nufrons or zemples.
Therefore, all snorps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | nufrons | unreachable_fact_name |
| 4 | " zemples." | zemples | zemples | wrong_candidate |
| 12 | " zemples." | zemples | zemples | wrong_candidate |
## 037/robustness/distractors/0

```text
All korvas are snorps.
All jastles are zemples.
All brovets are snorps.
All grivaks are yorbits.
All nufrons are brovets.
All yorbits are zemples.
Possible completions: zemples or snorps.
Therefore, all nufrons are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 037/robustness/distractors/1

```text
All brovets are nufrons.
All yorbits are zemples.
All jastles are zemples.
All grivaks are yorbits.
All snorps are brovets.
All korvas are nufrons.
Possible completions: nufrons or zemples.
Therefore, all snorps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | nufrons | unreachable_fact_name |
| 4 | " korvas." | korvas | nufrons | unreachable_fact_name |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 037/robustness/rename/0

```text
All sprocks are lomits.
All blickets are lomits.
All vromps are zeltrons.
All xandles are blickets.
Possible completions: zeltrons or lomits.
Therefore, all xandles are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | correct_target |
| 4 | " blickets." | blickets | lomits | reachable_one_hop |
| 12 | " blickets." | blickets | lomits | reachable_one_hop |
## 037/robustness/rename/1

```text
All tivaks are zeltrons.
All prandils are wugs.
All wugs are zeltrons.
All oskets are flomps.
Possible completions: zeltrons or flomps.
Therefore, all prandils are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | zeltrons | unreachable_fact_name |
| 4 | " wugs." | wugs | zeltrons | reachable_one_hop |
| 12 | " wugs." | wugs | flomps | reachable_one_hop |
## 038/direct/base/0

```text
All shalds are tivaks.
All zorks are kelbrins.
All flomps are tivaks.
All plinets are shalds.
Possible completions: shalds or kelbrins.
Therefore, all plinets are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | correct_target |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 038/direct/base/1

```text
All shalds are tivaks.
All zorks are kelbrins.
All flomps are tivaks.
All plinets are shalds.
Possible completions: kelbrins or tivaks.
Therefore, all shalds are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 038/twohop/base/0

```text
All shalds are tivaks.
All zorks are kelbrins.
All flomps are tivaks.
All plinets are shalds.
Possible completions: tivaks or kelbrins.
Therefore, all plinets are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | tivaks | reachable_one_hop |
| 4 | " shalds." | shalds | tivaks | reachable_one_hop |
| 12 | " shalds." | shalds | tivaks | reachable_one_hop |
## 038/twohop/base/1

```text
All shalds are plinets.
All zorks are kelbrins.
All tivaks are shalds.
All flomps are plinets.
Possible completions: kelbrins or plinets.
Therefore, all tivaks are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | kelbrins | reachable_one_hop |
| 4 | " shalds." | shalds | plinets | reachable_one_hop |
| 12 | " shalds." | shalds | plinets | reachable_one_hop |
## 038/broken/first/0

```text
All shalds are tivaks.
All zorks are kelbrins.
All flomps are tivaks.
All plinets are zorks.
Possible completions: tivaks or kelbrins.
Therefore, all plinets are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | tivaks | reachable_one_hop |
| 4 | " zorks." | zorks | tivaks | reachable_one_hop |
| 12 | " zorks." | zorks | kelbrins | reachable_one_hop |
## 038/broken/second/1

```text
All shalds are kelbrins.
All zorks are kelbrins.
All flomps are tivaks.
All plinets are shalds.
Possible completions: tivaks or kelbrins.
Therefore, all plinets are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | tivaks | reachable_one_hop |
| 4 | " shalds." | shalds | tivaks | reachable_one_hop |
| 12 | " shalds." | shalds | tivaks | reachable_one_hop |
## 038/robustness/reorder/0

```text
All zorks are kelbrins.
All flomps are tivaks.
All plinets are shalds.
All shalds are tivaks.
Possible completions: tivaks or kelbrins.
Therefore, all plinets are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | tivaks | reachable_one_hop |
| 4 | " shalds." | shalds | tivaks | reachable_one_hop |
| 12 | " shalds." | shalds | tivaks | reachable_one_hop |
## 038/robustness/reorder/1

```text
All zorks are kelbrins.
All shalds are plinets.
All flomps are plinets.
All tivaks are shalds.
Possible completions: kelbrins or plinets.
Therefore, all tivaks are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | plinets | reachable_one_hop |
| 4 | " shalds." | shalds | plinets | reachable_one_hop |
| 12 | " shalds." | shalds | plinets | reachable_one_hop |
## 038/robustness/distractors/0

```text
All flomps are tivaks.
All lomits are kelbrins.
All shalds are tivaks.
All plinets are shalds.
All xandles are lomits.
All zorks are kelbrins.
Possible completions: tivaks or kelbrins.
Therefore, all plinets are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | kelbrins | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 12 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
## 038/robustness/distractors/1

```text
All zorks are kelbrins.
All flomps are plinets.
All lomits are kelbrins.
All xandles are lomits.
All shalds are plinets.
All tivaks are shalds.
Possible completions: kelbrins or plinets.
Therefore, all tivaks are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 4 | " shalds." | shalds | kelbrins | reachable_one_hop |
| 12 | " shalds." | shalds | plinets | reachable_one_hop |
## 038/robustness/rename/0

```text
All lomits are ruspins.
All korvas are ulvets.
All sprocks are ruspins.
All snorps are lomits.
Possible completions: ruspins or ulvets.
Therefore, all snorps are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | ruspins | reachable_one_hop |
| 4 | " lomits." | lomits | ruspins | reachable_one_hop |
| 12 | " lomits." | lomits | ruspins | reachable_one_hop |
## 038/robustness/rename/1

```text
All sprocks are crundles.
All welbins are korvas.
All grivaks are sprocks.
All yorbits are crundles.
Possible completions: korvas or crundles.
Therefore, all grivaks are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | korvas | reachable_one_hop |
| 4 | " sprocks." | sprocks | crundles | reachable_one_hop |
| 12 | " sprocks." | sprocks | crundles | reachable_one_hop |
## 039/direct/base/0

```text
All shalds are flomps.
All quavels are snorps.
All sprocks are zeltrons.
All snorps are flomps.
Possible completions: zeltrons or snorps.
Therefore, all quavels are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | snorps | unreachable_fact_name |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " flomps." | flomps | snorps | other_reachable |
## 039/direct/base/1

```text
All shalds are flomps.
All quavels are snorps.
All sprocks are zeltrons.
All snorps are flomps.
Possible completions: flomps or zeltrons.
Therefore, all snorps are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | flomps | correct_target |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " flomps." | flomps | flomps | correct_target |
## 039/twohop/base/0

```text
All shalds are flomps.
All quavels are snorps.
All sprocks are zeltrons.
All snorps are flomps.
Possible completions: zeltrons or flomps.
Therefore, all quavels are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | zeltrons | reachable_one_hop |
| 4 | " snorps." | snorps | flomps | reachable_one_hop |
| 12 | " flomps." | flomps | flomps | correct_target |
## 039/twohop/base/1

```text
All snorps are quavels.
All flomps are snorps.
All shalds are quavels.
All sprocks are zeltrons.
Possible completions: quavels or zeltrons.
Therefore, all flomps are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | zeltrons | reachable_one_hop |
| 4 | " shalds." | shalds | zeltrons | unreachable_fact_name |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 039/broken/first/0

```text
All shalds are flomps.
All quavels are sprocks.
All sprocks are zeltrons.
All snorps are flomps.
Possible completions: zeltrons or flomps.
Therefore, all quavels are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | zeltrons | unreachable_fact_name |
| 4 | " sprocks." | sprocks | zeltrons | reachable_one_hop |
| 12 | " flomps." | flomps | flomps | wrong_candidate |
## 039/broken/second/1

```text
All shalds are flomps.
All quavels are snorps.
All sprocks are zeltrons.
All snorps are zeltrons.
Possible completions: zeltrons or flomps.
Therefore, all quavels are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | zeltrons | unreachable_fact_name |
| 4 | " snorps." | snorps | zeltrons | reachable_one_hop |
| 12 | " flomps." | flomps | flomps | wrong_candidate |
## 039/robustness/reorder/0

```text
All quavels are snorps.
All sprocks are zeltrons.
All snorps are flomps.
All shalds are flomps.
Possible completions: zeltrons or flomps.
Therefore, all quavels are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | zeltrons | reachable_one_hop |
| 4 | " snorps." | snorps | flomps | reachable_one_hop |
| 12 | " flomps." | flomps | flomps | correct_target |
## 039/robustness/reorder/1

```text
All snorps are quavels.
All shalds are quavels.
All sprocks are zeltrons.
All flomps are snorps.
Possible completions: quavels or zeltrons.
Therefore, all flomps are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | quavels | reachable_one_hop |
| 4 | " snorps." | snorps | zeltrons | reachable_one_hop |
| 12 | " snorps." | snorps | zeltrons | reachable_one_hop |
## 039/robustness/distractors/0

```text
All yorbits are zeltrons.
All shalds are flomps.
All snorps are flomps.
All vibbles are yorbits.
All sprocks are zeltrons.
All quavels are snorps.
Possible completions: zeltrons or flomps.
Therefore, all quavels are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | zeltrons | unreachable_fact_name |
| 4 | " snorps." | snorps | flomps | reachable_one_hop |
| 12 | " snorps." | snorps | flomps | reachable_one_hop |
## 039/robustness/distractors/1

```text
All sprocks are zeltrons.
All vibbles are yorbits.
All yorbits are zeltrons.
All shalds are quavels.
All snorps are quavels.
All flomps are snorps.
Possible completions: quavels or zeltrons.
Therefore, all flomps are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | quavels | reachable_one_hop |
| 4 | " snorps." | snorps | zeltrons | reachable_one_hop |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 039/robustness/rename/0

```text
All crundles are tivaks.
All yorbits are zorks.
All wugs are tufas.
All zorks are tivaks.
Possible completions: tufas or tivaks.
Therefore, all yorbits are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | tufas | reachable_one_hop |
| 4 | " zorks." | zorks | tivaks | reachable_one_hop |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 039/robustness/rename/1

```text
All ulvets are nerps.
All blickets are ulvets.
All tufas are nerps.
All xandles are vibbles.
Possible completions: nerps or vibbles.
Therefore, all blickets are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " ulvets." | ulvets | nerps | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 040/direct/base/0

```text
All helpons are brovets.
All tufas are nufrons.
All nufrons are brovets.
All xandles are ruspins.
Possible completions: nufrons or ruspins.
Therefore, all tufas are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | nufrons | other_reachable |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 040/direct/base/1

```text
All helpons are brovets.
All tufas are nufrons.
All nufrons are brovets.
All xandles are ruspins.
Possible completions: ruspins or brovets.
Therefore, all nufrons are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | correct_target |
| 4 | " brovets." | brovets | brovets | correct_target |
| 12 | " brovets." | brovets | brovets | correct_target |
## 040/twohop/base/0

```text
All helpons are brovets.
All tufas are nufrons.
All nufrons are brovets.
All xandles are ruspins.
Possible completions: brovets or ruspins.
Therefore, all tufas are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | brovets | reachable_one_hop |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 040/twohop/base/1

```text
All brovets are nufrons.
All xandles are ruspins.
All helpons are tufas.
All nufrons are tufas.
Possible completions: ruspins or tufas.
Therefore, all brovets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 040/broken/first/0

```text
All helpons are brovets.
All tufas are xandles.
All nufrons are brovets.
All xandles are ruspins.
Possible completions: brovets or ruspins.
Therefore, all tufas are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | brovets | reachable_one_hop |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 040/broken/second/1

```text
All helpons are brovets.
All tufas are nufrons.
All nufrons are ruspins.
All xandles are ruspins.
Possible completions: brovets or ruspins.
Therefore, all tufas are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | brovets | reachable_one_hop |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 040/robustness/reorder/0

```text
All helpons are brovets.
All nufrons are brovets.
All tufas are nufrons.
All xandles are ruspins.
Possible completions: brovets or ruspins.
Therefore, all tufas are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | brovets | reachable_one_hop |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 040/robustness/reorder/1

```text
All xandles are ruspins.
All brovets are nufrons.
All helpons are tufas.
All nufrons are tufas.
Possible completions: ruspins or tufas.
Therefore, all brovets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | ruspins | reachable_one_hop |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " nufrons." | nufrons | tufas | reachable_one_hop |
## 040/robustness/distractors/0

```text
All helpons are brovets.
All sprocks are shalds.
All tufas are nufrons.
All xandles are ruspins.
All shalds are ruspins.
All nufrons are brovets.
Possible completions: brovets or ruspins.
Therefore, all tufas are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | brovets | reachable_one_hop |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " nufrons." | nufrons | ruspins | reachable_one_hop |
## 040/robustness/distractors/1

```text
All shalds are ruspins.
All brovets are nufrons.
All sprocks are shalds.
All xandles are ruspins.
All helpons are tufas.
All nufrons are tufas.
Possible completions: ruspins or tufas.
Therefore, all brovets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | tufas | reachable_one_hop |
| 4 | " nufrons." | nufrons | tufas | reachable_one_hop |
| 12 | " tufas." | tufas | tufas | correct_target |
## 040/robustness/rename/0

```text
All lomits are zemples.
All kelbrins are korvas.
All korvas are zemples.
All wugs are tivaks.
Possible completions: zemples or tivaks.
Therefore, all kelbrins are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | zemples | unreachable_fact_name |
| 4 | " tivaks." | tivaks | tivaks | wrong_candidate |
| 12 | " tivaks." | tivaks | tivaks | wrong_candidate |
## 040/robustness/rename/1

```text
All grivaks are zorks.
All vromps are snorps.
All plinets are wugs.
All zorks are wugs.
Possible completions: snorps or wugs.
Therefore, all grivaks are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | wugs | reachable_one_hop |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 041/direct/base/0

```text
All shalds are yorbits.
All welbins are shalds.
All tufas are yorbits.
All plinets are nufrons.
Possible completions: nufrons or shalds.
Therefore, all welbins are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | correct_target |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 041/direct/base/1

```text
All shalds are yorbits.
All welbins are shalds.
All tufas are yorbits.
All plinets are nufrons.
Possible completions: yorbits or nufrons.
Therefore, all shalds are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " yorbits." | yorbits | yorbits | correct_target |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 041/twohop/base/0

```text
All shalds are yorbits.
All welbins are shalds.
All tufas are yorbits.
All plinets are nufrons.
Possible completions: nufrons or yorbits.
Therefore, all welbins are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | yorbits | unreachable_fact_name |
| 4 | " shalds." | shalds | yorbits | reachable_one_hop |
| 12 | " shalds." | shalds | yorbits | reachable_one_hop |
## 041/twohop/base/1

```text
All plinets are nufrons.
All shalds are welbins.
All yorbits are shalds.
All tufas are welbins.
Possible completions: welbins or nufrons.
Therefore, all yorbits are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 4 | " shalds." | shalds | nufrons | reachable_one_hop |
| 12 | " shalds." | shalds | welbins | reachable_one_hop |
## 041/broken/first/0

```text
All shalds are yorbits.
All welbins are plinets.
All tufas are yorbits.
All plinets are nufrons.
Possible completions: nufrons or yorbits.
Therefore, all welbins are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | nufrons | reachable_one_hop |
| 4 | " plinets." | plinets | yorbits | reachable_one_hop |
| 12 | " plinets." | plinets | yorbits | reachable_one_hop |
## 041/broken/second/1

```text
All shalds are nufrons.
All welbins are shalds.
All tufas are yorbits.
All plinets are nufrons.
Possible completions: nufrons or yorbits.
Therefore, all welbins are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | nufrons | reachable_one_hop |
| 4 | " shalds." | shalds | nufrons | reachable_one_hop |
| 12 | " shalds." | shalds | nufrons | reachable_one_hop |
## 041/robustness/reorder/0

```text
All tufas are yorbits.
All shalds are yorbits.
All welbins are shalds.
All plinets are nufrons.
Possible completions: nufrons or yorbits.
Therefore, all welbins are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | yorbits | unreachable_fact_name |
| 4 | " shalds." | shalds | yorbits | reachable_one_hop |
| 12 | " shalds." | shalds | yorbits | reachable_one_hop |
## 041/robustness/reorder/1

```text
All yorbits are shalds.
All tufas are welbins.
All shalds are welbins.
All plinets are nufrons.
Possible completions: welbins or nufrons.
Therefore, all yorbits are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 4 | " shalds." | shalds | nufrons | reachable_one_hop |
| 12 | " shalds." | shalds | nufrons | reachable_one_hop |
## 041/robustness/distractors/0

```text
All tufas are yorbits.
All welbins are shalds.
All vibbles are nufrons.
All nerps are vibbles.
All plinets are nufrons.
All shalds are yorbits.
Possible completions: nufrons or yorbits.
Therefore, all welbins are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | yorbits | reachable_one_hop |
| 4 | " shalds." | shalds | yorbits | reachable_one_hop |
| 12 | " shalds." | shalds | yorbits | reachable_one_hop |
## 041/robustness/distractors/1

```text
All nerps are vibbles.
All shalds are welbins.
All plinets are nufrons.
All vibbles are nufrons.
All tufas are welbins.
All yorbits are shalds.
Possible completions: welbins or nufrons.
Therefore, all yorbits are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | nufrons | reachable_one_hop |
| 4 | " shalds." | shalds | nufrons | reachable_one_hop |
| 12 | " shalds." | shalds | nufrons | reachable_one_hop |
## 041/robustness/rename/0

```text
All daxes are grivaks.
All flomps are daxes.
All prandils are grivaks.
All zemples are wugs.
Possible completions: wugs or grivaks.
Therefore, all flomps are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | wugs | reachable_one_hop |
| 4 | " daxes." | daxes | grivaks | reachable_one_hop |
| 12 | " daxes." | daxes | grivaks | reachable_one_hop |
## 041/robustness/rename/1

```text
All daxes are zemples.
All vibbles are tivaks.
All oskets are vibbles.
All murdles are tivaks.
Possible completions: tivaks or zemples.
Therefore, all oskets are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | tivaks | unreachable_fact_name |
| 4 | " vibbles." | vibbles | tivaks | reachable_one_hop |
| 12 | " vibbles." | vibbles | tivaks | reachable_one_hop |
## 042/direct/base/0

```text
All grivaks are zorks.
All ruspins are nufrons.
All quavels are sprocks.
All sprocks are nufrons.
Possible completions: sprocks or zorks.
Therefore, all quavels are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | sprocks | other_reachable |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 042/direct/base/1

```text
All grivaks are zorks.
All ruspins are nufrons.
All quavels are sprocks.
All sprocks are nufrons.
Possible completions: zorks or nufrons.
Therefore, all sprocks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 042/twohop/base/0

```text
All grivaks are zorks.
All ruspins are nufrons.
All quavels are sprocks.
All sprocks are nufrons.
Possible completions: nufrons or zorks.
Therefore, all quavels are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | nufrons | reachable_one_hop |
| 4 | " sprocks." | sprocks | zorks | reachable_one_hop |
| 12 | " sprocks." | sprocks | nufrons | reachable_one_hop |
## 042/twohop/base/1

```text
All ruspins are quavels.
All nufrons are sprocks.
All sprocks are quavels.
All grivaks are zorks.
Possible completions: zorks or quavels.
Therefore, all nufrons are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 4 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 12 | " quavels." | quavels | quavels | correct_target |
## 042/broken/first/0

```text
All grivaks are zorks.
All ruspins are nufrons.
All quavels are grivaks.
All sprocks are nufrons.
Possible completions: nufrons or zorks.
Therefore, all quavels are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | zorks | unreachable_fact_name |
| 4 | " grivaks." | grivaks | zorks | reachable_one_hop |
| 12 | " grivaks." | grivaks | zorks | reachable_one_hop |
## 042/broken/second/1

```text
All grivaks are zorks.
All ruspins are nufrons.
All quavels are sprocks.
All sprocks are zorks.
Possible completions: nufrons or zorks.
Therefore, all quavels are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | zorks | reachable_one_hop |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " zorks." | zorks | zorks | correct_target |
## 042/robustness/reorder/0

```text
All quavels are sprocks.
All sprocks are nufrons.
All grivaks are zorks.
All ruspins are nufrons.
Possible completions: nufrons or zorks.
Therefore, all quavels are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | zorks | unreachable_fact_name |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 042/robustness/reorder/1

```text
All grivaks are zorks.
All ruspins are quavels.
All nufrons are sprocks.
All sprocks are quavels.
Possible completions: zorks or quavels.
Therefore, all nufrons are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 4 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 12 | " sprocks." | sprocks | quavels | reachable_one_hop |
## 042/robustness/distractors/0

```text
All ruspins are nufrons.
All zeltrons are zorks.
All quavels are sprocks.
All grivaks are zorks.
All snorps are zeltrons.
All sprocks are nufrons.
Possible completions: nufrons or zorks.
Therefore, all quavels are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | nufrons | reachable_one_hop |
| 4 | " sprocks." | sprocks | zorks | reachable_one_hop |
| 12 | " zorks." | zorks | zorks | wrong_candidate |
## 042/robustness/distractors/1

```text
All snorps are zeltrons.
All nufrons are sprocks.
All grivaks are zorks.
All ruspins are quavels.
All zeltrons are zorks.
All sprocks are quavels.
Possible completions: zorks or quavels.
Therefore, all nufrons are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 4 | " sprocks." | sprocks | quavels | reachable_one_hop |
| 12 | " quavels." | quavels | quavels | correct_target |
## 042/robustness/rename/0

```text
All yorbits are zeltrons.
All wugs are zemples.
All prandils are blickets.
All blickets are zemples.
Possible completions: zemples or zeltrons.
Therefore, all prandils are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | zemples | reachable_one_hop |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 042/robustness/rename/1

```text
All murdles are nerps.
All wugs are tivaks.
All tivaks are nerps.
All blickets are vibbles.
Possible completions: vibbles or nerps.
Therefore, all wugs are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | vibbles | unreachable_fact_name |
| 4 | " tivaks." | tivaks | nerps | reachable_one_hop |
| 12 | " tivaks." | tivaks | nerps | reachable_one_hop |
## 043/direct/base/0

```text
All vibbles are nufrons.
All sprocks are kelbrins.
All kelbrins are jastles.
All quavels are jastles.
Possible completions: nufrons or kelbrins.
Therefore, all sprocks are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | nufrons | other_reachable |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " jastles." | jastles | kelbrins | other_reachable |
## 043/direct/base/1

```text
All vibbles are nufrons.
All sprocks are kelbrins.
All kelbrins are jastles.
All quavels are jastles.
Possible completions: jastles or nufrons.
Therefore, all kelbrins are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 043/twohop/base/0

```text
All vibbles are nufrons.
All sprocks are kelbrins.
All kelbrins are jastles.
All quavels are jastles.
Possible completions: nufrons or jastles.
Therefore, all sprocks are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | jastles | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | jastles | reachable_one_hop |
| 12 | " jastles." | jastles | jastles | correct_target |
## 043/twohop/base/1

```text
All quavels are sprocks.
All kelbrins are sprocks.
All vibbles are nufrons.
All jastles are kelbrins.
Possible completions: sprocks or nufrons.
Therefore, all jastles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " kelbrins." | kelbrins | sprocks | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | sprocks | reachable_one_hop |
## 043/broken/first/0

```text
All vibbles are nufrons.
All sprocks are vibbles.
All kelbrins are jastles.
All quavels are jastles.
Possible completions: nufrons or jastles.
Therefore, all sprocks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | nufrons | reachable_one_hop |
| 4 | " vibbles." | vibbles | jastles | reachable_one_hop |
| 12 | " vibbles." | vibbles | jastles | reachable_one_hop |
## 043/broken/second/1

```text
All vibbles are nufrons.
All sprocks are kelbrins.
All kelbrins are nufrons.
All quavels are jastles.
Possible completions: nufrons or jastles.
Therefore, all sprocks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " kelbrins." | kelbrins | jastles | reachable_one_hop |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 043/robustness/reorder/0

```text
All kelbrins are jastles.
All quavels are jastles.
All sprocks are kelbrins.
All vibbles are nufrons.
Possible completions: nufrons or jastles.
Therefore, all sprocks are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " kelbrins." | kelbrins | jastles | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | jastles | reachable_one_hop |
## 043/robustness/reorder/1

```text
All quavels are sprocks.
All kelbrins are sprocks.
All jastles are kelbrins.
All vibbles are nufrons.
Possible completions: sprocks or nufrons.
Therefore, all jastles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | sprocks | unreachable_fact_name |
| 4 | " kelbrins." | kelbrins | nufrons | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | nufrons | reachable_one_hop |
## 043/robustness/distractors/0

```text
All nerps are nufrons.
All quavels are jastles.
All sprocks are kelbrins.
All kelbrins are jastles.
All flomps are nerps.
All vibbles are nufrons.
Possible completions: nufrons or jastles.
Therefore, all sprocks are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | jastles | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | jastles | reachable_one_hop |
| 12 | " jastles." | jastles | jastles | correct_target |
## 043/robustness/distractors/1

```text
All flomps are nerps.
All kelbrins are sprocks.
All vibbles are nufrons.
All nerps are nufrons.
All jastles are kelbrins.
All quavels are sprocks.
Possible completions: sprocks or nufrons.
Therefore, all jastles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | sprocks | unreachable_fact_name |
| 4 | " kelbrins." | kelbrins | sprocks | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | sprocks | reachable_one_hop |
## 043/robustness/rename/0

```text
All grivaks are snorps.
All korvas are prandils.
All prandils are flomps.
All lomits are flomps.
Possible completions: snorps or flomps.
Therefore, all korvas are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | snorps | unreachable_fact_name |
| 4 | " prandils." | prandils | flomps | reachable_one_hop |
| 12 | " flomps." | flomps | flomps | correct_target |
## 043/robustness/rename/1

```text
All lomits are blickets.
All daxes are blickets.
All grivaks are flomps.
All zeltrons are daxes.
Possible completions: blickets or flomps.
Therefore, all zeltrons are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | correct_target |
| 4 | " daxes." | daxes | flomps | reachable_one_hop |
| 12 | " daxes." | daxes | flomps | reachable_one_hop |
## 044/direct/base/0

```text
All daxes are zemples.
All xandles are zemples.
All ulvets are xandles.
All tufas are shalds.
Possible completions: xandles or shalds.
Therefore, all ulvets are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | xandles | correct_target |
| 4 | " shalds." | shalds | shalds | wrong_candidate |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 044/direct/base/1

```text
All daxes are zemples.
All xandles are zemples.
All ulvets are xandles.
All tufas are shalds.
Possible completions: shalds or zemples.
Therefore, all xandles are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | wrong_candidate |
| 4 | " shalds." | shalds | shalds | wrong_candidate |
| 12 | " zemples." | zemples | zemples | correct_target |
## 044/twohop/base/0

```text
All daxes are zemples.
All xandles are zemples.
All ulvets are xandles.
All tufas are shalds.
Possible completions: zemples or shalds.
Therefore, all ulvets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " shalds." | shalds | shalds | wrong_candidate |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 044/twohop/base/1

```text
All tufas are shalds.
All xandles are ulvets.
All zemples are xandles.
All daxes are ulvets.
Possible completions: shalds or ulvets.
Therefore, all zemples are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | shalds | unreachable_fact_name |
| 4 | " ulvets." | ulvets | ulvets | correct_target |
| 12 | " ulvets." | ulvets | ulvets | correct_target |
## 044/broken/first/0

```text
All daxes are zemples.
All xandles are zemples.
All ulvets are tufas.
All tufas are shalds.
Possible completions: zemples or shalds.
Therefore, all ulvets are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " tufas." | tufas | shalds | reachable_one_hop |
| 12 | " tufas." | tufas | shalds | reachable_one_hop |
## 044/broken/second/1

```text
All daxes are zemples.
All xandles are shalds.
All ulvets are xandles.
All tufas are shalds.
Possible completions: zemples or shalds.
Therefore, all ulvets are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 044/robustness/reorder/0

```text
All ulvets are xandles.
All daxes are zemples.
All xandles are zemples.
All tufas are shalds.
Possible completions: zemples or shalds.
Therefore, all ulvets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " xandles." | xandles | shalds | reachable_one_hop |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 044/robustness/reorder/1

```text
All daxes are ulvets.
All tufas are shalds.
All zemples are xandles.
All xandles are ulvets.
Possible completions: shalds or ulvets.
Therefore, all zemples are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | ulvets | reachable_one_hop |
| 4 | " ulvets." | ulvets | ulvets | correct_target |
| 12 | " ulvets." | ulvets | ulvets | correct_target |
## 044/robustness/distractors/0

```text
All blickets are tivaks.
All daxes are zemples.
All ulvets are xandles.
All xandles are zemples.
All tufas are shalds.
All tivaks are shalds.
Possible completions: zemples or shalds.
Therefore, all ulvets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " shalds." | shalds | shalds | wrong_candidate |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 044/robustness/distractors/1

```text
All xandles are ulvets.
All daxes are ulvets.
All blickets are tivaks.
All tufas are shalds.
All zemples are xandles.
All tivaks are shalds.
Possible completions: shalds or ulvets.
Therefore, all zemples are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | correct_target |
| 4 | " xandles." | xandles | ulvets | reachable_one_hop |
| 12 | " xandles." | xandles | ulvets | reachable_one_hop |
## 044/robustness/rename/0

```text
All plinets are sprocks.
All welbins are sprocks.
All snorps are welbins.
All vromps are ruspins.
Possible completions: sprocks or ruspins.
Therefore, all snorps are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | sprocks | unreachable_fact_name |
| 4 | " vromps." | vromps | ruspins | unreachable_fact_name |
| 12 | " vromps." | vromps | ruspins | unreachable_fact_name |
## 044/robustness/rename/1

```text
All lomits are zeltrons.
All vibbles are blickets.
All korvas are vibbles.
All crundles are blickets.
Possible completions: zeltrons or blickets.
Therefore, all korvas are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | zeltrons | reachable_one_hop |
| 4 | " vibbles." | vibbles | blickets | reachable_one_hop |
| 12 | " vibbles." | vibbles | blickets | reachable_one_hop |
## 045/direct/base/0

```text
All ulvets are zeltrons.
All zemples are yorbits.
All nufrons are welbins.
All yorbits are welbins.
Possible completions: zeltrons or yorbits.
Therefore, all zemples are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | yorbits | other_reachable |
| 4 | " welbins." | welbins | yorbits | other_reachable |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 045/direct/base/1

```text
All ulvets are zeltrons.
All zemples are yorbits.
All nufrons are welbins.
All yorbits are welbins.
Possible completions: welbins or zeltrons.
Therefore, all yorbits are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " welbins." | welbins | welbins | correct_target |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 045/twohop/base/0

```text
All ulvets are zeltrons.
All zemples are yorbits.
All nufrons are welbins.
All yorbits are welbins.
Possible completions: zeltrons or welbins.
Therefore, all zemples are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | welbins | reachable_one_hop |
| 4 | " yorbits." | yorbits | welbins | reachable_one_hop |
| 12 | " yorbits." | yorbits | welbins | reachable_one_hop |
## 045/twohop/base/1

```text
All welbins are yorbits.
All ulvets are zeltrons.
All yorbits are zemples.
All nufrons are zemples.
Possible completions: zemples or zeltrons.
Therefore, all welbins are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 4 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 12 | " zemples." | zemples | zemples | correct_target |
## 045/broken/first/0

```text
All ulvets are zeltrons.
All zemples are ulvets.
All nufrons are welbins.
All yorbits are welbins.
Possible completions: zeltrons or welbins.
Therefore, all zemples are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | welbins | reachable_one_hop |
| 4 | " nufrons." | nufrons | zeltrons | unreachable_fact_name |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 045/broken/second/1

```text
All ulvets are zeltrons.
All zemples are yorbits.
All nufrons are welbins.
All yorbits are zeltrons.
Possible completions: zeltrons or welbins.
Therefore, all zemples are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | welbins | reachable_one_hop |
| 4 | " yorbits." | yorbits | zeltrons | reachable_one_hop |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 045/robustness/reorder/0

```text
All yorbits are welbins.
All nufrons are welbins.
All ulvets are zeltrons.
All zemples are yorbits.
Possible completions: zeltrons or welbins.
Therefore, all zemples are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | welbins | reachable_one_hop |
| 4 | " yorbits." | yorbits | zeltrons | reachable_one_hop |
| 12 | " yorbits." | yorbits | zeltrons | reachable_one_hop |
## 045/robustness/reorder/1

```text
All yorbits are zemples.
All welbins are yorbits.
All ulvets are zeltrons.
All nufrons are zemples.
Possible completions: zemples or zeltrons.
Therefore, all welbins are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | zeltrons | reachable_one_hop |
| 4 | " yorbits." | yorbits | zeltrons | reachable_one_hop |
| 12 | " zemples." | zemples | zemples | correct_target |
## 045/robustness/distractors/0

```text
All nufrons are welbins.
All shalds are nerps.
All yorbits are welbins.
All ulvets are zeltrons.
All zemples are yorbits.
All nerps are zeltrons.
Possible completions: zeltrons or welbins.
Therefore, all zemples are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | zeltrons | reachable_one_hop |
| 4 | " yorbits." | yorbits | zeltrons | reachable_one_hop |
| 12 | " yorbits." | yorbits | zeltrons | reachable_one_hop |
## 045/robustness/distractors/1

```text
All ulvets are zeltrons.
All nufrons are zemples.
All shalds are nerps.
All welbins are yorbits.
All nerps are zeltrons.
All yorbits are zemples.
Possible completions: zemples or zeltrons.
Therefore, all welbins are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | zeltrons | reachable_one_hop |
| 4 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 045/robustness/rename/0

```text
All murdles are snorps.
All ruspins are plinets.
All oskets are tufas.
All plinets are tufas.
Possible completions: snorps or tufas.
Therefore, all ruspins are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | snorps | reachable_one_hop |
| 4 | " plinets." | plinets | tufas | reachable_one_hop |
| 12 | " plinets." | plinets | tufas | reachable_one_hop |
## 045/robustness/rename/1

```text
All zorks are daxes.
All grivaks are blickets.
All daxes are korvas.
All helpons are korvas.
Possible completions: korvas or blickets.
Therefore, all zorks are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | blickets | reachable_one_hop |
| 4 | " daxes." | daxes | korvas | reachable_one_hop |
| 12 | " daxes." | daxes | korvas | reachable_one_hop |
## 046/direct/base/0

```text
All tufas are ulvets.
All zorks are zeltrons.
All snorps are zorks.
All wugs are zeltrons.
Possible completions: zorks or ulvets.
Therefore, all snorps are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " zorks." | zorks | zorks | correct_target |
## 046/direct/base/1

```text
All tufas are ulvets.
All zorks are zeltrons.
All snorps are zorks.
All wugs are zeltrons.
Possible completions: ulvets or zeltrons.
Therefore, all zorks are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 046/twohop/base/0

```text
All tufas are ulvets.
All zorks are zeltrons.
All snorps are zorks.
All wugs are zeltrons.
Possible completions: zeltrons or ulvets.
Therefore, all snorps are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | ulvets | correct_target |
| 4 | " zorks." | zorks | ulvets | reachable_one_hop |
| 12 | " zorks." | zorks | zeltrons | reachable_one_hop |
## 046/twohop/base/1

```text
All wugs are snorps.
All tufas are ulvets.
All zeltrons are zorks.
All zorks are snorps.
Possible completions: ulvets or snorps.
Therefore, all zeltrons are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | correct_target |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 046/broken/first/0

```text
All tufas are ulvets.
All zorks are zeltrons.
All snorps are tufas.
All wugs are zeltrons.
Possible completions: zeltrons or ulvets.
Therefore, all snorps are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | zeltrons | reachable_one_hop |
| 4 | " tufas." | tufas | ulvets | reachable_one_hop |
| 12 | " tufas." | tufas | ulvets | reachable_one_hop |
## 046/broken/second/1

```text
All tufas are ulvets.
All zorks are ulvets.
All snorps are zorks.
All wugs are zeltrons.
Possible completions: zeltrons or ulvets.
Therefore, all snorps are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | correct_target |
| 4 | " ulvets." | ulvets | ulvets | correct_target |
| 12 | " zorks." | zorks | ulvets | reachable_one_hop |
## 046/robustness/reorder/0

```text
All tufas are ulvets.
All wugs are zeltrons.
All zorks are zeltrons.
All snorps are zorks.
Possible completions: zeltrons or ulvets.
Therefore, all snorps are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | ulvets | correct_target |
| 4 | " zorks." | zorks | ulvets | reachable_one_hop |
| 12 | " zorks." | zorks | zeltrons | reachable_one_hop |
## 046/robustness/reorder/1

```text
All wugs are snorps.
All zeltrons are zorks.
All tufas are ulvets.
All zorks are snorps.
Possible completions: ulvets or snorps.
Therefore, all zeltrons are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 4 | " zorks." | zorks | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | correct_target |
## 046/robustness/distractors/0

```text
All snorps are zorks.
All shalds are ulvets.
All flomps are shalds.
All wugs are zeltrons.
All zorks are zeltrons.
All tufas are ulvets.
Possible completions: zeltrons or ulvets.
Therefore, all snorps are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 4 | " zorks." | zorks | ulvets | reachable_one_hop |
| 12 | " zorks." | zorks | ulvets | reachable_one_hop |
## 046/robustness/distractors/1

```text
All flomps are shalds.
All tufas are ulvets.
All zeltrons are zorks.
All wugs are snorps.
All zorks are snorps.
All shalds are ulvets.
Possible completions: ulvets or snorps.
Therefore, all zeltrons are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | snorps | reachable_one_hop |
| 4 | " zorks." | zorks | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | correct_target |
## 046/robustness/rename/0

```text
All oskets are nufrons.
All murdles are yorbits.
All vromps are murdles.
All zemples are yorbits.
Possible completions: yorbits or nufrons.
Therefore, all vromps are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 12 | " nufrons." | nufrons | nufrons | wrong_candidate |
## 046/robustness/rename/1

```text
All zemples are quavels.
All sprocks are nufrons.
All tivaks are brovets.
All brovets are quavels.
Possible completions: nufrons or quavels.
Therefore, all tivaks are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | nufrons | reachable_one_hop |
| 4 | " quavels." | quavels | quavels | correct_target |
| 12 | " quavels." | quavels | quavels | correct_target |
## 047/direct/base/0

```text
All ruspins are oskets.
All yorbits are zorks.
All zorks are helpons.
All ulvets are helpons.
Possible completions: oskets or zorks.
Therefore, all yorbits are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | zorks | unreachable_fact_name |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " ulvets." | ulvets | zorks | unreachable_fact_name |
## 047/direct/base/1

```text
All ruspins are oskets.
All yorbits are zorks.
All zorks are helpons.
All ulvets are helpons.
Possible completions: helpons or oskets.
Therefore, all zorks are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | helpons | unreachable_fact_name |
| 4 | " helpons." | helpons | helpons | correct_target |
| 12 | " helpons." | helpons | helpons | correct_target |
## 047/twohop/base/0

```text
All ruspins are oskets.
All yorbits are zorks.
All zorks are helpons.
All ulvets are helpons.
Possible completions: oskets or helpons.
Therefore, all yorbits are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | oskets | unreachable_fact_name |
| 4 | " zorks." | zorks | helpons | reachable_one_hop |
| 12 | " zorks." | zorks | helpons | reachable_one_hop |
## 047/twohop/base/1

```text
All zorks are yorbits.
All ruspins are oskets.
All ulvets are yorbits.
All helpons are zorks.
Possible completions: yorbits or oskets.
Therefore, all helpons are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | yorbits | reachable_one_hop |
| 4 | " zorks." | zorks | yorbits | reachable_one_hop |
| 12 | " zorks." | zorks | yorbits | reachable_one_hop |
## 047/broken/first/0

```text
All ruspins are oskets.
All yorbits are ruspins.
All zorks are helpons.
All ulvets are helpons.
Possible completions: oskets or helpons.
Therefore, all yorbits are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | oskets | unreachable_fact_name |
| 4 | " ruspins." | ruspins | helpons | reachable_one_hop |
| 12 | " ruspins." | ruspins | helpons | reachable_one_hop |
## 047/broken/second/1

```text
All ruspins are oskets.
All yorbits are zorks.
All zorks are oskets.
All ulvets are helpons.
Possible completions: oskets or helpons.
Therefore, all yorbits are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | oskets | unreachable_fact_name |
| 4 | " zorks." | zorks | oskets | reachable_one_hop |
| 12 | " zorks." | zorks | oskets | reachable_one_hop |
## 047/robustness/reorder/0

```text
All zorks are helpons.
All ruspins are oskets.
All ulvets are helpons.
All yorbits are zorks.
Possible completions: oskets or helpons.
Therefore, all yorbits are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " zorks." | zorks | helpons | reachable_one_hop |
| 12 | " zorks." | zorks | helpons | reachable_one_hop |
## 047/robustness/reorder/1

```text
All ulvets are yorbits.
All helpons are zorks.
All zorks are yorbits.
All ruspins are oskets.
Possible completions: yorbits or oskets.
Therefore, all helpons are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | yorbits | unreachable_fact_name |
| 4 | " ruspins." | ruspins | yorbits | unreachable_fact_name |
| 12 | " ruspins." | ruspins | yorbits | unreachable_fact_name |
## 047/robustness/distractors/0

```text
All yorbits are zorks.
All snorps are oskets.
All ulvets are helpons.
All zorks are helpons.
All ruspins are oskets.
All prandils are snorps.
Possible completions: oskets or helpons.
Therefore, all yorbits are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | helpons | reachable_one_hop |
| 4 | " zorks." | zorks | helpons | reachable_one_hop |
| 12 | " zorks." | zorks | helpons | reachable_one_hop |
## 047/robustness/distractors/1

```text
All ruspins are oskets.
All snorps are oskets.
All ulvets are yorbits.
All prandils are snorps.
All helpons are zorks.
All zorks are yorbits.
Possible completions: yorbits or oskets.
Therefore, all helpons are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | yorbits | reachable_one_hop |
| 4 | " zorks." | zorks | yorbits | reachable_one_hop |
| 12 | " zorks." | zorks | yorbits | reachable_one_hop |
## 047/robustness/rename/0

```text
All vromps are nerps.
All wugs are zeltrons.
All zeltrons are jastles.
All tufas are jastles.
Possible completions: nerps or jastles.
Therefore, all wugs are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | jastles | unreachable_fact_name |
| 4 | " tufas." | tufas | jastles | unreachable_fact_name |
| 12 | " jastles." | jastles | jastles | correct_target |
## 047/robustness/rename/1

```text
All grivaks are quavels.
All nerps are wugs.
All welbins are quavels.
All flomps are grivaks.
Possible completions: quavels or wugs.
Therefore, all flomps are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | quavels | reachable_one_hop |
| 4 | " grivaks." | grivaks | quavels | reachable_one_hop |
| 12 | " grivaks." | grivaks | wugs | reachable_one_hop |
## 048/direct/base/0

```text
All nufrons are welbins.
All jastles are welbins.
All tivaks are nufrons.
All wugs are oskets.
Possible completions: nufrons or oskets.
Therefore, all tivaks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 048/direct/base/1

```text
All nufrons are welbins.
All jastles are welbins.
All tivaks are nufrons.
All wugs are oskets.
Possible completions: oskets or welbins.
Therefore, all nufrons are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " welbins." | welbins | welbins | correct_target |
| 12 | " welbins." | welbins | welbins | correct_target |
## 048/twohop/base/0

```text
All nufrons are welbins.
All jastles are welbins.
All tivaks are nufrons.
All wugs are oskets.
Possible completions: welbins or oskets.
Therefore, all tivaks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | welbins | reachable_one_hop |
| 4 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 12 | " nufrons." | nufrons | welbins | reachable_one_hop |
## 048/twohop/base/1

```text
All welbins are nufrons.
All jastles are tivaks.
All nufrons are tivaks.
All wugs are oskets.
Possible completions: oskets or tivaks.
Therefore, all welbins are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | tivaks | correct_target |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " nufrons." | nufrons | tivaks | reachable_one_hop |
## 048/broken/first/0

```text
All nufrons are welbins.
All jastles are welbins.
All tivaks are wugs.
All wugs are oskets.
Possible completions: welbins or oskets.
Therefore, all tivaks are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | wrong_candidate |
| 4 | " wugs." | wugs | oskets | reachable_one_hop |
| 12 | " wugs." | wugs | welbins | reachable_one_hop |
## 048/broken/second/1

```text
All nufrons are oskets.
All jastles are welbins.
All tivaks are nufrons.
All wugs are oskets.
Possible completions: welbins or oskets.
Therefore, all tivaks are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | welbins | reachable_one_hop |
| 4 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 12 | " nufrons." | nufrons | oskets | reachable_one_hop |
## 048/robustness/reorder/0

```text
All wugs are oskets.
All jastles are welbins.
All nufrons are welbins.
All tivaks are nufrons.
Possible completions: welbins or oskets.
Therefore, all tivaks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " nufrons." | nufrons | welbins | reachable_one_hop |
| 12 | " nufrons." | nufrons | welbins | reachable_one_hop |
## 048/robustness/reorder/1

```text
All wugs are oskets.
All welbins are nufrons.
All jastles are tivaks.
All nufrons are tivaks.
Possible completions: oskets or tivaks.
Therefore, all welbins are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | oskets | unreachable_fact_name |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " nufrons." | nufrons | tivaks | reachable_one_hop |
## 048/robustness/distractors/0

```text
All tivaks are nufrons.
All wugs are oskets.
All ulvets are prandils.
All nufrons are welbins.
All jastles are welbins.
All prandils are oskets.
Possible completions: welbins or oskets.
Therefore, all tivaks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | welbins | reachable_one_hop |
| 4 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 12 | " nufrons." | nufrons | welbins | reachable_one_hop |
## 048/robustness/distractors/1

```text
All prandils are oskets.
All jastles are tivaks.
All nufrons are tivaks.
All ulvets are prandils.
All welbins are nufrons.
All wugs are oskets.
Possible completions: oskets or tivaks.
Therefore, all welbins are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " nufrons." | nufrons | tivaks | reachable_one_hop |
| 12 | " prandils." | prandils | tivaks | unreachable_fact_name |
## 048/robustness/rename/0

```text
All blickets are tufas.
All brovets are tufas.
All crundles are blickets.
All korvas are ruspins.
Possible completions: tufas or ruspins.
Therefore, all crundles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " blickets." | blickets | ruspins | reachable_one_hop |
| 12 | " blickets." | blickets | tufas | reachable_one_hop |
## 048/robustness/rename/1

```text
All shalds are ruspins.
All tufas are vromps.
All ruspins are vromps.
All vibbles are snorps.
Possible completions: snorps or vromps.
Therefore, all shalds are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | snorps | unreachable_fact_name |
| 4 | " vibbles." | vibbles | snorps | unreachable_fact_name |
| 12 | " ruspins." | ruspins | snorps | reachable_one_hop |
## 049/direct/base/0

```text
All ruspins are grivaks.
All murdles are shalds.
All tufas are nufrons.
All nufrons are grivaks.
Possible completions: shalds or nufrons.
Therefore, all tufas are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | nufrons | other_reachable |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 049/direct/base/1

```text
All ruspins are grivaks.
All murdles are shalds.
All tufas are nufrons.
All nufrons are grivaks.
Possible completions: grivaks or shalds.
Therefore, all nufrons are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | correct_target |
| 4 | " grivaks." | grivaks | grivaks | correct_target |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 049/twohop/base/0

```text
All ruspins are grivaks.
All murdles are shalds.
All tufas are nufrons.
All nufrons are grivaks.
Possible completions: shalds or grivaks.
Therefore, all tufas are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | grivaks | reachable_one_hop |
| 4 | " nufrons." | nufrons | grivaks | reachable_one_hop |
| 12 | " nufrons." | nufrons | grivaks | reachable_one_hop |
## 049/twohop/base/1

```text
All grivaks are nufrons.
All murdles are shalds.
All nufrons are tufas.
All ruspins are tufas.
Possible completions: tufas or shalds.
Therefore, all grivaks are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | wrong_candidate |
| 4 | " nufrons." | nufrons | tufas | reachable_one_hop |
| 12 | " nufrons." | nufrons | shalds | reachable_one_hop |
## 049/broken/first/0

```text
All ruspins are grivaks.
All murdles are shalds.
All tufas are murdles.
All nufrons are grivaks.
Possible completions: shalds or grivaks.
Therefore, all tufas are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | grivaks | unreachable_fact_name |
| 4 | " murdles." | murdles | grivaks | reachable_one_hop |
| 12 | " murdles." | murdles | grivaks | reachable_one_hop |
## 049/broken/second/1

```text
All ruspins are grivaks.
All murdles are shalds.
All tufas are nufrons.
All nufrons are shalds.
Possible completions: shalds or grivaks.
Therefore, all tufas are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | shalds | reachable_one_hop |
| 4 | " nufrons." | nufrons | shalds | reachable_one_hop |
| 12 | " nufrons." | nufrons | shalds | reachable_one_hop |
## 049/robustness/reorder/0

```text
All tufas are nufrons.
All murdles are shalds.
All ruspins are grivaks.
All nufrons are grivaks.
Possible completions: shalds or grivaks.
Therefore, all tufas are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | shalds | reachable_one_hop |
| 4 | " nufrons." | nufrons | grivaks | reachable_one_hop |
| 12 | " nufrons." | nufrons | grivaks | reachable_one_hop |
## 049/robustness/reorder/1

```text
All nufrons are tufas.
All ruspins are tufas.
All murdles are shalds.
All grivaks are nufrons.
Possible completions: tufas or shalds.
Therefore, all grivaks are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | tufas | reachable_one_hop |
| 4 | " nufrons." | nufrons | tufas | reachable_one_hop |
| 12 | " nufrons." | nufrons | tufas | reachable_one_hop |
## 049/robustness/distractors/0

```text
All welbins are shalds.
All murdles are shalds.
All brovets are welbins.
All ruspins are grivaks.
All nufrons are grivaks.
All tufas are nufrons.
Possible completions: shalds or grivaks.
Therefore, all tufas are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | grivaks | reachable_one_hop |
| 4 | " nufrons." | nufrons | grivaks | reachable_one_hop |
| 12 | " nufrons." | nufrons | grivaks | reachable_one_hop |
## 049/robustness/distractors/1

```text
All grivaks are nufrons.
All brovets are welbins.
All ruspins are tufas.
All welbins are shalds.
All nufrons are tufas.
All murdles are shalds.
Possible completions: tufas or shalds.
Therefore, all grivaks are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | tufas | reachable_one_hop |
| 4 | " nufrons." | nufrons | tufas | reachable_one_hop |
| 12 | " nufrons." | nufrons | shalds | reachable_one_hop |
## 049/robustness/rename/0

```text
All brovets are welbins.
All zorks are wugs.
All snorps are jastles.
All jastles are welbins.
Possible completions: wugs or welbins.
Therefore, all snorps are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | welbins | reachable_one_hop |
| 4 | " welbins." | welbins | welbins | correct_target |
| 12 | " jastles." | jastles | wugs | reachable_one_hop |
## 049/robustness/rename/1

```text
All blickets are nerps.
All vromps are zemples.
All nerps are sprocks.
All zeltrons are sprocks.
Possible completions: sprocks or zemples.
Therefore, all blickets are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " nerps." | nerps | sprocks | reachable_one_hop |
| 12 | " zeltrons." | zeltrons | sprocks | unreachable_fact_name |
## 050/direct/base/0

```text
All crundles are tufas.
All tufas are yorbits.
All sprocks are prandils.
All quavels are yorbits.
Possible completions: tufas or prandils.
Therefore, all crundles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | tufas | other_reachable |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " prandils." | prandils | prandils | wrong_candidate |
## 050/direct/base/1

```text
All crundles are tufas.
All tufas are yorbits.
All sprocks are prandils.
All quavels are yorbits.
Possible completions: prandils or yorbits.
Therefore, all tufas are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " yorbits." | yorbits | yorbits | correct_target |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 050/twohop/base/0

```text
All crundles are tufas.
All tufas are yorbits.
All sprocks are prandils.
All quavels are yorbits.
Possible completions: yorbits or prandils.
Therefore, all crundles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " tufas." | tufas | prandils | reachable_one_hop |
| 12 | " prandils." | prandils | prandils | wrong_candidate |
## 050/twohop/base/1

```text
All yorbits are tufas.
All sprocks are prandils.
All tufas are crundles.
All quavels are crundles.
Possible completions: prandils or crundles.
Therefore, all yorbits are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | crundles | reachable_one_hop |
| 4 | " crundles." | crundles | crundles | correct_target |
| 12 | " crundles." | crundles | crundles | correct_target |
## 050/broken/first/0

```text
All crundles are sprocks.
All tufas are yorbits.
All sprocks are prandils.
All quavels are yorbits.
Possible completions: yorbits or prandils.
Therefore, all crundles are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | yorbits | reachable_one_hop |
| 4 | " sprocks." | sprocks | prandils | reachable_one_hop |
| 12 | " prandils." | prandils | prandils | correct_target |
## 050/broken/second/1

```text
All crundles are tufas.
All tufas are prandils.
All sprocks are prandils.
All quavels are yorbits.
Possible completions: yorbits or prandils.
Therefore, all crundles are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " tufas." | tufas | prandils | reachable_one_hop |
| 12 | " prandils." | prandils | prandils | correct_target |
## 050/robustness/reorder/0

```text
All crundles are tufas.
All quavels are yorbits.
All tufas are yorbits.
All sprocks are prandils.
Possible completions: yorbits or prandils.
Therefore, all crundles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " tufas." | tufas | prandils | reachable_one_hop |
| 12 | " prandils." | prandils | prandils | wrong_candidate |
## 050/robustness/reorder/1

```text
All sprocks are prandils.
All quavels are crundles.
All tufas are crundles.
All yorbits are tufas.
Possible completions: prandils or crundles.
Therefore, all yorbits are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | prandils | reachable_one_hop |
| 4 | " tufas." | tufas | crundles | reachable_one_hop |
| 12 | " tufas." | tufas | crundles | reachable_one_hop |
## 050/robustness/distractors/0

```text
All tufas are yorbits.
All sprocks are prandils.
All quavels are yorbits.
All crundles are tufas.
All kelbrins are prandils.
All nufrons are kelbrins.
Possible completions: yorbits or prandils.
Therefore, all crundles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | yorbits | reachable_one_hop |
| 4 | " tufas." | tufas | prandils | reachable_one_hop |
| 12 | " tufas." | tufas | prandils | reachable_one_hop |
## 050/robustness/distractors/1

```text
All yorbits are tufas.
All nufrons are kelbrins.
All quavels are crundles.
All tufas are crundles.
All sprocks are prandils.
All kelbrins are prandils.
Possible completions: prandils or crundles.
Therefore, all yorbits are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | crundles | reachable_one_hop |
| 4 | " tufas." | tufas | crundles | reachable_one_hop |
| 12 | " crundles." | crundles | crundles | correct_target |
## 050/robustness/rename/0

```text
All vibbles are zeltrons.
All zeltrons are vromps.
All jastles are blickets.
All lomits are vromps.
Possible completions: vromps or blickets.
Therefore, all vibbles are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | blickets | reachable_one_hop |
| 4 | " zeltrons." | zeltrons | blickets | reachable_one_hop |
| 12 | " blickets." | blickets | blickets | wrong_candidate |
## 050/robustness/rename/1

```text
All zeltrons are vromps.
All zorks are daxes.
All vromps are plinets.
All murdles are plinets.
Possible completions: daxes or plinets.
Therefore, all zeltrons are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | daxes | reachable_one_hop |
| 4 | " vromps." | vromps | daxes | reachable_one_hop |
| 12 | " plinets." | plinets | plinets | correct_target |
## 051/direct/base/0

```text
All ulvets are blickets.
All shalds are blickets.
All yorbits are nerps.
All sprocks are shalds.
Possible completions: nerps or shalds.
Therefore, all sprocks are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | wrong_candidate |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 051/direct/base/1

```text
All ulvets are blickets.
All shalds are blickets.
All yorbits are nerps.
All sprocks are shalds.
Possible completions: blickets or nerps.
Therefore, all shalds are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | correct_target |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 051/twohop/base/0

```text
All ulvets are blickets.
All shalds are blickets.
All yorbits are nerps.
All sprocks are shalds.
Possible completions: nerps or blickets.
Therefore, all sprocks are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | nerps | reachable_one_hop |
| 4 | " shalds." | shalds | blickets | reachable_one_hop |
| 12 | " shalds." | shalds | blickets | reachable_one_hop |
## 051/twohop/base/1

```text
All yorbits are nerps.
All ulvets are sprocks.
All blickets are shalds.
All shalds are sprocks.
Possible completions: sprocks or nerps.
Therefore, all blickets are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | sprocks | reachable_one_hop |
| 4 | " shalds." | shalds | nerps | reachable_one_hop |
| 12 | " shalds." | shalds | sprocks | reachable_one_hop |
## 051/broken/first/0

```text
All ulvets are blickets.
All shalds are blickets.
All yorbits are nerps.
All sprocks are yorbits.
Possible completions: nerps or blickets.
Therefore, all sprocks are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " yorbits." | yorbits | nerps | reachable_one_hop |
| 12 | " yorbits." | yorbits | blickets | reachable_one_hop |
## 051/broken/second/1

```text
All ulvets are blickets.
All shalds are nerps.
All yorbits are nerps.
All sprocks are shalds.
Possible completions: nerps or blickets.
Therefore, all sprocks are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | nerps | reachable_one_hop |
| 4 | " shalds." | shalds | nerps | reachable_one_hop |
| 12 | " shalds." | shalds | nerps | reachable_one_hop |
## 051/robustness/reorder/0

```text
All shalds are blickets.
All yorbits are nerps.
All sprocks are shalds.
All ulvets are blickets.
Possible completions: nerps or blickets.
Therefore, all sprocks are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | nerps | reachable_one_hop |
| 4 | " shalds." | shalds | blickets | reachable_one_hop |
| 12 | " shalds." | shalds | blickets | reachable_one_hop |
## 051/robustness/reorder/1

```text
All yorbits are nerps.
All shalds are sprocks.
All blickets are shalds.
All ulvets are sprocks.
Possible completions: sprocks or nerps.
Therefore, all blickets are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | nerps | unreachable_fact_name |
| 4 | " shalds." | shalds | sprocks | reachable_one_hop |
| 12 | " shalds." | shalds | sprocks | reachable_one_hop |
## 051/robustness/distractors/0

```text
All sprocks are shalds.
All shalds are blickets.
All tivaks are nerps.
All flomps are tivaks.
All ulvets are blickets.
All yorbits are nerps.
Possible completions: nerps or blickets.
Therefore, all sprocks are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | wrong_candidate |
| 4 | " shalds." | shalds | blickets | reachable_one_hop |
| 12 | " shalds." | shalds | blickets | reachable_one_hop |
## 051/robustness/distractors/1

```text
All ulvets are sprocks.
All flomps are tivaks.
All yorbits are nerps.
All tivaks are nerps.
All shalds are sprocks.
All blickets are shalds.
Possible completions: sprocks or nerps.
Therefore, all blickets are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " shalds." | shalds | nerps | reachable_one_hop |
| 12 | " shalds." | shalds | nerps | reachable_one_hop |
## 051/robustness/rename/0

```text
All zorks are prandils.
All quavels are prandils.
All flomps are oskets.
All snorps are quavels.
Possible completions: oskets or prandils.
Therefore, all snorps are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | correct_target |
| 4 | " quavels." | quavels | prandils | reachable_one_hop |
| 12 | " quavels." | quavels | prandils | reachable_one_hop |
## 051/robustness/rename/1

```text
All murdles are daxes.
All kelbrins are vromps.
All tufas are helpons.
All helpons are vromps.
Possible completions: vromps or daxes.
Therefore, all tufas are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | daxes | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 052/direct/base/0

```text
All vibbles are vromps.
All snorps are sprocks.
All zemples are tivaks.
All sprocks are vromps.
Possible completions: sprocks or tivaks.
Therefore, all snorps are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | sprocks | other_reachable |
| 4 | " vromps." | vromps | tivaks | other_reachable |
| 12 | " vromps." | vromps | tivaks | other_reachable |
## 052/direct/base/1

```text
All vibbles are vromps.
All snorps are sprocks.
All zemples are tivaks.
All sprocks are vromps.
Possible completions: tivaks or vromps.
Therefore, all sprocks are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | vromps | correct_target |
| 4 | " vromps." | vromps | vromps | correct_target |
| 12 | " vromps." | vromps | vromps | correct_target |
## 052/twohop/base/0

```text
All vibbles are vromps.
All snorps are sprocks.
All zemples are tivaks.
All sprocks are vromps.
Possible completions: vromps or tivaks.
Therefore, all snorps are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | vromps | reachable_one_hop |
| 4 | " tivaks." | tivaks | tivaks | wrong_candidate |
| 12 | " tivaks." | tivaks | tivaks | wrong_candidate |
## 052/twohop/base/1

```text
All sprocks are snorps.
All zemples are tivaks.
All vibbles are snorps.
All vromps are sprocks.
Possible completions: tivaks or snorps.
Therefore, all vromps are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | tivaks | reachable_one_hop |
| 4 | " sprocks." | sprocks | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | correct_target |
## 052/broken/first/0

```text
All vibbles are vromps.
All snorps are zemples.
All zemples are tivaks.
All sprocks are vromps.
Possible completions: vromps or tivaks.
Therefore, all snorps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | vromps | wrong_candidate |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 052/broken/second/1

```text
All vibbles are vromps.
All snorps are sprocks.
All zemples are tivaks.
All sprocks are tivaks.
Possible completions: vromps or tivaks.
Therefore, all snorps are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | vromps | reachable_one_hop |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 052/robustness/reorder/0

```text
All zemples are tivaks.
All snorps are sprocks.
All sprocks are vromps.
All vibbles are vromps.
Possible completions: vromps or tivaks.
Therefore, all snorps are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | vromps | correct_target |
| 4 | " tivaks." | tivaks | tivaks | wrong_candidate |
| 12 | " tivaks." | tivaks | tivaks | wrong_candidate |
## 052/robustness/reorder/1

```text
All zemples are tivaks.
All vibbles are snorps.
All sprocks are snorps.
All vromps are sprocks.
Possible completions: tivaks or snorps.
Therefore, all vromps are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | tivaks | reachable_one_hop |
| 4 | " sprocks." | sprocks | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | correct_target |
## 052/robustness/distractors/0

```text
All zemples are tivaks.
All shalds are brovets.
All vibbles are vromps.
All brovets are tivaks.
All snorps are sprocks.
All sprocks are vromps.
Possible completions: vromps or tivaks.
Therefore, all snorps are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | vromps | correct_target |
| 4 | " vromps." | vromps | vromps | correct_target |
| 12 | " tivaks." | tivaks | tivaks | wrong_candidate |
## 052/robustness/distractors/1

```text
All sprocks are snorps.
All shalds are brovets.
All zemples are tivaks.
All vromps are sprocks.
All brovets are tivaks.
All vibbles are snorps.
Possible completions: tivaks or snorps.
Therefore, all vromps are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | tivaks | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 052/robustness/rename/0

```text
All grivaks are flomps.
All brovets are kelbrins.
All oskets are shalds.
All kelbrins are flomps.
Possible completions: flomps or shalds.
Therefore, all brovets are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | flomps | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | flomps | reachable_one_hop |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 052/robustness/rename/1

```text
All wugs are tufas.
All quavels are brovets.
All shalds are tufas.
All korvas are wugs.
Possible completions: brovets or tufas.
Therefore, all korvas are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | tufas | reachable_one_hop |
| 4 | " wugs." | wugs | tufas | reachable_one_hop |
| 12 | " wugs." | wugs | tufas | reachable_one_hop |
## 053/direct/base/0

```text
All tivaks are zeltrons.
All welbins are zeltrons.
All vibbles are yorbits.
All korvas are welbins.
Possible completions: yorbits or welbins.
Therefore, all korvas are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 12 | " welbins." | welbins | welbins | correct_target |
## 053/direct/base/1

```text
All tivaks are zeltrons.
All welbins are zeltrons.
All vibbles are yorbits.
All korvas are welbins.
Possible completions: zeltrons or yorbits.
Therefore, all welbins are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 053/twohop/base/0

```text
All tivaks are zeltrons.
All welbins are zeltrons.
All vibbles are yorbits.
All korvas are welbins.
Possible completions: yorbits or zeltrons.
Therefore, all korvas are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 053/twohop/base/1

```text
All tivaks are korvas.
All vibbles are yorbits.
All zeltrons are welbins.
All welbins are korvas.
Possible completions: korvas or yorbits.
Therefore, all zeltrons are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | korvas | correct_target |
| 4 | " korvas." | korvas | korvas | correct_target |
| 12 | " korvas." | korvas | korvas | correct_target |
## 053/broken/first/0

```text
All tivaks are zeltrons.
All welbins are zeltrons.
All vibbles are yorbits.
All korvas are vibbles.
Possible completions: yorbits or zeltrons.
Therefore, all korvas are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " vibbles." | vibbles | zeltrons | reachable_one_hop |
| 12 | " vibbles." | vibbles | zeltrons | reachable_one_hop |
## 053/broken/second/1

```text
All tivaks are zeltrons.
All welbins are yorbits.
All vibbles are yorbits.
All korvas are welbins.
Possible completions: yorbits or zeltrons.
Therefore, all korvas are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 12 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
## 053/robustness/reorder/0

```text
All welbins are zeltrons.
All vibbles are yorbits.
All korvas are welbins.
All tivaks are zeltrons.
Possible completions: yorbits or zeltrons.
Therefore, all korvas are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 053/robustness/reorder/1

```text
All vibbles are yorbits.
All tivaks are korvas.
All welbins are korvas.
All zeltrons are welbins.
Possible completions: korvas or yorbits.
Therefore, all zeltrons are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " welbins." | welbins | korvas | reachable_one_hop |
| 12 | " welbins." | welbins | yorbits | reachable_one_hop |
## 053/robustness/distractors/0

```text
All daxes are yorbits.
All korvas are welbins.
All welbins are zeltrons.
All nufrons are daxes.
All tivaks are zeltrons.
All vibbles are yorbits.
Possible completions: yorbits or zeltrons.
Therefore, all korvas are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | yorbits | reachable_one_hop |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " yorbits." | yorbits | yorbits | wrong_candidate |
## 053/robustness/distractors/1

```text
All daxes are yorbits.
All tivaks are korvas.
All welbins are korvas.
All vibbles are yorbits.
All nufrons are daxes.
All zeltrons are welbins.
Possible completions: korvas or yorbits.
Therefore, all zeltrons are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 4 | " daxes." | daxes | yorbits | unreachable_fact_name |
| 12 | " daxes." | daxes | yorbits | unreachable_fact_name |
## 053/robustness/rename/0

```text
All wugs are nerps.
All nufrons are nerps.
All lomits are brovets.
All blickets are nufrons.
Possible completions: brovets or nerps.
Therefore, all blickets are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | wrong_candidate |
| 4 | " nufrons." | nufrons | nerps | reachable_one_hop |
| 12 | " nufrons." | nufrons | nerps | reachable_one_hop |
## 053/robustness/rename/1

```text
All daxes are brovets.
All lomits are sprocks.
All wugs are prandils.
All prandils are brovets.
Possible completions: brovets or sprocks.
Therefore, all wugs are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | correct_target |
| 4 | " prandils." | prandils | brovets | reachable_one_hop |
| 12 | " brovets." | brovets | brovets | correct_target |
## 054/direct/base/0

```text
All snorps are kelbrins.
All ulvets are murdles.
All flomps are zemples.
All kelbrins are zemples.
Possible completions: kelbrins or murdles.
Therefore, all snorps are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " zemples." | zemples | kelbrins | other_reachable |
## 054/direct/base/1

```text
All snorps are kelbrins.
All ulvets are murdles.
All flomps are zemples.
All kelbrins are zemples.
Possible completions: murdles or zemples.
Therefore, all kelbrins are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | correct_target |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 054/twohop/base/0

```text
All snorps are kelbrins.
All ulvets are murdles.
All flomps are zemples.
All kelbrins are zemples.
Possible completions: zemples or murdles.
Therefore, all snorps are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | zemples | reachable_one_hop |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 054/twohop/base/1

```text
All ulvets are murdles.
All kelbrins are snorps.
All flomps are snorps.
All zemples are kelbrins.
Possible completions: murdles or snorps.
Therefore, all zemples are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | murdles | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | snorps | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | snorps | reachable_one_hop |
## 054/broken/first/0

```text
All snorps are ulvets.
All ulvets are murdles.
All flomps are zemples.
All kelbrins are zemples.
Possible completions: zemples or murdles.
Therefore, all snorps are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | zemples | reachable_one_hop |
| 4 | " zemples." | zemples | zemples | wrong_candidate |
| 12 | " murdles." | murdles | murdles | correct_target |
## 054/broken/second/1

```text
All snorps are kelbrins.
All ulvets are murdles.
All flomps are zemples.
All kelbrins are murdles.
Possible completions: zemples or murdles.
Therefore, all snorps are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | zemples | reachable_one_hop |
| 4 | " murdles." | murdles | murdles | correct_target |
| 12 | " murdles." | murdles | murdles | correct_target |
## 054/robustness/reorder/0

```text
All ulvets are murdles.
All kelbrins are zemples.
All snorps are kelbrins.
All flomps are zemples.
Possible completions: zemples or murdles.
Therefore, all snorps are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | murdles | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | zemples | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | zemples | reachable_one_hop |
## 054/robustness/reorder/1

```text
All ulvets are murdles.
All zemples are kelbrins.
All flomps are snorps.
All kelbrins are snorps.
Possible completions: murdles or snorps.
Therefore, all zemples are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | murdles | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " kelbrins." | kelbrins | snorps | reachable_one_hop |
## 054/robustness/distractors/0

```text
All vibbles are murdles.
All kelbrins are zemples.
All ulvets are murdles.
All snorps are kelbrins.
All flomps are zemples.
All prandils are vibbles.
Possible completions: zemples or murdles.
Therefore, all snorps are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | zemples | unreachable_fact_name |
| 4 | " vibbles." | vibbles | zemples | unreachable_fact_name |
| 12 | " vibbles." | vibbles | zemples | unreachable_fact_name |
## 054/robustness/distractors/1

```text
All vibbles are murdles.
All flomps are snorps.
All prandils are vibbles.
All zemples are kelbrins.
All kelbrins are snorps.
All ulvets are murdles.
Possible completions: murdles or snorps.
Therefore, all zemples are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | murdles | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | snorps | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | snorps | reachable_one_hop |
## 054/robustness/rename/0

```text
All tivaks are brovets.
All nufrons are shalds.
All ruspins are sprocks.
All brovets are sprocks.
Possible completions: sprocks or shalds.
Therefore, all tivaks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | sprocks | reachable_one_hop |
| 4 | " brovets." | brovets | sprocks | reachable_one_hop |
| 12 | " shalds." | shalds | shalds | wrong_candidate |
## 054/robustness/rename/1

```text
All daxes are nufrons.
All prandils are vibbles.
All crundles are vibbles.
All plinets are prandils.
Possible completions: nufrons or vibbles.
Therefore, all plinets are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 4 | " prandils." | prandils | nufrons | reachable_one_hop |
| 12 | " prandils." | prandils | vibbles | reachable_one_hop |
## 055/direct/base/0

```text
All zemples are ulvets.
All nerps are prandils.
All prandils are blickets.
All lomits are blickets.
Possible completions: ulvets or prandils.
Therefore, all nerps are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | ulvets | unreachable_fact_name |
| 4 | " blickets." | blickets | prandils | other_reachable |
| 12 | " prandils." | prandils | prandils | correct_target |
## 055/direct/base/1

```text
All zemples are ulvets.
All nerps are prandils.
All prandils are blickets.
All lomits are blickets.
Possible completions: blickets or ulvets.
Therefore, all prandils are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | correct_target |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 055/twohop/base/0

```text
All zemples are ulvets.
All nerps are prandils.
All prandils are blickets.
All lomits are blickets.
Possible completions: ulvets or blickets.
Therefore, all nerps are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 055/twohop/base/1

```text
All zemples are ulvets.
All blickets are prandils.
All lomits are nerps.
All prandils are nerps.
Possible completions: nerps or ulvets.
Therefore, all blickets are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 4 | " prandils." | prandils | nerps | reachable_one_hop |
| 12 | " nerps." | nerps | nerps | correct_target |
## 055/broken/first/0

```text
All zemples are ulvets.
All nerps are zemples.
All prandils are blickets.
All lomits are blickets.
Possible completions: ulvets or blickets.
Therefore, all nerps are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | correct_target |
| 4 | " prandils." | prandils | blickets | unreachable_fact_name |
| 12 | " blickets." | blickets | blickets | wrong_candidate |
## 055/broken/second/1

```text
All zemples are ulvets.
All nerps are prandils.
All prandils are ulvets.
All lomits are blickets.
Possible completions: ulvets or blickets.
Therefore, all nerps are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | correct_target |
| 4 | " ulvets." | ulvets | ulvets | correct_target |
| 12 | " ulvets." | ulvets | ulvets | correct_target |
## 055/robustness/reorder/0

```text
All lomits are blickets.
All zemples are ulvets.
All nerps are prandils.
All prandils are blickets.
Possible completions: ulvets or blickets.
Therefore, all nerps are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | blickets | reachable_one_hop |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 055/robustness/reorder/1

```text
All lomits are nerps.
All blickets are prandils.
All prandils are nerps.
All zemples are ulvets.
Possible completions: nerps or ulvets.
Therefore, all blickets are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 055/robustness/distractors/0

```text
All helpons are ulvets.
All prandils are blickets.
All zemples are ulvets.
All vromps are helpons.
All nerps are prandils.
All lomits are blickets.
Possible completions: ulvets or blickets.
Therefore, all nerps are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 055/robustness/distractors/1

```text
All blickets are prandils.
All vromps are helpons.
All prandils are nerps.
All helpons are ulvets.
All lomits are nerps.
All zemples are ulvets.
Possible completions: nerps or ulvets.
Therefore, all blickets are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | nerps | reachable_one_hop |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 055/robustness/rename/0

```text
All yorbits are tufas.
All brovets are zorks.
All zorks are vibbles.
All crundles are vibbles.
Possible completions: tufas or vibbles.
Therefore, all brovets are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | vibbles | reachable_one_hop |
| 4 | " zorks." | zorks | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 055/robustness/rename/1

```text
All plinets are flomps.
All yorbits are vibbles.
All wugs are xandles.
All vibbles are xandles.
Possible completions: xandles or flomps.
Therefore, all yorbits are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | flomps | reachable_one_hop |
| 4 | " vibbles." | vibbles | flomps | reachable_one_hop |
| 12 | " vibbles." | vibbles | flomps | reachable_one_hop |
## 056/direct/base/0

```text
All vibbles are snorps.
All zemples are brovets.
All shalds are vibbles.
All murdles are snorps.
Possible completions: vibbles or brovets.
Therefore, all shalds are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 056/direct/base/1

```text
All vibbles are snorps.
All zemples are brovets.
All shalds are vibbles.
All murdles are snorps.
Possible completions: brovets or snorps.
Therefore, all vibbles are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | correct_target |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 056/twohop/base/0

```text
All vibbles are snorps.
All zemples are brovets.
All shalds are vibbles.
All murdles are snorps.
Possible completions: snorps or brovets.
Therefore, all shalds are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | brovets | reachable_one_hop |
| 4 | " vibbles." | vibbles | snorps | reachable_one_hop |
| 12 | " vibbles." | vibbles | snorps | reachable_one_hop |
## 056/twohop/base/1

```text
All snorps are vibbles.
All vibbles are shalds.
All zemples are brovets.
All murdles are shalds.
Possible completions: brovets or shalds.
Therefore, all snorps are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | wrong_candidate |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 056/broken/first/0

```text
All vibbles are snorps.
All zemples are brovets.
All shalds are zemples.
All murdles are snorps.
Possible completions: snorps or brovets.
Therefore, all shalds are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | snorps | reachable_one_hop |
| 4 | " zemples." | zemples | snorps | reachable_one_hop |
| 12 | " zemples." | zemples | snorps | reachable_one_hop |
## 056/broken/second/1

```text
All vibbles are brovets.
All zemples are brovets.
All shalds are vibbles.
All murdles are snorps.
Possible completions: snorps or brovets.
Therefore, all shalds are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | brovets | reachable_one_hop |
| 4 | " vibbles." | vibbles | snorps | reachable_one_hop |
| 12 | " vibbles." | vibbles | snorps | reachable_one_hop |
## 056/robustness/reorder/0

```text
All zemples are brovets.
All shalds are vibbles.
All murdles are snorps.
All vibbles are snorps.
Possible completions: snorps or brovets.
Therefore, all shalds are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | brovets | reachable_one_hop |
| 4 | " vibbles." | vibbles | snorps | reachable_one_hop |
| 12 | " vibbles." | vibbles | snorps | reachable_one_hop |
## 056/robustness/reorder/1

```text
All murdles are shalds.
All vibbles are shalds.
All snorps are vibbles.
All zemples are brovets.
Possible completions: brovets or shalds.
Therefore, all snorps are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | shalds | unreachable_fact_name |
| 4 | " vibbles." | vibbles | shalds | reachable_one_hop |
| 12 | " vibbles." | vibbles | shalds | reachable_one_hop |
## 056/robustness/distractors/0

```text
All zemples are brovets.
All shalds are vibbles.
All tivaks are brovets.
All vibbles are snorps.
All zorks are tivaks.
All murdles are snorps.
Possible completions: snorps or brovets.
Therefore, all shalds are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | brovets | reachable_one_hop |
| 4 | " vibbles." | vibbles | snorps | reachable_one_hop |
| 12 | " vibbles." | vibbles | snorps | reachable_one_hop |
## 056/robustness/distractors/1

```text
All zemples are brovets.
All zorks are tivaks.
All tivaks are brovets.
All vibbles are shalds.
All snorps are vibbles.
All murdles are shalds.
Possible completions: brovets or shalds.
Therefore, all snorps are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | shalds | reachable_one_hop |
| 4 | " vibbles." | vibbles | shalds | reachable_one_hop |
| 12 | " vibbles." | vibbles | shalds | reachable_one_hop |
## 056/robustness/rename/0

```text
All nerps are sprocks.
All welbins are vromps.
All ulvets are nerps.
All nufrons are sprocks.
Possible completions: sprocks or vromps.
Therefore, all ulvets are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | sprocks | reachable_one_hop |
| 4 | " nerps." | nerps | sprocks | reachable_one_hop |
| 12 | " nerps." | nerps | vromps | reachable_one_hop |
## 056/robustness/rename/1

```text
All welbins are ruspins.
All ruspins are crundles.
All tivaks are prandils.
All zorks are crundles.
Possible completions: prandils or crundles.
Therefore, all welbins are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | wrong_candidate |
| 4 | " crundles." | crundles | crundles | correct_target |
| 12 | " crundles." | crundles | crundles | correct_target |
## 057/direct/base/0

```text
All vibbles are yorbits.
All daxes are vibbles.
All grivaks are nufrons.
All vromps are yorbits.
Possible completions: nufrons or vibbles.
Therefore, all daxes are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 057/direct/base/1

```text
All vibbles are yorbits.
All daxes are vibbles.
All grivaks are nufrons.
All vromps are yorbits.
Possible completions: yorbits or nufrons.
Therefore, all vibbles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " yorbits." | yorbits | yorbits | correct_target |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 057/twohop/base/0

```text
All vibbles are yorbits.
All daxes are vibbles.
All grivaks are nufrons.
All vromps are yorbits.
Possible completions: nufrons or yorbits.
Therefore, all daxes are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | yorbits | reachable_one_hop |
| 4 | " vibbles." | vibbles | yorbits | reachable_one_hop |
| 12 | " vibbles." | vibbles | yorbits | reachable_one_hop |
## 057/twohop/base/1

```text
All yorbits are vibbles.
All grivaks are nufrons.
All vromps are daxes.
All vibbles are daxes.
Possible completions: daxes or nufrons.
Therefore, all yorbits are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | daxes | reachable_one_hop |
| 4 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 12 | " vibbles." | vibbles | daxes | reachable_one_hop |
## 057/broken/first/0

```text
All vibbles are yorbits.
All daxes are grivaks.
All grivaks are nufrons.
All vromps are yorbits.
Possible completions: nufrons or yorbits.
Therefore, all daxes are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | yorbits | reachable_one_hop |
| 4 | " yorbits." | yorbits | yorbits | wrong_candidate |
| 12 | " yorbits." | yorbits | yorbits | wrong_candidate |
## 057/broken/second/1

```text
All vibbles are nufrons.
All daxes are vibbles.
All grivaks are nufrons.
All vromps are yorbits.
Possible completions: nufrons or yorbits.
Therefore, all daxes are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | nufrons | reachable_one_hop |
| 4 | " vibbles." | vibbles | yorbits | reachable_one_hop |
| 12 | " vibbles." | vibbles | nufrons | reachable_one_hop |
## 057/robustness/reorder/0

```text
All vromps are yorbits.
All daxes are vibbles.
All vibbles are yorbits.
All grivaks are nufrons.
Possible completions: nufrons or yorbits.
Therefore, all daxes are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | yorbits | reachable_one_hop |
| 4 | " yorbits." | yorbits | yorbits | correct_target |
| 12 | " vibbles." | vibbles | yorbits | reachable_one_hop |
## 057/robustness/reorder/1

```text
All yorbits are vibbles.
All vromps are daxes.
All vibbles are daxes.
All grivaks are nufrons.
Possible completions: daxes or nufrons.
Therefore, all yorbits are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | correct_target |
| 4 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 12 | " vibbles." | vibbles | daxes | reachable_one_hop |
## 057/robustness/distractors/0

```text
All vibbles are yorbits.
All vromps are yorbits.
All zeltrons are snorps.
All daxes are vibbles.
All snorps are nufrons.
All grivaks are nufrons.
Possible completions: nufrons or yorbits.
Therefore, all daxes are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 12 | " vibbles." | vibbles | nufrons | reachable_one_hop |
## 057/robustness/distractors/1

```text
All snorps are nufrons.
All vromps are daxes.
All zeltrons are snorps.
All vibbles are daxes.
All grivaks are nufrons.
All yorbits are vibbles.
Possible completions: daxes or nufrons.
Therefore, all yorbits are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | daxes | reachable_one_hop |
| 4 | " vibbles." | vibbles | nufrons | reachable_one_hop |
| 12 | " vibbles." | vibbles | nufrons | reachable_one_hop |
## 057/robustness/rename/0

```text
All kelbrins are zorks.
All wugs are kelbrins.
All sprocks are blickets.
All tufas are zorks.
Possible completions: blickets or zorks.
Therefore, all wugs are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | wrong_candidate |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " kelbrins." | kelbrins | zorks | reachable_one_hop |
## 057/robustness/rename/1

```text
All zorks are prandils.
All brovets are korvas.
All wugs are jastles.
All prandils are jastles.
Possible completions: jastles or korvas.
Therefore, all zorks are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | jastles | reachable_one_hop |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " prandils." | prandils | jastles | reachable_one_hop |
## 058/direct/base/0

```text
All yorbits are crundles.
All helpons are daxes.
All crundles are brovets.
All flomps are brovets.
Possible completions: crundles or daxes.
Therefore, all yorbits are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 058/direct/base/1

```text
All yorbits are crundles.
All helpons are daxes.
All crundles are brovets.
All flomps are brovets.
Possible completions: daxes or brovets.
Therefore, all crundles are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " brovets." | brovets | brovets | correct_target |
| 12 | " brovets." | brovets | brovets | correct_target |
## 058/twohop/base/0

```text
All yorbits are crundles.
All helpons are daxes.
All crundles are brovets.
All flomps are brovets.
Possible completions: brovets or daxes.
Therefore, all yorbits are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 058/twohop/base/1

```text
All helpons are daxes.
All flomps are yorbits.
All crundles are yorbits.
All brovets are crundles.
Possible completions: daxes or yorbits.
Therefore, all brovets are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " crundles." | crundles | daxes | reachable_one_hop |
| 12 | " crundles." | crundles | daxes | reachable_one_hop |
## 058/broken/first/0

```text
All yorbits are helpons.
All helpons are daxes.
All crundles are brovets.
All flomps are brovets.
Possible completions: brovets or daxes.
Therefore, all yorbits are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | correct_target |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 058/broken/second/1

```text
All yorbits are crundles.
All helpons are daxes.
All crundles are daxes.
All flomps are brovets.
Possible completions: brovets or daxes.
Therefore, all yorbits are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | wrong_candidate |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 058/robustness/reorder/0

```text
All crundles are brovets.
All yorbits are crundles.
All helpons are daxes.
All flomps are brovets.
Possible completions: brovets or daxes.
Therefore, all yorbits are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " crundles." | crundles | brovets | reachable_one_hop |
| 4 | " crundles." | crundles | daxes | reachable_one_hop |
| 12 | " crundles." | crundles | daxes | reachable_one_hop |
## 058/robustness/reorder/1

```text
All crundles are yorbits.
All flomps are yorbits.
All helpons are daxes.
All brovets are crundles.
Possible completions: daxes or yorbits.
Therefore, all brovets are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | yorbits | wrong_candidate |
| 4 | " crundles." | crundles | daxes | reachable_one_hop |
| 12 | " crundles." | crundles | yorbits | reachable_one_hop |
## 058/robustness/distractors/0

```text
All helpons are daxes.
All zemples are daxes.
All flomps are brovets.
All yorbits are crundles.
All crundles are brovets.
All shalds are zemples.
Possible completions: brovets or daxes.
Therefore, all yorbits are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | daxes | unreachable_fact_name |
| 4 | " crundles." | crundles | daxes | reachable_one_hop |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 058/robustness/distractors/1

```text
All helpons are daxes.
All shalds are zemples.
All brovets are crundles.
All flomps are yorbits.
All zemples are daxes.
All crundles are yorbits.
Possible completions: daxes or yorbits.
Therefore, all brovets are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " crundles." | crundles | yorbits | reachable_one_hop |
| 12 | " crundles." | crundles | daxes | reachable_one_hop |
## 058/robustness/rename/0

```text
All quavels are zeltrons.
All vromps are grivaks.
All zeltrons are ruspins.
All prandils are ruspins.
Possible completions: ruspins or grivaks.
Therefore, all quavels are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 058/robustness/rename/1

```text
All korvas are prandils.
All zorks are tufas.
All nufrons are tufas.
All zemples are nufrons.
Possible completions: prandils or tufas.
Therefore, all zemples are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | prandils | reachable_one_hop |
| 4 | " nufrons." | nufrons | tufas | reachable_one_hop |
| 12 | " nufrons." | nufrons | tufas | reachable_one_hop |
## 059/direct/base/0

```text
All zeltrons are vibbles.
All murdles are snorps.
All zorks are sprocks.
All sprocks are snorps.
Possible completions: vibbles or sprocks.
Therefore, all zorks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | sprocks | other_reachable |
| 4 | " snorps." | snorps | sprocks | other_reachable |
| 12 | " snorps." | snorps | sprocks | other_reachable |
## 059/direct/base/1

```text
All zeltrons are vibbles.
All murdles are snorps.
All zorks are sprocks.
All sprocks are snorps.
Possible completions: snorps or vibbles.
Therefore, all sprocks are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 059/twohop/base/0

```text
All zeltrons are vibbles.
All murdles are snorps.
All zorks are sprocks.
All sprocks are snorps.
Possible completions: vibbles or snorps.
Therefore, all zorks are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | vibbles | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 059/twohop/base/1

```text
All sprocks are zorks.
All zeltrons are vibbles.
All snorps are sprocks.
All murdles are zorks.
Possible completions: zorks or vibbles.
Therefore, all snorps are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | zorks | reachable_one_hop |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 059/broken/first/0

```text
All zeltrons are vibbles.
All murdles are snorps.
All zorks are zeltrons.
All sprocks are snorps.
Possible completions: vibbles or snorps.
Therefore, all zorks are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | vibbles | unreachable_fact_name |
| 4 | " zeltrons." | zeltrons | vibbles | reachable_one_hop |
| 12 | " zeltrons." | zeltrons | snorps | reachable_one_hop |
## 059/broken/second/1

```text
All zeltrons are vibbles.
All murdles are snorps.
All zorks are sprocks.
All sprocks are vibbles.
Possible completions: vibbles or snorps.
Therefore, all zorks are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 059/robustness/reorder/0

```text
All murdles are snorps.
All zorks are sprocks.
All zeltrons are vibbles.
All sprocks are snorps.
Possible completions: vibbles or snorps.
Therefore, all zorks are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | vibbles | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 059/robustness/reorder/1

```text
All murdles are zorks.
All zeltrons are vibbles.
All snorps are sprocks.
All sprocks are zorks.
Possible completions: zorks or vibbles.
Therefore, all snorps are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " zorks." | zorks | zorks | correct_target |
## 059/robustness/distractors/0

```text
All zorks are sprocks.
All sprocks are snorps.
All flomps are oskets.
All oskets are vibbles.
All murdles are snorps.
All zeltrons are vibbles.
Possible completions: vibbles or snorps.
Therefore, all zorks are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 059/robustness/distractors/1

```text
All snorps are sprocks.
All oskets are vibbles.
All flomps are oskets.
All zeltrons are vibbles.
All sprocks are zorks.
All murdles are zorks.
Possible completions: zorks or vibbles.
Therefore, all snorps are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | vibbles | reachable_one_hop |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 059/robustness/rename/0

```text
All ulvets are grivaks.
All vromps are lomits.
All helpons are jastles.
All jastles are lomits.
Possible completions: grivaks or lomits.
Therefore, all helpons are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | grivaks | reachable_one_hop |
| 4 | " lomits." | lomits | lomits | correct_target |
| 12 | " lomits." | lomits | lomits | correct_target |
## 059/robustness/rename/1

```text
All daxes are tufas.
All korvas are brovets.
All quavels are daxes.
All lomits are tufas.
Possible completions: tufas or brovets.
Therefore, all quavels are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | brovets | reachable_one_hop |
| 4 | " daxes." | daxes | tufas | reachable_one_hop |
| 12 | " daxes." | daxes | tufas | reachable_one_hop |
## 060/direct/base/0

```text
All flomps are lomits.
All zemples are plinets.
All quavels are lomits.
All tivaks are flomps.
Possible completions: flomps or plinets.
Therefore, all tivaks are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | flomps | correct_target |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " flomps." | flomps | flomps | correct_target |
## 060/direct/base/1

```text
All flomps are lomits.
All zemples are plinets.
All quavels are lomits.
All tivaks are flomps.
Possible completions: plinets or lomits.
Therefore, all flomps are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | correct_target |
| 4 | " lomits." | lomits | lomits | correct_target |
| 12 | " lomits." | lomits | lomits | correct_target |
## 060/twohop/base/0

```text
All flomps are lomits.
All zemples are plinets.
All quavels are lomits.
All tivaks are flomps.
Possible completions: lomits or plinets.
Therefore, all tivaks are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | lomits | reachable_one_hop |
| 4 | " lomits." | lomits | lomits | correct_target |
| 12 | " flomps." | flomps | lomits | reachable_one_hop |
## 060/twohop/base/1

```text
All flomps are tivaks.
All quavels are tivaks.
All lomits are flomps.
All zemples are plinets.
Possible completions: plinets or tivaks.
Therefore, all lomits are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | plinets | reachable_one_hop |
| 4 | " flomps." | flomps | plinets | reachable_one_hop |
| 12 | " flomps." | flomps | tivaks | reachable_one_hop |
## 060/broken/first/0

```text
All flomps are lomits.
All zemples are plinets.
All quavels are lomits.
All tivaks are zemples.
Possible completions: lomits or plinets.
Therefore, all tivaks are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | wrong_candidate |
| 4 | " lomits." | lomits | lomits | wrong_candidate |
| 12 | " zemples." | zemples | plinets | reachable_one_hop |
## 060/broken/second/1

```text
All flomps are plinets.
All zemples are plinets.
All quavels are lomits.
All tivaks are flomps.
Possible completions: lomits or plinets.
Therefore, all tivaks are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | lomits | reachable_one_hop |
| 4 | " flomps." | flomps | lomits | reachable_one_hop |
| 12 | " flomps." | flomps | plinets | reachable_one_hop |
## 060/robustness/reorder/0

```text
All quavels are lomits.
All zemples are plinets.
All tivaks are flomps.
All flomps are lomits.
Possible completions: lomits or plinets.
Therefore, all tivaks are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | lomits | reachable_one_hop |
| 4 | " flomps." | flomps | lomits | reachable_one_hop |
| 12 | " flomps." | flomps | lomits | reachable_one_hop |
## 060/robustness/reorder/1

```text
All lomits are flomps.
All flomps are tivaks.
All zemples are plinets.
All quavels are tivaks.
Possible completions: plinets or tivaks.
Therefore, all lomits are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | plinets | reachable_one_hop |
| 4 | " flomps." | flomps | plinets | reachable_one_hop |
| 12 | " flomps." | flomps | tivaks | reachable_one_hop |
## 060/robustness/distractors/0

```text
All quavels are lomits.
All ruspins are plinets.
All zemples are plinets.
All flomps are lomits.
All tivaks are flomps.
All murdles are ruspins.
Possible completions: lomits or plinets.
Therefore, all tivaks are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | lomits | unreachable_fact_name |
| 4 | " flomps." | flomps | lomits | reachable_one_hop |
| 12 | " flomps." | flomps | lomits | reachable_one_hop |
## 060/robustness/distractors/1

```text
All zemples are plinets.
All murdles are ruspins.
All flomps are tivaks.
All quavels are tivaks.
All lomits are flomps.
All ruspins are plinets.
Possible completions: plinets or tivaks.
Therefore, all lomits are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | plinets | reachable_one_hop |
| 4 | " flomps." | flomps | plinets | reachable_one_hop |
| 12 | " flomps." | flomps | tivaks | reachable_one_hop |
## 060/robustness/rename/0

```text
All xandles are snorps.
All oskets are zeltrons.
All ruspins are snorps.
All prandils are xandles.
Possible completions: snorps or zeltrons.
Therefore, all prandils are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | snorps | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " xandles." | xandles | snorps | reachable_one_hop |
## 060/robustness/rename/1

```text
All zeltrons are welbins.
All yorbits are welbins.
All ruspins are zeltrons.
All crundles are grivaks.
Possible completions: grivaks or welbins.
Therefore, all ruspins are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " zeltrons." | zeltrons | grivaks | reachable_one_hop |
| 12 | " zeltrons." | zeltrons | grivaks | reachable_one_hop |
## 061/direct/base/0

```text
All crundles are daxes.
All zorks are wugs.
All quavels are vibbles.
All daxes are vibbles.
Possible completions: wugs or daxes.
Therefore, all crundles are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | correct_target |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 061/direct/base/1

```text
All crundles are daxes.
All zorks are wugs.
All quavels are vibbles.
All daxes are vibbles.
Possible completions: vibbles or wugs.
Therefore, all daxes are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 061/twohop/base/0

```text
All crundles are daxes.
All zorks are wugs.
All quavels are vibbles.
All daxes are vibbles.
Possible completions: wugs or vibbles.
Therefore, all crundles are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | vibbles | reachable_one_hop |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 061/twohop/base/1

```text
All quavels are crundles.
All daxes are crundles.
All zorks are wugs.
All vibbles are daxes.
Possible completions: crundles or wugs.
Therefore, all vibbles are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | crundles | reachable_one_hop |
| 4 | " daxes." | daxes | crundles | reachable_one_hop |
| 12 | " daxes." | daxes | crundles | reachable_one_hop |
## 061/broken/first/0

```text
All crundles are zorks.
All zorks are wugs.
All quavels are vibbles.
All daxes are vibbles.
Possible completions: wugs or vibbles.
Therefore, all crundles are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 061/broken/second/1

```text
All crundles are daxes.
All zorks are wugs.
All quavels are vibbles.
All daxes are wugs.
Possible completions: wugs or vibbles.
Therefore, all crundles are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | vibbles | reachable_one_hop |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 061/robustness/reorder/0

```text
All zorks are wugs.
All daxes are vibbles.
All quavels are vibbles.
All crundles are daxes.
Possible completions: wugs or vibbles.
Therefore, all crundles are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | wugs | reachable_one_hop |
| 4 | " daxes." | daxes | wugs | reachable_one_hop |
| 12 | " daxes." | daxes | vibbles | reachable_one_hop |
## 061/robustness/reorder/1

```text
All zorks are wugs.
All vibbles are daxes.
All daxes are crundles.
All quavels are crundles.
Possible completions: crundles or wugs.
Therefore, all vibbles are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | crundles | reachable_one_hop |
| 4 | " wugs." | wugs | wugs | wrong_candidate |
| 12 | " crundles." | crundles | crundles | correct_target |
## 061/robustness/distractors/0

```text
All zeltrons are prandils.
All crundles are daxes.
All daxes are vibbles.
All prandils are wugs.
All quavels are vibbles.
All zorks are wugs.
Possible completions: wugs or vibbles.
Therefore, all crundles are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | wugs | reachable_one_hop |
| 4 | " wugs." | wugs | wugs | wrong_candidate |
| 12 | " wugs." | wugs | wugs | wrong_candidate |
## 061/robustness/distractors/1

```text
All zorks are wugs.
All quavels are crundles.
All prandils are wugs.
All zeltrons are prandils.
All vibbles are daxes.
All daxes are crundles.
Possible completions: crundles or wugs.
Therefore, all vibbles are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | crundles | reachable_one_hop |
| 4 | " daxes." | daxes | crundles | reachable_one_hop |
| 12 | " daxes." | daxes | crundles | reachable_one_hop |
## 061/robustness/rename/0

```text
All kelbrins are snorps.
All grivaks are plinets.
All prandils are vromps.
All snorps are vromps.
Possible completions: plinets or vromps.
Therefore, all kelbrins are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | wrong_candidate |
| 4 | " snorps." | snorps | plinets | reachable_one_hop |
| 12 | " vromps." | vromps | vromps | correct_target |
## 061/robustness/rename/1

```text
All blickets are kelbrins.
All oskets are kelbrins.
All xandles are tivaks.
All nerps are oskets.
Possible completions: kelbrins or tivaks.
Therefore, all nerps are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | kelbrins | reachable_one_hop |
| 4 | " oskets." | oskets | kelbrins | reachable_one_hop |
| 12 | " oskets." | oskets | tivaks | reachable_one_hop |
## 062/direct/base/0

```text
All zorks are lomits.
All zemples are daxes.
All wugs are daxes.
All nerps are wugs.
Possible completions: wugs or lomits.
Therefore, all nerps are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 062/direct/base/1

```text
All zorks are lomits.
All zemples are daxes.
All wugs are daxes.
All nerps are wugs.
Possible completions: lomits or daxes.
Therefore, all wugs are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | wrong_candidate |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 062/twohop/base/0

```text
All zorks are lomits.
All zemples are daxes.
All wugs are daxes.
All nerps are wugs.
Possible completions: daxes or lomits.
Therefore, all nerps are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | daxes | reachable_one_hop |
| 4 | " wugs." | wugs | daxes | reachable_one_hop |
| 12 | " wugs." | wugs | daxes | reachable_one_hop |
## 062/twohop/base/1

```text
All zorks are lomits.
All wugs are nerps.
All daxes are wugs.
All zemples are nerps.
Possible completions: lomits or nerps.
Therefore, all daxes are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | lomits | reachable_one_hop |
| 4 | " wugs." | wugs | nerps | reachable_one_hop |
| 12 | " wugs." | wugs | nerps | reachable_one_hop |
## 062/broken/first/0

```text
All zorks are lomits.
All zemples are daxes.
All wugs are daxes.
All nerps are zorks.
Possible completions: daxes or lomits.
Therefore, all nerps are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | lomits | reachable_one_hop |
| 4 | " zorks." | zorks | lomits | reachable_one_hop |
| 12 | " zorks." | zorks | lomits | reachable_one_hop |
## 062/broken/second/1

```text
All zorks are lomits.
All zemples are daxes.
All wugs are lomits.
All nerps are wugs.
Possible completions: daxes or lomits.
Therefore, all nerps are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | daxes | reachable_one_hop |
| 4 | " wugs." | wugs | lomits | reachable_one_hop |
| 12 | " wugs." | wugs | lomits | reachable_one_hop |
## 062/robustness/reorder/0

```text
All zemples are daxes.
All zorks are lomits.
All wugs are daxes.
All nerps are wugs.
Possible completions: daxes or lomits.
Therefore, all nerps are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | daxes | reachable_one_hop |
| 4 | " wugs." | wugs | daxes | reachable_one_hop |
| 12 | " wugs." | wugs | daxes | reachable_one_hop |
## 062/robustness/reorder/1

```text
All zemples are nerps.
All zorks are lomits.
All wugs are nerps.
All daxes are wugs.
Possible completions: lomits or nerps.
Therefore, all daxes are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " wugs." | wugs | nerps | reachable_one_hop |
| 12 | " wugs." | wugs | nerps | reachable_one_hop |
## 062/robustness/distractors/0

```text
All nufrons are quavels.
All zemples are daxes.
All quavels are lomits.
All nerps are wugs.
All wugs are daxes.
All zorks are lomits.
Possible completions: daxes or lomits.
Therefore, all nerps are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | daxes | reachable_one_hop |
| 4 | " wugs." | wugs | lomits | reachable_one_hop |
| 12 | " lomits." | lomits | lomits | wrong_candidate |
## 062/robustness/distractors/1

```text
All wugs are nerps.
All zorks are lomits.
All quavels are lomits.
All daxes are wugs.
All nufrons are quavels.
All zemples are nerps.
Possible completions: lomits or nerps.
Therefore, all daxes are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | lomits | reachable_one_hop |
| 4 | " wugs." | wugs | nerps | reachable_one_hop |
| 12 | " nerps." | nerps | nerps | correct_target |
## 062/robustness/rename/0

```text
All shalds are helpons.
All crundles are vromps.
All brovets are vromps.
All ruspins are brovets.
Possible completions: vromps or helpons.
Therefore, all ruspins are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | vromps | correct_target |
| 4 | " brovets." | brovets | vromps | reachable_one_hop |
| 12 | " vromps." | vromps | vromps | correct_target |
## 062/robustness/rename/1

```text
All prandils are helpons.
All jastles are quavels.
All snorps are jastles.
All vromps are quavels.
Possible completions: helpons or quavels.
Therefore, all snorps are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | helpons | unreachable_fact_name |
| 4 | " vromps." | vromps | quavels | unreachable_fact_name |
| 12 | " vromps." | vromps | quavels | unreachable_fact_name |
## 063/direct/base/0

```text
All zorks are vibbles.
All ruspins are zorks.
All tivaks are sprocks.
All tufas are vibbles.
Possible completions: sprocks or zorks.
Therefore, all ruspins are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | zorks | unreachable_fact_name |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " zorks." | zorks | zorks | correct_target |
## 063/direct/base/1

```text
All zorks are vibbles.
All ruspins are zorks.
All tivaks are sprocks.
All tufas are vibbles.
Possible completions: vibbles or sprocks.
Therefore, all zorks are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 063/twohop/base/0

```text
All zorks are vibbles.
All ruspins are zorks.
All tivaks are sprocks.
All tufas are vibbles.
Possible completions: sprocks or vibbles.
Therefore, all ruspins are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " zorks." | zorks | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 063/twohop/base/1

```text
All vibbles are zorks.
All tivaks are sprocks.
All zorks are ruspins.
All tufas are ruspins.
Possible completions: ruspins or sprocks.
Therefore, all vibbles are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 12 | " sprocks." | sprocks | sprocks | wrong_candidate |
## 063/broken/first/0

```text
All zorks are vibbles.
All ruspins are tivaks.
All tivaks are sprocks.
All tufas are vibbles.
Possible completions: sprocks or vibbles.
Therefore, all ruspins are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | sprocks | unreachable_fact_name |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " tivaks." | tivaks | vibbles | reachable_one_hop |
## 063/broken/second/1

```text
All zorks are sprocks.
All ruspins are zorks.
All tivaks are sprocks.
All tufas are vibbles.
Possible completions: sprocks or vibbles.
Therefore, all ruspins are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | vibbles | unreachable_fact_name |
| 4 | " zorks." | zorks | vibbles | reachable_one_hop |
| 12 | " zorks." | zorks | vibbles | reachable_one_hop |
## 063/robustness/reorder/0

```text
All tufas are vibbles.
All zorks are vibbles.
All tivaks are sprocks.
All ruspins are zorks.
Possible completions: sprocks or vibbles.
Therefore, all ruspins are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | vibbles | wrong_candidate |
| 4 | " zorks." | zorks | vibbles | reachable_one_hop |
| 12 | " zorks." | zorks | vibbles | reachable_one_hop |
## 063/robustness/reorder/1

```text
All zorks are ruspins.
All tufas are ruspins.
All vibbles are zorks.
All tivaks are sprocks.
Possible completions: ruspins or sprocks.
Therefore, all vibbles are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | ruspins | reachable_one_hop |
| 4 | " zorks." | zorks | ruspins | reachable_one_hop |
| 12 | " zorks." | zorks | ruspins | reachable_one_hop |
## 063/robustness/distractors/0

```text
All tivaks are sprocks.
All ruspins are zorks.
All zorks are vibbles.
All yorbits are nerps.
All tufas are vibbles.
All nerps are sprocks.
Possible completions: sprocks or vibbles.
Therefore, all ruspins are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | sprocks | reachable_one_hop |
| 4 | " zorks." | zorks | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 063/robustness/distractors/1

```text
All zorks are ruspins.
All yorbits are nerps.
All tufas are ruspins.
All tivaks are sprocks.
All nerps are sprocks.
All vibbles are zorks.
Possible completions: ruspins or sprocks.
Therefore, all vibbles are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | ruspins | reachable_one_hop |
| 4 | " zorks." | zorks | ruspins | reachable_one_hop |
| 12 | " zorks." | zorks | ruspins | reachable_one_hop |
## 063/robustness/rename/0

```text
All jastles are crundles.
All daxes are jastles.
All plinets are prandils.
All vromps are crundles.
Possible completions: prandils or crundles.
Therefore, all daxes are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | prandils | reachable_one_hop |
| 4 | " jastles." | jastles | crundles | reachable_one_hop |
| 12 | " jastles." | jastles | crundles | reachable_one_hop |
## 063/robustness/rename/1

```text
All shalds are zemples.
All prandils are xandles.
All zemples are kelbrins.
All ulvets are kelbrins.
Possible completions: kelbrins or xandles.
Therefore, all shalds are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 064/direct/base/0

```text
All welbins are flomps.
All flomps are ruspins.
All korvas are vibbles.
All blickets are ruspins.
Possible completions: flomps or vibbles.
Therefore, all welbins are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " ruspins." | ruspins | flomps | other_reachable |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 064/direct/base/1

```text
All welbins are flomps.
All flomps are ruspins.
All korvas are vibbles.
All blickets are ruspins.
Possible completions: vibbles or ruspins.
Therefore, all flomps are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 064/twohop/base/0

```text
All welbins are flomps.
All flomps are ruspins.
All korvas are vibbles.
All blickets are ruspins.
Possible completions: ruspins or vibbles.
Therefore, all welbins are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 064/twohop/base/1

```text
All korvas are vibbles.
All ruspins are flomps.
All flomps are welbins.
All blickets are welbins.
Possible completions: vibbles or welbins.
Therefore, all ruspins are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " flomps." | flomps | vibbles | reachable_one_hop |
| 12 | " flomps." | flomps | vibbles | reachable_one_hop |
## 064/broken/first/0

```text
All welbins are korvas.
All flomps are ruspins.
All korvas are vibbles.
All blickets are ruspins.
Possible completions: ruspins or vibbles.
Therefore, all welbins are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 064/broken/second/1

```text
All welbins are flomps.
All flomps are vibbles.
All korvas are vibbles.
All blickets are ruspins.
Possible completions: ruspins or vibbles.
Therefore, all welbins are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 064/robustness/reorder/0

```text
All flomps are ruspins.
All blickets are ruspins.
All welbins are flomps.
All korvas are vibbles.
Possible completions: ruspins or vibbles.
Therefore, all welbins are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " flomps." | flomps | vibbles | reachable_one_hop |
## 064/robustness/reorder/1

```text
All flomps are welbins.
All korvas are vibbles.
All blickets are welbins.
All ruspins are flomps.
Possible completions: vibbles or welbins.
Therefore, all ruspins are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " flomps." | flomps | welbins | reachable_one_hop |
| 12 | " flomps." | flomps | vibbles | reachable_one_hop |
## 064/robustness/distractors/0

```text
All welbins are flomps.
All yorbits are vibbles.
All crundles are yorbits.
All korvas are vibbles.
All flomps are ruspins.
All blickets are ruspins.
Possible completions: ruspins or vibbles.
Therefore, all welbins are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " flomps." | flomps | ruspins | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 064/robustness/distractors/1

```text
All korvas are vibbles.
All ruspins are flomps.
All flomps are welbins.
All blickets are welbins.
All yorbits are vibbles.
All crundles are yorbits.
Possible completions: vibbles or welbins.
Therefore, all ruspins are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 064/robustness/rename/0

```text
All shalds are zorks.
All zorks are helpons.
All brovets are murdles.
All plinets are helpons.
Possible completions: helpons or murdles.
Therefore, all shalds are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | helpons | unreachable_fact_name |
| 4 | " zorks." | zorks | murdles | reachable_one_hop |
| 12 | " murdles." | murdles | murdles | wrong_candidate |
## 064/robustness/rename/1

```text
All shalds are murdles.
All nufrons are zemples.
All zemples are jastles.
All zorks are jastles.
Possible completions: murdles or jastles.
Therefore, all nufrons are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | jastles | unreachable_fact_name |
| 4 | " zemples." | zemples | jastles | reachable_one_hop |
| 12 | " jastles." | jastles | jastles | correct_target |
## 065/direct/base/0

```text
All ruspins are shalds.
All lomits are shalds.
All crundles are nerps.
All tufas are lomits.
Possible completions: nerps or lomits.
Therefore, all tufas are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | wrong_candidate |
| 4 | " lomits." | lomits | lomits | correct_target |
| 12 | " lomits." | lomits | lomits | correct_target |
## 065/direct/base/1

```text
All ruspins are shalds.
All lomits are shalds.
All crundles are nerps.
All tufas are lomits.
Possible completions: shalds or nerps.
Therefore, all lomits are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | correct_target |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 065/twohop/base/0

```text
All ruspins are shalds.
All lomits are shalds.
All crundles are nerps.
All tufas are lomits.
Possible completions: nerps or shalds.
Therefore, all tufas are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | nerps | reachable_one_hop |
| 4 | " lomits." | lomits | shalds | reachable_one_hop |
| 12 | " lomits." | lomits | shalds | reachable_one_hop |
## 065/twohop/base/1

```text
All lomits are tufas.
All ruspins are tufas.
All shalds are lomits.
All crundles are nerps.
Possible completions: tufas or nerps.
Therefore, all shalds are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | tufas | reachable_one_hop |
| 4 | " lomits." | lomits | tufas | reachable_one_hop |
| 12 | " lomits." | lomits | tufas | reachable_one_hop |
## 065/broken/first/0

```text
All ruspins are shalds.
All lomits are shalds.
All crundles are nerps.
All tufas are crundles.
Possible completions: nerps or shalds.
Therefore, all tufas are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " crundles." | crundles | shalds | reachable_one_hop |
| 12 | " crundles." | crundles | shalds | reachable_one_hop |
## 065/broken/second/1

```text
All ruspins are shalds.
All lomits are nerps.
All crundles are nerps.
All tufas are lomits.
Possible completions: nerps or shalds.
Therefore, all tufas are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | nerps | reachable_one_hop |
| 4 | " lomits." | lomits | nerps | reachable_one_hop |
| 12 | " lomits." | lomits | shalds | reachable_one_hop |
## 065/robustness/reorder/0

```text
All crundles are nerps.
All lomits are shalds.
All tufas are lomits.
All ruspins are shalds.
Possible completions: nerps or shalds.
Therefore, all tufas are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | nerps | unreachable_fact_name |
| 4 | " lomits." | lomits | shalds | reachable_one_hop |
| 12 | " lomits." | lomits | shalds | reachable_one_hop |
## 065/robustness/reorder/1

```text
All lomits are tufas.
All shalds are lomits.
All crundles are nerps.
All ruspins are tufas.
Possible completions: tufas or nerps.
Therefore, all shalds are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | tufas | reachable_one_hop |
| 4 | " lomits." | lomits | tufas | reachable_one_hop |
| 12 | " lomits." | lomits | tufas | reachable_one_hop |
## 065/robustness/distractors/0

```text
All crundles are nerps.
All lomits are shalds.
All flomps are nerps.
All ruspins are shalds.
All tivaks are flomps.
All tufas are lomits.
Possible completions: nerps or shalds.
Therefore, all tufas are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | nerps | reachable_one_hop |
| 4 | " lomits." | lomits | shalds | reachable_one_hop |
| 12 | " lomits." | lomits | shalds | reachable_one_hop |
## 065/robustness/distractors/1

```text
All crundles are nerps.
All ruspins are tufas.
All flomps are nerps.
All lomits are tufas.
All tivaks are flomps.
All shalds are lomits.
Possible completions: tufas or nerps.
Therefore, all shalds are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " lomits." | lomits | tufas | reachable_one_hop |
| 12 | " lomits." | lomits | tufas | reachable_one_hop |
## 065/robustness/rename/0

```text
All prandils are snorps.
All oskets are snorps.
All yorbits are grivaks.
All daxes are oskets.
Possible completions: grivaks or snorps.
Therefore, all daxes are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | grivaks | reachable_one_hop |
| 4 | " oskets." | oskets | snorps | reachable_one_hop |
| 12 | " oskets." | oskets | snorps | reachable_one_hop |
## 065/robustness/rename/1

```text
All zeltrons are sprocks.
All flomps are sprocks.
All welbins are zeltrons.
All zorks are vibbles.
Possible completions: sprocks or vibbles.
Therefore, all welbins are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | sprocks | reachable_one_hop |
| 4 | " zeltrons." | zeltrons | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 066/direct/base/0

```text
All murdles are sprocks.
All shalds are murdles.
All grivaks are sprocks.
All ulvets are nerps.
Possible completions: murdles or nerps.
Therefore, all shalds are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | nerps | unreachable_fact_name |
| 4 | " nerps." | nerps | nerps | wrong_candidate |
| 12 | " murdles." | murdles | murdles | correct_target |
## 066/direct/base/1

```text
All murdles are sprocks.
All shalds are murdles.
All grivaks are sprocks.
All ulvets are nerps.
Possible completions: nerps or sprocks.
Therefore, all murdles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 066/twohop/base/0

```text
All murdles are sprocks.
All shalds are murdles.
All grivaks are sprocks.
All ulvets are nerps.
Possible completions: sprocks or nerps.
Therefore, all shalds are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | nerps | unreachable_fact_name |
| 4 | " nerps." | nerps | nerps | wrong_candidate |
| 12 | " murdles." | murdles | sprocks | reachable_one_hop |
## 066/twohop/base/1

```text
All grivaks are shalds.
All murdles are shalds.
All ulvets are nerps.
All sprocks are murdles.
Possible completions: nerps or shalds.
Therefore, all sprocks are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | wrong_candidate |
| 4 | " murdles." | murdles | shalds | reachable_one_hop |
| 12 | " murdles." | murdles | shalds | reachable_one_hop |
## 066/broken/first/0

```text
All murdles are sprocks.
All shalds are ulvets.
All grivaks are sprocks.
All ulvets are nerps.
Possible completions: sprocks or nerps.
Therefore, all shalds are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | sprocks | unreachable_fact_name |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 066/broken/second/1

```text
All murdles are nerps.
All shalds are murdles.
All grivaks are sprocks.
All ulvets are nerps.
Possible completions: sprocks or nerps.
Therefore, all shalds are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | sprocks | unreachable_fact_name |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " murdles." | murdles | nerps | reachable_one_hop |
## 066/robustness/reorder/0

```text
All grivaks are sprocks.
All murdles are sprocks.
All shalds are murdles.
All ulvets are nerps.
Possible completions: sprocks or nerps.
Therefore, all shalds are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " murdles." | murdles | nerps | reachable_one_hop |
| 12 | " murdles." | murdles | nerps | reachable_one_hop |
## 066/robustness/reorder/1

```text
All grivaks are shalds.
All murdles are shalds.
All sprocks are murdles.
All ulvets are nerps.
Possible completions: nerps or shalds.
Therefore, all sprocks are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | nerps | unreachable_fact_name |
| 4 | " murdles." | murdles | nerps | reachable_one_hop |
| 12 | " murdles." | murdles | shalds | reachable_one_hop |
## 066/robustness/distractors/0

```text
All grivaks are sprocks.
All murdles are sprocks.
All zeltrons are ruspins.
All shalds are murdles.
All ulvets are nerps.
All ruspins are nerps.
Possible completions: sprocks or nerps.
Therefore, all shalds are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " nerps." | nerps | nerps | wrong_candidate |
| 12 | " nerps." | nerps | nerps | wrong_candidate |
## 066/robustness/distractors/1

```text
All grivaks are shalds.
All sprocks are murdles.
All zeltrons are ruspins.
All ruspins are nerps.
All ulvets are nerps.
All murdles are shalds.
Possible completions: nerps or shalds.
Therefore, all sprocks are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | shalds | unreachable_fact_name |
| 4 | " murdles." | murdles | nerps | reachable_one_hop |
| 12 | " murdles." | murdles | shalds | reachable_one_hop |
## 066/robustness/rename/0

```text
All oskets are nufrons.
All helpons are oskets.
All vibbles are nufrons.
All lomits are xandles.
Possible completions: nufrons or xandles.
Therefore, all helpons are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " xandles." | xandles | xandles | wrong_candidate |
| 12 | " xandles." | xandles | xandles | wrong_candidate |
## 066/robustness/rename/1

```text
All vibbles are blickets.
All quavels are blickets.
All tivaks are crundles.
All welbins are quavels.
Possible completions: crundles or blickets.
Therefore, all welbins are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | blickets | reachable_one_hop |
| 4 | " quavels." | quavels | blickets | reachable_one_hop |
| 12 | " blickets." | blickets | blickets | correct_target |
## 067/direct/base/0

```text
All welbins are vibbles.
All lomits are blickets.
All nufrons are quavels.
All vibbles are blickets.
Possible completions: quavels or vibbles.
Therefore, all welbins are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 067/direct/base/1

```text
All welbins are vibbles.
All lomits are blickets.
All nufrons are quavels.
All vibbles are blickets.
Possible completions: blickets or quavels.
Therefore, all vibbles are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | correct_target |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 067/twohop/base/0

```text
All welbins are vibbles.
All lomits are blickets.
All nufrons are quavels.
All vibbles are blickets.
Possible completions: quavels or blickets.
Therefore, all welbins are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | quavels | reachable_one_hop |
| 4 | " vibbles." | vibbles | blickets | reachable_one_hop |
| 12 | " vibbles." | vibbles | blickets | reachable_one_hop |
## 067/twohop/base/1

```text
All blickets are vibbles.
All lomits are welbins.
All vibbles are welbins.
All nufrons are quavels.
Possible completions: welbins or quavels.
Therefore, all blickets are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | quavels | reachable_one_hop |
| 4 | " vibbles." | vibbles | quavels | reachable_one_hop |
| 12 | " quavels." | quavels | quavels | wrong_candidate |
## 067/broken/first/0

```text
All welbins are nufrons.
All lomits are blickets.
All nufrons are quavels.
All vibbles are blickets.
Possible completions: quavels or blickets.
Therefore, all welbins are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | quavels | unreachable_fact_name |
| 4 | " blickets." | blickets | blickets | wrong_candidate |
| 12 | " blickets." | blickets | blickets | wrong_candidate |
## 067/broken/second/1

```text
All welbins are vibbles.
All lomits are blickets.
All nufrons are quavels.
All vibbles are quavels.
Possible completions: quavels or blickets.
Therefore, all welbins are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | correct_target |
| 4 | " vibbles." | vibbles | blickets | reachable_one_hop |
| 12 | " vibbles." | vibbles | blickets | reachable_one_hop |
## 067/robustness/reorder/0

```text
All lomits are blickets.
All nufrons are quavels.
All vibbles are blickets.
All welbins are vibbles.
Possible completions: quavels or blickets.
Therefore, all welbins are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | blickets | reachable_one_hop |
| 4 | " vibbles." | vibbles | blickets | reachable_one_hop |
| 12 | " vibbles." | vibbles | blickets | reachable_one_hop |
## 067/robustness/reorder/1

```text
All lomits are welbins.
All blickets are vibbles.
All vibbles are welbins.
All nufrons are quavels.
Possible completions: welbins or quavels.
Therefore, all blickets are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | welbins | unreachable_fact_name |
| 4 | " vibbles." | vibbles | quavels | reachable_one_hop |
| 12 | " nufrons." | nufrons | quavels | unreachable_fact_name |
## 067/robustness/distractors/0

```text
All daxes are crundles.
All crundles are quavels.
All lomits are blickets.
All nufrons are quavels.
All welbins are vibbles.
All vibbles are blickets.
Possible completions: quavels or blickets.
Therefore, all welbins are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | blickets | reachable_one_hop |
| 4 | " vibbles." | vibbles | blickets | reachable_one_hop |
| 12 | " vibbles." | vibbles | blickets | reachable_one_hop |
## 067/robustness/distractors/1

```text
All nufrons are quavels.
All lomits are welbins.
All daxes are crundles.
All blickets are vibbles.
All crundles are quavels.
All vibbles are welbins.
Possible completions: welbins or quavels.
Therefore, all blickets are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | quavels | reachable_one_hop |
| 4 | " vibbles." | vibbles | welbins | reachable_one_hop |
| 12 | " vibbles." | vibbles | welbins | reachable_one_hop |
## 067/robustness/rename/0

```text
All shalds are zorks.
All korvas are jastles.
All prandils are zeltrons.
All zorks are jastles.
Possible completions: zeltrons or jastles.
Therefore, all shalds are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | zeltrons | wrong_candidate |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 067/robustness/rename/1

```text
All jastles are crundles.
All ruspins are yorbits.
All crundles are yorbits.
All kelbrins are flomps.
Possible completions: yorbits or flomps.
Therefore, all jastles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " crundles." | crundles | flomps | reachable_one_hop |
| 4 | " flomps." | flomps | flomps | wrong_candidate |
| 12 | " flomps." | flomps | flomps | wrong_candidate |
## 068/direct/base/0

```text
All sprocks are welbins.
All xandles are brovets.
All oskets are sprocks.
All tivaks are welbins.
Possible completions: sprocks or brovets.
Therefore, all oskets are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 068/direct/base/1

```text
All sprocks are welbins.
All xandles are brovets.
All oskets are sprocks.
All tivaks are welbins.
Possible completions: brovets or welbins.
Therefore, all sprocks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " welbins." | welbins | welbins | correct_target |
| 12 | " welbins." | welbins | welbins | correct_target |
## 068/twohop/base/0

```text
All sprocks are welbins.
All xandles are brovets.
All oskets are sprocks.
All tivaks are welbins.
Possible completions: welbins or brovets.
Therefore, all oskets are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | welbins | reachable_one_hop |
| 4 | " sprocks." | sprocks | brovets | reachable_one_hop |
| 12 | " sprocks." | sprocks | welbins | reachable_one_hop |
## 068/twohop/base/1

```text
All welbins are sprocks.
All tivaks are oskets.
All xandles are brovets.
All sprocks are oskets.
Possible completions: brovets or oskets.
Therefore, all welbins are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | brovets | reachable_one_hop |
| 4 | " sprocks." | sprocks | brovets | reachable_one_hop |
| 12 | " sprocks." | sprocks | oskets | reachable_one_hop |
## 068/broken/first/0

```text
All sprocks are welbins.
All xandles are brovets.
All oskets are xandles.
All tivaks are welbins.
Possible completions: welbins or brovets.
Therefore, all oskets are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | welbins | unreachable_fact_name |
| 4 | " xandles." | xandles | welbins | reachable_one_hop |
| 12 | " xandles." | xandles | welbins | reachable_one_hop |
## 068/broken/second/1

```text
All sprocks are brovets.
All xandles are brovets.
All oskets are sprocks.
All tivaks are welbins.
Possible completions: welbins or brovets.
Therefore, all oskets are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | brovets | reachable_one_hop |
| 4 | " sprocks." | sprocks | brovets | reachable_one_hop |
| 12 | " sprocks." | sprocks | brovets | reachable_one_hop |
## 068/robustness/reorder/0

```text
All xandles are brovets.
All tivaks are welbins.
All oskets are sprocks.
All sprocks are welbins.
Possible completions: welbins or brovets.
Therefore, all oskets are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | welbins | reachable_one_hop |
| 4 | " brovets." | brovets | brovets | wrong_candidate |
| 12 | " sprocks." | sprocks | brovets | reachable_one_hop |
## 068/robustness/reorder/1

```text
All sprocks are oskets.
All xandles are brovets.
All welbins are sprocks.
All tivaks are oskets.
Possible completions: brovets or oskets.
Therefore, all welbins are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | brovets | reachable_one_hop |
| 4 | " sprocks." | sprocks | brovets | reachable_one_hop |
| 12 | " sprocks." | sprocks | brovets | reachable_one_hop |
## 068/robustness/distractors/0

```text
All oskets are sprocks.
All sprocks are welbins.
All ruspins are prandils.
All xandles are brovets.
All tivaks are welbins.
All prandils are brovets.
Possible completions: welbins or brovets.
Therefore, all oskets are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | brovets | reachable_one_hop |
| 4 | " brovets." | brovets | brovets | wrong_candidate |
| 12 | " brovets." | brovets | brovets | wrong_candidate |
## 068/robustness/distractors/1

```text
All prandils are brovets.
All tivaks are oskets.
All xandles are brovets.
All welbins are sprocks.
All sprocks are oskets.
All ruspins are prandils.
Possible completions: brovets or oskets.
Therefore, all welbins are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | brovets | reachable_one_hop |
| 4 | " prandils." | prandils | brovets | unreachable_fact_name |
| 12 | " sprocks." | sprocks | brovets | reachable_one_hop |
## 068/robustness/rename/0

```text
All yorbits are crundles.
All tufas are jastles.
All flomps are yorbits.
All nerps are crundles.
Possible completions: crundles or jastles.
Therefore, all flomps are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | jastles | reachable_one_hop |
| 4 | " yorbits." | yorbits | jastles | reachable_one_hop |
| 12 | " yorbits." | yorbits | jastles | reachable_one_hop |
## 068/robustness/rename/1

```text
All tufas are nerps.
All blickets are zeltrons.
All zorks are daxes.
All nerps are zeltrons.
Possible completions: daxes or zeltrons.
Therefore, all tufas are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " nerps." | nerps | zeltrons | reachable_one_hop |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 069/direct/base/0

```text
All jastles are ruspins.
All flomps are shalds.
All lomits are flomps.
All zemples are shalds.
Possible completions: ruspins or flomps.
Therefore, all lomits are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | flomps | unreachable_fact_name |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " flomps." | flomps | flomps | correct_target |
## 069/direct/base/1

```text
All jastles are ruspins.
All flomps are shalds.
All lomits are flomps.
All zemples are shalds.
Possible completions: shalds or ruspins.
Therefore, all flomps are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | correct_target |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " shalds." | shalds | shalds | correct_target |
## 069/twohop/base/0

```text
All jastles are ruspins.
All flomps are shalds.
All lomits are flomps.
All zemples are shalds.
Possible completions: ruspins or shalds.
Therefore, all lomits are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | ruspins | unreachable_fact_name |
| 4 | " flomps." | flomps | shalds | reachable_one_hop |
| 12 | " flomps." | flomps | shalds | reachable_one_hop |
## 069/twohop/base/1

```text
All shalds are flomps.
All zemples are lomits.
All jastles are ruspins.
All flomps are lomits.
Possible completions: lomits or ruspins.
Therefore, all shalds are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | lomits | reachable_one_hop |
| 4 | " flomps." | flomps | lomits | reachable_one_hop |
| 12 | " lomits." | lomits | lomits | correct_target |
## 069/broken/first/0

```text
All jastles are ruspins.
All flomps are shalds.
All lomits are jastles.
All zemples are shalds.
Possible completions: ruspins or shalds.
Therefore, all lomits are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | ruspins | reachable_one_hop |
| 4 | " jastles." | jastles | ruspins | reachable_one_hop |
| 12 | " jastles." | jastles | ruspins | reachable_one_hop |
## 069/broken/second/1

```text
All jastles are ruspins.
All flomps are ruspins.
All lomits are flomps.
All zemples are shalds.
Possible completions: ruspins or shalds.
Therefore, all lomits are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | ruspins | unreachable_fact_name |
| 4 | " flomps." | flomps | shalds | reachable_one_hop |
| 12 | " flomps." | flomps | shalds | reachable_one_hop |
## 069/robustness/reorder/0

```text
All zemples are shalds.
All jastles are ruspins.
All flomps are shalds.
All lomits are flomps.
Possible completions: ruspins or shalds.
Therefore, all lomits are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | ruspins | reachable_one_hop |
| 4 | " flomps." | flomps | shalds | reachable_one_hop |
| 12 | " flomps." | flomps | ruspins | reachable_one_hop |
## 069/robustness/reorder/1

```text
All zemples are lomits.
All flomps are lomits.
All shalds are flomps.
All jastles are ruspins.
Possible completions: lomits or ruspins.
Therefore, all shalds are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | lomits | unreachable_fact_name |
| 4 | " flomps." | flomps | ruspins | reachable_one_hop |
| 12 | " flomps." | flomps | ruspins | reachable_one_hop |
## 069/robustness/distractors/0

```text
All snorps are ruspins.
All jastles are ruspins.
All zemples are shalds.
All flomps are shalds.
All prandils are snorps.
All lomits are flomps.
Possible completions: ruspins or shalds.
Therefore, all lomits are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 4 | " flomps." | flomps | ruspins | reachable_one_hop |
| 12 | " flomps." | flomps | ruspins | reachable_one_hop |
## 069/robustness/distractors/1

```text
All shalds are flomps.
All flomps are lomits.
All zemples are lomits.
All snorps are ruspins.
All prandils are snorps.
All jastles are ruspins.
Possible completions: lomits or ruspins.
Therefore, all shalds are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | ruspins | reachable_one_hop |
| 4 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 069/robustness/rename/0

```text
All kelbrins are helpons.
All oskets are quavels.
All murdles are oskets.
All vibbles are quavels.
Possible completions: helpons or quavels.
Therefore, all murdles are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | helpons | reachable_one_hop |
| 4 | " quavels." | quavels | quavels | correct_target |
| 12 | " quavels." | quavels | quavels | correct_target |
## 069/robustness/rename/1

```text
All wugs are vromps.
All crundles are brovets.
All vibbles are tufas.
All vromps are brovets.
Possible completions: brovets or tufas.
Therefore, all wugs are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | brovets | reachable_one_hop |
| 4 | " vromps." | vromps | brovets | reachable_one_hop |
| 12 | " tufas." | tufas | tufas | wrong_candidate |
## 070/direct/base/0

```text
All tufas are sprocks.
All daxes are tufas.
All helpons are oskets.
All flomps are sprocks.
Possible completions: tufas or oskets.
Therefore, all daxes are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | tufas | other_reachable |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 070/direct/base/1

```text
All tufas are sprocks.
All daxes are tufas.
All helpons are oskets.
All flomps are sprocks.
Possible completions: oskets or sprocks.
Therefore, all tufas are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 070/twohop/base/0

```text
All tufas are sprocks.
All daxes are tufas.
All helpons are oskets.
All flomps are sprocks.
Possible completions: sprocks or oskets.
Therefore, all daxes are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " tufas." | tufas | sprocks | reachable_one_hop |
| 12 | " tufas." | tufas | sprocks | reachable_one_hop |
## 070/twohop/base/1

```text
All helpons are oskets.
All tufas are daxes.
All flomps are daxes.
All sprocks are tufas.
Possible completions: oskets or daxes.
Therefore, all sprocks are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " tufas." | tufas | daxes | reachable_one_hop |
| 12 | " tufas." | tufas | daxes | reachable_one_hop |
## 070/broken/first/0

```text
All tufas are sprocks.
All daxes are helpons.
All helpons are oskets.
All flomps are sprocks.
Possible completions: sprocks or oskets.
Therefore, all daxes are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " helpons." | helpons | sprocks | reachable_one_hop |
| 12 | " sprocks." | sprocks | sprocks | wrong_candidate |
## 070/broken/second/1

```text
All tufas are oskets.
All daxes are tufas.
All helpons are oskets.
All flomps are sprocks.
Possible completions: sprocks or oskets.
Therefore, all daxes are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " tufas." | tufas | oskets | reachable_one_hop |
| 12 | " tufas." | tufas | oskets | reachable_one_hop |
## 070/robustness/reorder/0

```text
All tufas are sprocks.
All helpons are oskets.
All daxes are tufas.
All flomps are sprocks.
Possible completions: sprocks or oskets.
Therefore, all daxes are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | sprocks | reachable_one_hop |
| 4 | " tufas." | tufas | sprocks | reachable_one_hop |
| 12 | " tufas." | tufas | sprocks | reachable_one_hop |
## 070/robustness/reorder/1

```text
All sprocks are tufas.
All flomps are daxes.
All tufas are daxes.
All helpons are oskets.
Possible completions: oskets or daxes.
Therefore, all sprocks are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " tufas." | tufas | daxes | reachable_one_hop |
| 12 | " daxes." | daxes | daxes | correct_target |
## 070/robustness/distractors/0

```text
All flomps are sprocks.
All tufas are sprocks.
All ruspins are nufrons.
All daxes are tufas.
All helpons are oskets.
All nufrons are oskets.
Possible completions: sprocks or oskets.
Therefore, all daxes are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " tufas." | tufas | oskets | reachable_one_hop |
| 12 | " tufas." | tufas | oskets | reachable_one_hop |
## 070/robustness/distractors/1

```text
All helpons are oskets.
All sprocks are tufas.
All tufas are daxes.
All flomps are daxes.
All ruspins are nufrons.
All nufrons are oskets.
Possible completions: oskets or daxes.
Therefore, all sprocks are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " tufas." | tufas | daxes | reachable_one_hop |
| 12 | " tufas." | tufas | daxes | reachable_one_hop |
## 070/robustness/rename/0

```text
All korvas are grivaks.
All yorbits are korvas.
All zeltrons are ruspins.
All xandles are grivaks.
Possible completions: grivaks or ruspins.
Therefore, all yorbits are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | correct_target |
| 4 | " korvas." | korvas | ruspins | reachable_one_hop |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 070/robustness/rename/1

```text
All yorbits are snorps.
All vibbles are plinets.
All zorks are plinets.
All crundles are vibbles.
Possible completions: snorps or plinets.
Therefore, all crundles are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | snorps | reachable_one_hop |
| 4 | " vibbles." | vibbles | plinets | reachable_one_hop |
| 12 | " vibbles." | vibbles | plinets | reachable_one_hop |
## 071/direct/base/0

```text
All helpons are vromps.
All blickets are tivaks.
All daxes are zemples.
All tivaks are vromps.
Possible completions: zemples or tivaks.
Therefore, all blickets are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | zemples | other_reachable |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 071/direct/base/1

```text
All helpons are vromps.
All blickets are tivaks.
All daxes are zemples.
All tivaks are vromps.
Possible completions: vromps or zemples.
Therefore, all tivaks are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | vromps | correct_target |
| 4 | " vromps." | vromps | vromps | correct_target |
| 12 | " vromps." | vromps | vromps | correct_target |
## 071/twohop/base/0

```text
All helpons are vromps.
All blickets are tivaks.
All daxes are zemples.
All tivaks are vromps.
Possible completions: zemples or vromps.
Therefore, all blickets are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | zemples | reachable_one_hop |
| 4 | " tivaks." | tivaks | vromps | reachable_one_hop |
| 12 | " vromps." | vromps | vromps | correct_target |
## 071/twohop/base/1

```text
All tivaks are blickets.
All vromps are tivaks.
All helpons are blickets.
All daxes are zemples.
Possible completions: blickets or zemples.
Therefore, all vromps are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | correct_target |
| 4 | " tivaks." | tivaks | blickets | reachable_one_hop |
| 12 | " tivaks." | tivaks | zemples | reachable_one_hop |
## 071/broken/first/0

```text
All helpons are vromps.
All blickets are daxes.
All daxes are zemples.
All tivaks are vromps.
Possible completions: zemples or vromps.
Therefore, all blickets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | zemples | reachable_one_hop |
| 4 | " vromps." | vromps | vromps | wrong_candidate |
| 12 | " vromps." | vromps | vromps | wrong_candidate |
## 071/broken/second/1

```text
All helpons are vromps.
All blickets are tivaks.
All daxes are zemples.
All tivaks are zemples.
Possible completions: zemples or vromps.
Therefore, all blickets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | zemples | reachable_one_hop |
| 4 | " tivaks." | tivaks | vromps | reachable_one_hop |
| 12 | " tivaks." | tivaks | vromps | reachable_one_hop |
## 071/robustness/reorder/0

```text
All blickets are tivaks.
All helpons are vromps.
All tivaks are vromps.
All daxes are zemples.
Possible completions: zemples or vromps.
Therefore, all blickets are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | zemples | wrong_candidate |
| 4 | " tivaks." | tivaks | vromps | reachable_one_hop |
| 12 | " vromps." | vromps | vromps | correct_target |
## 071/robustness/reorder/1

```text
All helpons are blickets.
All daxes are zemples.
All tivaks are blickets.
All vromps are tivaks.
Possible completions: blickets or zemples.
Therefore, all vromps are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | correct_target |
| 4 | " tivaks." | tivaks | blickets | reachable_one_hop |
| 12 | " tivaks." | tivaks | blickets | reachable_one_hop |
## 071/robustness/distractors/0

```text
All helpons are vromps.
All xandles are snorps.
All snorps are zemples.
All daxes are zemples.
All tivaks are vromps.
All blickets are tivaks.
Possible completions: zemples or vromps.
Therefore, all blickets are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | vromps | correct_target |
| 4 | " tivaks." | tivaks | vromps | reachable_one_hop |
| 12 | " tivaks." | tivaks | vromps | reachable_one_hop |
## 071/robustness/distractors/1

```text
All xandles are snorps.
All snorps are zemples.
All daxes are zemples.
All vromps are tivaks.
All helpons are blickets.
All tivaks are blickets.
Possible completions: blickets or zemples.
Therefore, all vromps are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | blickets | reachable_one_hop |
| 4 | " tivaks." | tivaks | blickets | reachable_one_hop |
| 12 | " tivaks." | tivaks | blickets | reachable_one_hop |
## 071/robustness/rename/0

```text
All korvas are brovets.
All nerps are grivaks.
All vibbles are prandils.
All grivaks are brovets.
Possible completions: prandils or brovets.
Therefore, all nerps are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | prandils | reachable_one_hop |
| 4 | " brovets." | brovets | brovets | correct_target |
| 12 | " brovets." | brovets | brovets | correct_target |
## 071/robustness/rename/1

```text
All ruspins are zorks.
All crundles are ruspins.
All jastles are zorks.
All oskets are welbins.
Possible completions: zorks or welbins.
Therefore, all crundles are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | zorks | reachable_one_hop |
| 4 | " ruspins." | ruspins | zorks | reachable_one_hop |
| 12 | " zorks." | zorks | zorks | correct_target |
## 072/direct/base/0

```text
All xandles are wugs.
All quavels are wugs.
All zorks are kelbrins.
All plinets are xandles.
Possible completions: xandles or kelbrins.
Therefore, all plinets are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | xandles | correct_target |
| 4 | " xandles." | xandles | xandles | correct_target |
| 12 | " xandles." | xandles | xandles | correct_target |
## 072/direct/base/1

```text
All xandles are wugs.
All quavels are wugs.
All zorks are kelbrins.
All plinets are xandles.
Possible completions: kelbrins or wugs.
Therefore, all xandles are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 072/twohop/base/0

```text
All xandles are wugs.
All quavels are wugs.
All zorks are kelbrins.
All plinets are xandles.
Possible completions: wugs or kelbrins.
Therefore, all plinets are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " xandles." | xandles | wugs | reachable_one_hop |
| 12 | " xandles." | xandles | wugs | reachable_one_hop |
## 072/twohop/base/1

```text
All zorks are kelbrins.
All quavels are plinets.
All wugs are xandles.
All xandles are plinets.
Possible completions: kelbrins or plinets.
Therefore, all wugs are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | plinets | reachable_one_hop |
| 4 | " plinets." | plinets | plinets | correct_target |
| 12 | " plinets." | plinets | plinets | correct_target |
## 072/broken/first/0

```text
All xandles are wugs.
All quavels are wugs.
All zorks are kelbrins.
All plinets are zorks.
Possible completions: wugs or kelbrins.
Therefore, all plinets are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | wugs | reachable_one_hop |
| 4 | " zorks." | zorks | kelbrins | reachable_one_hop |
| 12 | " zorks." | zorks | kelbrins | reachable_one_hop |
## 072/broken/second/1

```text
All xandles are kelbrins.
All quavels are wugs.
All zorks are kelbrins.
All plinets are xandles.
Possible completions: wugs or kelbrins.
Therefore, all plinets are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | wrong_candidate |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 072/robustness/reorder/0

```text
All zorks are kelbrins.
All quavels are wugs.
All xandles are wugs.
All plinets are xandles.
Possible completions: wugs or kelbrins.
Therefore, all plinets are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " xandles." | xandles | kelbrins | reachable_one_hop |
| 12 | " xandles." | xandles | wugs | reachable_one_hop |
## 072/robustness/reorder/1

```text
All xandles are plinets.
All zorks are kelbrins.
All quavels are plinets.
All wugs are xandles.
Possible completions: kelbrins or plinets.
Therefore, all wugs are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 4 | " plinets." | plinets | plinets | correct_target |
| 12 | " plinets." | plinets | plinets | correct_target |
## 072/robustness/distractors/0

```text
All zemples are shalds.
All zorks are kelbrins.
All plinets are xandles.
All xandles are wugs.
All quavels are wugs.
All shalds are kelbrins.
Possible completions: wugs or kelbrins.
Therefore, all plinets are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | wugs | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 12 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
## 072/robustness/distractors/1

```text
All quavels are plinets.
All wugs are xandles.
All xandles are plinets.
All zorks are kelbrins.
All shalds are kelbrins.
All zemples are shalds.
Possible completions: kelbrins or plinets.
Therefore, all wugs are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | kelbrins | reachable_one_hop |
| 4 | " plinets." | plinets | plinets | correct_target |
| 12 | " plinets." | plinets | plinets | correct_target |
## 072/robustness/rename/0

```text
All welbins are vromps.
All snorps are vromps.
All prandils are crundles.
All grivaks are welbins.
Possible completions: vromps or crundles.
Therefore, all grivaks are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | vromps | correct_target |
| 4 | " welbins." | welbins | vromps | reachable_one_hop |
| 12 | " welbins." | welbins | vromps | reachable_one_hop |
## 072/robustness/rename/1

```text
All flomps are tufas.
All sprocks are ruspins.
All tivaks are yorbits.
All yorbits are ruspins.
Possible completions: tufas or ruspins.
Therefore, all tivaks are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | ruspins | reachable_one_hop |
| 4 | " yorbits." | yorbits | ruspins | reachable_one_hop |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 073/direct/base/0

```text
All sprocks are prandils.
All vibbles are yorbits.
All prandils are yorbits.
All shalds are welbins.
Possible completions: welbins or prandils.
Therefore, all sprocks are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | correct_target |
| 4 | " prandils." | prandils | prandils | correct_target |
| 12 | " prandils." | prandils | prandils | correct_target |
## 073/direct/base/1

```text
All sprocks are prandils.
All vibbles are yorbits.
All prandils are yorbits.
All shalds are welbins.
Possible completions: yorbits or welbins.
Therefore, all prandils are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | yorbits | correct_target |
| 4 | " yorbits." | yorbits | yorbits | correct_target |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 073/twohop/base/0

```text
All sprocks are prandils.
All vibbles are yorbits.
All prandils are yorbits.
All shalds are welbins.
Possible completions: welbins or yorbits.
Therefore, all sprocks are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | wrong_candidate |
| 4 | " prandils." | prandils | yorbits | reachable_one_hop |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 073/twohop/base/1

```text
All shalds are welbins.
All prandils are sprocks.
All yorbits are prandils.
All vibbles are sprocks.
Possible completions: sprocks or welbins.
Therefore, all yorbits are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " prandils." | prandils | sprocks | reachable_one_hop |
| 12 | " prandils." | prandils | sprocks | reachable_one_hop |
## 073/broken/first/0

```text
All sprocks are shalds.
All vibbles are yorbits.
All prandils are yorbits.
All shalds are welbins.
Possible completions: welbins or yorbits.
Therefore, all sprocks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " shalds." | shalds | yorbits | reachable_one_hop |
| 12 | " yorbits." | yorbits | yorbits | wrong_candidate |
## 073/broken/second/1

```text
All sprocks are prandils.
All vibbles are yorbits.
All prandils are welbins.
All shalds are welbins.
Possible completions: welbins or yorbits.
Therefore, all sprocks are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | yorbits | reachable_one_hop |
| 4 | " prandils." | prandils | yorbits | reachable_one_hop |
| 12 | " prandils." | prandils | yorbits | reachable_one_hop |
## 073/robustness/reorder/0

```text
All prandils are yorbits.
All shalds are welbins.
All vibbles are yorbits.
All sprocks are prandils.
Possible completions: welbins or yorbits.
Therefore, all sprocks are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | yorbits | reachable_one_hop |
| 4 | " prandils." | prandils | yorbits | reachable_one_hop |
| 12 | " prandils." | prandils | yorbits | reachable_one_hop |
## 073/robustness/reorder/1

```text
All prandils are sprocks.
All vibbles are sprocks.
All yorbits are prandils.
All shalds are welbins.
Possible completions: sprocks or welbins.
Therefore, all yorbits are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " prandils." | prandils | sprocks | reachable_one_hop |
| 12 | " prandils." | prandils | sprocks | reachable_one_hop |
## 073/robustness/distractors/0

```text
All vibbles are yorbits.
All crundles are welbins.
All daxes are crundles.
All prandils are yorbits.
All sprocks are prandils.
All shalds are welbins.
Possible completions: welbins or yorbits.
Therefore, all sprocks are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | yorbits | unreachable_fact_name |
| 4 | " prandils." | prandils | welbins | reachable_one_hop |
| 12 | " prandils." | prandils | yorbits | reachable_one_hop |
## 073/robustness/distractors/1

```text
All crundles are welbins.
All vibbles are sprocks.
All yorbits are prandils.
All daxes are crundles.
All prandils are sprocks.
All shalds are welbins.
Possible completions: sprocks or welbins.
Therefore, all yorbits are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | sprocks | reachable_one_hop |
| 4 | " prandils." | prandils | sprocks | reachable_one_hop |
| 12 | " prandils." | prandils | sprocks | reachable_one_hop |
## 073/robustness/rename/0

```text
All grivaks are tufas.
All zorks are zemples.
All tufas are zemples.
All brovets are blickets.
Possible completions: blickets or zemples.
Therefore, all grivaks are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | wrong_candidate |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 073/robustness/rename/1

```text
All korvas are ruspins.
All snorps are brovets.
All plinets are snorps.
All oskets are brovets.
Possible completions: brovets or ruspins.
Therefore, all plinets are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | ruspins | unreachable_fact_name |
| 4 | " snorps." | snorps | ruspins | reachable_one_hop |
| 12 | " ruspins." | ruspins | ruspins | wrong_candidate |
## 074/direct/base/0

```text
All shalds are snorps.
All nufrons are zemples.
All welbins are ulvets.
All zemples are snorps.
Possible completions: zemples or ulvets.
Therefore, all nufrons are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | zemples | other_reachable |
| 4 | " snorps." | snorps | zemples | other_reachable |
| 12 | " snorps." | snorps | zemples | other_reachable |
## 074/direct/base/1

```text
All shalds are snorps.
All nufrons are zemples.
All welbins are ulvets.
All zemples are snorps.
Possible completions: ulvets or snorps.
Therefore, all zemples are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | correct_target |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 074/twohop/base/0

```text
All shalds are snorps.
All nufrons are zemples.
All welbins are ulvets.
All zemples are snorps.
Possible completions: snorps or ulvets.
Therefore, all nufrons are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | snorps | reachable_one_hop |
| 4 | " zemples." | zemples | ulvets | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | correct_target |
## 074/twohop/base/1

```text
All welbins are ulvets.
All zemples are nufrons.
All shalds are nufrons.
All snorps are zemples.
Possible completions: ulvets or nufrons.
Therefore, all snorps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | ulvets | reachable_one_hop |
| 4 | " zemples." | zemples | nufrons | reachable_one_hop |
| 12 | " zemples." | zemples | nufrons | reachable_one_hop |
## 074/broken/first/0

```text
All shalds are snorps.
All nufrons are welbins.
All welbins are ulvets.
All zemples are snorps.
Possible completions: snorps or ulvets.
Therefore, all nufrons are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | snorps | unreachable_fact_name |
| 4 | " snorps." | snorps | snorps | wrong_candidate |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 074/broken/second/1

```text
All shalds are snorps.
All nufrons are zemples.
All welbins are ulvets.
All zemples are ulvets.
Possible completions: snorps or ulvets.
Therefore, all nufrons are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | snorps | reachable_one_hop |
| 4 | " ulvets." | ulvets | ulvets | correct_target |
| 12 | " ulvets." | ulvets | ulvets | correct_target |
## 074/robustness/reorder/0

```text
All welbins are ulvets.
All zemples are snorps.
All shalds are snorps.
All nufrons are zemples.
Possible completions: snorps or ulvets.
Therefore, all nufrons are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | snorps | reachable_one_hop |
| 4 | " zemples." | zemples | snorps | reachable_one_hop |
| 12 | " zemples." | zemples | snorps | reachable_one_hop |
## 074/robustness/reorder/1

```text
All zemples are nufrons.
All welbins are ulvets.
All snorps are zemples.
All shalds are nufrons.
Possible completions: ulvets or nufrons.
Therefore, all snorps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 4 | " zemples." | zemples | nufrons | reachable_one_hop |
| 12 | " zemples." | zemples | nufrons | reachable_one_hop |
## 074/robustness/distractors/0

```text
All nufrons are zemples.
All zemples are snorps.
All shalds are snorps.
All welbins are ulvets.
All tivaks are wugs.
All wugs are ulvets.
Possible completions: snorps or ulvets.
Therefore, all nufrons are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | snorps | reachable_one_hop |
| 4 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 12 | " ulvets." | ulvets | ulvets | wrong_candidate |
## 074/robustness/distractors/1

```text
All snorps are zemples.
All shalds are nufrons.
All wugs are ulvets.
All welbins are ulvets.
All zemples are nufrons.
All tivaks are wugs.
Possible completions: ulvets or nufrons.
Therefore, all snorps are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | ulvets | reachable_one_hop |
| 4 | " zemples." | zemples | nufrons | reachable_one_hop |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 074/robustness/rename/0

```text
All brovets are zorks.
All prandils are daxes.
All flomps are plinets.
All daxes are zorks.
Possible completions: zorks or plinets.
Therefore, all prandils are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " daxes." | daxes | zorks | reachable_one_hop |
| 12 | " plinets." | plinets | plinets | wrong_candidate |
## 074/robustness/rename/1

```text
All crundles are plinets.
All tufas are vibbles.
All daxes are vibbles.
All grivaks are tufas.
Possible completions: plinets or vibbles.
Therefore, all grivaks are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | wrong_candidate |
| 4 | " tufas." | tufas | plinets | reachable_one_hop |
| 12 | " tufas." | tufas | plinets | reachable_one_hop |
## 075/direct/base/0

```text
All snorps are sprocks.
All sprocks are wugs.
All blickets are welbins.
All daxes are wugs.
Possible completions: welbins or sprocks.
Therefore, all snorps are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | wrong_candidate |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 075/direct/base/1

```text
All snorps are sprocks.
All sprocks are wugs.
All blickets are welbins.
All daxes are wugs.
Possible completions: wugs or welbins.
Therefore, all sprocks are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 075/twohop/base/0

```text
All snorps are sprocks.
All sprocks are wugs.
All blickets are welbins.
All daxes are wugs.
Possible completions: welbins or wugs.
Therefore, all snorps are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | wrong_candidate |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 075/twohop/base/1

```text
All daxes are snorps.
All wugs are sprocks.
All blickets are welbins.
All sprocks are snorps.
Possible completions: snorps or welbins.
Therefore, all wugs are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | snorps | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 075/broken/first/0

```text
All snorps are blickets.
All sprocks are wugs.
All blickets are welbins.
All daxes are wugs.
Possible completions: welbins or wugs.
Therefore, all snorps are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " wugs." | wugs | wugs | wrong_candidate |
| 12 | " wugs." | wugs | wugs | wrong_candidate |
## 075/broken/second/1

```text
All snorps are sprocks.
All sprocks are welbins.
All blickets are welbins.
All daxes are wugs.
Possible completions: welbins or wugs.
Therefore, all snorps are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | wrong_candidate |
| 4 | " wugs." | wugs | wugs | wrong_candidate |
| 12 | " wugs." | wugs | wugs | wrong_candidate |
## 075/robustness/reorder/0

```text
All daxes are wugs.
All blickets are welbins.
All sprocks are wugs.
All snorps are sprocks.
Possible completions: welbins or wugs.
Therefore, all snorps are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | wrong_candidate |
| 4 | " sprocks." | sprocks | wugs | reachable_one_hop |
| 12 | " sprocks." | sprocks | wugs | reachable_one_hop |
## 075/robustness/reorder/1

```text
All wugs are sprocks.
All sprocks are snorps.
All daxes are snorps.
All blickets are welbins.
Possible completions: snorps or welbins.
Therefore, all wugs are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | correct_target |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 075/robustness/distractors/0

```text
All sprocks are wugs.
All jastles are welbins.
All snorps are sprocks.
All blickets are welbins.
All daxes are wugs.
All ulvets are jastles.
Possible completions: welbins or wugs.
Therefore, all snorps are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | wugs | reachable_one_hop |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 075/robustness/distractors/1

```text
All ulvets are jastles.
All blickets are welbins.
All wugs are sprocks.
All sprocks are snorps.
All jastles are welbins.
All daxes are snorps.
Possible completions: snorps or welbins.
Therefore, all wugs are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | snorps | correct_target |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 075/robustness/rename/0

```text
All zorks are vromps.
All vromps are nufrons.
All oskets are shalds.
All kelbrins are nufrons.
Possible completions: shalds or nufrons.
Therefore, all zorks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 075/robustness/rename/1

```text
All yorbits are nufrons.
All brovets are nerps.
All xandles are helpons.
All nerps are nufrons.
Possible completions: nufrons or helpons.
Therefore, all brovets are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | nufrons | unreachable_fact_name |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 076/direct/base/0

```text
All daxes are jastles.
All jastles are oskets.
All tivaks are vibbles.
All wugs are oskets.
Possible completions: jastles or vibbles.
Therefore, all daxes are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 076/direct/base/1

```text
All daxes are jastles.
All jastles are oskets.
All tivaks are vibbles.
All wugs are oskets.
Possible completions: vibbles or oskets.
Therefore, all jastles are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " oskets." | oskets | oskets | correct_target |
## 076/twohop/base/0

```text
All daxes are jastles.
All jastles are oskets.
All tivaks are vibbles.
All wugs are oskets.
Possible completions: oskets or vibbles.
Therefore, all daxes are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 076/twohop/base/1

```text
All wugs are daxes.
All tivaks are vibbles.
All jastles are daxes.
All oskets are jastles.
Possible completions: vibbles or daxes.
Therefore, all oskets are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | daxes | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 076/broken/first/0

```text
All daxes are tivaks.
All jastles are oskets.
All tivaks are vibbles.
All wugs are oskets.
Possible completions: oskets or vibbles.
Therefore, all daxes are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " tivaks." | tivaks | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 076/broken/second/1

```text
All daxes are jastles.
All jastles are vibbles.
All tivaks are vibbles.
All wugs are oskets.
Possible completions: oskets or vibbles.
Therefore, all daxes are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 076/robustness/reorder/0

```text
All tivaks are vibbles.
All daxes are jastles.
All wugs are oskets.
All jastles are oskets.
Possible completions: oskets or vibbles.
Therefore, all daxes are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | vibbles | reachable_one_hop |
| 4 | " jastles." | jastles | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 076/robustness/reorder/1

```text
All tivaks are vibbles.
All jastles are daxes.
All wugs are daxes.
All oskets are jastles.
Possible completions: vibbles or daxes.
Therefore, all oskets are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | vibbles | reachable_one_hop |
| 4 | " jastles." | jastles | daxes | reachable_one_hop |
| 12 | " jastles." | jastles | daxes | reachable_one_hop |
## 076/robustness/distractors/0

```text
All tivaks are vibbles.
All wugs are oskets.
All murdles are kelbrins.
All kelbrins are vibbles.
All daxes are jastles.
All jastles are oskets.
Possible completions: oskets or vibbles.
Therefore, all daxes are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | oskets | reachable_one_hop |
| 4 | " jastles." | jastles | oskets | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 076/robustness/distractors/1

```text
All jastles are daxes.
All wugs are daxes.
All murdles are kelbrins.
All kelbrins are vibbles.
All oskets are jastles.
All tivaks are vibbles.
Possible completions: vibbles or daxes.
Therefore, all oskets are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | daxes | reachable_one_hop |
| 4 | " jastles." | jastles | daxes | reachable_one_hop |
| 12 | " daxes." | daxes | daxes | correct_target |
## 076/robustness/rename/0

```text
All helpons are blickets.
All blickets are shalds.
All prandils are vromps.
All yorbits are shalds.
Possible completions: shalds or vromps.
Therefore, all helpons are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | correct_target |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " vromps." | vromps | vromps | wrong_candidate |
## 076/robustness/rename/1

```text
All zemples are brovets.
All helpons are plinets.
All lomits are brovets.
All shalds are lomits.
Possible completions: plinets or brovets.
Therefore, all shalds are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | wrong_candidate |
| 4 | " lomits." | lomits | plinets | reachable_one_hop |
| 12 | " lomits." | lomits | plinets | reachable_one_hop |
## 077/direct/base/0

```text
All tufas are shalds.
All shalds are zorks.
All zemples are zorks.
All prandils are xandles.
Possible completions: xandles or shalds.
Therefore, all tufas are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | xandles | unreachable_fact_name |
| 4 | " shalds." | shalds | shalds | correct_target |
| 12 | " shalds." | shalds | shalds | correct_target |
## 077/direct/base/1

```text
All tufas are shalds.
All shalds are zorks.
All zemples are zorks.
All prandils are xandles.
Possible completions: zorks or xandles.
Therefore, all shalds are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | zorks | unreachable_fact_name |
| 4 | " zorks." | zorks | zorks | correct_target |
| 12 | " zorks." | zorks | zorks | correct_target |
## 077/twohop/base/0

```text
All tufas are shalds.
All shalds are zorks.
All zemples are zorks.
All prandils are xandles.
Possible completions: xandles or zorks.
Therefore, all tufas are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | xandles | correct_target |
| 4 | " shalds." | shalds | zorks | reachable_one_hop |
| 12 | " zorks." | zorks | zorks | correct_target |
## 077/twohop/base/1

```text
All zorks are shalds.
All zemples are tufas.
All shalds are tufas.
All prandils are xandles.
Possible completions: tufas or xandles.
Therefore, all zorks are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | tufas | reachable_one_hop |
| 4 | " shalds." | shalds | xandles | reachable_one_hop |
| 12 | " shalds." | shalds | tufas | reachable_one_hop |
## 077/broken/first/0

```text
All tufas are prandils.
All shalds are zorks.
All zemples are zorks.
All prandils are xandles.
Possible completions: xandles or zorks.
Therefore, all tufas are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | xandles | reachable_one_hop |
| 4 | " prandils." | prandils | zorks | reachable_one_hop |
| 12 | " prandils." | prandils | zorks | reachable_one_hop |
## 077/broken/second/1

```text
All tufas are shalds.
All shalds are xandles.
All zemples are zorks.
All prandils are xandles.
Possible completions: xandles or zorks.
Therefore, all tufas are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | zorks | unreachable_fact_name |
| 4 | " zorks." | zorks | zorks | wrong_candidate |
| 12 | " shalds." | shalds | zorks | reachable_one_hop |
## 077/robustness/reorder/0

```text
All tufas are shalds.
All prandils are xandles.
All zemples are zorks.
All shalds are zorks.
Possible completions: xandles or zorks.
Therefore, all tufas are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | zorks | reachable_one_hop |
| 4 | " shalds." | shalds | zorks | reachable_one_hop |
| 12 | " shalds." | shalds | zorks | reachable_one_hop |
## 077/robustness/reorder/1

```text
All prandils are xandles.
All zemples are tufas.
All zorks are shalds.
All shalds are tufas.
Possible completions: tufas or xandles.
Therefore, all zorks are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " shalds." | shalds | tufas | reachable_one_hop |
| 12 | " tufas." | tufas | tufas | correct_target |
## 077/robustness/distractors/0

```text
All prandils are xandles.
All vibbles are xandles.
All tufas are shalds.
All wugs are vibbles.
All zemples are zorks.
All shalds are zorks.
Possible completions: xandles or zorks.
Therefore, all tufas are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | zorks | reachable_one_hop |
| 4 | " shalds." | shalds | zorks | reachable_one_hop |
| 12 | " shalds." | shalds | zorks | reachable_one_hop |
## 077/robustness/distractors/1

```text
All zorks are shalds.
All shalds are tufas.
All vibbles are xandles.
All prandils are xandles.
All wugs are vibbles.
All zemples are tufas.
Possible completions: tufas or xandles.
Therefore, all zorks are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | tufas | reachable_one_hop |
| 4 | " shalds." | shalds | tufas | reachable_one_hop |
| 12 | " tufas." | tufas | tufas | correct_target |
## 077/robustness/rename/0

```text
All quavels are korvas.
All korvas are flomps.
All sprocks are flomps.
All jastles are crundles.
Possible completions: crundles or flomps.
Therefore, all quavels are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | crundles | unreachable_fact_name |
| 4 | " korvas." | korvas | flomps | reachable_one_hop |
| 12 | " flomps." | flomps | flomps | correct_target |
## 077/robustness/rename/1

```text
All crundles are flomps.
All daxes are quavels.
All flomps are quavels.
All welbins are blickets.
Possible completions: quavels or blickets.
Therefore, all crundles are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | correct_target |
| 4 | " flomps." | flomps | blickets | reachable_one_hop |
| 12 | " flomps." | flomps | blickets | reachable_one_hop |
## 078/direct/base/0

```text
All brovets are wugs.
All korvas are daxes.
All welbins are brovets.
All blickets are wugs.
Possible completions: brovets or daxes.
Therefore, all welbins are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | correct_target |
| 4 | " blickets." | blickets | brovets | unreachable_fact_name |
| 12 | " wugs." | wugs | brovets | other_reachable |
## 078/direct/base/1

```text
All brovets are wugs.
All korvas are daxes.
All welbins are brovets.
All blickets are wugs.
Possible completions: daxes or wugs.
Therefore, all brovets are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 078/twohop/base/0

```text
All brovets are wugs.
All korvas are daxes.
All welbins are brovets.
All blickets are wugs.
Possible completions: wugs or daxes.
Therefore, all welbins are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | wugs | reachable_one_hop |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 078/twohop/base/1

```text
All korvas are daxes.
All brovets are welbins.
All blickets are welbins.
All wugs are brovets.
Possible completions: daxes or welbins.
Therefore, all wugs are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " brovets." | brovets | daxes | reachable_one_hop |
| 12 | " brovets." | brovets | daxes | reachable_one_hop |
## 078/broken/first/0

```text
All brovets are wugs.
All korvas are daxes.
All welbins are korvas.
All blickets are wugs.
Possible completions: wugs or daxes.
Therefore, all welbins are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | wrong_candidate |
| 4 | " wugs." | wugs | wugs | wrong_candidate |
| 12 | " wugs." | wugs | wugs | wrong_candidate |
## 078/broken/second/1

```text
All brovets are daxes.
All korvas are daxes.
All welbins are brovets.
All blickets are wugs.
Possible completions: wugs or daxes.
Therefore, all welbins are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | daxes | unreachable_fact_name |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 078/robustness/reorder/0

```text
All blickets are wugs.
All korvas are daxes.
All welbins are brovets.
All brovets are wugs.
Possible completions: wugs or daxes.
Therefore, all welbins are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 078/robustness/reorder/1

```text
All brovets are welbins.
All korvas are daxes.
All wugs are brovets.
All blickets are welbins.
Possible completions: daxes or welbins.
Therefore, all wugs are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | daxes | unreachable_fact_name |
| 4 | " blickets." | blickets | daxes | unreachable_fact_name |
| 12 | " blickets." | blickets | daxes | unreachable_fact_name |
## 078/robustness/distractors/0

```text
All brovets are wugs.
All blickets are wugs.
All welbins are brovets.
All korvas are daxes.
All nufrons are vromps.
All vromps are daxes.
Possible completions: wugs or daxes.
Therefore, all welbins are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | wugs | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 078/robustness/distractors/1

```text
All nufrons are vromps.
All blickets are welbins.
All brovets are welbins.
All vromps are daxes.
All wugs are brovets.
All korvas are daxes.
Possible completions: daxes or welbins.
Therefore, all wugs are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 078/robustness/rename/0

```text
All yorbits are snorps.
All helpons are tivaks.
All ruspins are yorbits.
All kelbrins are snorps.
Possible completions: snorps or tivaks.
Therefore, all ruspins are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | snorps | reachable_one_hop |
| 4 | " yorbits." | yorbits | snorps | reachable_one_hop |
| 12 | " yorbits." | yorbits | snorps | reachable_one_hop |
## 078/robustness/rename/1

```text
All nufrons are xandles.
All quavels are zemples.
All prandils are zemples.
All vibbles are quavels.
Possible completions: xandles or zemples.
Therefore, all vibbles are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | xandles | reachable_one_hop |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " quavels." | quavels | zemples | reachable_one_hop |
## 079/direct/base/0

```text
All zeltrons are nerps.
All quavels are brovets.
All yorbits are nerps.
All murdles are yorbits.
Possible completions: brovets or yorbits.
Therefore, all murdles are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | wrong_candidate |
| 4 | " yorbits." | yorbits | yorbits | correct_target |
| 12 | " yorbits." | yorbits | yorbits | correct_target |
## 079/direct/base/1

```text
All zeltrons are nerps.
All quavels are brovets.
All yorbits are nerps.
All murdles are yorbits.
Possible completions: nerps or brovets.
Therefore, all yorbits are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 079/twohop/base/0

```text
All zeltrons are nerps.
All quavels are brovets.
All yorbits are nerps.
All murdles are yorbits.
Possible completions: brovets or nerps.
Therefore, all murdles are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | wrong_candidate |
| 4 | " yorbits." | yorbits | nerps | reachable_one_hop |
| 12 | " yorbits." | yorbits | nerps | reachable_one_hop |
## 079/twohop/base/1

```text
All quavels are brovets.
All nerps are yorbits.
All zeltrons are murdles.
All yorbits are murdles.
Possible completions: murdles or brovets.
Therefore, all nerps are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | wrong_candidate |
| 4 | " yorbits." | yorbits | brovets | reachable_one_hop |
| 12 | " yorbits." | yorbits | brovets | reachable_one_hop |
## 079/broken/first/0

```text
All zeltrons are nerps.
All quavels are brovets.
All yorbits are nerps.
All murdles are quavels.
Possible completions: brovets or nerps.
Therefore, all murdles are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | brovets | reachable_one_hop |
| 4 | " nerps." | nerps | nerps | wrong_candidate |
| 12 | " nerps." | nerps | nerps | wrong_candidate |
## 079/broken/second/1

```text
All zeltrons are nerps.
All quavels are brovets.
All yorbits are brovets.
All murdles are yorbits.
Possible completions: brovets or nerps.
Therefore, all murdles are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | brovets | reachable_one_hop |
| 4 | " yorbits." | yorbits | nerps | reachable_one_hop |
| 12 | " yorbits." | yorbits | nerps | reachable_one_hop |
## 079/robustness/reorder/0

```text
All murdles are yorbits.
All zeltrons are nerps.
All yorbits are nerps.
All quavels are brovets.
Possible completions: brovets or nerps.
Therefore, all murdles are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 079/robustness/reorder/1

```text
All zeltrons are murdles.
All nerps are yorbits.
All yorbits are murdles.
All quavels are brovets.
Possible completions: murdles or brovets.
Therefore, all nerps are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | murdles | unreachable_fact_name |
| 4 | " yorbits." | yorbits | brovets | reachable_one_hop |
| 12 | " yorbits." | yorbits | brovets | reachable_one_hop |
## 079/robustness/distractors/0

```text
All murdles are yorbits.
All quavels are brovets.
All zeltrons are nerps.
All flomps are tufas.
All tufas are brovets.
All yorbits are nerps.
Possible completions: brovets or nerps.
Therefore, all murdles are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | nerps | reachable_one_hop |
| 4 | " yorbits." | yorbits | nerps | reachable_one_hop |
| 12 | " nerps." | nerps | nerps | correct_target |
## 079/robustness/distractors/1

```text
All flomps are tufas.
All quavels are brovets.
All nerps are yorbits.
All yorbits are murdles.
All tufas are brovets.
All zeltrons are murdles.
Possible completions: murdles or brovets.
Therefore, all nerps are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | brovets | unreachable_fact_name |
| 4 | " tufas." | tufas | brovets | unreachable_fact_name |
| 12 | " brovets." | brovets | brovets | wrong_candidate |
## 079/robustness/rename/0

```text
All lomits are helpons.
All wugs are grivaks.
All kelbrins are helpons.
All prandils are kelbrins.
Possible completions: grivaks or helpons.
Therefore, all prandils are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | grivaks | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | helpons | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | helpons | reachable_one_hop |
## 079/robustness/rename/1

```text
All blickets are helpons.
All shalds are daxes.
All sprocks are grivaks.
All daxes are grivaks.
Possible completions: grivaks or helpons.
Therefore, all shalds are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | helpons | reachable_one_hop |
| 4 | " daxes." | daxes | grivaks | reachable_one_hop |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 080/direct/base/0

```text
All daxes are welbins.
All korvas are nufrons.
All xandles are welbins.
All tufas are xandles.
Possible completions: xandles or nufrons.
Therefore, all tufas are
```

אמת: **xandles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | xandles | correct_target |
| 4 | " xandles." | xandles | xandles | correct_target |
| 12 | " xandles." | xandles | xandles | correct_target |
## 080/direct/base/1

```text
All daxes are welbins.
All korvas are nufrons.
All xandles are welbins.
All tufas are xandles.
Possible completions: nufrons or welbins.
Therefore, all xandles are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 4 | " xandles." | xandles | welbins | source_itself |
| 12 | " tufas." | tufas | welbins | unreachable_fact_name |
## 080/twohop/base/0

```text
All daxes are welbins.
All korvas are nufrons.
All xandles are welbins.
All tufas are xandles.
Possible completions: welbins or nufrons.
Therefore, all tufas are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | welbins | reachable_one_hop |
| 4 | " xandles." | xandles | welbins | reachable_one_hop |
| 12 | " xandles." | xandles | nufrons | reachable_one_hop |
## 080/twohop/base/1

```text
All xandles are tufas.
All daxes are tufas.
All welbins are xandles.
All korvas are nufrons.
Possible completions: nufrons or tufas.
Therefore, all welbins are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | tufas | reachable_one_hop |
| 4 | " xandles." | xandles | tufas | reachable_one_hop |
| 12 | " tufas." | tufas | tufas | correct_target |
## 080/broken/first/0

```text
All daxes are welbins.
All korvas are nufrons.
All xandles are welbins.
All tufas are korvas.
Possible completions: welbins or nufrons.
Therefore, all tufas are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | nufrons | reachable_one_hop |
| 4 | " korvas." | korvas | nufrons | reachable_one_hop |
| 12 | " korvas." | korvas | nufrons | reachable_one_hop |
## 080/broken/second/1

```text
All daxes are welbins.
All korvas are nufrons.
All xandles are nufrons.
All tufas are xandles.
Possible completions: welbins or nufrons.
Therefore, all tufas are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | nufrons | reachable_one_hop |
| 4 | " xandles." | xandles | nufrons | reachable_one_hop |
| 12 | " xandles." | xandles | nufrons | reachable_one_hop |
## 080/robustness/reorder/0

```text
All tufas are xandles.
All xandles are welbins.
All korvas are nufrons.
All daxes are welbins.
Possible completions: welbins or nufrons.
Therefore, all tufas are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 4 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 12 | " nufrons." | nufrons | nufrons | wrong_candidate |
## 080/robustness/reorder/1

```text
All welbins are xandles.
All korvas are nufrons.
All daxes are tufas.
All xandles are tufas.
Possible completions: nufrons or tufas.
Therefore, all welbins are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 080/robustness/distractors/0

```text
All korvas are nufrons.
All zorks are nufrons.
All daxes are welbins.
All tufas are xandles.
All xandles are welbins.
All yorbits are zorks.
Possible completions: welbins or nufrons.
Therefore, all tufas are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | nufrons | reachable_one_hop |
| 4 | " xandles." | xandles | welbins | reachable_one_hop |
| 12 | " zorks." | zorks | nufrons | unreachable_fact_name |
## 080/robustness/distractors/1

```text
All yorbits are zorks.
All welbins are xandles.
All xandles are tufas.
All korvas are nufrons.
All daxes are tufas.
All zorks are nufrons.
Possible completions: nufrons or tufas.
Therefore, all welbins are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " xandles." | xandles | tufas | reachable_one_hop |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 080/robustness/rename/0

```text
All blickets are murdles.
All wugs are oskets.
All jastles are murdles.
All snorps are jastles.
Possible completions: murdles or oskets.
Therefore, all snorps are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | murdles | reachable_one_hop |
| 4 | " jastles." | jastles | murdles | reachable_one_hop |
| 12 | " jastles." | jastles | oskets | reachable_one_hop |
## 080/robustness/rename/1

```text
All sprocks are zorks.
All ruspins are zorks.
All tivaks are sprocks.
All yorbits are wugs.
Possible completions: wugs or zorks.
Therefore, all tivaks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | zorks | wrong_candidate |
| 4 | " sprocks." | sprocks | wugs | reachable_one_hop |
| 12 | " wugs." | wugs | wugs | wrong_candidate |
## 081/direct/base/0

```text
All helpons are sprocks.
All blickets are oskets.
All ruspins are oskets.
All murdles are ruspins.
Possible completions: sprocks or ruspins.
Therefore, all murdles are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 081/direct/base/1

```text
All helpons are sprocks.
All blickets are oskets.
All ruspins are oskets.
All murdles are ruspins.
Possible completions: oskets or sprocks.
Therefore, all ruspins are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " oskets." | oskets | oskets | correct_target |
## 081/twohop/base/0

```text
All helpons are sprocks.
All blickets are oskets.
All ruspins are oskets.
All murdles are ruspins.
Possible completions: sprocks or oskets.
Therefore, all murdles are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " ruspins." | ruspins | sprocks | reachable_one_hop |
| 12 | " ruspins." | ruspins | oskets | reachable_one_hop |
## 081/twohop/base/1

```text
All helpons are sprocks.
All ruspins are murdles.
All blickets are murdles.
All oskets are ruspins.
Possible completions: murdles or sprocks.
Therefore, all oskets are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " ruspins." | ruspins | murdles | reachable_one_hop |
| 12 | " ruspins." | ruspins | sprocks | reachable_one_hop |
## 081/broken/first/0

```text
All helpons are sprocks.
All blickets are oskets.
All ruspins are oskets.
All murdles are helpons.
Possible completions: sprocks or oskets.
Therefore, all murdles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | sprocks | reachable_one_hop |
| 4 | " helpons." | helpons | sprocks | reachable_one_hop |
| 12 | " helpons." | helpons | sprocks | reachable_one_hop |
## 081/broken/second/1

```text
All helpons are sprocks.
All blickets are oskets.
All ruspins are sprocks.
All murdles are ruspins.
Possible completions: sprocks or oskets.
Therefore, all murdles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " ruspins." | ruspins | sprocks | reachable_one_hop |
| 12 | " ruspins." | ruspins | sprocks | reachable_one_hop |
## 081/robustness/reorder/0

```text
All blickets are oskets.
All ruspins are oskets.
All helpons are sprocks.
All murdles are ruspins.
Possible completions: sprocks or oskets.
Therefore, all murdles are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " ruspins." | ruspins | sprocks | reachable_one_hop |
| 12 | " ruspins." | ruspins | oskets | reachable_one_hop |
## 081/robustness/reorder/1

```text
All oskets are ruspins.
All helpons are sprocks.
All ruspins are murdles.
All blickets are murdles.
Possible completions: murdles or sprocks.
Therefore, all oskets are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | sprocks | reachable_one_hop |
| 4 | " murdles." | murdles | murdles | correct_target |
| 12 | " sprocks." | sprocks | sprocks | wrong_candidate |
## 081/robustness/distractors/0

```text
All helpons are sprocks.
All ruspins are oskets.
All murdles are ruspins.
All tivaks are sprocks.
All flomps are tivaks.
All blickets are oskets.
Possible completions: sprocks or oskets.
Therefore, all murdles are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | sprocks | unreachable_fact_name |
| 4 | " tivaks." | tivaks | oskets | unreachable_fact_name |
| 12 | " tivaks." | tivaks | oskets | unreachable_fact_name |
## 081/robustness/distractors/1

```text
All tivaks are sprocks.
All ruspins are murdles.
All oskets are ruspins.
All helpons are sprocks.
All blickets are murdles.
All flomps are tivaks.
Possible completions: murdles or sprocks.
Therefore, all oskets are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 4 | " tivaks." | tivaks | sprocks | unreachable_fact_name |
| 12 | " tivaks." | tivaks | sprocks | unreachable_fact_name |
## 081/robustness/rename/0

```text
All wugs are kelbrins.
All nerps are ulvets.
All tivaks are ulvets.
All lomits are tivaks.
Possible completions: kelbrins or ulvets.
Therefore, all lomits are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | kelbrins | reachable_one_hop |
| 4 | " tivaks." | tivaks | kelbrins | reachable_one_hop |
| 12 | " tivaks." | tivaks | kelbrins | reachable_one_hop |
## 081/robustness/rename/1

```text
All xandles are welbins.
All zeltrons are lomits.
All flomps are lomits.
All wugs are zeltrons.
Possible completions: lomits or welbins.
Therefore, all wugs are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zeltrons." | zeltrons | lomits | reachable_one_hop |
| 4 | " zeltrons." | zeltrons | lomits | reachable_one_hop |
| 12 | " zeltrons." | zeltrons | lomits | reachable_one_hop |
## 082/direct/base/0

```text
All tivaks are oskets.
All nufrons are zemples.
All nerps are zemples.
All zorks are nerps.
Possible completions: nerps or oskets.
Therefore, all zorks are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | nerps | correct_target |
| 4 | " nerps." | nerps | nerps | correct_target |
| 12 | " nerps." | nerps | nerps | correct_target |
## 082/direct/base/1

```text
All tivaks are oskets.
All nufrons are zemples.
All nerps are zemples.
All zorks are nerps.
Possible completions: oskets or zemples.
Therefore, all nerps are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 082/twohop/base/0

```text
All tivaks are oskets.
All nufrons are zemples.
All nerps are zemples.
All zorks are nerps.
Possible completions: zemples or oskets.
Therefore, all zorks are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " nerps." | nerps | zemples | reachable_one_hop |
| 12 | " nerps." | nerps | zemples | reachable_one_hop |
## 082/twohop/base/1

```text
All zemples are nerps.
All tivaks are oskets.
All nufrons are zorks.
All nerps are zorks.
Possible completions: oskets or zorks.
Therefore, all zemples are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " nerps." | nerps | zorks | reachable_one_hop |
| 12 | " nerps." | nerps | zorks | reachable_one_hop |
## 082/broken/first/0

```text
All tivaks are oskets.
All nufrons are zemples.
All nerps are zemples.
All zorks are tivaks.
Possible completions: zemples or oskets.
Therefore, all zorks are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | oskets | reachable_one_hop |
| 4 | " tivaks." | tivaks | oskets | reachable_one_hop |
| 12 | " tivaks." | tivaks | oskets | reachable_one_hop |
## 082/broken/second/1

```text
All tivaks are oskets.
All nufrons are zemples.
All nerps are oskets.
All zorks are nerps.
Possible completions: zemples or oskets.
Therefore, all zorks are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | oskets | reachable_one_hop |
| 4 | " nerps." | nerps | oskets | reachable_one_hop |
| 12 | " nerps." | nerps | oskets | reachable_one_hop |
## 082/robustness/reorder/0

```text
All nerps are zemples.
All zorks are nerps.
All nufrons are zemples.
All tivaks are oskets.
Possible completions: zemples or oskets.
Therefore, all zorks are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | zemples | unreachable_fact_name |
| 4 | " nerps." | nerps | zemples | reachable_one_hop |
| 12 | " nerps." | nerps | oskets | reachable_one_hop |
## 082/robustness/reorder/1

```text
All nerps are zorks.
All zemples are nerps.
All nufrons are zorks.
All tivaks are oskets.
Possible completions: oskets or zorks.
Therefore, all zemples are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | oskets | unreachable_fact_name |
| 4 | " nerps." | nerps | zorks | reachable_one_hop |
| 12 | " nerps." | nerps | zorks | reachable_one_hop |
## 082/robustness/distractors/0

```text
All nerps are zemples.
All zorks are nerps.
All nufrons are zemples.
All tivaks are oskets.
All flomps are oskets.
All lomits are flomps.
Possible completions: zemples or oskets.
Therefore, all zorks are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | zemples | reachable_one_hop |
| 4 | " nerps." | nerps | oskets | reachable_one_hop |
| 12 | " nerps." | nerps | zemples | reachable_one_hop |
## 082/robustness/distractors/1

```text
All zemples are nerps.
All tivaks are oskets.
All flomps are oskets.
All lomits are flomps.
All nufrons are zorks.
All nerps are zorks.
Possible completions: oskets or zorks.
Therefore, all zemples are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | oskets | reachable_one_hop |
| 4 | " nerps." | nerps | zorks | reachable_one_hop |
| 12 | " nerps." | nerps | zorks | reachable_one_hop |
## 082/robustness/rename/0

```text
All zeltrons are vibbles.
All flomps are wugs.
All yorbits are wugs.
All plinets are yorbits.
Possible completions: wugs or vibbles.
Therefore, all plinets are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " yorbits." | yorbits | wugs | reachable_one_hop |
| 12 | " yorbits." | yorbits | wugs | reachable_one_hop |
## 082/robustness/rename/1

```text
All quavels are grivaks.
All snorps are yorbits.
All brovets are shalds.
All grivaks are shalds.
Possible completions: yorbits or shalds.
Therefore, all quavels are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | yorbits | reachable_one_hop |
| 4 | " grivaks." | grivaks | shalds | reachable_one_hop |
| 12 | " grivaks." | grivaks | shalds | reachable_one_hop |
## 083/direct/base/0

```text
All lomits are tivaks.
All zeltrons are tivaks.
All welbins are ulvets.
All zorks are lomits.
Possible completions: ulvets or lomits.
Therefore, all zorks are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 4 | " lomits." | lomits | lomits | correct_target |
| 12 | " lomits." | lomits | lomits | correct_target |
## 083/direct/base/1

```text
All lomits are tivaks.
All zeltrons are tivaks.
All welbins are ulvets.
All zorks are lomits.
Possible completions: tivaks or ulvets.
Therefore, all lomits are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | tivaks | correct_target |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 083/twohop/base/0

```text
All lomits are tivaks.
All zeltrons are tivaks.
All welbins are ulvets.
All zorks are lomits.
Possible completions: ulvets or tivaks.
Therefore, all zorks are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | ulvets | reachable_one_hop |
| 4 | " lomits." | lomits | tivaks | reachable_one_hop |
| 12 | " lomits." | lomits | tivaks | reachable_one_hop |
## 083/twohop/base/1

```text
All zeltrons are zorks.
All lomits are zorks.
All welbins are ulvets.
All tivaks are lomits.
Possible completions: zorks or ulvets.
Therefore, all tivaks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " lomits." | lomits | zorks | reachable_one_hop |
| 12 | " lomits." | lomits | zorks | reachable_one_hop |
## 083/broken/first/0

```text
All lomits are tivaks.
All zeltrons are tivaks.
All welbins are ulvets.
All zorks are welbins.
Possible completions: ulvets or tivaks.
Therefore, all zorks are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | correct_target |
| 4 | " tivaks." | tivaks | tivaks | wrong_candidate |
| 12 | " tivaks." | tivaks | tivaks | wrong_candidate |
## 083/broken/second/1

```text
All lomits are ulvets.
All zeltrons are tivaks.
All welbins are ulvets.
All zorks are lomits.
Possible completions: ulvets or tivaks.
Therefore, all zorks are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | ulvets | reachable_one_hop |
| 4 | " lomits." | lomits | tivaks | reachable_one_hop |
| 12 | " lomits." | lomits | tivaks | reachable_one_hop |
## 083/robustness/reorder/0

```text
All lomits are tivaks.
All zorks are lomits.
All zeltrons are tivaks.
All welbins are ulvets.
Possible completions: ulvets or tivaks.
Therefore, all zorks are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " lomits." | lomits | tivaks | reachable_one_hop |
## 083/robustness/reorder/1

```text
All tivaks are lomits.
All welbins are ulvets.
All zeltrons are zorks.
All lomits are zorks.
Possible completions: zorks or ulvets.
Therefore, all tivaks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 12 | " ulvets." | ulvets | ulvets | wrong_candidate |
## 083/robustness/distractors/0

```text
All zeltrons are tivaks.
All lomits are tivaks.
All xandles are zemples.
All zemples are ulvets.
All welbins are ulvets.
All zorks are lomits.
Possible completions: ulvets or tivaks.
Therefore, all zorks are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | tivaks | reachable_one_hop |
| 4 | " lomits." | lomits | tivaks | reachable_one_hop |
| 12 | " lomits." | lomits | tivaks | reachable_one_hop |
## 083/robustness/distractors/1

```text
All xandles are zemples.
All tivaks are lomits.
All zeltrons are zorks.
All zemples are ulvets.
All lomits are zorks.
All welbins are ulvets.
Possible completions: zorks or ulvets.
Therefore, all tivaks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | ulvets | reachable_one_hop |
| 4 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 12 | " ulvets." | ulvets | ulvets | wrong_candidate |
## 083/robustness/rename/0

```text
All quavels are helpons.
All xandles are helpons.
All tufas are kelbrins.
All brovets are quavels.
Possible completions: kelbrins or helpons.
Therefore, all brovets are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | kelbrins | reachable_one_hop |
| 4 | " quavels." | quavels | kelbrins | reachable_one_hop |
| 12 | " quavels." | quavels | helpons | reachable_one_hop |
## 083/robustness/rename/1

```text
All korvas are shalds.
All tufas are shalds.
All blickets are helpons.
All daxes are tufas.
Possible completions: shalds or helpons.
Therefore, all daxes are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | shalds | correct_target |
| 4 | " tufas." | tufas | shalds | reachable_one_hop |
| 12 | " tufas." | tufas | shalds | reachable_one_hop |
## 084/direct/base/0

```text
All sprocks are daxes.
All ruspins are plinets.
All crundles are plinets.
All zeltrons are ruspins.
Possible completions: ruspins or daxes.
Therefore, all zeltrons are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 084/direct/base/1

```text
All sprocks are daxes.
All ruspins are plinets.
All crundles are plinets.
All zeltrons are ruspins.
Possible completions: daxes or plinets.
Therefore, all ruspins are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " plinets." | plinets | plinets | correct_target |
| 12 | " plinets." | plinets | plinets | correct_target |
## 084/twohop/base/0

```text
All sprocks are daxes.
All ruspins are plinets.
All crundles are plinets.
All zeltrons are ruspins.
Possible completions: plinets or daxes.
Therefore, all zeltrons are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | correct_target |
| 4 | " ruspins." | ruspins | daxes | reachable_one_hop |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 084/twohop/base/1

```text
All crundles are zeltrons.
All ruspins are zeltrons.
All plinets are ruspins.
All sprocks are daxes.
Possible completions: daxes or zeltrons.
Therefore, all plinets are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 084/broken/first/0

```text
All sprocks are daxes.
All ruspins are plinets.
All crundles are plinets.
All zeltrons are sprocks.
Possible completions: plinets or daxes.
Therefore, all zeltrons are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | daxes | reachable_one_hop |
| 4 | " sprocks." | sprocks | daxes | reachable_one_hop |
| 12 | " sprocks." | sprocks | daxes | reachable_one_hop |
## 084/broken/second/1

```text
All sprocks are daxes.
All ruspins are daxes.
All crundles are plinets.
All zeltrons are ruspins.
Possible completions: plinets or daxes.
Therefore, all zeltrons are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | wrong_candidate |
| 4 | " ruspins." | ruspins | daxes | reachable_one_hop |
| 12 | " daxes." | daxes | daxes | correct_target |
## 084/robustness/reorder/0

```text
All zeltrons are ruspins.
All sprocks are daxes.
All ruspins are plinets.
All crundles are plinets.
Possible completions: plinets or daxes.
Therefore, all zeltrons are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " plinets." | plinets | plinets | correct_target |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 084/robustness/reorder/1

```text
All plinets are ruspins.
All ruspins are zeltrons.
All sprocks are daxes.
All crundles are zeltrons.
Possible completions: daxes or zeltrons.
Therefore, all plinets are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " zeltrons." | zeltrons | zeltrons | correct_target |
| 12 | " zeltrons." | zeltrons | zeltrons | correct_target |
## 084/robustness/distractors/0

```text
All sprocks are daxes.
All quavels are daxes.
All oskets are quavels.
All zeltrons are ruspins.
All ruspins are plinets.
All crundles are plinets.
Possible completions: plinets or daxes.
Therefore, all zeltrons are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " plinets." | plinets | plinets | correct_target |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 084/robustness/distractors/1

```text
All plinets are ruspins.
All ruspins are zeltrons.
All crundles are zeltrons.
All oskets are quavels.
All quavels are daxes.
All sprocks are daxes.
Possible completions: daxes or zeltrons.
Therefore, all plinets are
```

אמת: **zeltrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | daxes | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 084/robustness/rename/0

```text
All brovets are helpons.
All zorks are jastles.
All vibbles are jastles.
All zemples are zorks.
Possible completions: jastles or helpons.
Therefore, all zemples are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | jastles | reachable_one_hop |
| 4 | " zorks." | zorks | jastles | reachable_one_hop |
| 12 | " zorks." | zorks | jastles | reachable_one_hop |
## 084/robustness/rename/1

```text
All shalds are oskets.
All vibbles are oskets.
All snorps are vibbles.
All zorks are blickets.
Possible completions: blickets or oskets.
Therefore, all snorps are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | wrong_candidate |
| 4 | " vibbles." | vibbles | blickets | reachable_one_hop |
| 12 | " vibbles." | vibbles | blickets | reachable_one_hop |
## 085/direct/base/0

```text
All prandils are nerps.
All lomits are korvas.
All korvas are oskets.
All vromps are oskets.
Possible completions: nerps or korvas.
Therefore, all lomits are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | nerps | unreachable_fact_name |
| 4 | " oskets." | oskets | korvas | other_reachable |
| 12 | " oskets." | oskets | korvas | other_reachable |
## 085/direct/base/1

```text
All prandils are nerps.
All lomits are korvas.
All korvas are oskets.
All vromps are oskets.
Possible completions: oskets or nerps.
Therefore, all korvas are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | correct_target |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " oskets." | oskets | oskets | correct_target |
## 085/twohop/base/0

```text
All prandils are nerps.
All lomits are korvas.
All korvas are oskets.
All vromps are oskets.
Possible completions: nerps or oskets.
Therefore, all lomits are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vromps." | vromps | oskets | unreachable_fact_name |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " korvas." | korvas | oskets | reachable_one_hop |
## 085/twohop/base/1

```text
All prandils are nerps.
All oskets are korvas.
All korvas are lomits.
All vromps are lomits.
Possible completions: lomits or nerps.
Therefore, all oskets are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | lomits | unreachable_fact_name |
| 4 | " lomits." | lomits | lomits | correct_target |
| 12 | " lomits." | lomits | lomits | correct_target |
## 085/broken/first/0

```text
All prandils are nerps.
All lomits are prandils.
All korvas are oskets.
All vromps are oskets.
Possible completions: nerps or oskets.
Therefore, all lomits are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | nerps | reachable_one_hop |
| 4 | " oskets." | oskets | oskets | wrong_candidate |
| 12 | " prandils." | prandils | oskets | reachable_one_hop |
## 085/broken/second/1

```text
All prandils are nerps.
All lomits are korvas.
All korvas are nerps.
All vromps are oskets.
Possible completions: nerps or oskets.
Therefore, all lomits are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | nerps | unreachable_fact_name |
| 4 | " oskets." | oskets | oskets | wrong_candidate |
| 12 | " korvas." | korvas | oskets | reachable_one_hop |
## 085/robustness/reorder/0

```text
All vromps are oskets.
All prandils are nerps.
All lomits are korvas.
All korvas are oskets.
Possible completions: nerps or oskets.
Therefore, all lomits are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | correct_target |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " korvas." | korvas | oskets | reachable_one_hop |
## 085/robustness/reorder/1

```text
All vromps are lomits.
All korvas are lomits.
All prandils are nerps.
All oskets are korvas.
Possible completions: lomits or nerps.
Therefore, all oskets are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | correct_target |
| 4 | " korvas." | korvas | lomits | reachable_one_hop |
| 12 | " korvas." | korvas | lomits | reachable_one_hop |
## 085/robustness/distractors/0

```text
All daxes are sprocks.
All sprocks are nerps.
All lomits are korvas.
All korvas are oskets.
All prandils are nerps.
All vromps are oskets.
Possible completions: nerps or oskets.
Therefore, all lomits are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | nerps | unreachable_fact_name |
| 4 | " prandils." | prandils | oskets | unreachable_fact_name |
| 12 | " korvas." | korvas | oskets | reachable_one_hop |
## 085/robustness/distractors/1

```text
All korvas are lomits.
All vromps are lomits.
All daxes are sprocks.
All sprocks are nerps.
All prandils are nerps.
All oskets are korvas.
Possible completions: lomits or nerps.
Therefore, all oskets are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | lomits | correct_target |
| 4 | " korvas." | korvas | nerps | reachable_one_hop |
| 12 | " korvas." | korvas | lomits | reachable_one_hop |
## 085/robustness/rename/0

```text
All crundles are brovets.
All yorbits are tufas.
All tufas are shalds.
All daxes are shalds.
Possible completions: brovets or shalds.
Therefore, all yorbits are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | brovets | reachable_one_hop |
| 4 | " tufas." | tufas | shalds | reachable_one_hop |
| 12 | " tufas." | tufas | shalds | reachable_one_hop |
## 085/robustness/rename/1

```text
All shalds are helpons.
All kelbrins are nufrons.
All nufrons are sprocks.
All wugs are sprocks.
Possible completions: sprocks or helpons.
Therefore, all kelbrins are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | sprocks | reachable_one_hop |
| 4 | " nufrons." | nufrons | sprocks | reachable_one_hop |
| 12 | " nufrons." | nufrons | sprocks | reachable_one_hop |
## 086/direct/base/0

```text
All zeltrons are prandils.
All murdles are jastles.
All welbins are nerps.
All nerps are prandils.
Possible completions: nerps or jastles.
Therefore, all welbins are
```

אמת: **nerps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | jastles | other_reachable |
| 4 | " prandils." | prandils | jastles | other_reachable |
| 12 | " prandils." | prandils | jastles | other_reachable |
## 086/direct/base/1

```text
All zeltrons are prandils.
All murdles are jastles.
All welbins are nerps.
All nerps are prandils.
Possible completions: jastles or prandils.
Therefore, all nerps are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | correct_target |
| 4 | " prandils." | prandils | prandils | correct_target |
| 12 | " prandils." | prandils | prandils | correct_target |
## 086/twohop/base/0

```text
All zeltrons are prandils.
All murdles are jastles.
All welbins are nerps.
All nerps are prandils.
Possible completions: prandils or jastles.
Therefore, all welbins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | correct_target |
| 4 | " prandils." | prandils | prandils | correct_target |
| 12 | " prandils." | prandils | prandils | correct_target |
## 086/twohop/base/1

```text
All prandils are nerps.
All murdles are jastles.
All nerps are welbins.
All zeltrons are welbins.
Possible completions: jastles or welbins.
Therefore, all prandils are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | wrong_candidate |
| 4 | " welbins." | welbins | welbins | correct_target |
| 12 | " welbins." | welbins | welbins | correct_target |
## 086/broken/first/0

```text
All zeltrons are prandils.
All murdles are jastles.
All welbins are murdles.
All nerps are prandils.
Possible completions: prandils or jastles.
Therefore, all welbins are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | wrong_candidate |
| 4 | " prandils." | prandils | prandils | wrong_candidate |
| 12 | " prandils." | prandils | prandils | wrong_candidate |
## 086/broken/second/1

```text
All zeltrons are prandils.
All murdles are jastles.
All welbins are nerps.
All nerps are jastles.
Possible completions: prandils or jastles.
Therefore, all welbins are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | jastles | reachable_one_hop |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 086/robustness/reorder/0

```text
All murdles are jastles.
All zeltrons are prandils.
All nerps are prandils.
All welbins are nerps.
Possible completions: prandils or jastles.
Therefore, all welbins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " prandils." | prandils | prandils | correct_target |
| 4 | " nerps." | nerps | prandils | reachable_one_hop |
| 12 | " nerps." | nerps | jastles | reachable_one_hop |
## 086/robustness/reorder/1

```text
All zeltrons are welbins.
All nerps are welbins.
All murdles are jastles.
All prandils are nerps.
Possible completions: jastles or welbins.
Therefore, all prandils are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | wrong_candidate |
| 4 | " nerps." | nerps | jastles | reachable_one_hop |
| 12 | " nerps." | nerps | jastles | reachable_one_hop |
## 086/robustness/distractors/0

```text
All plinets are korvas.
All zeltrons are prandils.
All nerps are prandils.
All murdles are jastles.
All welbins are nerps.
All korvas are jastles.
Possible completions: prandils or jastles.
Therefore, all welbins are
```

אמת: **prandils**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | jastles | reachable_one_hop |
| 4 | " nerps." | nerps | jastles | reachable_one_hop |
| 12 | " jastles." | jastles | jastles | wrong_candidate |
## 086/robustness/distractors/1

```text
All nerps are welbins.
All prandils are nerps.
All murdles are jastles.
All plinets are korvas.
All zeltrons are welbins.
All korvas are jastles.
Possible completions: jastles or welbins.
Therefore, all prandils are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | wrong_candidate |
| 4 | " jastles." | jastles | jastles | wrong_candidate |
| 12 | " jastles." | jastles | jastles | wrong_candidate |
## 086/robustness/rename/0

```text
All crundles are blickets.
All korvas are grivaks.
All vibbles are zemples.
All zemples are blickets.
Possible completions: blickets or grivaks.
Therefore, all vibbles are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | blickets | correct_target |
| 4 | " blickets." | blickets | blickets | correct_target |
| 12 | " blickets." | blickets | blickets | correct_target |
## 086/robustness/rename/1

```text
All daxes are blickets.
All tufas are grivaks.
All blickets are zemples.
All helpons are zemples.
Possible completions: grivaks or zemples.
Therefore, all daxes are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | wrong_candidate |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 087/direct/base/0

```text
All nufrons are oskets.
All blickets are daxes.
All tivaks are lomits.
All lomits are daxes.
Possible completions: oskets or lomits.
Therefore, all tivaks are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | lomits | other_reachable |
| 4 | " daxes." | daxes | lomits | other_reachable |
| 12 | " daxes." | daxes | lomits | other_reachable |
## 087/direct/base/1

```text
All nufrons are oskets.
All blickets are daxes.
All tivaks are lomits.
All lomits are daxes.
Possible completions: daxes or oskets.
Therefore, all lomits are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | correct_target |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 087/twohop/base/0

```text
All nufrons are oskets.
All blickets are daxes.
All tivaks are lomits.
All lomits are daxes.
Possible completions: oskets or daxes.
Therefore, all tivaks are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | daxes | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 087/twohop/base/1

```text
All blickets are tivaks.
All daxes are lomits.
All nufrons are oskets.
All lomits are tivaks.
Possible completions: tivaks or oskets.
Therefore, all daxes are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | tivaks | reachable_one_hop |
| 4 | " lomits." | lomits | tivaks | reachable_one_hop |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 087/broken/first/0

```text
All nufrons are oskets.
All blickets are daxes.
All tivaks are nufrons.
All lomits are daxes.
Possible completions: oskets or daxes.
Therefore, all tivaks are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | oskets | reachable_one_hop |
| 4 | " nufrons." | nufrons | daxes | reachable_one_hop |
| 12 | " nufrons." | nufrons | daxes | reachable_one_hop |
## 087/broken/second/1

```text
All nufrons are oskets.
All blickets are daxes.
All tivaks are lomits.
All lomits are oskets.
Possible completions: oskets or daxes.
Therefore, all tivaks are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | oskets | reachable_one_hop |
| 4 | " lomits." | lomits | daxes | reachable_one_hop |
| 12 | " lomits." | lomits | daxes | reachable_one_hop |
## 087/robustness/reorder/0

```text
All lomits are daxes.
All blickets are daxes.
All tivaks are lomits.
All nufrons are oskets.
Possible completions: oskets or daxes.
Therefore, all tivaks are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | oskets | wrong_candidate |
| 4 | " lomits." | lomits | daxes | reachable_one_hop |
| 12 | " daxes." | daxes | daxes | correct_target |
## 087/robustness/reorder/1

```text
All daxes are lomits.
All nufrons are oskets.
All lomits are tivaks.
All blickets are tivaks.
Possible completions: tivaks or oskets.
Therefore, all daxes are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | oskets | reachable_one_hop |
| 4 | " lomits." | lomits | tivaks | reachable_one_hop |
| 12 | " lomits." | lomits | tivaks | reachable_one_hop |
## 087/robustness/distractors/0

```text
All nufrons are oskets.
All tivaks are lomits.
All lomits are daxes.
All snorps are ruspins.
All blickets are daxes.
All ruspins are oskets.
Possible completions: oskets or daxes.
Therefore, all tivaks are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | oskets | reachable_one_hop |
| 4 | " lomits." | lomits | daxes | reachable_one_hop |
| 12 | " daxes." | daxes | daxes | correct_target |
## 087/robustness/distractors/1

```text
All ruspins are oskets.
All blickets are tivaks.
All nufrons are oskets.
All daxes are lomits.
All snorps are ruspins.
All lomits are tivaks.
Possible completions: tivaks or oskets.
Therefore, all daxes are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | tivaks | reachable_one_hop |
| 4 | " lomits." | lomits | tivaks | reachable_one_hop |
| 12 | " lomits." | lomits | tivaks | reachable_one_hop |
## 087/robustness/rename/0

```text
All shalds are ruspins.
All prandils are vibbles.
All zorks are snorps.
All snorps are vibbles.
Possible completions: ruspins or vibbles.
Therefore, all zorks are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | vibbles | reachable_one_hop |
| 4 | " snorps." | snorps | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 087/robustness/rename/1

```text
All kelbrins are shalds.
All nerps are zorks.
All brovets are helpons.
All zorks are shalds.
Possible completions: shalds or helpons.
Therefore, all nerps are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | shalds | reachable_one_hop |
| 4 | " zorks." | zorks | shalds | reachable_one_hop |
| 12 | " shalds." | shalds | shalds | correct_target |
## 088/direct/base/0

```text
All murdles are quavels.
All daxes are murdles.
All welbins are quavels.
All flomps are snorps.
Possible completions: murdles or snorps.
Therefore, all daxes are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | murdles | other_reachable |
| 4 | " snorps." | snorps | snorps | wrong_candidate |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 088/direct/base/1

```text
All murdles are quavels.
All daxes are murdles.
All welbins are quavels.
All flomps are snorps.
Possible completions: snorps or quavels.
Therefore, all murdles are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | correct_target |
| 4 | " quavels." | quavels | quavels | correct_target |
| 12 | " quavels." | quavels | quavels | correct_target |
## 088/twohop/base/0

```text
All murdles are quavels.
All daxes are murdles.
All welbins are quavels.
All flomps are snorps.
Possible completions: quavels or snorps.
Therefore, all daxes are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | quavels | reachable_one_hop |
| 4 | " snorps." | snorps | snorps | wrong_candidate |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 088/twohop/base/1

```text
All murdles are daxes.
All quavels are murdles.
All welbins are daxes.
All flomps are snorps.
Possible completions: snorps or daxes.
Therefore, all quavels are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | snorps | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 088/broken/first/0

```text
All murdles are quavels.
All daxes are flomps.
All welbins are quavels.
All flomps are snorps.
Possible completions: quavels or snorps.
Therefore, all daxes are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | wrong_candidate |
| 4 | " flomps." | flomps | snorps | reachable_one_hop |
| 12 | " snorps." | snorps | snorps | correct_target |
## 088/broken/second/1

```text
All murdles are snorps.
All daxes are murdles.
All welbins are quavels.
All flomps are snorps.
Possible completions: quavels or snorps.
Therefore, all daxes are
```

אמת: **snorps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | wrong_candidate |
| 4 | " snorps." | snorps | snorps | correct_target |
| 12 | " snorps." | snorps | snorps | correct_target |
## 088/robustness/reorder/0

```text
All murdles are quavels.
All welbins are quavels.
All daxes are murdles.
All flomps are snorps.
Possible completions: quavels or snorps.
Therefore, all daxes are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | correct_target |
| 4 | " snorps." | snorps | snorps | wrong_candidate |
| 12 | " snorps." | snorps | snorps | wrong_candidate |
## 088/robustness/reorder/1

```text
All flomps are snorps.
All quavels are murdles.
All welbins are daxes.
All murdles are daxes.
Possible completions: snorps or daxes.
Therefore, all quavels are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | snorps | unreachable_fact_name |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 088/robustness/distractors/0

```text
All jastles are snorps.
All flomps are snorps.
All welbins are quavels.
All plinets are jastles.
All murdles are quavels.
All daxes are murdles.
Possible completions: quavels or snorps.
Therefore, all daxes are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | quavels | correct_target |
| 4 | " murdles." | murdles | snorps | reachable_one_hop |
| 12 | " murdles." | murdles | snorps | reachable_one_hop |
## 088/robustness/distractors/1

```text
All quavels are murdles.
All welbins are daxes.
All plinets are jastles.
All murdles are daxes.
All flomps are snorps.
All jastles are snorps.
Possible completions: snorps or daxes.
Therefore, all quavels are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | snorps | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 088/robustness/rename/0

```text
All xandles are tufas.
All prandils are xandles.
All korvas are tufas.
All ruspins are tivaks.
Possible completions: tufas or tivaks.
Therefore, all prandils are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | tufas | unreachable_fact_name |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 088/robustness/rename/1

```text
All prandils are sprocks.
All tivaks are prandils.
All kelbrins are sprocks.
All helpons are crundles.
Possible completions: crundles or sprocks.
Therefore, all tivaks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " crundles." | crundles | crundles | wrong_candidate |
| 4 | " prandils." | prandils | crundles | reachable_one_hop |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 089/direct/base/0

```text
All zorks are jastles.
All helpons are sprocks.
All korvas are vibbles.
All jastles are sprocks.
Possible completions: vibbles or jastles.
Therefore, all zorks are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 089/direct/base/1

```text
All zorks are jastles.
All helpons are sprocks.
All korvas are vibbles.
All jastles are sprocks.
Possible completions: sprocks or vibbles.
Therefore, all jastles are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 089/twohop/base/0

```text
All zorks are jastles.
All helpons are sprocks.
All korvas are vibbles.
All jastles are sprocks.
Possible completions: vibbles or sprocks.
Therefore, all zorks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | vibbles | reachable_one_hop |
| 4 | " sprocks." | sprocks | sprocks | correct_target |
| 12 | " sprocks." | sprocks | sprocks | correct_target |
## 089/twohop/base/1

```text
All jastles are zorks.
All korvas are vibbles.
All helpons are zorks.
All sprocks are jastles.
Possible completions: zorks or vibbles.
Therefore, all sprocks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | zorks | reachable_one_hop |
| 4 | " jastles." | jastles | zorks | reachable_one_hop |
| 12 | " jastles." | jastles | zorks | reachable_one_hop |
## 089/broken/first/0

```text
All zorks are korvas.
All helpons are sprocks.
All korvas are vibbles.
All jastles are sprocks.
Possible completions: vibbles or sprocks.
Therefore, all zorks are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " sprocks." | sprocks | sprocks | wrong_candidate |
| 12 | " sprocks." | sprocks | sprocks | wrong_candidate |
## 089/broken/second/1

```text
All zorks are jastles.
All helpons are sprocks.
All korvas are vibbles.
All jastles are vibbles.
Possible completions: vibbles or sprocks.
Therefore, all zorks are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " jastles." | jastles | vibbles | reachable_one_hop |
| 12 | " jastles." | jastles | sprocks | reachable_one_hop |
## 089/robustness/reorder/0

```text
All jastles are sprocks.
All korvas are vibbles.
All helpons are sprocks.
All zorks are jastles.
Possible completions: vibbles or sprocks.
Therefore, all zorks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " sprocks." | sprocks | sprocks | correct_target |
| 4 | " jastles." | jastles | sprocks | reachable_one_hop |
| 12 | " jastles." | jastles | sprocks | reachable_one_hop |
## 089/robustness/reorder/1

```text
All sprocks are jastles.
All jastles are zorks.
All korvas are vibbles.
All helpons are zorks.
Possible completions: zorks or vibbles.
Therefore, all sprocks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " helpons." | helpons | zorks | unreachable_fact_name |
| 4 | " jastles." | jastles | vibbles | reachable_one_hop |
| 12 | " jastles." | jastles | vibbles | reachable_one_hop |
## 089/robustness/distractors/0

```text
All oskets are shalds.
All jastles are sprocks.
All zorks are jastles.
All shalds are vibbles.
All korvas are vibbles.
All helpons are sprocks.
Possible completions: vibbles or sprocks.
Therefore, all zorks are
```

אמת: **sprocks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " jastles." | jastles | sprocks | reachable_one_hop |
| 12 | " jastles." | jastles | sprocks | reachable_one_hop |
## 089/robustness/distractors/1

```text
All shalds are vibbles.
All jastles are zorks.
All sprocks are jastles.
All helpons are zorks.
All oskets are shalds.
All korvas are vibbles.
Possible completions: zorks or vibbles.
Therefore, all sprocks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 089/robustness/rename/0

```text
All yorbits are brovets.
All quavels are tivaks.
All oskets are zemples.
All brovets are tivaks.
Possible completions: zemples or tivaks.
Therefore, all yorbits are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | zemples | reachable_one_hop |
| 4 | " brovets." | brovets | tivaks | reachable_one_hop |
| 12 | " brovets." | brovets | tivaks | reachable_one_hop |
## 089/robustness/rename/1

```text
All welbins are lomits.
All snorps are daxes.
All nufrons are lomits.
All zemples are welbins.
Possible completions: lomits or daxes.
Therefore, all zemples are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | lomits | reachable_one_hop |
| 4 | " welbins." | welbins | lomits | reachable_one_hop |
| 12 | " welbins." | welbins | lomits | reachable_one_hop |
## 090/direct/base/0

```text
All jastles are ulvets.
All tufas are zorks.
All murdles are ulvets.
All blickets are murdles.
Possible completions: murdles or zorks.
Therefore, all blickets are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | murdles | correct_target |
| 4 | " murdles." | murdles | murdles | correct_target |
| 12 | " murdles." | murdles | murdles | correct_target |
## 090/direct/base/1

```text
All jastles are ulvets.
All tufas are zorks.
All murdles are ulvets.
All blickets are murdles.
Possible completions: zorks or ulvets.
Therefore, all murdles are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | wrong_candidate |
| 4 | " ulvets." | ulvets | ulvets | correct_target |
| 12 | " ulvets." | ulvets | ulvets | correct_target |
## 090/twohop/base/0

```text
All jastles are ulvets.
All tufas are zorks.
All murdles are ulvets.
All blickets are murdles.
Possible completions: ulvets or zorks.
Therefore, all blickets are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | correct_target |
| 4 | " murdles." | murdles | ulvets | reachable_one_hop |
| 12 | " murdles." | murdles | ulvets | reachable_one_hop |
## 090/twohop/base/1

```text
All tufas are zorks.
All murdles are blickets.
All jastles are blickets.
All ulvets are murdles.
Possible completions: zorks or blickets.
Therefore, all ulvets are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | wrong_candidate |
| 4 | " murdles." | murdles | blickets | reachable_one_hop |
| 12 | " murdles." | murdles | blickets | reachable_one_hop |
## 090/broken/first/0

```text
All jastles are ulvets.
All tufas are zorks.
All murdles are ulvets.
All blickets are tufas.
Possible completions: ulvets or zorks.
Therefore, all blickets are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | wrong_candidate |
| 4 | " tufas." | tufas | ulvets | reachable_one_hop |
| 12 | " tufas." | tufas | zorks | reachable_one_hop |
## 090/broken/second/1

```text
All jastles are ulvets.
All tufas are zorks.
All murdles are zorks.
All blickets are murdles.
Possible completions: ulvets or zorks.
Therefore, all blickets are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | zorks | reachable_one_hop |
| 4 | " murdles." | murdles | zorks | reachable_one_hop |
| 12 | " murdles." | murdles | zorks | reachable_one_hop |
## 090/robustness/reorder/0

```text
All tufas are zorks.
All jastles are ulvets.
All murdles are ulvets.
All blickets are murdles.
Possible completions: ulvets or zorks.
Therefore, all blickets are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | correct_target |
| 4 | " murdles." | murdles | ulvets | reachable_one_hop |
| 12 | " murdles." | murdles | zorks | reachable_one_hop |
## 090/robustness/reorder/1

```text
All jastles are blickets.
All tufas are zorks.
All murdles are blickets.
All ulvets are murdles.
Possible completions: zorks or blickets.
Therefore, all ulvets are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | zorks | reachable_one_hop |
| 4 | " murdles." | murdles | blickets | reachable_one_hop |
| 12 | " murdles." | murdles | blickets | reachable_one_hop |
## 090/robustness/distractors/0

```text
All blickets are murdles.
All nerps are ruspins.
All jastles are ulvets.
All murdles are ulvets.
All ruspins are zorks.
All tufas are zorks.
Possible completions: ulvets or zorks.
Therefore, all blickets are
```

אמת: **ulvets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | ulvets | correct_target |
| 4 | " ulvets." | ulvets | ulvets | correct_target |
| 12 | " zorks." | zorks | zorks | wrong_candidate |
## 090/robustness/distractors/1

```text
All tufas are zorks.
All ulvets are murdles.
All jastles are blickets.
All nerps are ruspins.
All murdles are blickets.
All ruspins are zorks.
Possible completions: zorks or blickets.
Therefore, all ulvets are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | wrong_candidate |
| 4 | " ruspins." | ruspins | blickets | unreachable_fact_name |
| 12 | " blickets." | blickets | blickets | correct_target |
## 090/robustness/rename/0

```text
All yorbits are welbins.
All brovets are snorps.
All korvas are welbins.
All quavels are korvas.
Possible completions: welbins or snorps.
Therefore, all quavels are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | welbins | reachable_one_hop |
| 4 | " korvas." | korvas | snorps | reachable_one_hop |
| 12 | " korvas." | korvas | snorps | reachable_one_hop |
## 090/robustness/rename/1

```text
All zemples are vibbles.
All nufrons are shalds.
All lomits are shalds.
All brovets are nufrons.
Possible completions: vibbles or shalds.
Therefore, all brovets are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | vibbles | reachable_one_hop |
| 4 | " nufrons." | nufrons | shalds | reachable_one_hop |
| 12 | " nufrons." | nufrons | shalds | reachable_one_hop |
## 091/direct/base/0

```text
All plinets are murdles.
All zemples are vibbles.
All vromps are tufas.
All murdles are tufas.
Possible completions: vibbles or murdles.
Therefore, all plinets are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " tufas." | tufas | vibbles | other_reachable |
| 12 | " tufas." | tufas | vibbles | other_reachable |
## 091/direct/base/1

```text
All plinets are murdles.
All zemples are vibbles.
All vromps are tufas.
All murdles are tufas.
Possible completions: tufas or vibbles.
Therefore, all murdles are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 091/twohop/base/0

```text
All plinets are murdles.
All zemples are vibbles.
All vromps are tufas.
All murdles are tufas.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 091/twohop/base/1

```text
All zemples are vibbles.
All tufas are murdles.
All vromps are plinets.
All murdles are plinets.
Possible completions: plinets or vibbles.
Therefore, all tufas are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 091/broken/first/0

```text
All plinets are zemples.
All zemples are vibbles.
All vromps are tufas.
All murdles are tufas.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " tufas." | tufas | tufas | wrong_candidate |
| 12 | " tufas." | tufas | tufas | wrong_candidate |
## 091/broken/second/1

```text
All plinets are murdles.
All zemples are vibbles.
All vromps are tufas.
All murdles are vibbles.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 091/robustness/reorder/0

```text
All zemples are vibbles.
All murdles are tufas.
All vromps are tufas.
All plinets are murdles.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " murdles." | murdles | tufas | reachable_one_hop |
| 12 | " murdles." | murdles | tufas | reachable_one_hop |
## 091/robustness/reorder/1

```text
All vromps are plinets.
All murdles are plinets.
All tufas are murdles.
All zemples are vibbles.
Possible completions: plinets or vibbles.
Therefore, all tufas are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | correct_target |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 091/robustness/distractors/0

```text
All murdles are tufas.
All korvas are vibbles.
All zemples are vibbles.
All plinets are murdles.
All ruspins are korvas.
All vromps are tufas.
Possible completions: vibbles or tufas.
Therefore, all plinets are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 091/robustness/distractors/1

```text
All korvas are vibbles.
All vromps are plinets.
All ruspins are korvas.
All murdles are plinets.
All tufas are murdles.
All zemples are vibbles.
Possible completions: plinets or vibbles.
Therefore, all tufas are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | vibbles | unreachable_fact_name |
| 4 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 12 | " vibbles." | vibbles | vibbles | wrong_candidate |
## 091/robustness/rename/0

```text
All nerps are daxes.
All jastles are prandils.
All lomits are korvas.
All daxes are korvas.
Possible completions: prandils or korvas.
Therefore, all nerps are
```

אמת: **korvas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | prandils | reachable_one_hop |
| 4 | " korvas." | korvas | korvas | correct_target |
| 12 | " prandils." | prandils | prandils | wrong_candidate |
## 091/robustness/rename/1

```text
All korvas are blickets.
All lomits are nerps.
All ruspins are shalds.
All nerps are shalds.
Possible completions: shalds or blickets.
Therefore, all lomits are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nerps." | nerps | shalds | reachable_one_hop |
| 4 | " ruspins." | ruspins | shalds | unreachable_fact_name |
| 12 | " blickets." | blickets | blickets | wrong_candidate |
## 092/direct/base/0

```text
All tivaks are lomits.
All lomits are brovets.
All zemples are kelbrins.
All crundles are brovets.
Possible completions: lomits or kelbrins.
Therefore, all tivaks are
```

אמת: **lomits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | kelbrins | correct_target |
| 4 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 12 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
## 092/direct/base/1

```text
All tivaks are lomits.
All lomits are brovets.
All zemples are kelbrins.
All crundles are brovets.
Possible completions: kelbrins or brovets.
Therefore, all lomits are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 4 | " brovets." | brovets | brovets | correct_target |
| 12 | " brovets." | brovets | brovets | correct_target |
## 092/twohop/base/0

```text
All tivaks are lomits.
All lomits are brovets.
All zemples are kelbrins.
All crundles are brovets.
Possible completions: brovets or kelbrins.
Therefore, all tivaks are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 4 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 12 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
## 092/twohop/base/1

```text
All brovets are lomits.
All zemples are kelbrins.
All crundles are tivaks.
All lomits are tivaks.
Possible completions: kelbrins or tivaks.
Therefore, all brovets are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | kelbrins | reachable_one_hop |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 092/broken/first/0

```text
All tivaks are zemples.
All lomits are brovets.
All zemples are kelbrins.
All crundles are brovets.
Possible completions: brovets or kelbrins.
Therefore, all tivaks are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 092/broken/second/1

```text
All tivaks are lomits.
All lomits are kelbrins.
All zemples are kelbrins.
All crundles are brovets.
Possible completions: brovets or kelbrins.
Therefore, all tivaks are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | wrong_candidate |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 092/robustness/reorder/0

```text
All crundles are brovets.
All zemples are kelbrins.
All lomits are brovets.
All tivaks are lomits.
Possible completions: brovets or kelbrins.
Therefore, all tivaks are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | correct_target |
| 4 | " lomits." | lomits | kelbrins | reachable_one_hop |
| 12 | " lomits." | lomits | kelbrins | reachable_one_hop |
## 092/robustness/reorder/1

```text
All zemples are kelbrins.
All crundles are tivaks.
All lomits are tivaks.
All brovets are lomits.
Possible completions: kelbrins or tivaks.
Therefore, all brovets are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | kelbrins | reachable_one_hop |
| 4 | " lomits." | lomits | tivaks | reachable_one_hop |
| 12 | " lomits." | lomits | tivaks | reachable_one_hop |
## 092/robustness/distractors/0

```text
All crundles are brovets.
All shalds are kelbrins.
All tivaks are lomits.
All zemples are kelbrins.
All oskets are shalds.
All lomits are brovets.
Possible completions: brovets or kelbrins.
Therefore, all tivaks are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | brovets | reachable_one_hop |
| 4 | " brovets." | brovets | brovets | correct_target |
| 12 | " brovets." | brovets | brovets | correct_target |
## 092/robustness/distractors/1

```text
All oskets are shalds.
All shalds are kelbrins.
All lomits are tivaks.
All zemples are kelbrins.
All brovets are lomits.
All crundles are tivaks.
Possible completions: kelbrins or tivaks.
Therefore, all brovets are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 4 | " lomits." | lomits | tivaks | reachable_one_hop |
| 12 | " lomits." | lomits | tivaks | reachable_one_hop |
## 092/robustness/rename/0

```text
All wugs are zorks.
All zorks are grivaks.
All zeltrons are snorps.
All plinets are grivaks.
Possible completions: grivaks or snorps.
Therefore, all wugs are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | grivaks | unreachable_fact_name |
| 4 | " snorps." | snorps | snorps | wrong_candidate |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 092/robustness/rename/1

```text
All welbins are korvas.
All quavels are vibbles.
All nerps are grivaks.
All korvas are grivaks.
Possible completions: vibbles or grivaks.
Therefore, all welbins are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | correct_target |
| 4 | " grivaks." | grivaks | grivaks | correct_target |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 093/direct/base/0

```text
All yorbits are tivaks.
All quavels are vibbles.
All tufas are vibbles.
All helpons are tufas.
Possible completions: tivaks or tufas.
Therefore, all helpons are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | tivaks | wrong_candidate |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 093/direct/base/1

```text
All yorbits are tivaks.
All quavels are vibbles.
All tufas are vibbles.
All helpons are tufas.
Possible completions: vibbles or tivaks.
Therefore, all tufas are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | correct_target |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 093/twohop/base/0

```text
All yorbits are tivaks.
All quavels are vibbles.
All tufas are vibbles.
All helpons are tufas.
Possible completions: tivaks or vibbles.
Therefore, all helpons are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | tivaks | wrong_candidate |
| 4 | " tufas." | tufas | vibbles | reachable_one_hop |
| 12 | " tufas." | tufas | vibbles | reachable_one_hop |
## 093/twohop/base/1

```text
All vibbles are tufas.
All tufas are helpons.
All yorbits are tivaks.
All quavels are helpons.
Possible completions: helpons or tivaks.
Therefore, all vibbles are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | helpons | reachable_one_hop |
| 4 | " tufas." | tufas | helpons | reachable_one_hop |
| 12 | " tivaks." | tivaks | tivaks | wrong_candidate |
## 093/broken/first/0

```text
All yorbits are tivaks.
All quavels are vibbles.
All tufas are vibbles.
All helpons are yorbits.
Possible completions: tivaks or vibbles.
Therefore, all helpons are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | tivaks | correct_target |
| 4 | " yorbits." | yorbits | tivaks | reachable_one_hop |
| 12 | " yorbits." | yorbits | tivaks | reachable_one_hop |
## 093/broken/second/1

```text
All yorbits are tivaks.
All quavels are vibbles.
All tufas are tivaks.
All helpons are tufas.
Possible completions: tivaks or vibbles.
Therefore, all helpons are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | tivaks | correct_target |
| 4 | " tufas." | tufas | tivaks | reachable_one_hop |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 093/robustness/reorder/0

```text
All yorbits are tivaks.
All helpons are tufas.
All tufas are vibbles.
All quavels are vibbles.
Possible completions: tivaks or vibbles.
Therefore, all helpons are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tivaks | reachable_one_hop |
| 4 | " tufas." | tufas | vibbles | reachable_one_hop |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 093/robustness/reorder/1

```text
All yorbits are tivaks.
All quavels are helpons.
All vibbles are tufas.
All tufas are helpons.
Possible completions: helpons or tivaks.
Therefore, all vibbles are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | helpons | reachable_one_hop |
| 4 | " helpons." | helpons | helpons | correct_target |
| 12 | " tufas." | tufas | helpons | reachable_one_hop |
## 093/robustness/distractors/0

```text
All tufas are vibbles.
All snorps are tivaks.
All quavels are vibbles.
All yorbits are tivaks.
All helpons are tufas.
All ruspins are snorps.
Possible completions: tivaks or vibbles.
Therefore, all helpons are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | vibbles | reachable_one_hop |
| 4 | " snorps." | snorps | vibbles | unreachable_fact_name |
| 12 | " snorps." | snorps | vibbles | unreachable_fact_name |
## 093/robustness/distractors/1

```text
All ruspins are snorps.
All tufas are helpons.
All vibbles are tufas.
All yorbits are tivaks.
All quavels are helpons.
All snorps are tivaks.
Possible completions: helpons or tivaks.
Therefore, all vibbles are
```

אמת: **helpons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | helpons | unreachable_fact_name |
| 4 | " tivaks." | tivaks | tivaks | wrong_candidate |
| 12 | " tivaks." | tivaks | tivaks | wrong_candidate |
## 093/robustness/rename/0

```text
All xandles are daxes.
All kelbrins are zorks.
All lomits are zorks.
All sprocks are lomits.
Possible completions: daxes or zorks.
Therefore, all sprocks are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " lomits." | lomits | daxes | reachable_one_hop |
| 4 | " lomits." | lomits | zorks | reachable_one_hop |
| 12 | " lomits." | lomits | zorks | reachable_one_hop |
## 093/robustness/rename/1

```text
All jastles are zorks.
All zorks are welbins.
All zeltrons are grivaks.
All snorps are welbins.
Possible completions: welbins or grivaks.
Therefore, all jastles are
```

אמת: **welbins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " welbins." | welbins | welbins | correct_target |
| 4 | " zorks." | zorks | grivaks | reachable_one_hop |
| 12 | " snorps." | snorps | grivaks | unreachable_fact_name |
## 094/direct/base/0

```text
All daxes are tufas.
All tivaks are crundles.
All quavels are tivaks.
All blickets are crundles.
Possible completions: tivaks or tufas.
Therefore, all quavels are
```

אמת: **tivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | tivaks | unreachable_fact_name |
| 4 | " tivaks." | tivaks | tivaks | correct_target |
| 12 | " tivaks." | tivaks | tivaks | correct_target |
## 094/direct/base/1

```text
All daxes are tufas.
All tivaks are crundles.
All quavels are tivaks.
All blickets are crundles.
Possible completions: tufas or crundles.
Therefore, all tivaks are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " quavels." | quavels | crundles | unreachable_fact_name |
| 4 | " crundles." | crundles | crundles | correct_target |
| 12 | " crundles." | crundles | crundles | correct_target |
## 094/twohop/base/0

```text
All daxes are tufas.
All tivaks are crundles.
All quavels are tivaks.
All blickets are crundles.
Possible completions: crundles or tufas.
Therefore, all quavels are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " blickets." | blickets | crundles | unreachable_fact_name |
| 4 | " tivaks." | tivaks | crundles | reachable_one_hop |
| 12 | " tivaks." | tivaks | crundles | reachable_one_hop |
## 094/twohop/base/1

```text
All crundles are tivaks.
All tivaks are quavels.
All daxes are tufas.
All blickets are quavels.
Possible completions: tufas or quavels.
Therefore, all crundles are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | wrong_candidate |
| 4 | " tufas." | tufas | quavels | wrong_candidate |
| 12 | " tufas." | tufas | tufas | wrong_candidate |
## 094/broken/first/0

```text
All daxes are tufas.
All tivaks are crundles.
All quavels are daxes.
All blickets are crundles.
Possible completions: crundles or tufas.
Therefore, all quavels are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | tufas | reachable_one_hop |
| 4 | " tufas." | tufas | tufas | correct_target |
| 12 | " tufas." | tufas | tufas | correct_target |
## 094/broken/second/1

```text
All daxes are tufas.
All tivaks are tufas.
All quavels are tivaks.
All blickets are crundles.
Possible completions: crundles or tufas.
Therefore, all quavels are
```

אמת: **tufas**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | correct_target |
| 4 | " tivaks." | tivaks | tufas | reachable_one_hop |
| 12 | " tivaks." | tivaks | crundles | reachable_one_hop |
## 094/robustness/reorder/0

```text
All tivaks are crundles.
All quavels are tivaks.
All daxes are tufas.
All blickets are crundles.
Possible completions: crundles or tufas.
Therefore, all quavels are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | crundles | reachable_one_hop |
| 4 | " tivaks." | tivaks | tufas | reachable_one_hop |
| 12 | " tufas." | tufas | tufas | wrong_candidate |
## 094/robustness/reorder/1

```text
All blickets are quavels.
All daxes are tufas.
All tivaks are quavels.
All crundles are tivaks.
Possible completions: tufas or quavels.
Therefore, all crundles are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tivaks." | tivaks | quavels | reachable_one_hop |
| 4 | " tivaks." | tivaks | quavels | reachable_one_hop |
| 12 | " tivaks." | tivaks | quavels | reachable_one_hop |
## 094/robustness/distractors/0

```text
All snorps are korvas.
All blickets are crundles.
All tivaks are crundles.
All quavels are tivaks.
All daxes are tufas.
All korvas are tufas.
Possible completions: crundles or tufas.
Therefore, all quavels are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " korvas." | korvas | tufas | unreachable_fact_name |
| 4 | " tufas." | tufas | tufas | wrong_candidate |
| 12 | " tufas." | tufas | tufas | wrong_candidate |
## 094/robustness/distractors/1

```text
All daxes are tufas.
All korvas are tufas.
All snorps are korvas.
All tivaks are quavels.
All blickets are quavels.
All crundles are tivaks.
Possible completions: tufas or quavels.
Therefore, all crundles are
```

אמת: **quavels**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | tufas | wrong_candidate |
| 4 | " tivaks." | tivaks | quavels | reachable_one_hop |
| 12 | " tivaks." | tivaks | quavels | reachable_one_hop |
## 094/robustness/rename/0

```text
All jastles are zemples.
All vromps are vibbles.
All wugs are vromps.
All kelbrins are vibbles.
Possible completions: vibbles or zemples.
Therefore, all wugs are
```

אמת: **vibbles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | zemples | unreachable_fact_name |
| 4 | " vibbles." | vibbles | vibbles | correct_target |
| 12 | " vibbles." | vibbles | vibbles | correct_target |
## 094/robustness/rename/1

```text
All murdles are shalds.
All shalds are flomps.
All lomits are vibbles.
All jastles are flomps.
Possible completions: vibbles or flomps.
Therefore, all murdles are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | vibbles | wrong_candidate |
| 4 | " flomps." | flomps | flomps | correct_target |
| 12 | " flomps." | flomps | flomps | correct_target |
## 095/direct/base/0

```text
All zemples are jastles.
All korvas are jastles.
All ruspins are nufrons.
All plinets are zemples.
Possible completions: nufrons or zemples.
Therefore, all plinets are
```

אמת: **zemples**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 4 | " zemples." | zemples | zemples | correct_target |
| 12 | " zemples." | zemples | zemples | correct_target |
## 095/direct/base/1

```text
All zemples are jastles.
All korvas are jastles.
All ruspins are nufrons.
All plinets are zemples.
Possible completions: jastles or nufrons.
Therefore, all zemples are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " jastles." | jastles | jastles | correct_target |
| 12 | " jastles." | jastles | jastles | correct_target |
## 095/twohop/base/0

```text
All zemples are jastles.
All korvas are jastles.
All ruspins are nufrons.
All plinets are zemples.
Possible completions: nufrons or jastles.
Therefore, all plinets are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " zemples." | zemples | jastles | reachable_one_hop |
| 12 | " zemples." | zemples | jastles | reachable_one_hop |
## 095/twohop/base/1

```text
All jastles are zemples.
All korvas are plinets.
All zemples are plinets.
All ruspins are nufrons.
Possible completions: plinets or nufrons.
Therefore, all jastles are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | correct_target |
| 4 | " ruspins." | ruspins | plinets | unreachable_fact_name |
| 12 | " plinets." | plinets | plinets | correct_target |
## 095/broken/first/0

```text
All zemples are jastles.
All korvas are jastles.
All ruspins are nufrons.
All plinets are ruspins.
Possible completions: nufrons or jastles.
Therefore, all plinets are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | wrong_candidate |
| 4 | " ruspins." | ruspins | jastles | reachable_one_hop |
| 12 | " ruspins." | ruspins | jastles | reachable_one_hop |
## 095/broken/second/1

```text
All zemples are nufrons.
All korvas are jastles.
All ruspins are nufrons.
All plinets are zemples.
Possible completions: nufrons or jastles.
Therefore, all plinets are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | nufrons | reachable_one_hop |
| 4 | " zemples." | zemples | nufrons | reachable_one_hop |
| 12 | " zemples." | zemples | nufrons | reachable_one_hop |
## 095/robustness/reorder/0

```text
All korvas are jastles.
All zemples are jastles.
All plinets are zemples.
All ruspins are nufrons.
Possible completions: nufrons or jastles.
Therefore, all plinets are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | jastles | unreachable_fact_name |
| 4 | " zemples." | zemples | jastles | reachable_one_hop |
| 12 | " zemples." | zemples | jastles | reachable_one_hop |
## 095/robustness/reorder/1

```text
All zemples are plinets.
All jastles are zemples.
All ruspins are nufrons.
All korvas are plinets.
Possible completions: plinets or nufrons.
Therefore, all jastles are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " plinets." | plinets | plinets | correct_target |
| 4 | " zemples." | zemples | plinets | reachable_one_hop |
| 12 | " plinets." | plinets | plinets | correct_target |
## 095/robustness/distractors/0

```text
All zemples are jastles.
All korvas are jastles.
All zeltrons are sprocks.
All ruspins are nufrons.
All sprocks are nufrons.
All plinets are zemples.
Possible completions: nufrons or jastles.
Therefore, all plinets are
```

אמת: **jastles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " jastles." | jastles | jastles | correct_target |
| 4 | " zemples." | zemples | jastles | reachable_one_hop |
| 12 | " zemples." | zemples | jastles | reachable_one_hop |
## 095/robustness/distractors/1

```text
All zemples are plinets.
All ruspins are nufrons.
All jastles are zemples.
All zeltrons are sprocks.
All korvas are plinets.
All sprocks are nufrons.
Possible completions: plinets or nufrons.
Therefore, all jastles are
```

אמת: **plinets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zemples." | zemples | plinets | reachable_one_hop |
| 4 | " zemples." | zemples | plinets | reachable_one_hop |
| 12 | " zemples." | zemples | plinets | reachable_one_hop |
## 095/robustness/rename/0

```text
All vibbles are wugs.
All yorbits are wugs.
All tivaks are quavels.
All kelbrins are vibbles.
Possible completions: quavels or wugs.
Therefore, all kelbrins are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | wugs | reachable_one_hop |
| 4 | " vibbles." | vibbles | wugs | reachable_one_hop |
| 12 | " vibbles." | vibbles | wugs | reachable_one_hop |
## 095/robustness/rename/1

```text
All vibbles are vromps.
All blickets are zorks.
All vromps are zorks.
All nerps are lomits.
Possible completions: zorks or lomits.
Therefore, all vibbles are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " zorks." | zorks | zorks | correct_target |
| 4 | " vromps." | vromps | lomits | reachable_one_hop |
| 12 | " lomits." | lomits | lomits | wrong_candidate |
## 096/direct/base/0

```text
All kelbrins are wugs.
All grivaks are ruspins.
All korvas are daxes.
All wugs are ruspins.
Possible completions: wugs or daxes.
Therefore, all kelbrins are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 096/direct/base/1

```text
All kelbrins are wugs.
All grivaks are ruspins.
All korvas are daxes.
All wugs are ruspins.
Possible completions: daxes or ruspins.
Therefore, all wugs are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 096/twohop/base/0

```text
All kelbrins are wugs.
All grivaks are ruspins.
All korvas are daxes.
All wugs are ruspins.
Possible completions: ruspins or daxes.
Therefore, all kelbrins are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | daxes | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 096/twohop/base/1

```text
All ruspins are wugs.
All grivaks are kelbrins.
All wugs are kelbrins.
All korvas are daxes.
Possible completions: daxes or kelbrins.
Therefore, all ruspins are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 096/broken/first/0

```text
All kelbrins are korvas.
All grivaks are ruspins.
All korvas are daxes.
All wugs are ruspins.
Possible completions: ruspins or daxes.
Therefore, all kelbrins are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | wrong_candidate |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 096/broken/second/1

```text
All kelbrins are wugs.
All grivaks are ruspins.
All korvas are daxes.
All wugs are daxes.
Possible completions: ruspins or daxes.
Therefore, all kelbrins are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | daxes | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | correct_target |
| 12 | " daxes." | daxes | daxes | correct_target |
## 096/robustness/reorder/0

```text
All korvas are daxes.
All kelbrins are wugs.
All grivaks are ruspins.
All wugs are ruspins.
Possible completions: ruspins or daxes.
Therefore, all kelbrins are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | daxes | reachable_one_hop |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 096/robustness/reorder/1

```text
All wugs are kelbrins.
All ruspins are wugs.
All korvas are daxes.
All grivaks are kelbrins.
Possible completions: daxes or kelbrins.
Therefore, all ruspins are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | kelbrins | unreachable_fact_name |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 096/robustness/distractors/0

```text
All tufas are murdles.
All kelbrins are wugs.
All wugs are ruspins.
All murdles are daxes.
All grivaks are ruspins.
All korvas are daxes.
Possible completions: ruspins or daxes.
Therefore, all kelbrins are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ruspins." | ruspins | ruspins | correct_target |
| 4 | " daxes." | daxes | daxes | wrong_candidate |
| 12 | " daxes." | daxes | daxes | wrong_candidate |
## 096/robustness/distractors/1

```text
All tufas are murdles.
All murdles are daxes.
All korvas are daxes.
All ruspins are wugs.
All grivaks are kelbrins.
All wugs are kelbrins.
Possible completions: daxes or kelbrins.
Therefore, all ruspins are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | kelbrins | reachable_one_hop |
| 4 | " kelbrins." | kelbrins | kelbrins | correct_target |
| 12 | " kelbrins." | kelbrins | kelbrins | correct_target |
## 096/robustness/rename/0

```text
All quavels are tufas.
All helpons are flomps.
All nufrons are lomits.
All tufas are flomps.
Possible completions: flomps or lomits.
Therefore, all quavels are
```

אמת: **flomps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " tufas." | tufas | flomps | reachable_one_hop |
| 4 | " tufas." | tufas | flomps | reachable_one_hop |
| 12 | " tufas." | tufas | flomps | reachable_one_hop |
## 096/robustness/rename/1

```text
All zemples are vibbles.
All shalds are nufrons.
All vibbles are nufrons.
All tufas are vromps.
Possible completions: vromps or nufrons.
Therefore, all zemples are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | nufrons | reachable_one_hop |
| 4 | " vibbles." | vibbles | nufrons | reachable_one_hop |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 097/direct/base/0

```text
All flomps are oskets.
All nufrons are wugs.
All daxes are yorbits.
All yorbits are wugs.
Possible completions: oskets or yorbits.
Therefore, all daxes are
```

אמת: **yorbits**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | yorbits | other_reachable |
| 4 | " wugs." | wugs | yorbits | other_reachable |
| 12 | " wugs." | wugs | yorbits | other_reachable |
## 097/direct/base/1

```text
All flomps are oskets.
All nufrons are wugs.
All daxes are yorbits.
All yorbits are wugs.
Possible completions: wugs or oskets.
Therefore, all yorbits are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " wugs." | wugs | wugs | correct_target |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 097/twohop/base/0

```text
All flomps are oskets.
All nufrons are wugs.
All daxes are yorbits.
All yorbits are wugs.
Possible completions: oskets or wugs.
Therefore, all daxes are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | oskets | reachable_one_hop |
| 4 | " yorbits." | yorbits | wugs | reachable_one_hop |
| 12 | " yorbits." | yorbits | wugs | reachable_one_hop |
## 097/twohop/base/1

```text
All yorbits are daxes.
All nufrons are daxes.
All flomps are oskets.
All wugs are yorbits.
Possible completions: daxes or oskets.
Therefore, all wugs are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | daxes | reachable_one_hop |
| 4 | " yorbits." | yorbits | daxes | reachable_one_hop |
| 12 | " yorbits." | yorbits | daxes | reachable_one_hop |
## 097/broken/first/0

```text
All flomps are oskets.
All nufrons are wugs.
All daxes are flomps.
All yorbits are wugs.
Possible completions: oskets or wugs.
Therefore, all daxes are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " flomps." | flomps | oskets | reachable_one_hop |
| 4 | " flomps." | flomps | wugs | reachable_one_hop |
| 12 | " flomps." | flomps | wugs | reachable_one_hop |
## 097/broken/second/1

```text
All flomps are oskets.
All nufrons are wugs.
All daxes are yorbits.
All yorbits are oskets.
Possible completions: oskets or wugs.
Therefore, all daxes are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | oskets | reachable_one_hop |
| 4 | " yorbits." | yorbits | oskets | reachable_one_hop |
| 12 | " yorbits." | yorbits | oskets | reachable_one_hop |
## 097/robustness/reorder/0

```text
All nufrons are wugs.
All flomps are oskets.
All daxes are yorbits.
All yorbits are wugs.
Possible completions: oskets or wugs.
Therefore, all daxes are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | wugs | reachable_one_hop |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 097/robustness/reorder/1

```text
All flomps are oskets.
All yorbits are daxes.
All nufrons are daxes.
All wugs are yorbits.
Possible completions: daxes or oskets.
Therefore, all wugs are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | daxes | reachable_one_hop |
| 4 | " yorbits." | yorbits | daxes | reachable_one_hop |
| 12 | " yorbits." | yorbits | daxes | reachable_one_hop |
## 097/robustness/distractors/0

```text
All flomps are oskets.
All blickets are zeltrons.
All nufrons are wugs.
All daxes are yorbits.
All yorbits are wugs.
All zeltrons are oskets.
Possible completions: oskets or wugs.
Therefore, all daxes are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " yorbits." | yorbits | wugs | reachable_one_hop |
| 4 | " yorbits." | yorbits | wugs | reachable_one_hop |
| 12 | " yorbits." | yorbits | wugs | reachable_one_hop |
## 097/robustness/distractors/1

```text
All zeltrons are oskets.
All nufrons are daxes.
All yorbits are daxes.
All flomps are oskets.
All blickets are zeltrons.
All wugs are yorbits.
Possible completions: daxes or oskets.
Therefore, all wugs are
```

אמת: **daxes**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | correct_target |
| 4 | " yorbits." | yorbits | daxes | reachable_one_hop |
| 12 | " yorbits." | yorbits | daxes | reachable_one_hop |
## 097/robustness/rename/0

```text
All blickets are murdles.
All jastles are vromps.
All lomits are shalds.
All shalds are vromps.
Possible completions: murdles or vromps.
Therefore, all lomits are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " shalds." | shalds | vromps | reachable_one_hop |
| 4 | " shalds." | shalds | vromps | reachable_one_hop |
| 12 | " shalds." | shalds | vromps | reachable_one_hop |
## 097/robustness/rename/1

```text
All ulvets are vromps.
All helpons are vromps.
All lomits are nerps.
All murdles are ulvets.
Possible completions: vromps or nerps.
Therefore, all murdles are
```

אמת: **vromps**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " ulvets." | ulvets | vromps | reachable_one_hop |
| 4 | " ulvets." | ulvets | vromps | reachable_one_hop |
| 12 | " ulvets." | ulvets | vromps | reachable_one_hop |
## 098/direct/base/0

```text
All yorbits are brovets.
All wugs are murdles.
All plinets are kelbrins.
All murdles are brovets.
Possible completions: murdles or kelbrins.
Therefore, all wugs are
```

אמת: **murdles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | murdles | other_reachable |
| 4 | " brovets." | brovets | murdles | other_reachable |
| 12 | " brovets." | brovets | murdles | other_reachable |
## 098/direct/base/1

```text
All yorbits are brovets.
All wugs are murdles.
All plinets are kelbrins.
All murdles are brovets.
Possible completions: kelbrins or brovets.
Therefore, all murdles are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " brovets." | brovets | brovets | correct_target |
| 4 | " brovets." | brovets | brovets | correct_target |
| 12 | " brovets." | brovets | brovets | correct_target |
## 098/twohop/base/0

```text
All yorbits are brovets.
All wugs are murdles.
All plinets are kelbrins.
All murdles are brovets.
Possible completions: brovets or kelbrins.
Therefore, all wugs are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | brovets | reachable_one_hop |
| 4 | " murdles." | murdles | brovets | reachable_one_hop |
| 12 | " murdles." | murdles | brovets | reachable_one_hop |
## 098/twohop/base/1

```text
All brovets are murdles.
All murdles are wugs.
All plinets are kelbrins.
All yorbits are wugs.
Possible completions: kelbrins or wugs.
Therefore, all brovets are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | kelbrins | reachable_one_hop |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 098/broken/first/0

```text
All yorbits are brovets.
All wugs are plinets.
All plinets are kelbrins.
All murdles are brovets.
Possible completions: brovets or kelbrins.
Therefore, all wugs are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | brovets | unreachable_fact_name |
| 4 | " plinets." | plinets | brovets | reachable_one_hop |
| 12 | " plinets." | plinets | brovets | reachable_one_hop |
## 098/broken/second/1

```text
All yorbits are brovets.
All wugs are murdles.
All plinets are kelbrins.
All murdles are kelbrins.
Possible completions: brovets or kelbrins.
Therefore, all wugs are
```

אמת: **kelbrins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | brovets | reachable_one_hop |
| 4 | " murdles." | murdles | kelbrins | reachable_one_hop |
| 12 | " murdles." | murdles | kelbrins | reachable_one_hop |
## 098/robustness/reorder/0

```text
All wugs are murdles.
All plinets are kelbrins.
All murdles are brovets.
All yorbits are brovets.
Possible completions: brovets or kelbrins.
Therefore, all wugs are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | brovets | reachable_one_hop |
| 4 | " brovets." | brovets | brovets | correct_target |
| 12 | " brovets." | brovets | brovets | correct_target |
## 098/robustness/reorder/1

```text
All brovets are murdles.
All yorbits are wugs.
All plinets are kelbrins.
All murdles are wugs.
Possible completions: kelbrins or wugs.
Therefore, all brovets are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | kelbrins | reachable_one_hop |
| 4 | " wugs." | wugs | wugs | correct_target |
| 12 | " wugs." | wugs | wugs | correct_target |
## 098/robustness/distractors/0

```text
All jastles are nerps.
All nerps are kelbrins.
All wugs are murdles.
All plinets are kelbrins.
All murdles are brovets.
All yorbits are brovets.
Possible completions: brovets or kelbrins.
Therefore, all wugs are
```

אמת: **brovets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | brovets | reachable_one_hop |
| 4 | " murdles." | murdles | kelbrins | reachable_one_hop |
| 12 | " murdles." | murdles | brovets | reachable_one_hop |
## 098/robustness/distractors/1

```text
All brovets are murdles.
All nerps are kelbrins.
All plinets are kelbrins.
All murdles are wugs.
All yorbits are wugs.
All jastles are nerps.
Possible completions: kelbrins or wugs.
Therefore, all brovets are
```

אמת: **wugs**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " murdles." | murdles | kelbrins | reachable_one_hop |
| 4 | " murdles." | murdles | wugs | reachable_one_hop |
| 12 | " wugs." | wugs | wugs | correct_target |
## 098/robustness/rename/0

```text
All prandils are crundles.
All quavels are vibbles.
All tufas are helpons.
All vibbles are crundles.
Possible completions: crundles or helpons.
Therefore, all quavels are
```

אמת: **crundles**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " vibbles." | vibbles | crundles | reachable_one_hop |
| 4 | " vibbles." | vibbles | crundles | reachable_one_hop |
| 12 | " vibbles." | vibbles | crundles | reachable_one_hop |
## 098/robustness/rename/1

```text
All helpons are ulvets.
All ulvets are ruspins.
All korvas are daxes.
All flomps are ruspins.
Possible completions: daxes or ruspins.
Therefore, all helpons are
```

אמת: **ruspins**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " daxes." | daxes | daxes | wrong_candidate |
| 4 | " ruspins." | ruspins | ruspins | correct_target |
| 12 | " ruspins." | ruspins | ruspins | correct_target |
## 099/direct/base/0

```text
All zorks are oskets.
All lomits are nufrons.
All oskets are nufrons.
All nerps are grivaks.
Possible completions: grivaks or oskets.
Therefore, all zorks are
```

אמת: **oskets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | wrong_candidate |
| 4 | " oskets." | oskets | oskets | correct_target |
| 12 | " oskets." | oskets | oskets | correct_target |
## 099/direct/base/1

```text
All zorks are oskets.
All lomits are nufrons.
All oskets are nufrons.
All nerps are grivaks.
Possible completions: nufrons or grivaks.
Therefore, all oskets are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " nufrons." | nufrons | nufrons | correct_target |
| 4 | " nufrons." | nufrons | nufrons | correct_target |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 099/twohop/base/0

```text
All zorks are oskets.
All lomits are nufrons.
All oskets are nufrons.
All nerps are grivaks.
Possible completions: grivaks or nufrons.
Therefore, all zorks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | wrong_candidate |
| 4 | " oskets." | oskets | grivaks | reachable_one_hop |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 099/twohop/base/1

```text
All nufrons are oskets.
All nerps are grivaks.
All oskets are zorks.
All lomits are zorks.
Possible completions: zorks or grivaks.
Therefore, all nufrons are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | grivaks | reachable_one_hop |
| 4 | " oskets." | oskets | grivaks | reachable_one_hop |
| 12 | " grivaks." | grivaks | grivaks | wrong_candidate |
## 099/broken/first/0

```text
All zorks are nerps.
All lomits are nufrons.
All oskets are nufrons.
All nerps are grivaks.
Possible completions: grivaks or nufrons.
Therefore, all zorks are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | correct_target |
| 4 | " nufrons." | nufrons | nufrons | wrong_candidate |
| 12 | " nufrons." | nufrons | nufrons | wrong_candidate |
## 099/broken/second/1

```text
All zorks are oskets.
All lomits are nufrons.
All oskets are grivaks.
All nerps are grivaks.
Possible completions: grivaks or nufrons.
Therefore, all zorks are
```

אמת: **grivaks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " grivaks." | grivaks | grivaks | correct_target |
| 4 | " oskets." | oskets | grivaks | reachable_one_hop |
| 12 | " grivaks." | grivaks | grivaks | correct_target |
## 099/robustness/reorder/0

```text
All oskets are nufrons.
All nerps are grivaks.
All lomits are nufrons.
All zorks are oskets.
Possible completions: grivaks or nufrons.
Therefore, all zorks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | grivaks | reachable_one_hop |
| 4 | " oskets." | oskets | grivaks | reachable_one_hop |
| 12 | " oskets." | oskets | nufrons | reachable_one_hop |
## 099/robustness/reorder/1

```text
All nufrons are oskets.
All oskets are zorks.
All nerps are grivaks.
All lomits are zorks.
Possible completions: zorks or grivaks.
Therefore, all nufrons are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | grivaks | reachable_one_hop |
| 4 | " grivaks." | grivaks | grivaks | wrong_candidate |
| 12 | " grivaks." | grivaks | grivaks | wrong_candidate |
## 099/robustness/distractors/0

```text
All zorks are oskets.
All flomps are grivaks.
All lomits are nufrons.
All blickets are flomps.
All nerps are grivaks.
All oskets are nufrons.
Possible completions: grivaks or nufrons.
Therefore, all zorks are
```

אמת: **nufrons**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | grivaks | reachable_one_hop |
| 4 | " oskets." | oskets | nufrons | reachable_one_hop |
| 12 | " nufrons." | nufrons | nufrons | correct_target |
## 099/robustness/distractors/1

```text
All nerps are grivaks.
All lomits are zorks.
All nufrons are oskets.
All blickets are flomps.
All oskets are zorks.
All flomps are grivaks.
Possible completions: zorks or grivaks.
Therefore, all nufrons are
```

אמת: **zorks**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " oskets." | oskets | zorks | reachable_one_hop |
| 4 | " grivaks." | grivaks | grivaks | wrong_candidate |
| 12 | " grivaks." | grivaks | grivaks | wrong_candidate |
## 099/robustness/rename/0

```text
All shalds are yorbits.
All ruspins are blickets.
All yorbits are blickets.
All helpons are kelbrins.
Possible completions: kelbrins or blickets.
Therefore, all shalds are
```

אמת: **blickets**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
| 4 | " yorbits." | yorbits | blickets | reachable_one_hop |
| 12 | " kelbrins." | kelbrins | kelbrins | wrong_candidate |
## 099/robustness/rename/1

```text
All quavels are snorps.
All flomps are welbins.
All snorps are shalds.
All plinets are shalds.
Possible completions: shalds or welbins.
Therefore, all quavels are
```

אמת: **shalds**

| הדגמות | פלט מדויק | free | candidate | סוג התשובה |
|---|---|---|---|---|
| 0 | " snorps." | snorps | shalds | reachable_one_hop |
| 4 | " snorps." | snorps | shalds | reachable_one_hop |
| 12 | " shalds." | shalds | shalds | correct_target |