# 📈 Support Vector Regression (SVR)
  
## What is SVR?
  
SVR (Support Vector Regression) 
  
גרסה של אלגוריתם מכונת וקטורים תומכים, 
אבל במקום סיווג (קלסיפיקציה) – הוא מבצע **רגרסיה** (חיזוי של ערכים רציפים, כמו מחירים או טמפרטורות)
  
הוא מנסה למצוא **פונקציה פשוטה ככל האפשר** שמתאימה לנתונים — אך תוך התעלמות משגיאות קטנות
  
<img src="svm16.png" style= "width: 100%" />
  
---
  
# 🎯 Core Idea
  
Instead of requiring the model to fit every point exactly, SVR allows a **tolerance margin (ε)** around the function. As long as the error is within this ε — we don't care. Only points **above or below this margin** matter
  
> ✨ Goal: Find a function where **as many points as possible fall within ±ε**
  
---
  
## 📐 The SVR Tube – "ε-Tube"
  
- This is a region of ±ε around the predicted function
- Points **inside the tube** → do not affect the function
- Points **outside the tube** → affect it (Support Vectors)
  
---
  
## 🧠 What Are Support Vectors in SVR?
  
- They are **points outside the tube** (error > ε).
- They receive weights <img src="https://latex.codecogs.com/gif.latex?\alpha_i"/> or <img src="https://latex.codecogs.com/gif.latex?\alpha_i^*"/>. see below
- They are the **only ones that influence the prediction function**.
  
### 🔍 Analogy:
> The graph is like a rubber band, and the points outside the tube are strings pulling on it — **shaping the function**.
  
## 🌟 What is Alpha-Star (<img src="https://latex.codecogs.com/gif.latex?\alpha_i^*"/>)?
  
In SVR, every support vector may influence the prediction in one of two ways:
  
- If the prediction is **too high** compared to the true value → it contributes with <img src="https://latex.codecogs.com/gif.latex?\alpha_i"/>
- If the prediction is **too low** compared to the true value → it contributes with <img src="https://latex.codecogs.com/gif.latex?\alpha_i^*"/>
  
This leads to the full prediction function:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?f(x)%20=%20\sum_i%20(\alpha_i%20-%20\alpha_i^*)%20K(x_i,%20x)%20+%20b"/></p>  
  
  
Only **one** of the two (<img src="https://latex.codecogs.com/gif.latex?\alpha_i"/> or <img src="https://latex.codecogs.com/gif.latex?\alpha_i^*"/>) is non-zero for a given point. Together, they create a tug-of-war:
  
- <img src="https://latex.codecogs.com/gif.latex?\alpha_i"/> pulls the function **down** (penalizing overestimation)
- <img src="https://latex.codecogs.com/gif.latex?\alpha_i^*"/> pulls the function **up** (penalizing underestimation)
  
> So the support vectors collectively shape the regression line based on whether the model over- or under-shoots the true value
  
##### 🔍 But what is <img src="https://latex.codecogs.com/gif.latex?K(x_i,%20x)"/>?
  
- <img src="https://latex.codecogs.com/gif.latex?K(x_i,%20x)"/> is the **kernel function**
- It measures the **similarity** between a training point <img src="https://latex.codecogs.com/gif.latex?x_i"/> and a prediction point <img src="https://latex.codecogs.com/gif.latex?x"/>.
- But here’s the magic:
  
> 🪄 The kernel allows us to act as if we’ve mapped the data into a higher-dimensional space — **without actually doing it**
  
This is what enables SVR (and SVM in general) to model complex, nonlinear functions without computational cost of actual transformation. That’s the **kernel trick**!
  
  
When we call `model.predict(x)` in SVR, the model already knows **which training points to use** — the **support vectors**
  
✅ Steps Under the Hood:
  
1. **Training phase (`.fit`)**:
   - The model solves the SVR optimization problem
   - It computes the values <img src="https://latex.codecogs.com/gif.latex?\alpha_i"/> and <img src="https://latex.codecogs.com/gif.latex?\alpha_i^*"/> for each training point
   - Only the points where <img src="https://latex.codecogs.com/gif.latex?\alpha_i%20-%20\alpha_i^*%20\neq%200"/> are kept — these are the **support vectors**
  
2. **Prediction phase (`.predict`)**:
   - The model uses only the saved support vectors
   - For a new input point <img src="https://latex.codecogs.com/gif.latex?x"/>, it calculates:
  
   <p align="center"><img src="https://latex.codecogs.com/gif.latex?f(x)%20=%20\sum_i%20(\alpha_i%20-%20\alpha_i^*)%20K(x_i,%20x)%20+%20b"/></p>  
  
  
   - Each <img src="https://latex.codecogs.com/gif.latex?x_i"/> is a support vector, and the kernel function <img src="https://latex.codecogs.com/gif.latex?K(x_i,%20x)"/> measures similarity to the new point.
   - The result is a weighted sum of similarities plus the bias <img src="https://latex.codecogs.com/gif.latex?b"/>.
  
