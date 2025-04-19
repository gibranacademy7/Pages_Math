import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, train_test_split, learning_curve
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
import time
import warnings

warnings.filterwarnings('ignore')

# Load or create dataset
print("Loading dataset...")

# You can try different datasets like these:
# mnist_784, fashion-mnist, covertype, shuttle, letter
dataset = fetch_openml('fashion-mnist', version=1, as_frame=False)
X, y = dataset.data, dataset.target

# Take a subset for faster computation if needed
subset_size = 5000
if X.shape[0] > subset_size:
    indices = np.random.choice(X.shape[0], subset_size, replace=False)
    X, y = X[indices], y[indices]
print(f"Dataset shape: {X.shape}, with {len(np.unique(y))} classes")

# Split the data into training, validation, and test sets
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

print(f"Training set: {X_train.shape}")
print(f"Validation set: {X_val.shape}")
print(f"Test set: {X_test.shape}")

# Create a pipeline that includes scaling and KNN
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

reduced_param_grid = {
    'knn__n_neighbors': np.arange(1, 31, 2),  # K values from 1 to 30 (odd numbers)
    'knn__weights': ['uniform', 'distance'],  # Weight function
    'knn__p': [1, 2]  # 1 for Manhattan, 2 for Euclidean
}

# Create GridSearchCV
print("Setting up GridSearchCV...")
grid_search = GridSearchCV(
    pipeline,
    reduced_param_grid,  # Use reduced_param_grid for faster execution
    cv=5,  # 5-fold cross-validation
    n_jobs=-1,  # Use all available cores
    verbose=1,
    scoring='accuracy',
    return_train_score=True
)

# Fit the model
print("Training model with GridSearchCV...")
start_time = time.time()
grid_search.fit(X_train, y_train)
end_time = time.time()
print(f"GridSearchCV completed in {end_time - start_time:.2f} seconds")

# Get the best parameters and score
print(f"Best parameters: {grid_search.best_params_}")
print(f"Best cross-validation score: {grid_search.best_score_:.4f}")

# Evaluate on validation set
best_model = grid_search.best_estimator_
val_predictions = best_model.predict(X_val)
val_accuracy = accuracy_score(y_val, val_predictions)
print(f"Validation accuracy: {val_accuracy:.4f}")

# Evaluate on test set
test_predictions = best_model.predict(X_test)
test_accuracy = accuracy_score(y_test, test_predictions)
print(f"Test accuracy: {test_accuracy:.4f}")

# Print classification report
print("\nClassification Report:")
print(classification_report(y_test, test_predictions))

# Plot confusion matrix
plt.figure(figsize=(10, 8))
cm = confusion_matrix(y_test, test_predictions)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('True Label')
plt.xlabel('Predicted Label')

# Visualize the grid search results
results = pd.DataFrame(grid_search.cv_results_)

# Extract K values and corresponding scores
k_values = [params['knn__n_neighbors'] for params in grid_search.cv_results_['params']]
mean_test_scores = grid_search.cv_results_['mean_test_score']
mean_train_scores = grid_search.cv_results_['mean_train_score']

# Group by K and get best score for each K
results_k = results.copy()
results_k['k'] = k_values
best_scores_by_k = results_k.groupby('k').agg({'mean_test_score': 'max'}).reset_index()

# Plot K vs. Accuracy (Best score for each K)
plt.figure(figsize=(12, 6))
plt.plot(best_scores_by_k['k'], best_scores_by_k['mean_test_score'],
         marker='o', markersize=8, linestyle='-', linewidth=2)
plt.title('Best Accuracy Score for each K Value', fontsize=16)
plt.xlabel('K (Number of Neighbors)', fontsize=14)
plt.ylabel('Cross-Validation Accuracy', fontsize=14)
plt.xticks(best_scores_by_k['k'])
plt.grid(True, alpha=0.3)

# Find and mark the optimal K
optimal_k = best_scores_by_k.loc[best_scores_by_k['mean_test_score'].idxmax()]
plt.plot(optimal_k['k'], optimal_k['mean_test_score'], 'ro', markersize=12, markeredgecolor='black')
plt.annotate(f"Optimal K = {int(optimal_k['k'])}\nAccuracy = {optimal_k['mean_test_score']:.4f}",
             xy=(optimal_k['k'], optimal_k['mean_test_score']),
             xytext=(optimal_k['k'] + 2, optimal_k['mean_test_score'] - 0.02),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=12)
plt.show()

# Plot validation curve (K vs. score for different parameter combinations)
plt.figure(figsize=(14, 8))

# Get unique weights from param grid
weights_options = grid_search.param_grid['knn__weights']
p_options = grid_search.param_grid['knn__p']
colors = ['blue', 'red', 'green', 'purple']
markers = ['o', 's', '^', 'd']

# Plot for each combination of weights and p
for i, weights in enumerate(weights_options):
    for j, p in enumerate(p_options):
        mask = (results['param_knn__weights'] == weights) & (results['param_knn__p'] == p)
        filtered_results = results[mask].sort_values('param_knn__n_neighbors')

        if not filtered_results.empty:
            plt.plot(filtered_results['param_knn__n_neighbors'],
                     filtered_results['mean_test_score'],
                     marker=markers[i + j], linestyle='-',
                     label=f'weights={weights}, p={p}',
                     color=colors[i + j])

plt.title('Validation Curve: K vs. Accuracy for Different Parameters', fontsize=16)
plt.xlabel('K (Number of Neighbors)', fontsize=14)
plt.ylabel('Cross-Validation Accuracy', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.tight_layout()
plt.show()
