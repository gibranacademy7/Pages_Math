
  
## סוגי עצי החלטה
  
## 1. CART (Classification and Regression Trees)
  
**דוגמה**  
- סיווג: חיזוי אם אדם יאושר להלוואה לפי גיל והכנסה  
- רגרסיה: חיזוי מחיר דירה לפי שטח ומספר חדרים
  
**מאפיין עיקרי**  
- יוצר תמיד **עץ בינארי** (כל צומת מתפצל לשני ענפים בלבד)  
- מתאים גם לבעיות **סיווג** וגם לבעיות **רגרסיה**
  
**מדד חלוקה**  
- **Gini impurity** (לבעיות סיווג)  
- **Mean Squared Error (MSE)** (לבעיות רגרסיה)
  
  
### מה זה Mean Squared Error (MSE) בעצי החלטה?
  
<img src="dec55.png" style="width: 70%" />
  
**מדד חלוקה** שנמצא בשימוש בעצי החלטה מסוג **רגרסיה**  
המטרה של המדד היא להעריך **כמה טוב הפיצול מנבא את הערכים הרציפים** (כמו מחיר, גיל, משקל)  
ככל שה-MSE קטן יותר, כך הפיצול נחשב **טוב יותר**  
  
##### הנוסחה של MSE
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?MSE%20=%20\frac{1}{n}%20\sum_{i=1}^{n}%20(y_i%20-%20\hat{y})^2"/></p>  
  
  
- <img src="https://latex.codecogs.com/gif.latex?n"/> – מספר הדגימות בצומת  
- <img src="https://latex.codecogs.com/gif.latex?y_i"/> – הערך האמיתי של דגימה <img src="https://latex.codecogs.com/gif.latex?i"/>  
- <img src="https://latex.codecogs.com/gif.latex?\hat{y}"/> – ממוצע הערכים בצומת (תחזית העץ)
  
##### איך זה עובד?
  
1. בכל צומת בעץ, העץ שוקל **פיצולים אפשריים** (למשל: האם לפצל לפי גיל גדול מ-30 או לא)  
2. עבור כל פיצול אפשרי, העץ מחשב את ה-MSE בכל תת-קבוצה שנוצרת  
3. העץ בוחר את הפיצול שמביא ל**ירידה הכי גדולה ב-MSE הכולל** (כלומר, שמקטין את השגיאה הכי הרבה)
  
##### דוגמה פשוטה
  
נניח שיש לנו את הנתונים הבאים (ננסה לנבא **מחיר דירה** לפי **שטח**):
  