Why This Is Efficient:
  
- You **don’t need to compare with every training point**, only the support vectors
- This keeps prediction fast and focused only on the most important examples
  
---
  
## ⚙️ General SVR Optimization Formula
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?\text{Minimize:%20}%20\frac{1}{2}%20\|w\|^2%20+%20C%20\sum_i%20(\xi_i%20+%20\xi_i^*)"/></p>  
  
  
Subject to:
  
<p align="center"><img src="https://latex.codecogs.com/gif.latex?\begin{aligned}&amp;%20y_i%20-%20w^T%20x_i%20-%20b%20\leq%20\varepsilon%20+%20\xi_i%20\\&amp;%20w^T%20x_i%20+%20b%20-%20y_i%20\leq%20\varepsilon%20+%20\xi_i^*\end{aligned}"/></p>  
  
  
Where:
- <img src="https://latex.codecogs.com/gif.latex?\xi_i"/>: the amount the prediction exceeds the upper boundary (above the ε-tube)
- <img src="https://latex.codecogs.com/gif.latex?\xi_i^*"/>: the amount the prediction falls below the lower boundary (below the ε-tube)
- Only one of <img src="https://latex.codecogs.com/gif.latex?\xi_i"/> or <img src="https://latex.codecogs.com/gif.latex?\xi_i^*"/> is non-zero per data point
- <img src="https://latex.codecogs.com/gif.latex?C"/> controls the penalty for large errors (how much we care about violations outside the tube)
- x𝑖 is the input vector (feature)
- 𝑦𝑖 is the true output (label) for that input
  
---
  
## 🔢 Linear vs Nonlinear SVR
  
- In **Linear SVR**, the function is explicitly:
  <p align="center"><img src="https://latex.codecogs.com/gif.latex?f(x)%20=%20w^T%20x%20+%20b"/></p>  
  
  and we can compute:
  <p align="center"><img src="https://latex.codecogs.com/gif.latex?w%20=%20\sum_i%20(\alpha_i%20-%20\alpha_i^*)%20x_i"/></p>  
  
  
- In **Nonlinear SVR**, we use a **kernel** to measure similarity, and we don’t compute an explicit w:
  <p align="center"><img src="https://latex.codecogs.com/gif.latex?f(x)%20=%20\sum_i%20(\alpha_i%20-%20\alpha_i^*)%20K(x_i,%20x)%20+%20b"/></p>  
  
  
---
  
## 🎛️ Important SVR Parameters
  
| Parameter | Role |
|----------|------|
| `ε` (epsilon) | Defines the width of the tube – errors smaller than ε are ignored |
| `C` | Penalizes points outside the tube – controls model complexity |
| `kernel` | Determines function shape (linear, rbf, poly, sigmoid) |
| `gamma` | Used in nonlinear kernels – sets how far each point's influence reaches |
  
---
  
## 🧪 Basic Example in Code
```python
from sklearn.svm import SVR
import numpy as np
import matplotlib.pyplot as plt
  
# Generate data
X = np.linspace(0, 10, 100).reshape(-1, 1)
y = np.sin(X).ravel()
y[::5] += 0.5 * np.random.randn(20)  # add some noise
  
# SVR model with RBF kernel
model = SVR(kernel='rbf', C=100, epsilon=0.1)
model.fit(X, y)
y_pred = model.predict(X)
  
# Plot
plt.scatter(X, y, color='gray', label='Data')
plt.plot(X, y_pred, color='red', label='SVR Prediction')
plt.title('SVR with ε-Tube')
plt.legend()
plt.show()
```
  
---
  
## 💬 Quick Summary
  
| Feature              | SVM (Classification)       | SVR (Regression)                      |
|----------------------|-----------------------------|----------------------------------------|
| Goal                 | Separate between classes    | Fit function with ε tolerance         |
| Margin               | Distance between classes    | No margin – there's a tolerance tube  |
| Support Vectors      | Touch the margin boundaries | Outside the tube – influence function |
| Penalized Points     | Misclassified samples        | Points with error > ε                 |
| Prediction Formula   | <img src="https://latex.codecogs.com/gif.latex?f(x)%20=%20w^T%20x%20+%20b"/>       | <img src="https://latex.codecogs.com/gif.latex?f(x)%20=%20\sum_i%20(\alpha_i%20-%20\alpha_i^*)%20K(x_i,%20x)%20+%20b"/> |
  
---
  
  