  
# 🌳 חישוב Gini Impurity בעץ החלטה — דוגמה מלאה
  
נניח שיש לנו מערכת נתונים פשוטה עם שני מאפיינים (X1, X2) וקטגוריה יעד (Y) כפי שמוצג בטבלה:
  
| X1 | X2 | Y |
|----|----|----|
| 1  | 3  | A |
| 2  | 1  | A |
| 3  | 2  | B |
| 4  | 3  | B |
| 5  | 1  | A |
| 6  | 2  | B |
  
---
  
## 🔹 חישוב Gini של השורש (Root)
  
סופרים כמה מכל קטגוריה:
  
- A: 3 דגימות → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20\frac{3}{6}"/></p>  
  
- B: 3 דגימות → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_B%20=%20\frac{3}{6}"/></p>  
  
  
נחשב Gini impurity בשורש:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(root)%20=%201%20-%20(0.5^2%20+%200.5^2)%20=%201%20-%20(0.25%20+%200.25)%20=%200.5"/></p>  
  
  
---
  
## ✂️ נבחן פיצול לפי X1 <= 3
  
### קבוצה שמאלית (X1 <= 3):
  
- דגימות: (1,A), (2,A), (3,B)  
- A: 2 מתוך 3 → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20\frac{2}{3},%20p_B%20=%20\frac{1}{3}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(left)%20=%201%20-%20\left(\left(\frac{2}{3}\right)^2%20+%20\left(\frac{1}{3}\right)^2\right)%20=%201%20-%20\left(\frac{4}{9}%20+%20\frac{1}{9}\right)%20=%201%20-%20\frac{5}{9}%20=%20\frac{4}{9}%20\approx%200.44"/></p>  
  
  
### קבוצה ימנית (X1 > 3):
  
- דגימות: (4,B), (5,A), (6,B)  
- A: 1 מתוך 3 → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20\frac{1}{3},%20p_B%20=%20\frac{2}{3}"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(right)%20=%201%20-%20\left(\left(\frac{1}{3}\right)^2%20+%20\left(\frac{2}{3}\right)^2\right)%20=%201%20-%20\left(\frac{1}{9}%20+%20\frac{4}{9}\right)%20=%201%20-%20\frac{5}{9}%20=%20\frac{4}{9}%20\approx%200.44"/></p>  
  
  
### חישוב Gini הכולל לאחר הפיצול:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G_{weighted}%20=%20\frac{3}{6}%20\cdot%200.44%20+%20\frac{3}{6}%20\cdot%200.44%20=%200.44"/></p>  
  
  
### רווח (Gain) מהפיצול:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Gain%20=%20G(root)%20-%20G_{weighted}%20=%200.5%20-%200.44%20=%200.06"/></p>  
  
  
---
  
## ✂️ נבחן פיצול לפי X2 <= 2
  
### קבוצה שמאלית (X2 <= 2):
  
- דגימות: (2,A), (3,B), (5,A), (6,B)  
- A: 2, B: 2 → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20p_B%20=%200.5"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(left)%20=%201%20-%20(0.5^2%20+%200.5^2)%20=%200.5"/></p>  
  
  
### קבוצה ימנית (X2 > 2):
  
- דגימות: (1,A), (4,B)  
- A: 1, B: 1 → <p align="center"><img src="https://latex.codecogs.com/gif.latex?p_A%20=%20p_B%20=%200.5"/></p>  
  
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G(right)%20=%200.5"/></p>  
  
  
### Gini משוקלל:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?G_{weighted}%20=%20\frac{4}{6}%20\cdot%200.5%20+%20\frac{2}{6}%20\cdot%200.5%20=%200.5"/></p>  
  
  
### רווח:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?Gain%20=%200.5%20-%200.5%20=%200"/></p>  
  
  
---
  
## ✅ מסקנה:
  
- הפיצול לפי **X1** מפחית את Gini ל-0.44 → רווח (Gain) של **0.06**
- הפיצול לפי **X2** לא משפר את Gini כלל
  
🔮 לכן עדיף לפצל לפי **X1 ≤ 3**
  
---
  
💃 ולגבי הטנגו... אם ה-GINI יורד — אנחנו רוקדים את ריקוד ההחלטות כמו מקצוענים 🕺❤️
  