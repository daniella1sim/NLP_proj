# Pythia-1B: מהתיקייה להרצת הפיילוט

החבילה נוצרה ב־6 בספטמבר 2026 ועודכנה לפי פלט ההתחברות של maximg: תור `studentkillable`, חשבון `gpu-students`, ו־Python 3.12.3. בקשת GPU הוגבלה ל־`geforce_rtx_3090`; זמינותו בתור עדיין טעונה בדיקה. כל החומר המקומי נמצא תחת `final proj/project/pythia_pilot`.
המשקולות יירדו למחשב שמריץ בפועל — Slurm, Colab או RunPod. אין צורך להוריד אותן למחשב האישי או לשכפל את מאגר GitHub.

**מה מוכן:** קוד, דאטה, checkpoint מקובע, התקנה, סקריפט Slurm, מחברת Colab, דוחות וחידוש ריצה שנקטעה.
**מה עדיין נדרש בשרת:** העתקת החבילה, התקנת הסביבה, הורדת המשקולות והרצת GPU. לפי הפלט שסיפקת יש הרשאת כתיבה והרשאת תור; לא בוצעה כאן הרצת Pythia או בדיקת יכולתו.

## 1. מה נריץ ולמה

המודל: [EleutherAI/pythia-1b](https://huggingface.co/EleutherAI/pythia-1b), הגרסה הרגילה, checkpoint סופי של האימון.
הגרסה המדויקת קבועה ב־`model_lock.json`: `f73d7dcc545c8bd326d8559c8ef84ffe92fea6b2`.
לפי כרטיס המודל, Pythia נועד גם למחקר interpretability והוא מודל אנגלי בסיסי. לכן הקלט באנגלית ובפורמט השלמה עם דוגמאות, בלי chat template.

אין בשלב זה אימון, RI או activation patching. קודם בודקים אם קיימת התנהגות ששווה לחקור.

| בדיקה | הקלט העקרוני | מה מחפשים |
|---|---|---|
| 1. עובדה מפורשת | All A are B; All B are C. האם All A are B? | שליפה נכונה; בקרה גם על הכיוון ההפוך |
| 2. שני צעדים | אותן עובדות. האם All A are C? | חיבור שתי עובדות; גם שאלת בקרה C→A |
| 3. שרשרת שבורה | All A are D; All B are C. אותה שאלה A→C | מעבר מתשובת Yes ל־No; נבדקת גם שבירה בעובדה השנייה |
| 4. עמידות | שינוי סדר, הוספת שרשרת מסיחה, או החלפת כל השמות | שימור תשובה נכונה תחת כל שינוי בנפרד |

`No` פירושו שהטענה **אינה נובעת מהעובדות**, ולא שההפך שלה הוכח. שליפת עובדה ישירה היא בדיקת בסיס, ולא שימוש בטרנזיטיביות.

הפיילוט כולל 100 משפחות בלתי תלויות של שמות/תפקידים, 12 פרומפטים בכל משפחה: 1,200 בסך הכול. התשובות מחושבות מגרף. לכל פרומפט שמורים העובדות, השאלה, התשובה, מסלול ההוכחה, מיקומי הישויות וגרסת הניסוי. בזמן ההרצה נוספים מיקומי הטוקנים.

ארבע דוגמאות קבועות, מאוזנות Yes/No ובשמות נפרדים, מדגימות את המשימה. קובץ נוסף עם 0 דוגמאות מאפשר השוואה על אותן שאלות. השמות המלאכותיים כגון `group000a` עשויים להתפצל לטוקנים; הקוד שומר את כל המיקומים ולא מניח שטוקן יחיד מייצג שם.

זהו **פיילוט התנהגותי**, לא benchmark סופי: השליליים ב־direct/twohop הם היפוך כיוון; בדיקת broken מוסיפה שליליים מסוג ניתוק. הצלחה עדיין מחייבת בהמשך גרפים מגוונים יותר, תבניות נוספות ו־held-out test לפני טענה רחבה על reasoning. גם few-shot אינו אימון משקולות.

## 2. משאבים נדרשים

נקודת פתיחה: GPU יחיד של NVIDIA, רצוי 16–24GB VRAM; בקשת Slurm של 4 ליבות CPU ו־16GB RAM. `--mem=16G` הוא RAM של המחשב, לא זיכרון GPU.

המשקולות ב־16 ביט תופסות בערך 2GB; זיכרון GPU כולל דורש יותר. לפיילוט הזה אין quantization או offloading. תכנן כ־20–30GB אחסון פנוי לסביבה, חבילות התקנה, משקולות ותוצאות — אומדן תפעולי עם מרווח, לא מדידת מכסה או התחייבות. זמן העבודה בפועל יימדד ב־smoke run; זמן ההמתנה בתור נפרד ממנו.

לא מורידים את The Pile, checkpoint-ים מוקדמים או שתי גרסאות של המשקולות. אין שמירת activations בשלב הזה. ספריית `storage/model` מכילה רק safetensors וקובצי טעינה/טוקניזציה.

## 3. התחברות ראשונה ובדיקת החשבון

ב־PowerShell במחשב האישי, החלף `YOUR_TAU_USERNAME` בשם משתמש האוניברסיטה שלך. לא הסקתי אותו משם תיקיית האחסון.

```powershell
ssh YOUR_TAU_USERNAME@slurm-client.cs.tau.ac.il
```

מחוץ לקמפוס נדרש VPN של TAU. הסיסמה מוקלדת בחלון ההתחברות. פרטי החיבור ומדיניות התורים: [תיעוד TAU Slurm](https://www.cs.tau.ac.il/system/slurm).

אחרי ההתחברות, הפקודות הבאות רצות **בשרת האוניברסיטה**:

```bash
bash
whoami
ls -ld /home/yandex/DLWorkShop2025b/maximg
test -w /home/yandex/DLWorkShop2025b/maximg && echo "Directory is writable"
df -h /home/yandex/DLWorkShop2025b/maximg
quota -s
sacctmgr -P -i show user -s "$USER"
sinfo -o "%20N %10c %10m %25f %30G"
python3 --version
```

`df` מציג מקום פנוי במערכת הקבצים, ואינו מאמת את המכסה האישית. בפלט שסיפקת מופיעים `studentkillable` וחשבון `gpu-students`. אין להסיק שכל GPU שמופיע ב־sinfo זמין לחשבון שלך. תיקיית הבית כמעט מלאה (5905M מתוך 6144M); אחסון הפרויקט נפרד, ובפלט המכסה שלו מופיע שימוש 17497M מול מכסה 16384G. אין צורך למחוק חומר ישן כדי להתחיל בהתקנה בתיקיית הפרויקט.

Python 3.12.3 שזמין אצלך מתאים לסקריפט ההתקנה. אין צורך ב־Conda או בהתקנת מערכת CUDA עצמאית. אם `python3 -m venv` נכשל בגלל חוסר ב־venv/ensurepip, עצור בשלב ההתקנה והעבר את הודעת השגיאה; אין סיבה לשנות את Python של המערכת. הפקודה `bash` בתחילת העבודה מאפשרת להשתמש בפקודות ההפעלה של הסביבה גם אם מעטפת הכניסה שלך היא tcsh.

## 4. העברת החבילה מהמחשב האישי

פתח חלון PowerShell נוסף **במחשב האישי**:

```powershell
Set-Location 'C:\Users\User\OneDrive\Documents\computer science\4B\NLP\final proj\project'
scp .\pythia_pilot.zip YOUR_TAU_USERNAME@slurm-client.cs.tau.ac.il:/home/yandex/DLWorkShop2025b/maximg/
```

חזור לחלון ה־SSH, **בשרת**:

```bash
cd /home/yandex/DLWorkShop2025b/maximg
python3 -m zipfile -e pythia_pilot.zip .
cd pythia_pilot
bash setup.sh
source env.sh
source .venv/bin/activate
python pilot.py download
```

יש לפרוס את ZIP פעם אחת לתיקייה חדשה. אל תדרוס חבילה שכבר שינית או שיש בה ניסויים פעילים. התקנה והורדה דורשות רשת; ההרצה עצמה משתמשת רק במשקולות מקומיות. המודל ציבורי ואין צורך ב־HF token.

`setup.sh` מתקין PyTorch 2.6.0 CUDA 11.8 וספריות בגרסאות קבועות, בסביבה פרטית בתוך תיקיית הפיילוט. שילוב גרסאות PyTorch מבוסס על [הוראות ההתקנה הרשמיות](https://pytorch.org/get-started/previous-versions/); בדיקת תאימות הדרייבר והחומרה בפועל נעשית בהרצה הקצרה. ל־GPU חדש שאינו נתמך בגרסה הזאת נצטרך התאמת PyTorch מתועדת.

מבנה התיקייה שייווצר בשרת:

```text
pythia_pilot/
  pilot.py                קוד ההערכה
  model_lock.json         זיהוי המשקולות המדויק
  data/                   0-shot ו־4-shot, מוכנים מראש
  .venv/                  סביבת Python
  storage/model/          משקולות וטוקנייזר
  storage/runs/           תוצאות לכל ריצה
  storage/pip-cache/      מטמון התקנה
  logs/                   פלט ושגיאות Slurm
```

## 5. בדיקת הרצה קצרה על GPU

מתוך תיקיית `pythia_pilot` בשרת, לאחר הורדה מוצלחת:

```bash
mkdir -p logs
sbatch --time=00:30:00 slurm.sbatch --name smoke_4shot --limit-families 2
squeue -u "$USER"
```

הפקודה תחזיר Job ID. בדוק את הקבצים לפי המספר שהתקבל:

```bash
tail -f logs/pythia-pilot-JOB_ID.out
cat logs/pythia-pilot-JOB_ID.err
```

החלף `JOB_ID` במספר בפועל. Ctrl+C מפסיק רק את צפיית `tail`. ריצת ה־smoke כוללת 24 פרומפטים — היא בדיקת תקינות, לא אומדן אמין ליכולת reasoning.

הסקריפט כבר מכיל `--partition=studentkillable`, `--account=gpu-students` ו־`--constraint=geforce_rtx_3090`, לפי הפלט שסיפקת. ניתן לבדוק את רשימת הצמתים בתור בעזרת `sinfo -p studentkillable -o "%20N %25f %30G %10t"`. אם אין בו 3090, צריך לבחור GPU NVIDIA תואם אחר לפי הפלט. אין להסיר את המגבלה ללא בדיקה, כי באשכול מופיעים גם AMD ו־B200, שאינם היעד של סביבת CUDA 11.8 שהוכנה כאן.

אין להריץ `python pilot.py run` ישירות בשרת הכניסה. רק דרך sbatch/srun. `PD` בתור הוא המתנה, לא כשל בקוד. לבדיקת מצב אחרי שהמשימה נעלמה מהתור:

```bash
sacct -j JOB_ID --format=JobID,State,ExitCode,Elapsed,MaxRSS
```

אחרי סיום מוצלח, בדוק:

```bash
cat storage/runs/smoke_4shot/summary.csv
cat storage/runs/smoke_4shot/session_*.json
```

צריך לראות 24 תוצאות, שם GPU, זמן ומדידת זיכרון. אם משך ההערכה ל־24 דוגמאות הוא T, אומדן ראשוני ל־1,200 הוא כ־50T, עם שונות ועומס מערכת. מדידת הזיכרון היא peak allocated של PyTorch, ולא כל זיכרון הדרייבר.

## 6. ארבע הבדיקות המלאות

אחרי שההרצה הקצרה הסתיימה כראוי:

```bash
sbatch slurm.sbatch --name pilot_4shot
```

ההשוואה ללא דוגמאות היא ריצה נפרדת, מומלץ אחרי קריאת תוצאת 4-shot:

```bash
sbatch slurm.sbatch --name pilot_0shot --shots 0
```

זמן ברירת המחדל הוא 3 שעות, לא תחזית לזמן שיידרש. אפשר לשנות `--time` לפני שם הסקריפט לפי המדידה והמגבלות. אם נקטעה ריצה, הגש שוב **אותה פקודה ואותו שם**: תוצאות נשמרות לאחר כל פרומפט והריצה מדלגת על מה שכבר הושלם. יש הגנה מפני שני כותבים שמשתמשים באותה תיקיית אחסון לחישוב; אל תפעיל אותו שם ריצה במקביל בסביבות שונות או בשני runtimes של Colab.

שינוי קוד, דאטה, גרסאות או הגדרות מחייב שם ריצה חדש. לסיכום ריצה חלקית, אחרי שהמשימה נעצרה:

```bash
python pilot.py report --name pilot_4shot
```

## 7. מה קוראים בתוצאות

| קובץ | תוכן |
|---|---|
| `summary.csv` | דיוק לפי בדיקה, שינוי ו־Yes/No; תקינות פורמט; דיוק יצירה חופשית; פער log-probability |
| `paired_metrics.json` | הצלחה משותפת בזוג נקי/שבור; שינוי בכיוון הנכון; יציבות והצלחה משותפת בשינויי עמידות |
| `results.jsonl` | כל פרומפט, gold, ציוני שתי התשובות, פלט חופשי, טוקנים ומיקומי ישויות |
| `manifest.json` | גרסת מודל, hash של קוד ודאטה, גרסאות חבילות והגדרות |
| `session_*.json` | חומרה, גרסאות, זמן ומדידת זיכרון לכל ניסיון הרצה |

הקוד משווה את סכום log-probabilities של ההשלמה ` Yes` מול ` No`, תוך תמיכה גם בתשובה מרובת טוקנים. זהו **דיוק בבחירה בין שתי מועמדות**, ולא הסתברות מוחלטת שהמודל יענה נכון. בנוסף נוצרים עד 8 טוקנים ללא sampling; נבדק אם הם מתחילים ב־Yes/No ומה התשובה. שני המדדים נשמרים בנפרד. תיקו בציונים נחשב ככישלון בחירה.

כל שורת דוח מחושבת על משפחות נפרדות, עם רווח Wilson של 95%. אין לאחד את כל 1,200 הווריאציות כאילו הן דוגמאות עצמאיות: יש תלות בתוך משפחה. ההפרדה ל־Yes/No חשובה, במיוחד כי בדיקת broken שלילית בלבד. דיוק גבוה בה לבדה יכול לנבוע מתשובת No קבועה; הסתכל גם על `clean_and_broken_correct`.

כהחלטת עבודה זמנית, נשאף לדיוק מאוזן גבוה בשליפה ישירה (למשל סביב 90% ומעלה), הצלחה משמעותית מעל baseline בשני צעדים, והצלחה משותפת בבקרות. אין סף קסם שמוכיח מנגנון. אם יש כשל, נבדוק קודם פורמט, tokenization ודוגמאות קונקרטיות; תוצאה חלשה בפרומפט אחד אינה מוכיחה שהמודל אינו מסוגל למשימה. שינוי פרומפט בעקבות תוצאות הופך את הסט ל־development set; נייצר test חדש בהמשך.

## 8. החזרת התוצאות למחשב

ב־PowerShell המקומי, לאחר סיום הריצה:

```powershell
Set-Location 'C:\Users\User\OneDrive\Documents\computer science\4B\NLP\final proj\project'
New-Item -ItemType Directory -Force .\results_from_slurm
scp -r YOUR_TAU_USERNAME@slurm-client.cs.tau.ac.il:/home/yandex/DLWorkShop2025b/maximg/pythia_pilot/storage/runs .\results_from_slurm\
scp -r YOUR_TAU_USERNAME@slurm-client.cs.tau.ac.il:/home/yandex/DLWorkShop2025b/maximg/pythia_pilot/logs .\results_from_slurm\
```

אין צורך להחזיר את המשקולות או סביבת Python. כל תוצר מקומי יישאר תחת `final proj`.

## 9. חלופה: Google Colab

פתח את `colab.ipynb` באמצעות File → Upload notebook, בחר Runtime → Change runtime type → GPU והריץ את התאים לפי הסדר. בתחילת המחברת מעלים את `pythia_pilot.zip`.

המחברת שומרת קוד ומודל בדיסק הזמני של Colab, ותוצאות לאחר כל פרומפט ב־Google Drive שלך, בתיקייה `MyDrive/pythia_pilot_runs`. חיבור Drive דורש התחברות שלך. המשקולות יורדות שוב אם ה־runtime נמחק; הן נשארות באותה revision מקובעת. בסיום יש תא להורדת ZIP של התוצאות למחשב — שמור אותו תחת `final proj/project`.

משאבי GPU ומשך runtime ב־Colab אינם מובטחים; [Colab FAQ](https://research.google.com/colaboratory/faq.html). המחברת משתמשת ב־PyTorch הקיים ב־Colab, מתקינה את אותן ספריות הערכה ומתעדת גרסאות. זו אינה הבטחה לזהות ביט־לביט בין GPUs. אם גרסת Python אינה תומכת בחבילות, השתמש ב־runtime תואם או ב־RunPod עם Python 3.11; שמור את הודעת השגיאה לצורך התאמה.

## 10. חלופה: RunPod

לא נוצר Pod ולא בוצעה רכישה. אם תבחר להשתמש בו, בחר GPU יחיד עם 16–24GB לפחות, ותמונת PyTorch עם Python 3.10–3.12. לפיילוט הזה אין צורך ב־GPU יקר במיוחד. בדוק מחיר ותנאי אחסון לפני ההפעלה.

העלה את ZIP דרך Jupyter של ה־Pod לתיקייה שמגובה ב־volume. בטרמינל שלו, בהנחה שזו `/workspace`:

```bash
cd /workspace
python3 -m zipfile -e pythia_pilot.zip .
cd pythia_pilot
source env.sh
python -m pip install -r requirements.txt
python -m unittest discover -s tests -v
nvidia-smi
python pilot.py download
python -u pilot.py run --name runpod_smoke --limit-families 2
python -u pilot.py run --name runpod_4shot
```

PyTorch נלקח כאן מהתמונה המוכנה ומתועד. הנתיב `/workspace` כשלעצמו אינו מבטיח התמדה: יש לבדוק שהוא mount של volume. לפי [תיעוד האחסון של RunPod](https://docs.runpod.io/pods/storage/types), סוגי האחסון שונים בהישרדות עצירה/מחיקת Pod. הורד תוצאות לפני סיום; השתמש ב־network volume אם נדרשת התמדה גם לאחר מחיקת Pod.

כדי להוריד דרך Jupyter, אחרי סיום:

```bash
python -m zipfile -c runpod_results.zip storage/runs
```

אפשר להתחיל ניסוי חדש בכל ספק עם אותה חבילה. כדי להמשיך ריצה חלקית ממש, יש להעביר גם את תיקיית הריצה ולשמור אותן גרסאות והגדרות; ברירת המחדל המומלצת היא שם ריצה חדש לכל ספק והשוואה מתועדת, ללא ערבוב שורות אוטומטי.

## 11. אם משהו נכשל

- **Permission denied בהתחברות:** בדוק VPN, שם משתמש והפעלת הרשאות מול TAU.
- **Invalid account/partition:** השתמש בפלט ההרשאות של חשבונך; לא משנים לשם תור אחר בניחוש.
- **No CUDA GPU:** ב־Slurm צריך sbatch/srun; ב־Colab צריך runtime עם GPU.
- **אין גישה ל־HF בצומת GPU:** זה צפוי בחלק מהסביבות; הורד קודם בשרת עם רשת, והריצה תטען מקומית.
- **CUDA out of memory או חוסר תאימות דרייבר:** שמור את לוג השגיאה ואת `nvidia-smi`. ההרצה כבר משתמשת בדוגמה אחת בכל פעם. נסה GPU עם יותר זיכרון או התאמת גרסת PyTorch; אין לעבור ל־quantization בשקט.
- **ריצה נקטעה:** אותו שם והגדרות יחדשו אותה. שחזור אוטומטי מסיר רק שורת JSON אחרונה שנכתבה חלקית.
- **המודל עונה רע:** זו תוצאת מחקר אפשרית, לא בהכרח תקלה. הפרד העדפת מועמדת, פורמט ותשובה חופשית לפני החלפת המודל.

## בדיקות שבוצעו בהכנת החבילה

בדיקות CPU של לוגיקת הגרף, 1,200 דוגמאות ובקרות, מיקומי תווים, שחזור קובץ שנקטע, גבול הטוקניזציה באמצעות tokenizer מדומה, ודוחות על תשובות ידועות. לא בוצעה כאן טעינת Pythia, בדיקת tokenizer האמיתי או הרצת GPU. אלה מטרות שלב ה־smoke בחשבונך.
