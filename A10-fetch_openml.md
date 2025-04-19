# `fetch_openml` and Fashion-MNIST Dataset

## `fetch_openml` Function

`fetch_openml` is a function provided by scikit-learn that allows you to download datasets from the [OpenML](https://www.openml.org/) repository. OpenML is a public repository of machine learning datasets and experiments that makes it easy to share and access datasets.

### Syntax

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(name=None, version='active', data_id=None, 
                    data_home=None, target_column=None, 
                    cache=True, return_X_y=False, as_frame=True)
```

### Key Parameters

| Parameter | Description |
|-----------|-------------|
| `name` | String name of the dataset. If provided, `data_id` is ignored. |
| `version` | Version of the dataset. Can be 'active' (default), 'all', or a specific version number. |
| `data_id` | OpenML ID of the dataset. Used only if `name` is not provided. |
| `data_home` | Directory where data is stored. |
| `target_column` | Specify which column is the target. By default, the last column is used. |
| `cache` | Whether to cache downloaded datasets. |
| `return_X_y` | If True, returns `(X, y)` instead of a Bunch object. |
| `as_frame` | If True, returns data as pandas DataFrames. If False, returns as numpy arrays. |

### Return Value

By default, `fetch_openml` returns a Bunch object containing:

- `data`: Features matrix (X)
- `target`: Target values (y)
- `feature_names`: Names of the features
- `categories`: Dictionary containing categorical feature information
- `details`: Additional information about the dataset

If `return_X_y=True`, it returns a tuple `(X, y)` instead.

## Fashion-MNIST Dataset

Fashion-MNIST is a dataset of Zalando's article images, designed as a drop-in replacement for the original MNIST dataset. It consists of 28x28 grayscale images of 10 categories of clothing items.

### Dataset Details

- **Size**: 60,000 training examples, 10,000 testing examples
- **Dimensions**: Each image is 28x28 pixels (784 features when flattened)
- **Format**: Grayscale (values from 0 to 255)
- **Number of classes**: 10

### Classes

| Label | Description |
|-------|-------------|
| 0 | T-shirt/top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle boot |

### Using Fashion-MNIST with `fetch_openml`

```python
from sklearn.datasets import fetch_openml

# Load Fashion-MNIST
X, y = fetch_openml('fashion-mnist', version=1, return_X_y=True)

# Reshape data to look at images (if desired)
import numpy as np
X_images = np.array(X).reshape(-1, 28, 28)

# Split into training and testing sets
X_train, X_test = X[:60000], X[60000:]
y_train, y_test = y[:60000], y[60000:]

# Scale pixel values to range [0, 1]
X_train = X_train / 255.0
X_test = X_test / 255.0
```

### Common Preprocessing Steps

1. **Scaling**: Normalize pixel values to [0, 1] by dividing by 255
2. **Reshaping**: For CNN models, reshape from flat (784 features) to 2D (28x28 pixels)
3. **One-hot encoding**: Convert numerical labels to one-hot encoded vectors

### Why Use Fashion-MNIST?

- More challenging than MNIST digits (higher baseline error rate)
- More representative of modern computer vision tasks
- Same size and format as MNIST, making it a drop-in replacement
- Helps avoid tuning algorithms to a specific dataset (MNIST)

## Example: Load and Visualize Fashion-MNIST

```python
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import fetch_openml

# Load data
X, y = fetch_openml('fashion-mnist', version=1, return_X_y=True, as_frame=False)

# Define class names
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Reshape the first 25 images
X_reshaped = X[:25].reshape(25, 28, 28)

# Plot the first 25 images
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(X_reshaped[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[int(y[i])])
plt.tight_layout()
plt.show()
```

Output:

<img src="fashion.png" />
