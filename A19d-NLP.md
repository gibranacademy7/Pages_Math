# ניתוח טקסט עם SpaCy – פונקציונליות בסיסית המשך

## ה- Lemmatization – הפשטת מילים לצורת בסיס תקנית

ה- Lemmatization היא שיטה לעיבוד מילים בשפה טבעית שבה כל מילה מומרת לצורת הבסיס שלה (lemma) לפי ההקשר התחבירי שלה

בניגוד ל־stemming שפשוט חותך סיומות לפי חוקים, lemmatization מתחשבת במשמעות הדקדוקית של המילה, בחלק הדיבר שלה, ובמבנה הלשוני הכללי

לדוגמה:

* המילה `running` תהפוך ל־`run`
* המילה `better` תהפוך ל־`good`

### יתרונות lemmatization

* מבוססת על ניתוח תחבירי ולא על חיתוך טכני
* מחזירה מילים תקניות שקיימות במילון
* מדויקת יותר מהבחינה הסמנטית

### דוגמה:

```python
import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("run running ran")
for token in doc:
    print(token.text, "→", token.lemma_)
```

פלט:

```
run → run
running → run
ran → run
```

### פרמטרים

```python
doc1 = nlp("I am a runner running in a race because I love to run since I ran today")

print(f'{"token.text":16}', f'{"token.pos_":15}', f'{"token.lemma":23}', f'{"token.lemma_":20}')
print('-' * 70)

for token in doc1:
    print(f'{token.text:10}', '\t', f'{token.pos_:10}', '\t', f'{token.lemma:10}', '\t', token.lemma_)

```

Ouput:
```
token.text       token.pos_      token.lemma             token.lemma_        
----------------------------------------------------------------------
I          	 PRON       	 4690420944186131903 	 I
am         	 AUX        	 10382539506755952630 	 be
a          	 DET        	 11901859001352538922 	 a
runner     	 NOUN       	 12640964157389618806 	 runner
running    	 VERB       	 12767647472892411841 	 run
in         	 ADP        	 3002984154512732771 	 in
a          	 DET        	 11901859001352538922 	 a
race       	 NOUN       	 8048469955494714898 	 race
because    	 SCONJ      	 16950148841647037698 	 because
I          	 PRON       	 4690420944186131903 	 I
love       	 VERB       	 3702023516439754181 	 love
to         	 PART       	 3791531372978436496 	 to
run        	 VERB       	 12767647472892411841 	 run
since      	 SCONJ      	 10066841407251338481 	 since
I          	 PRON       	 4690420944186131903 	 I
ran        	 VERB       	 12767647472892411841 	 run
today      	 NOUN       	 11042482332948150395 	 today
```

**1. `token.text`**

The actual word (token) as it appears in the sentence

**2. `token.pos_`**

The part-of-speech tag (POS) as a **readable string**, like:

* `PRON` – pronoun
* `AUX` – auxiliary verb
* `VERB` – main verb
* `NOUN` – noun

This is the **human-readable** label for grammatical role

**3. `token.lemma`**

The lemma of the token, as an **internal hash-based ID number** (spaCy uses numerical IDs internally for efficiency)
This is useful for internal lookup but not for human interpretation

**4. `token.lemma_`**

The lemma as a **readable string**, e.g.:

* `running`, `ran`, `run` → all will have `lemma_ = "run"`
* `am` → `lemma_ = "be"`

---

### ה- Stop Words – מילות עצירה

מילות עצירה הן מילים נפוצות בשפה שאין להן תרומה משמעותית להבנת התוכן המרכזי בטקסט
דוגמאות: the, is, and, in, to, etc

מילים אלו מוסרות בדרך כלל לפני ניתוח טקסט כמו ניתוח רגשות או חיפוש מסמכים

#### למה מסירים אותן

כאשר אנו מסירים מילות עצירה (כמו: the, is, and, in) מהטקסט, אנו משפרים את יעילות ואיכות העיבוד הלשוני בכמה דרכים עיקריות:

#### \* הסרתן מפחיתה את מספר הטוקנים

כאשר מסירים מילים חסרות משמעות תחבירית, מתקבל טקסט קצר יותר עם פחות טוקנים

**דוגמה:**

```text
Before: I am going to the store and I will buy some milk
After: going store buy milk
```

במקום 11 טוקנים – נשארים עם 4 בלבד

#### \* הסרתן מחדדת את התוכן המרכזי

כאשר מוחקים מילים שכיחות שלא מוסיפות מידע מהותי, נשארים רק המילים החשובות והייחודיות של המסמך

**דוגמה:**

