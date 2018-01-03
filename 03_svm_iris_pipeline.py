from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split, KFold, GridSearchCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler


iris = datasets.load_iris()
X = iris.data
y = iris.target

# Split training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=21, stratify=y)

# Set up classifier
poly_svm_clf = Pipeline((
    ("poly_features", PolynomialFeatures(degree=3)),
    ("scaler", StandardScaler()),
    ("svm_clf", LinearSVC(C=10, loss='hinge'))
))

deg_values = np.array(np.linspace(1, 4, 50), dtype=int)
c_values = np.linspace(0.01, 10, 50)

param_grid = [{
    'poly_features__degree': deg_values,
    'svm_clf__C': c_values
}]

grid_search = GridSearchCV(poly_svm_clf, param_grid, cv=3)
grid_search.fit(X_train, y_train)

print('Best parrams are: ', grid_search.best_params_)
print(grid_search.score(X_test, y_test))

# Create a score matrix
# scores = [x[1] for x in grid_search.grid_scores_]
scores = np.empty([deg_values.size, c_values.size])
for i, deg_value in enumerate(deg_values):
    for j, c_value in enumerate(c_values):

        # Set up classifier
        poly_svm_clf = Pipeline((
            ("poly_features", PolynomialFeatures(degree=deg_value)),
            ("scaler", StandardScaler()),
            ("svm_clf", LinearSVC(C=c_value, loss='hinge'))
        ))

        # Fit model and create score for degree an C
        poly_svm_clf.fit(X_train, y_train)
        scores[i,j] = poly_svm_clf.score(X_test, y_test)

plt.matshow(scores)
plt.xlabel('Degree')
plt.ylabel('C')
plt.colorbar()
plt.xticks([10, 20, 30, 40], [1, 2, 3, 4])
plt.yticks(np.arange(6)*10, np.linspace(deg_values.min(), deg_values.max(), 6))
plt.show()
