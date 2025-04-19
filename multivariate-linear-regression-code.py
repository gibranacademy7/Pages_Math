import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
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

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Print model coefficients
print(f"Intercept (β₀): {model.intercept_:.2f}")
for i, col in enumerate(X.columns):
    print(f"Coefficient for {col} (β{i+1}): {model.coef_[i]:.2f}")

# Make predictions for the entire dataset
y_pred_all = model.predict(X)
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Evaluate the model
train_mse = mean_squared_error(y_train, y_pred_train)
test_mse = mean_squared_error(y_test, y_pred_test)
train_r2 = r2_score(y_train, y_pred_train)
test_r2 = r2_score(y_test, y_pred_test)

print(f"\nTraining MSE: {train_mse:.2f}")
print(f"Testing MSE: {test_mse:.2f}")
print(f"Training R²: {train_r2:.2f}")
print(f"Testing R²: {test_r2:.2f}")

# Calculate adjusted R²
n = len(X_train)
p = X_train.shape[1]
adj_r2 = 1 - (1 - train_r2) * (n - 1) / (n - p - 1)
print(f"Adjusted R²: {adj_r2:.2f}")

# Make a prediction for a new apartment
new_apartment = np.array([[85, 3, 10, 7]])
predicted_price = model.predict(new_apartment)[0]
print(f"\nPredicted price for a new apartment: {predicted_price:.2f} thousand ILS")

# Visualize the data (simplified for 2D)
plt.figure(figsize=(12, 8))
# Create scatter plot with area vs price, with rooms shown by point size and age by color
scatter = plt.scatter(df['Area'], df['Price'], s=df['Rooms']*30, c=df['Age'], cmap='viridis', alpha=0.7)
# Add colorbar to show age scale
cbar = plt.colorbar(scatter)
cbar.set_label('Building Age (years)')
# Add visualization of the relationship between area and price
X_area = df[['Area']]
y_price = df['Price']
area_model = LinearRegression().fit(X_area, y_price)
area_line = np.linspace(min(df['Area']), max(df['Area']), 100).reshape(-1, 1)
price_line = area_model.predict(area_line)
plt.plot(area_line, price_line, color='red', linestyle='--')
plt.title('Multiple Linear Regression: Apartment Prices')
plt.xlabel('Area (sq m)')
plt.ylabel('Price (thousand ILS)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(['Area vs Price Trend', 'Apartments (size = rooms, color = age)'])
plt.tight_layout()
plt.show()

# Correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix of Apartment Features')
plt.tight_layout()
plt.show()

# Partial regression plots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
feature_names = X.columns
for i, ax in enumerate(axes.flat):
    if i < len(feature_names):
        feature = feature_names[i]
        sns.regplot(x=X[feature], y=y, ax=ax)
        ax.set_title(f'Partial Regression: {feature} vs Price')
        ax.set_xlabel(feature)
        ax.set_ylabel('Price (thousand ILS)')
        ax.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# ============ ADDED VISUALIZATION: PREDICTION VS ACTUAL ============

# Create a DataFrame with actual and predicted values
results_df = pd.DataFrame({
    'Actual': y,
    'Predicted': y_pred_all,
    'Residual': y - y_pred_all,
    'Dataset': ['Train' if idx in X_train.index else 'Test' for idx in X.index]
})

# Sort by actual values for better visualization
results_df = results_df.sort_values('Actual')
results_df = results_df.reset_index(drop=True)

# 1. Actual vs Predicted Plot
plt.figure(figsize=(14, 10))

# Create a subplot with 2 rows and 2 columns
plt.subplot(2, 2, 1)
sns.scatterplot(x='Actual', y='Predicted', hue='Dataset', data=results_df, s=100)
# Add perfect prediction line
min_val = min(results_df['Actual'].min(), results_df['Predicted'].min())
max_val = max(results_df['Actual'].max(), results_df['Predicted'].max())
plt.plot([min_val, max_val], [min_val, max_val], 'k--', alpha=0.5)
plt.title('Actual vs Predicted Prices')
plt.xlabel('Actual Price (thousand ILS)')
plt.ylabel('Predicted Price (thousand ILS)')
plt.grid(True, linestyle='--', alpha=0.7)

# 2. Residual Plot
plt.subplot(2, 2, 2)
sns.scatterplot(x='Actual', y='Residual', hue='Dataset', data=results_df, s=100)
plt.axhline(y=0, color='k', linestyle='--', alpha=0.5)
plt.title('Residual Plot (Actual vs Error)')
plt.xlabel('Actual Price (thousand ILS)')
plt.ylabel('Residual (Actual - Predicted)')
plt.grid(True, linestyle='--', alpha=0.7)

# 3. Bar Chart Comparison
plt.subplot(2, 1, 2)
# Create indices for bar positions
indices = np.arange(len(results_df))
# Width of bars
bar_width = 0.35
# Create bars
plt.bar(indices - bar_width/2, results_df['Actual'], bar_width, label='Actual', alpha=0.7)
plt.bar(indices + bar_width/2, results_df['Predicted'], bar_width, label='Predicted', alpha=0.7)
# Add error lines to show the difference
for i in indices:
    if results_df.iloc[i]['Actual'] > results_df.iloc[i]['Predicted']:
        plt.plot([i, i], [results_df.iloc[i]['Predicted'], results_df.iloc[i]['Actual']], 'r-', alpha=0.5)
    else:
        plt.plot([i, i], [results_df.iloc[i]['Actual'], results_df.iloc[i]['Predicted']], 'b-', alpha=0.5)

# Customize the plot
plt.xticks(indices, [f"Apt {i+1}" for i in indices])
plt.title('Actual vs Predicted Prices Comparison')
plt.xlabel('Apartment')
plt.ylabel('Price (thousand ILS)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

# 4. Additional visualization: Histogram of residuals
plt.figure(figsize=(10, 6))
sns.histplot(results_df['Residual'], kde=True, bins=10)
plt.axvline(x=0, color='r', linestyle='--')
plt.title('Distribution of Residuals')
plt.xlabel('Residual Value (Actual - Predicted)')
plt.ylabel('Frequency')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
