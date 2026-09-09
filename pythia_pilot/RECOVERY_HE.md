# תיקון לפי לוג 7 בספטמבר

לפני התקנה נוספת, בדוק את המשימה האחרונה: הקובץ המצורף הסתיים כש־865498 עדיין רצה על s-003. אין בו תוצאה סופית.

```bash
bash
cd /home/yandex/DLWorkShop2025b/maximg/pythia_pilot
sacct -j 865498 --format=JobID,State,Elapsed,NodeList,ExitCode
tail -n 80 logs/pythia-pilot-865498.out
tail -n 80 logs/pythia-pilot-865498.err
wc -l storage/runs/smoke_4shot/results.jsonl
```

אם אין קובץ results, לא נשמרה בו דוגמה. אם יש 24 שורות, COMPLETED עם ExitCode 0:0 והדוח נוצר, ההרצה הקצרה הצליחה. אם עדיין RUNNING, קרא את הלוגים ואל תפעיל ניסוי חלופי במקביל. זמן בתור וניתוק SSH אינם כשל של משימת batch.

## האבחון

- `ensurepip` חסר: סביבת venv המקורית לא נוצרה. Python 3.12 כשלעצמו אינו הבעיה.
- התקנת `requirements.txt` ישירות לתיקיית python_packages משכה דרך accelerate את PyTorch 2.14/CUDA 13. זה אינו ה־2.6/CUDA 11.8 שהוגדר ב־setup.sh. התקנת cu126 שיפרה התאמה לחומרה ישנה, אך השאירה את 2.14.
- על s-002 נכשלה אתחול CUDA, גם לאחר מעבר ל־cu126. הסיבה המדויקת אינה מוכחת; שגיאות ERR! ב־nvidia-smi מחשידות את מצב הצומת, אך אינן מספיקות לקבוע שזו הסיבה. הקצאת GPU ב־Slurm אינה מבטיחה שאתחול CUDA תקין.
- על s-005 המודל הגיע ל־forward ולחישוב rotary embeddings. PyTorch הפעיל מימוש Triton של מכפלת מטריצות, והקומפילציה נכשלה עקב Python.h חסר. בדיקת gcc באותו צומת חיזקה זאת. קיום header בשרת הכניסה או s-006 אינו מוכיח קיום ב־s-005.
- בתור המאושר מופיעים TITAN Xp ו־RTX 2080, לא 3090. מגבלת 3090 המקורית אינה מתאימה לתור הזה.

## המסלול המוכן אם הריצה הקודמת נכשלה

שלושת קובצי recovery יוצרים סביבה חדשה `.venv_recovery`, מנטרלים PYTHONPATH/חבילות משתמש, מתקינים Torch 2.6.0+cu118 ובוחרים את משפחת RTX 2080 מתוך התור המאושר. אין מחיקה, שינוי בקוד הניסוי או הורדה נוספת של המודל. נבחר שם ניסוי חדש כדי לא לערבב גרסאות.

ב־PowerShell המקומי:

```powershell
Set-Location 'C:\Users\User\OneDrive\Documents\computer science\4B\NLP\final proj\project\pythia_pilot'
scp .\recovery_setup.sh .\recovery.sbatch .\recovery_run.py maximg@slurm-client.cs.tau.ac.il:/home/yandex/DLWorkShop2025b/maximg/pythia_pilot/
```

ב־SSH, מתוך bash ותיקיית הפרויקט:

```bash
bash recovery_setup.sh
```

רק אם הופיע RECOVERY SETUP OK:

```bash
mkdir -p logs
sbatch recovery.sbatch --name recovery_smoke_v1 --limit-families 2
```

הסקריפט משתמש ב־virtualenv zipapp הרשמי כדי לעקוף ensurepip חסר, בלי sudo. הסביבה החדשה אינה מתקנת headers בצמתים; היא מחזירה אותנו למסלול החישוב שתוכנן, ובודקת בפועל שה־GPU יכול לבצע גם מכפלת FP16 וגם מכפלה בממדי rotary embeddings לפני טעינת המודל.

לצפייה, החלף את המספר שקיבלת במקום JOB_ID:

```bash
sacct -j JOB_ID --format=JobID,State,Elapsed,NodeList,ExitCode
tail -n 80 logs/pythia-recovery-JOB_ID.out
tail -n 80 logs/pythia-recovery-JOB_ID.err
```

הלוג מראה: סביבת Python → אתחול וחשבון CUDA → טעינת המודל והפיילוט. כך ניתן לזהות את שלב הכשל בלי להחליף רכיבים בניחוש. הקוד אינו משנה CUDA_VISIBLE_DEVICES שנקבע על ידי Slurm.

אחרי הצלחה של 24 דוגמאות וקריאת מדידת הזמן:

```bash
sbatch --time=03:00:00 recovery.sbatch --name recovery_pilot_4shot_v1
```

זו הרצת ארבע הבדיקות, 1,200 פרומפטים. השוואת 0-shot היא ריצה נוספת:

```bash
sbatch --time=03:00:00 recovery.sbatch --name recovery_pilot_0shot_v1 --shots 0
```

שמור את קובצי session/manifest והלוגים יחד. 3 שעות הן הקצאת זמן התחלתית, לא הבטחה שהריצה תסתיים בזמן הזה. ריצה שנקטעה ניתנת לחידוש עם אותה פקודה ואותו שם.

הקבצים נבדקו מקומית מבחינת תחביר Python וסיומות שורה של Linux. סביבת Linux וה־GPU טרם נבדקו כאן; הצלחת התיקון עדיין דורשת את ההרצה בחשבונך.

מקורות: [virtualenv zipapp](https://virtualenv.pypa.io/en/latest/installation.html#via-zipapp), [גרסאות PyTorch הרשמיות](https://pytorch.org/get-started/previous-versions/), [מדיניות CUDA וארכיטקטורות ישנות](https://dev-discuss.pytorch.org/t/introducing-cuda-13-2-and-deprecating-cuda-12-8-release-2-12/3337).
