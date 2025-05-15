# השוואה בין Gini Impurity ל-Entropy
  
## מטרת המדדים:
- **Gini Impurity** ו-**Entropy** הם מדדים שמודדים **"חוסר טוהר"** או **מידת ערבוב** בקבוצה.
- משתמשים בהם בעצי החלטה (**Classification Trees**) כדי לבחור את הפיצול הכי טוב.
  
## נוסחאות:
  
### 1. Gini Impurity:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Gini%20=%201%20-%20\sum_{i=1}^{k}%20p_i^2"/></p>  
  
  
- <img src="https://latex.codecogs.com/gif.latex?p_i"/> זה ההסתברות של כל מחלקה (class).
- הערך המקסימלי מתקבל כשהמחלקות מעורבבות שווה בשווה.
  
### 2. Entropy:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Entropy%20=%20-%20\sum_{i=1}^{k}%20p_i%20\cdot%20\log_2(p_i)"/></p>  
  
  
- גם פה <img src="https://latex.codecogs.com/gif.latex?p_i"/> זה ההסתברות של כל מחלקה.
- ערך גבוה יותר אומר יותר ערבוב (חוסר טוהר).
  
## דוגמה:
  
נניח שיש לך קבוצה עם 4 דוגמאות:
  
- 2 דוגמאות בקטגוריה A.
- 2 דוגמאות בקטגוריה B.
  
### חישוב Gini Impurity:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Gini%20=%201%20-%20(p_A^2%20+%20p_B^2)%20=%201%20-%20(0.5^2%20+%200.5^2)%20=%201%20-%20(0.25%20+%200.25)%20=%200.5"/></p>  
  
  
### חישוב Entropy:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Entropy%20=%20-%20(p_A%20\cdot%20\log_2(p_A)%20+%20p_B%20\cdot%20\log_2(p_B))%20=%20-%20(0.5%20\cdot%20\log_2(0.5)%20+%200.5%20\cdot%20\log_2(0.5))%20=%201"/></p>  
  
  
## השוואה כללית:
  
<img src="dec5.png" style="width: 50%" />
  
| מאפיין              | Gini Impurity            | Entropy                |
|----------------------|---------------------------|------------------------|
| נוסחה               | <img src="https://latex.codecogs.com/gif.latex?1%20-%20\sum%20p_i^2"/>       | <img src="https://latex.codecogs.com/gif.latex?-%20\sum%20p_i%20\log_2%20p_i"/> |
| ערך מקסימלי (2 מחלקות) | 0.5                      | 1                      |
| חישוב               | פשוט ומהיר יותר          | איטי יותר (יש לוגים)   |
| פרשנות              | מדד חוסר טוהר             | מדד חוסר טוהר (מידע)  |
  
  
## מתי להשתמש?
  
| מאפיין            | Gini Impurity           | Entropy                  |
|-------------------|-------------------------|--------------------------|
| חישוביות          | מהיר יותר (ללא לוגריתם) | איטי יותר (יש לוגריתם)   |
| רגישות            | פחות רגיש להבדלים קטנים | יותר רגיש להבדלים קטנים  |
| מתי לבחור         | כשחשובה מהירות          | כשחשובה דיוק/מידע         |
| שימוש נפוץ        | Decision Tree (CART)    | Decision Tree (ID3, C4.5)|
  
**המלצה כללית:**
- אם יש לך הרבה נתונים או אתה צריך חישוב מהיר → **Gini**  
- אם אתה רוצה להיות רגיש יותר לאי-ודאות → **Entropy**
  
- **Gini** is more commonly used in decision trees like **CART** (Classification And Regression Tree) because of its simpler computation
- **Entropy** is often used when information gain is meaningful, such as in the ID3 tree

# דוגמא
  
**ראה סוגי עצי החלטה בשקף הבא**

נניח שיש לנו מערכת נתונים פשוטה עם שני מאפיינים (X1, X2) וקטגוריה יעד (Y) כפי שמוצג בטבלה:
  
| X1 | X2 | Y |
|----|----|----|
| 1  | 3  | A  |
| 2  | 1  | A  |
| 3  | 2  | B  |
| 4  | 3  | B  |
| 5  | 1  | A  |
| 6  | 2  | B  |

##  Gini index Vs Entropy

<img src="dec14.png" style="widht: 100%" />

