"""Audit and analyze frozen v3 runs; use family-level bootstrap for uncertainty."""
from pathlib import Path
from collections import Counter, defaultdict
import hashlib
import json
import math
import random
import re
import statistics as st
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'results/prompt_v3_analysis'; OUT.mkdir(exist_ok=True)
def read(p): return [json.loads(s) for s in p.read_text().splitlines()]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def ci(values):
    rng=random.Random(20260908)
    a=sorted(st.mean(rng.choices(values,k=len(values))) for _ in range(3000))
    return [a[74],a[2924]]
def entails(edges,q):
    seen={q[0]}
    while True:
        nxt=seen|{b for a,b in edges if a in seen}
        if nxt==seen: return q[1] in seen
        seen=nxt
def metric(rs):
    pos=[r for r in rs if r['gold']=='Yes']; neg=[r for r in rs if r['gold']=='No']
    families=defaultdict(list)
    for r in rs: families[r['family']].append(r)
    fmeans=[st.mean(r['free_correct'] for r in v) for v in families.values()]
    auc=sum((a['yes_minus_no']>b['yes_minus_no'])+0.5*(a['yes_minus_no']==b['yes_minus_no']) for a in pos for b in neg)/(len(pos)*len(neg)) if pos and neg else None
    return dict(n=len(rs),free_correct=sum(r['free_correct'] for r in rs),
        candidate_correct=sum(r['correct'] for r in rs),free_accuracy=st.mean(r['free_correct'] for r in rs),
        ci95_family_bootstrap=ci(fmeans),free_predictions=dict(Counter(r['free_label'] for r in rs)),
        candidate_predictions=dict(Counter(r['predicted'] for r in rs)),
        yes_correct=sum(r['free_correct'] for r in pos),yes_n=len(pos),
        no_correct=sum(r['free_correct'] for r in neg),no_n=len(neg),auc=auc,
        mean_margin=st.mean(r['yes_minus_no'] for r in rs))
report={}; datasets={}; examples=['# שאלות ותשובות — פרומפט v3\n']
for n in (4,12):
    folder=ROOT/f'results/prompt_v3_review/full_prompt_v3_{n}shot_v1'
    rs=read(folder/'results.jsonl'); datasets[n]=rs
    data=ROOT/f'pilot_v2/data/pilot_{n}shot_prompt_v3.jsonl'
    source={r['id']:r for r in read(data)}
    worker=next((folder/'workers').iterdir())
    manifest=json.loads((worker/'manifest.json').read_text())
    sessions=[json.loads(p.read_text()) for p in worker.glob('session_*.json')]
    issues=[]
    if len(rs)!=1200 or len({r['id'] for r in rs})!=1200 or {r['id'] for r in rs}!=set(source): issues.append('Coverage')
    if manifest['data_sha256']!=sha(data): issues.append('Data hash')
    if manifest['code_sha256']!=sha(ROOT/'pilot_v2/pilot.py'): issues.append('Code hash')
    if manifest['attention']!='sdpa_math': issues.append('Attention backend')
    if read(worker/'results.jsonl')!=rs: issues.append('Merged rows')
    for r in rs:
        if any(r.get(k)!=v for k,v in source[r['id']].items()): issues.append('Input '+r['id'])
        if r['gold']!=('Yes' if entails(r['edges'],r['query']) else 'No'): issues.append('Gold '+r['id'])
        vals=[r['yes_minus_no'],*r['candidate_logprobs'].values(),*r['first_answer_logits'].values()]
        if not all(math.isfinite(x) for x in vals): issues.append('Nonfinite '+r['id'])
        m=r['candidate_logprobs']['Yes']-r['candidate_logprobs']['No']
        p='Yes' if m>0 else 'No' if m<0 else 'Tie'
        free=re.match(r'^\s*(Yes|No)\b',r['generated'])
        free=free.group(1) if free else None
        if p!=r['predicted'] or free!=r['free_label'] or (p==r['gold'])!=r['correct'] or (free==r['gold'])!=r['free_correct']: issues.append('Scoring '+r['id'])
    groups={k:metric([r for r in rs if r['check']==k]) for k in ('direct','twohop','broken','robustness')}
    sub={f'{check}/{v}':metric([r for r in rs if r['check']==check and r['variant']==v]) for check,vs in [('broken',['first','second']),('robustness',['reorder','distractors','rename'])] for v in vs}
    last={label:dict(n=sum(r['icl_last_label']==label for r in rs),
        free_predictions=dict(Counter(r['free_label'] for r in rs if r['icl_last_label']==label)),
        mean_margin=st.mean(r['yes_minus_no'] for r in rs if r['icl_last_label']==label)) for label in ('Yes','No')}
    paired={}; fam=defaultdict(dict)
    for r in rs: fam[r['family']][r['check'],r['variant'],r['polarity']]=r
    for v in ('first','second'):
        pairs=[(f['twohop','base','positive'],f['broken',v,'negative']) for f in fam.values()]
        paired[v]=dict(both_free_correct=sum(a['free_correct'] and b['free_correct'] for a,b in pairs),n=len(pairs),
            margin_decreases=sum(a['yes_minus_no']>b['yes_minus_no'] for a,b in pairs))
    correct_pairs={k:sum(f[k,'base','positive']['free_correct'] and f[k,'base','negative']['free_correct'] for f in fam.values()) for k in ('direct','twohop')}
    old=read(ROOT/f'results/full_sdpa_review/full_sdpa_{n}shot_v1/results.jsonl')
    report[n]=dict(issues=issues,overall=metric(rs),groups=groups,subgroups=sub,last_demo=last,
        paired=paired,both_polarities_correct=correct_pairs,
        old_accuracy={k:st.mean(r['free_correct'] for r in old if r['check']==k) for k in groups},
        changed_vs_old=sum(r['free_label']!=o['free_label'] for r,o in zip(rs,old)),
        elapsed_minutes=sum(s['elapsed_seconds'] for s in sessions)/60,
        peak_gpu_gib=[s['peak_allocated_gpu_gib'] for s in sessions])
    for r in rs:
        if r['family']==0 or r['free_label']=='Yes' or r['predicted']=='Tie':
            examples.append(f"## {n}-shot: {r['id']}\n\nאמת: {r['gold']}; תשובה: {r['free_label']}; בחירת מועמד: {r['predicted']}; הדגמה אחרונה: {r['icl_last_label']}; פער: {r['yes_minus_no']:.6f}\n\n```text\n{r['prompt']}\n```\n\nפלט:\n\n```text\n{r['generated']}\n```\n")