| שטח (מ"ר) | מחיר (אלפי ₪) |
|------------|---------------|
| 50         | 1000          |
| 60         | 1200          |
| 70         | 1300          |
| 80         | 1500          |
  
##### צומת ראשי (לפני פיצול):
  
- ממוצע המחירים:  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?\hat{y}%20=%20\frac{1000%20+%201200%20+%201300%20+%201500}{4}%20=%201250"/></p>  
  
  
- חישוב ה-MSE:  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?MSE%20=%20\frac{1}{4}%20\left(%20(1000%20-%201250)^2%20+%20(1200%20-%201250)^2%20+%20(1300%20-%201250)^2%20+%20(1500%20-%201250)^2%20\right)"/></p>  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?MSE%20=%20\frac{1}{4}%20(62500%20+%202500%20+%202500%20+%2062500)%20=%20\frac{130000}{4}%20=%2032500"/></p>  
  
  
##### אחרי פיצול (למשל לפי שטח גדול מ-65):
  
- קבוצה 1 (שטח ≤ 65):  
  - דירות: 50 מ"ר (1000), 60 מ"ר (1200)  
  - ממוצע: 1100  
  - MSE:  
  <p align="center"><img src="https://latex.codecogs.com/gif.latex?\frac{1}{2}%20\left(%20(1000%20-%201100)^2%20+%20(1200%20-%201100)^2%20\right)%20=%20\frac{1}{2}%20(10000%20+%2010000)%20=%2010000"/></p>  
  
  
- קבוצה 2 (שטח > 65):  
  - דירות: 70 מ"ר (1300), 80 מ"ר (1500)  
  - ממוצע: 1400  
  - MSE:  
  <p align="center"><img src="https://latex.codecogs.com/gif.latex?\frac{1}{2}%20\left(%20(1300%20-%201400)^2%20+%20(1500%20-%201400)^2%20\right)%20=%20\frac{1}{2}%20(10000%20+%2010000)%20=%2010000"/></p>  
  
  
- MSE כולל אחרי פיצול:  
  <p align="center"><img src="https://latex.codecogs.com/gif.latex?\frac{2}{4}%20\cdot%2010000%20+%20\frac{2}{4}%20\cdot%2010000%20=%2010000"/></p>  
  
  
##### סיכום:
  
- לפני פיצול: **MSE = 32500**  
- אחרי פיצול: **MSE = 10000**
  
מכאן שהפיצול **שיפר את הדיוק** (כי ה-MSE ירד)
  
## 2. ID3 (Iterative Dichotomiser 3)
  
<img src="dec7.png" style="width: 80%" />
  
**דוגמה**  
- סיווג אם לשחק טניס לפי תנאי מזג האוויר (תכונות כמו "שמשי", "גשום", "לח")
  
**מאפיין עיקרי**  
- עובד טוב עם **נתונים קטגוריים בלבד** – תכונות שמחולקות לקבוצות ברורות כמו צבע או מזג אוויר  
- **נתונים רציפים** (כמו גיל או הכנסה) דורשים **חלוקה לטווחים** לפני השימוש
- יוצר **עץ לא בהכרח בינארי** (כל צומת יכול להתפצל גם ליותר משני ענפים)  
  
**מדד חלוקה**  
- **Information Gain** (מבוסס על **Entropy**)
  
### מה זה Information Gain?
  
**מדד חלוקה** שמשמש בעצי החלטה (בעיקר **ID3** ו-**C4.5**)  
המטרה של IG היא למדוד **כמה אי-סדר (אנטרופי)** הצלחנו **להפחית** בעזרת פיצול נתונים לפי תכונה מסוימת  
ככל שה-IG **גבוה יותר**, הפיצול נחשב **טוב יותר** כי הוא עושה את הקבוצות **טהורות** יותר
  
##### למה צריך את זה?
  
בכל שלב בבניית עץ החלטה, צריך לבחור **איזו תכונה הכי משתלם לפצל לפיה**  
- תכונה עם **IG גבוה** תביא לחלוקה שבה הקבוצות הרבה יותר **אחידות**  
- תכונה עם **IG נמוך** לא תעזור לנו לסדר את הדאטה, והקבוצות ישארו **מעורבבות**
  
איי גיי עוזר לנו לבחור את **התכונה הכי טובה** לפיצול בכל צומת
  
##### איך מחשבים את זה?
  
1. מחשבים את ה-**Entropy** של הקבוצה לפני הפיצול:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Entropy(S)%20=%20-\sum_{i=1}^{c}%20p_i%20\log_2(p_i)"/></p>  
  
  
- <img src="https://latex.codecogs.com/gif.latex?S"/> – הקבוצה הנוכחית  
- <img src="https://latex.codecogs.com/gif.latex?c"/> – מספר הקבוצות (קטגוריות)  
- <img src="https://latex.codecogs.com/gif.latex?p_i"/> – הסיכוי של כל קבוצה (למשל, אחוז ה-Yes וה-No)
  
2. מחשבים את ה-**Entropy הממוצע אחרי הפיצול** (Weighted Average):
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Entropy_{after}%20=%20\sum_{j=1}^{k}%20\frac{|S_j|}{|S|}%20Entropy(S_j)"/></p>  
  
  
- <img src="https://latex.codecogs.com/gif.latex?k"/> – מספר תתי הקבוצות שנוצרו מהפיצול  
- <img src="https://latex.codecogs.com/gif.latex?S_j"/> – כל תת-קבוצה  
- <img src="https://latex.codecogs.com/gif.latex?|S_j|"/> – גודל תת-הקבוצה  
- <img src="https://latex.codecogs.com/gif.latex?|S|"/> – גודל הקבוצה המקורית
  
3. מחשבים את ה-**Information Gain**:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?IG%20=%20Entropy_{before}%20-%20Entropy_{after}"/></p>  
  
  
##### דוגמה
  
נתונים:  
| Outlook  | Play Tennis |
|----------|-------------|
| Sunny    | No          |
| Sunny    | No          |
| Overcast | Yes         |
| Rain     | Yes         |
| Rain     | Yes         |
| Rain     | No          |
| Overcast | Yes         |
| Sunny    | Yes         |
| Sunny    | Yes         |
| Rain     | Yes         |
| Sunny    | No          |
| Overcast | Yes         |
| Overcast | Yes         |
| Rain     | No          |
  
##### 1. מחשבים Entropy לפני הפיצול (כל הדאטה):
  
- **Yes** = 9, **No** = 5
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Entropy(S)%20=%20-\left(%20\frac{9}{14}%20\log_2%20\frac{9}{14}%20+%20\frac{5}{14}%20\log_2%20\frac{5}{14}%20\right)%20%20\approx%200.940"/></p>  
  
  
##### 2. מחשבים Entropy אחרי פיצול לפי Outlook:
  
- **Sunny** (5 דגימות): 2 Yes, 3 No → Entropy ≈ 0.971  
- **Overcast** (4 דגימות): 4 Yes, 0 No → Entropy = 0  
- **Rain** (5 דגימות): 3 Yes, 2 No → Entropy ≈ 0.971
  
- Weighted Entropy after split:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Entropy_{after}%20=%20\frac{5}{14}%20\cdot%200.971%20+%20\frac{4}{14}%20\cdot%200%20+%20\frac{5}{14}%20\cdot%200.971%20%20\approx%200.693"/></p>  
  
  
##### 3. מחשבים Information Gain:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?IG%20=%200.940%20-%200.693%20=%200.247"/></p>  
  
  
## 3. C4.5
  
<img src="dec6.png" style="width: 70%" />
  
**דוגמה**  
- חיזוי אם לקוח יקנה מחשב לפי גיל (רציף), תעסוקה (קטגוריה), והכנסה (רציף)
  
**מאפיין עיקרי**  
- **תומך בנתונים רציפים** – מסוגל להתמודד עם מספרים כמו גיל או הכנסה בלי לחלק לטווחים  
- **תומך בערכים חסרים** – יכול לעבוד גם אם חסר מידע בחלק מהפיצ'רים  
- כולל **גיזום (Pruning)** – קיצור העץ כדי למנוע **אוברפיטינג**
- יוצר **עץ לא בהכרח בינארי** (כל צומת יכול להתפצל גם ליותר משני ענפים)  
  
**מדד חלוקה**  
- **Gain Ratio** (שיפור של Information Gain)
  
### מה זה Gain Ratio?
  
  מדד חלוקה בעצי החלטה (למשל בעץ **C4.5**)  
המטרה שלו היא **לשפר** את **Information Gain** ולפתור את הבעיה שבה Information Gain **מעדיף תכונות עם הרבה ערכים שונים** (כמו ת"ז או מזהה ייחודי)  
**Gain Ratio** מתקן את זה על ידי חלוקה ב-**Split Information** (מידע על פיזור הפיצולים)
  
##### למה צריך את Gain Ratio?
  
- **איי גיי** יכול להעדיף תכונות שיש להן **המון ערכים ייחודיים**, גם אם זה **לא עוזר לסיווג**  
- **ראטיו גיין** בודק גם **כמה הפיצול מתפזר** – אם הפיצול מפזר את הנתונים להרבה קבוצות קטנות, הוא מעניש אותו
  
##### איך מחשבים Gain Ratio?
  
1. מחשבים את **Information Gain (IG)**:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?IG(S,%20A)%20=%20Entropy(S)%20-%20\sum_{i=1}^{k}%20\frac{|S_i|}{|S|}%20\cdot%20Entropy(S_i)"/></p>  
  
  
2. מחשבים את **Split Information**:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?SplitInfo(S,%20A)%20=%20-\sum_{i=1}^{k}%20\frac{|S_i|}{|S|}%20\cdot%20\log_2%20\left(%20\frac{|S_i|}{|S|}%20\right)"/></p>  
  
  
3. מחשבים את **Gain Ratio**:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?GainRatio(S,%20A)%20=%20\frac{IG(S,%20A)}{SplitInfo(S,%20A)}"/></p>  
  
  
##### דוגמה
  
נניח שיש תכונה אחת עם **3 ערכים** (למשל: Low, Medium, High)  
ותכונה אחרת עם **14 ערכים שונים** (כמו ת"ז)
  
- **איי גיי** עשוי לבחור את ת"ז כי הוא רואה שכל דגימה נכנסת לקבוצה נפרדת (כלומר, הפיצול מאוד חד)  
- אבל **גיין ראטיו** יסתכל גם על **כמה התפזרו הדגימות** בין הקבוצות  
- הוא יעניש פיצולים שמפזרים את הנתונים ליותר מדי קבוצות קטנות, ולכן יעדיף את התכונה עם Low/Medium/High
  
  
## 4. Random Forest
  
<img src="dec8.png" style="width: 80%" />
  
**דוגמה**  
- חיזוי **נטישת לקוחות** (למשל אם לקוח יעזוב חברת סלולר) לפי דפוסי שימוש, היסטוריית תשלומים ופניות לשירות לקוחות
  
**מאפיין עיקרי**  
- יער של **עצים אקראיים**  
  - כל עץ נבנה על **מדגם אקראי** של הנתונים (Random Sampling עם החזרה)  
  - בכל פיצול בעץ נבחרת **קבוצת תכונות אקראית** לבדיקה (Random Feature Selection)  
- משפר **דיוק** ומפחית **אוברפיטינג** ע"י שילוב תחזיות של עצים רבים
  
**מדד חלוקה**  
- כל עץ בתוך היער הוא לרוב **CART** – משתמש ב-**Gini impurity** (לסיווג) או **MSE** (לרגרסיה)
  
---
  
  
  
## השוואה קצרה:
  
### השוואה קצרה:
  
| תכונה                | CART            | ID3                 | C4.5           | Random Forest                       |
|-----------------------|-----------------|---------------------|----------------|-------------------------------------|
| **שימוש**            | סיווג ורגרסיה   | סיווג בלבד          | סיווג בלבד    | סיווג ורגרסיה                      |
| **מדד חלוקה**        | Gini / MSE      | Entropy + Info Gain | Gain Ratio     | Gini / MSE בכל עץ (כמו CART)       |
| **תומך במספרים רציפים** | כן             | לא                  | כן             | כן                                  |
| **תומך בנתונים חסרים של פיצ'ר** | כן              | לא                  | כן             | כן                                  |
| **סוג הפיצול**       | בינארי בלבד     | לא חייב בינארי      | לא חייב בינארי | בינארי בכל עץ (כמו CART), אבל שילוב ביחד שיטת אנסמבל |
  
  
  
  
  
  