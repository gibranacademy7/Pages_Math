import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Data
water = np.array([2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 4, 5, 6, 7])
sunlight = np.array([3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5])
plant_height = np.array([12, 18, 23, 26, 25, 22, 16, 24, 30, 32, 28, 22, 28, 34, 31])

# Combine features
X = np.column_stack((water, sunlight))
y = plant_height

# Polynomial features up to degree 3
poly = PolynomialFeatures(degree=3)
X_poly = poly.fit_transform(X)

# Train linear regression model
model = LinearRegression()
model.fit(X_poly, y)

# Grid for prediction
water_grid = np.linspace(2, 8, 30)
sunlight_grid = np.linspace(2, 6, 30)
water_mesh, sunlight_mesh = np.meshgrid(water_grid, sunlight_grid)

# Predict over grid
X_grid = np.column_stack((water_mesh.ravel(), sunlight_mesh.ravel()))
X_grid_poly = poly.transform(X_grid)
height_pred = model.predict(X_grid_poly).reshape(water_mesh.shape)

# Find optimal point
max_height = np.max(height_pred)
max_idx = np.unravel_index(np.argmax(height_pred), height_pred.shape)
optimal_water = water_mesh[max_idx]
optimal_sunlight = sunlight_mesh[max_idx]

# Print results
print(f"Model polynomial coefficients: {model.coef_}")
print(f"Optimal water amount: {optimal_water:.2f} liters per week")
print(f"Optimal sunlight exposure: {optimal_sunlight:.2f} hours per day")
print(f"Maximum predicted plant height: {max_height:.2f} cm")

# 3D Plot
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(water_mesh, sunlight_mesh, height_pred,
                       cmap=cm.viridis, alpha=0.7, linewidth=0)
ax.scatter(water, sunlight, plant_height, c='red', s=50, label='Data points')
ax.scatter([optimal_water], [optimal_sunlight], [max_height],
           c='yellow', s=100, label='Optimal point')

ax.set_xlabel('Water amount (liters/week)')
ax.set_ylabel('Sunlight exposure (hours/day)')
ax.set_zlabel('Plant height (cm)')
ax.set_title('Plant Growth Model: Water and Sunlight vs Height')
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
ax.legend()

plt.show()
