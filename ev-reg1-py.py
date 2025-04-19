import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.model_selection import train_test_split

# Create some example data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Add a few outliers
X = np.vstack([X, [[1.9]], [[1.95]], [[1.85]]])
y = np.vstack([y, [[10]], [[12]], [[14]]])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_train_pred = model.predict(X_train)
y_test_pred = model.predict(X_test)

# Calculate metrics
train_mae = mean_absolute_error(y_train, y_train_pred)
test_mae = mean_absolute_error(y_test, y_test_pred)

train_mse = mean_squared_error(y_train, y_train_pred)
test_mse = mean_squared_error(y_test, y_test_pred)

train_rmse = np.sqrt(train_mse)
test_rmse = np.sqrt(test_mse)

# Print results
print(f"Training MAE: {train_mae:.3f}")
print(f"Test MAE: {test_mae:.3f}")
print(f"Training MSE: {train_mse:.3f}")
print(f"Test MSE: {test_mse:.3f}")
print(f"Training RMSE: {train_rmse:.3f}")
print(f"Test RMSE: {test_rmse:.3f}")

# Plot the results
plt.figure(figsize=(12, 8))

# Plot data and regression line
plt.subplot(2, 2, 1)
plt.scatter(X_train, y_train, alpha=0.7, label='Training data')
plt.scatter(X_test, y_test, alpha=0.7, color='green', label='Test data')
plt.plot(X, model.predict(X), color='red', linewidth=2, label='Regression line')
plt.title('Linear Regression with Outliers')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()

# Plot residuals
plt.subplot(2, 2, 2)
plt.scatter(y_train_pred, y_train - y_train_pred, alpha=0.7)
plt.scatter(y_test_pred, y_test - y_test_pred, alpha=0.7, color='green')
plt.axhline(y=0, color='red', linestyle='-', linewidth=1)
plt.title('Residuals')
plt.xlabel('Predicted values')
plt.ylabel('Residuals')

# Plot absolute errors (for MAE)
plt.subplot(2, 2, 3)
plt.scatter(X_train, np.abs(y_train - y_train_pred), alpha=0.7, label='Training |error|')
plt.scatter(X_test, np.abs(y_test - y_test_pred), alpha=0.7, color='green', label='Test |error|')
plt.axhline(y=train_mae, color='blue', linestyle='--', linewidth=1, label=f'Train MAE: {train_mae:.3f}')
plt.axhline(y=test_mae, color='green', linestyle='--', linewidth=1, label=f'Test MAE: {test_mae:.3f}')
plt.title('Absolute Errors (MAE)')
plt.xlabel('X')
plt.ylabel('|Actual - Predicted|')
plt.legend()

# Plot squared errors (for MSE/RMSE)
plt.subplot(2, 2, 4)
plt.scatter(X_train, (y_train - y_train_pred)**2, alpha=0.7, label='Training error²')
plt.scatter(X_test, (y_test - y_test_pred)**2, alpha=0.7, color='green', label='Test error²')
plt.axhline(y=train_mse, color='blue', linestyle='--', linewidth=1, label=f'Train MSE: {train_mse:.3f}')
plt.axhline(y=test_mse, color='green', linestyle='--', linewidth=1, label=f'Test MSE: {test_mse:.3f}')
plt.title('Squared Errors (MSE)')
plt.xlabel('X')
plt.ylabel('(Actual - Predicted)²')
plt.legend()

plt.tight_layout()
plt.show()