```text
Original: The new phone is really fast and very efficient
After: new phone fast efficient
```

זה מדגיש בדיוק את התכונות החשובות של המכשיר

#### \* הסרתן מייעלת את תהליך הלמידה או הניתוח

באלגוריתמים של למידת מכונה או בניתוח טקסט – פחות טוקנים משמעו פחות תכונות (features) לבחינה, מה שמוביל לאימון מהיר יותר ומודלים פשוטים יותר

**דוגמה:**
אם מסמך מכיל 1,000 מילים ורק 400 מהן אינפורמטיביות, מודל שיוסמך על 400 תכונות יפעל מהר יותר ויבין טוב יותר את ההקשר האמיתי

### סיכום

הסרת מילות עצירה היא צעד חשוב בתהליך קדם-עיבוד של טקסט, שמוביל לדיוק, פשטות ויעילות גבוהה יותר


#### דוגמה:

```python
from spacy.lang.en.stop_words import STOP_WORDS
print("to" in STOP_WORDS)  # True
```

ניתן גם להוסיף או להסיר מילות עצירה בהתאמה אישית:

```python
nlp.vocab["awesome"].is_stop = True
nlp.vocab["the"].is_stop = False
```

ב־spaCy ניתן לגשת לרשימת מילות העצירה (stop words) ברירת המחדל, לבדוק אם מילה מסוימת נחשבת מילת עצירה, ולהוסיף מילות עצירה חדשות בהתאמה אישית

#### הדפסת רשימת מילות העצירה של spaCy:

```python
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

nlp = spacy.load("en_core_web_sm")
print(nlp.Defaults.stop_words)
```

Output:

```
{"'ve", 'everything', 'whence', "'ll", 'this', 'to', 'mostly', 'three', 'too', 'four', 'front', 'nor', 'beyond', 
  '‘ll', 'his', 'empty', 'n’t', 'done', 'using', 'nine', 'before', 'namely', 'cannot', 'whom', 'below', 'hers', 
  'itself', "'m", 'quite', 'which', 'sixty', '‘ve', "'s", 'several', 'unless', 'every', '’ll', 'and', 'show', 
  'none', 'i', 'move', 'was', 'were', 'there', 'much', 'my', 'go', 'bottom', 'of', 'same', 'someone', 'became',
   'nothing', 'he', 'name', "'d", 'nowhere', 'except', 're', 'herein', 'whenever', 'so', 'besides', 'them'...}
```

#### בדיקה האם מילה מסוימת היא stop word:

```python
print(nlp.vocab['myself'].is_stop)    # True
print(nlp.vocab['mystery'].is_stop)   # False
```

> משמש כדי לבדוק אם מילה מסוימת מזוהה כברירת מחדל כמילת עצירה

#### הוספת מילת עצירה חדשה באופן ידני:

```python
nlp.Defaults.stop_words.add('btw')
nlp.vocab['btw'].is_stop = True

print(nlp.vocab['btw'].is_stop)  # True
```

> שים לב: יש להשתמש באותיות קטנות בלבד בעת הוספה לרשימה
> אנו מסמנים את המילה כ־stop word על ידי הגדרת `is_stop = True`

### סיכום:

* ניתן להדפיס את כל מילות העצירה המובנות ב־spaCy
* ניתן לבדוק האם מילה היא stop word קיימת
* ניתן להוסיף מילות עצירה חדשות לפי הצורך

בדומה להוספה של מילת עצירה לרשימת ברירת המחדל, ניתן גם **להסיר מילת עצירה קיימת** אם נרצה שהיא תיחשב כחלק מהתוכן המשמעותי

#### דוגמה להסרת stop word:

```python
nlp.Defaults.stop_words.remove('beyond')
nlp.vocab['beyond'].is_stop = False

print(nlp.vocab['beyond'].is_stop)  # False
```

### הסבר:

* השורה הראשונה מסירה את המילה `'beyond'` מהסט של מילות העצירה
* לאחר מכן אנו מציינים במפורש שהמילה אינה עוד stop word על ידי הגדרת `is_stop = False`
* אפשר לבדוק את הסטטוס עם `nlp.vocab['beyond'].is_stop`

התוצאה: spaCy לא תתייחס יותר ל־`beyond` כמילת עצירה

ברגע ש־`beyond` אינה נחשבת עוד stop word, spaCy תתייחס אליה כאל מילת תוכן רגילה:

* היא תיכלל בניתוח מילות מפתח או תדירות מילים
* היא תישאר כחלק מהטקסט גם כשמנקים מילות עצירה
* היא תוכל לשמש כ־feature באימון של מודלים בלמידת מכונה

