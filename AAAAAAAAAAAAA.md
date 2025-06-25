### 🧠 התאמה אישית של NER ב־spaCy

#### למה נרצה להוסיף ישויות ידנית?
לפעמים spaCy לא מזהה ישויות שאנחנו כן רוצים לזהות – לדוגמה, "Tesla" לא מזוהה כברירת מחדל כישות מסוג ORG  
במקרים כאלה נוכל להוסיף את הישות ידנית למסמך

#### השלבים להוספת ישות ידנית:
1. שליפת הערך המספרי (hash) של התווית הרצויה (למשל "ORG")
2. יצירת Span מהמילה או הביטוי הרצוי
3. הוספת ה־Span לרשימת הישויות במסמך `doc.ents`

```python
from spacy.tokens import Span

ORG = doc.vocab.strings["ORG"]
new_ent = Span(doc, start=0, end=1, label=ORG)
doc.ents = list(doc.ents) + [new_ent]
```

#### דוגמה מתקדמת – Phrase Matcher
אם נרצה לזהות ביטויים שלמים כמו:
- `dashboard website`
- `dashboard-website`

נשתמש ב־PhraseMatcher לזיהוי הביטויים במסמך, ואז נוסיף אותם כישויות:

```python
from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)
patterns = [nlp("dashboard website"), nlp("dashboard-website")]
matcher.add("PRODUCT", patterns)

matches = matcher(doc)
new_ents = [Span(doc, start, end, label=doc.vocab.strings["PRODUCT"]) for match_id, start, end in matches]
doc.ents = list(doc.ents) + new_ents
```

#### שימושים נוספים:
אפשר גם:
- לספור ישויות לפי סוג: `len([ent for ent in doc.ents if ent.label_ == "ORG"])`
- להציג את כל הישויות עם הסוגים שלהן
- להדפיס את מיקום ההתחלה והסיום של כל ישות
