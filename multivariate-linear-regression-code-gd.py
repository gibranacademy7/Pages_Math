import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import seaborn as sns

# Create a DataFrame from our example data
columns = ['Area', 'Rooms', 'Age', 'Distance', 'Price']
data = [
    [70, 3, 15, 5, 1200],
    [90, 4, 10, 7, 1500],
    [60, 2, 20, 3, 1100],
    [120, 5, 5, 10, 1800],
    [80, 3, 12, 6, 1300],
    [110, 4, 8, 8, 1650],
    [100, 4, 7, 5, 1750],
    [75, 3, 18, 4, 1250],
    [95, 4, 9, 6, 1550],
    [130, 5, 3, 12, 1900]
]
df = pd.DataFrame(data, columns=columns)

# Prepare features (X) and target (y)
X = df.drop('Price', axis=1)
y = df['Price']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Add a column of ones for the intercept term
X_train_scaled = np.c_[np.ones(X_train_scaled.shape[0]), X_train_scaled]
X_test_scaled = np.c_[np.ones(X_test_scaled.shape[0]), X_test_scaled]

# Initialize parameters (coefficients)
theta = np.zeros(X_train_scaled.shape[1])

# Gradient Descent parameters
learning_rate = 0.01
iterations = 1000
m = len(y_train)

# Lists to store costs for visualization
costs = []

# Gradient Descent algorithm
for i in range(iterations):
    # Calculate predictions
    predictions = X_train_scaled.dot(theta)
    
    # Calculate errors
    errors = predictions - y_train
    
    # Calculate gradients
    gradients = (1/m) * X_train_scaled.T.dot(errors)
    
    # Update parameters
    theta = theta - learning_rate * gradients
    
    # Calculate cost
    cost = (1/(2*m)) * np.sum(errors**2)
    costs.append(cost)
    
    # Print progress every 100 iterations
    if i % 100 == 0:
        print(f"Iteration {i}, Cost: {cost:.2f}, Theta: {theta}")

# Final parameters
print("\nFinal parameters after Gradient Descent:")
feature_names = ['Intercept'] + X.columns.tolist()
for name, param in zip(feature_names, theta):
    print(f"{name}: {param:.2f}")

# Make predictions
y_pred_train = X_train_scaled.dot(theta)
y_pred_test = X_test_scaled.dot(theta)

# Calculate R² and Adjusted R²
train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)

n = len(X_train)
p = X_train.shape[1]
adj_r2 = 1 - (1 - train_r2) * (n - 1) / (n - p - 1)

print(f"\nTraining R²: {train_r2:.2f}")
print(f"Testing R²: {test_r2:.2f}")
print(f"Adjusted R²: {adj_r2:.2f}")

# Predict price for a new apartment
new_apartment = np.array([[85, 3, 10, 7]])
new_apartment_scaled = scaler.transform(new_apartment)
new_apartment_scaled = np.c_[np.ones(new_apartment_scaled.shape[0]), new_apartment_scaled]
predicted_price = new_apartment_scaled.dot(theta)[0]
print(f"\nPredicted price for a new apartment: {predicted_price:.2f} thousand ILS")

# Plot the cost history
plt.figure(figsize=(10, 6))
plt.plot(costs)
plt.title('Cost vs. Iteration')
plt.xlabel('Iteration')
plt.ylabel('Cost')
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot actual vs predicted values
plt.figure(figsize=(10, 6))
plt.scatter(y_train, y_pred_train, color='blue', label='Training data')
plt.scatter(y_test, y_pred_test, color='red', label='Testing data')
plt.plot([min(y), max(y)], [min(y), max(y)], 'k--')
plt.title('Actual vs Predicted Prices')
plt.xlabel('Actual Price (thousand ILS)')
plt.ylabel('Predicted Price (thousand ILS)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Apartment Features')
plt.tight_layout()
plt.show()

# Visualize feature importances (using absolute values of coefficients)
# We need to exclude the intercept and account for feature scaling
scaled_coeffs = theta[1:] / scaler.scale_
plt.figure(figsize=(10, 6))
plt.bar(X.columns, np.abs(scaled_coeffs))
plt.title('Feature Importance (Absolute Scaled Coefficients)')
plt.xlabel('Features')
plt.ylabel('|Coefficient|')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