כך אפשר לוודא שמילים חשובות לנו לא יוסרו בטעות בתהליכי קדם־עיבוד

---

### ה- Phrase Matching ב־ spaCy

ה- Phrase Matching הוא תהליך שמטרתו לזהות ביטויים (צירופים של מילים) שמופיעים בטקסט
זהו כלי שימושי ב־NLP לזיהוי שמות, מונחים, תאריכים, קטגוריות ועוד

ב־spaCy משתמשים במחלקה `PhraseMatcher` שמבוססת על המודל והטוקניזציה הפנימית שלו

### למה זה חשוב

* מאפשר לזהות ביטויים קבועים או מונחים מתוך רשימה
* מייעל תהליכי חיפוש, סיווג טקסטים, שליפת מידע
* תומך בהתאמות עם רגישות למבנה תחבירי או פיסוק

### שלבי עבודה בסיסיים:

```python
from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(nlp.vocab)

patterns = [nlp("Solar Power"), nlp("solarpower"), nlp("solar-power")]
matcher.add("SOLARPOWER", patterns)

doc = nlp("This building uses Solar-Power and solarpower systems")
matches = matcher(doc)

for match_id, start, end in matches:
    print(doc[start:end].text)
```

#### פלט:

```
Solar-Power
solarpower
```

### מה קורה בפועל

* אנו מוסיפים למתאם (`matcher`) שלוש וריאציות של אותו ביטוי
* spaCy מזהה את כולן במשפט למרות ההבדלים במבנה (רווח, מקף, יחד)

### התאמה מתקדמת עם הקשרים תחביריים

```python
# Removing the previous matcher to avoid duplicates
matcher.remove("SOLARPOWER")

# Redefining with advanced patterns
patterns = [
    nlp("solarpower"),
    nlp("solar power"),
    nlp("solar-power"),
    nlp("solar--power"),
    nlp("solar.power"),
    nlp("solar_powered")
]
matcher.add("SOLARPOWER", patterns)

doc = nlp("The company installs solar-powered and SolarPower panels")

matches = matcher(doc)
for match_id, start, end in matches:
    print(doc[start:end].text)
```

#### פלט:

```
solar-powered
SolarPower
```

### סיכום:

* ה- PhraseMatcher של spaCy מאפשר לזהות ביטויים בטקסט באופן מהיר וגמיש
* ניתן להוסיף תבניות פשוטות או מורכבות לפי הצורך
* חשוב להסיר מתאמים קודמים לפני הוספת תבניות חדשות באותו שם
* מתאים מאוד לזיהוי מונחים ומילים רלוונטיות בטקסט אמיתי

### סיכום הדוגמאות שראינו: 

#### • הגדרת תבניות (Pattern Specification)

ב־Phrase Matching הדגרנו מראש תבניות או רצפי טוקנים שרוצים לזהות בטקסט
תבניות אלו יכולות להיות מילים בודדות או מבנים מורכבים הכוללים וריאציות תחביריות או סימני פיסוק

לדוגמה:

* ד- "machine learning"
* ד- "natural language processing"
* ד- "data-driven approach"
* ד- "artificial-intelligence" (כולל מקף) (Efficiency)

#### • יעילות (Efficiency)

הטכניקה של Phrase Matching מותאמת לעבודה מהירה ויעילה במיוחד בטקסטים ארוכים או ביישומים בזמן אמת

#### • התאמה אישית (Customization)

התאמנו את תהליך ההתאמה למקרים שונים כמו:

* אותיות רישיות מול קטנות (לדוגמה: Run לעומת run, AI לעומת ai)
* צורות דקדוקיות משתנות (כגון: run, running, ran – כולן קשורות לאותו שורש)
* פיסוק מגוון (כמו: machine-learning, machine.learning, machine learning)
* צרכים לשוניים מיוחדים בהתאם לאפליקציה או למטרה

דוגמאות:

* ד- "COVID19", "COVID-19", "covid 19" – שלוש וריאציות של אותו מושג
* ד- "e-mail" לעומת "email" – אותו מונח עם או בלי מקף
* ד- "U.S.A." לעומת "USA" – עם נקודות או בלעדיהן (Applications)

#### • יישומים (Applications)

ה- Phrase Matching שימושי למגוון רחב של מטרות:

* חילוץ מידע (כמו שמות, תאריכים, מונחים מקצועיים)
* סיווג טקסטים לפי קטגוריות לפי ביטויים קיימים
* שיפור מנועי חיפוש על ידי זיהוי ביטויים רלוונטיים שמובילים לתוצאות מדויקות יותר


