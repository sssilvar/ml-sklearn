from __future__ import print_function

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import datasets
import numpy as np

# Set ggplot as default style for visualisation
plt.style.use('ggplot')

# Load digits dataset
digits = datasets.load_digits()
X = digits.data
y = np.array(digits.target)

# Split the dataset 70-30
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)

# Vary the number of neighbors to check the performance
n_neighbors = np.linspace(1, 10, 10, dtype=int)
knn_score = np.empty(n_neighbors.shape)
for i, n in enumerate(n_neighbors):
    # Set up the k-NN classifier
    knn = KNeighborsClassifier(n_neighbors=n)

    # Fit model and calculate accuracy
    knn.fit(X_train, y_train)
    knn_score[i] = knn.score(X_test, y_test)

# Visualise the results
plt.figure()
plt.title('n-Neighbors performance curve')
plt.xlabel('Number of neighbors')
plt.ylabel('Accuracy')
plt.xlim([n_neighbors.min(), n_neighbors.max()])
plt.plot(n_neighbors, knn_score)
plt.show()