delta={}
for key in ('direct','twohop','broken','robustness'):
    byfamily=defaultdict(list)
    for a,b in zip(datasets[4],datasets[12]):
        assert a['id']==b['id']
        if a['check']==key: byfamily[a['family']].append(int(b['free_correct'])-int(a['free_correct']))
    vals=[st.mean(v) for v in byfamily.values()]
    delta[key]=dict(delta=st.mean(vals),ci95_family_bootstrap=ci(vals))
report['delta_12_minus_4']=delta
(OUT/'audit_and_statistics.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
(OUT/'EXAMPLES_HE.md').write_text('\n'.join(examples),encoding='utf-8')
lines=['# תוצאות ארבעת המבחנים — פרומפט v3\n',
       'שתי ההרצות מכילות 1,200 רשומות ייחודיות כל אחת. בדיקות ההתאמה לדאטה המקומי, חתימות הקוד והדאטה, תוויות האמת וחישוב המדדים עברו. כל ציוני התשובות השמורים סופיים. המניפסט מתעד sdpa_math.\n',
       'הדיוק בדוח מתייחס לתשובה החופשית המתחילה ב־Yes או No. כל 2,400 התשובות עמדו בפורמט. בארבע הדגמות היו שלושה מקרי תיקו בין ציוני המועמדים, שבהם ההפקה החופשית בחרה No.\n',
       '| מבחן | מספר שאלות לכל הרצה | 4 הדגמות | 12 הדגמות |\n|---|---:|---:|---:|']
labels={'direct':'קשר ישיר','twohop':'שני צעדים','broken':'שרשרת שבורה','robustness':'עמידות לשינויים'}
for k,label in labels.items():
    a,b=report[4]['groups'][k],report[12]['groups'][k]
    lines.append(f"| {label} | {a['n']} | {a['free_correct']}/{a['n']} ({a['free_accuracy']:.2%}) | {b['free_correct']}/{b['n']} ({b['free_accuracy']:.2%}) |")
lines += ['\n## פירוט תתי־המבחנים\n','| תנאי | 4: חיובי נכון | 4: שלילי נכון | 12: חיובי נכון | 12: שלילי נכון |\n|---|---:|---:|---:|---:|']
for k in report[4]['subgroups']:
    a,b=report[4]['subgroups'][k],report[12]['subgroups'][k]
    lines.append(f"| {k} | {a['yes_correct']}/{a['yes_n']} | {a['no_correct']}/{a['no_n']} | {b['yes_correct']}/{b['yes_n']} | {b['no_correct']}/{b['no_n']} |")
lines += ['\nבשרשרת שבורה אין שאלות חיוביות, ולכן 0/0 בטבלה פירושו לא ישים.\n',
          '## פירוש\n',
          'בארבע הדגמות כל התשובות היו No. בשתים־עשרה היו 1,194 תשובות No ושש Yes; חמש מהן נכונות ואחת שגויה. הדיוק הכולל הוא 700/1200 לעומת 704/1200. קו הבסיס של תמיד No הוא 700/1200 משום שיש 700 שאלות שליליות ו־500 חיוביות.\n',
          'בשתי ההרצות, אפס מ־100 משפחות הצליחו גם בשאלת השרשרת התקינה וגם בשאלה לאחר שבירתה, לכל אחד משני סוגי השבירה. גם בזוגות החיובי והשלילי של הקשר הישיר ושל שני הצעדים לא הייתה אף משפחה שבה שתי התשובות נכונות.\n',
          'ה־100% בשרשרת שבורה אינו ראיה להסבר לוגי של המודל: זה בדיוק מה שמתקבל מתשובת No קבועה. ארבע ההצלחות הנוספות ב־12 הדגמות נמצאות בתנאי העמידות; הן אינן הצלחה יציבה שעוברת בין כל הווריאציות.\n',
          '## השפעת ההדגמה האחרונה\n',
          'לאחר הדגמה אחרונה Yes המודל ענה No בכל 600 השאלות בכל הרצה. לאחר הדגמה אחרונה No הוא ענה No בכל 600 השאלות ב־4-shot, וב־594 מתוך 600 ב־12-shot. לכן חיקוי ישיר של התווית האחרונה אינו הסבר מספיק. אין להסיק השפעה סיבתית של התווית האחרונה בלבד: גם תוכן ההדגמות וזהות המשפחות משתנים בין הקבוצות.\n',
          '## ציונים רציפים\n',
          '| מבחן | AUC ב־4 | AUC ב־12 |\n|---|---:|---:|']
for k in ('direct','twohop','robustness'):
    lines.append(f"| {labels[k]} | {report[4]['groups'][k]['auc']:.3f} | {report[12]['groups'][k]['auc']:.3f} |")
lines += ['\nAUC חושב על log P(Yes) פחות log P(No). ערך 0.5 פירושו שאין יתרון בדירוג דוגמאות חיוביות מעל שליליות; 1 פירושו הפרדה מלאה. המדדים תיאוריים ואינם בדיקת מובהקות. אין כאן אות חזק של יכולת double hop שמוסתרת רק על ידי סף תשובה.\n',
          '## מגבלות סטטיסטיות\n',
          'יש 100 משפחות עם וריאציות תלויות, ולא 1,200 בעיות עצמאיות. בקובץ JSON נשמרים גם רווחי bootstrap על משפחות (3,000 דגימות חוזרות, seed קבוע). רווח מנוון במבחן שכל המשפחות קיבלו בו אותו ציון מתאר אפס שונות במדגם המשפחות שנצפה; הוא אינו ודאות לגבי אוכלוסיית פרומפטים חדשה. ההבדל ב־12 פחות 4 בתנאי העמידות הוא 0.67 נקודות אחוז, עם רווח bootstrap של 0 עד 1.5 נקודות אחוז. לא בוצעה בדיקת מובהקות מאשרת.\n',
          'לעומת הפרומפט הקודם, הדיוק החופשי הכולל לא השתנה ב־4-shot ועלה ב־12-shot מ־698 ל־704 תשובות נכונות. מבחני הבסיס נשארו ב־50%.\n']
(OUT/'REPORT_HE.md').write_text('\n'.join(lines),encoding='utf-8')
print(json.dumps(report,indent=2))
