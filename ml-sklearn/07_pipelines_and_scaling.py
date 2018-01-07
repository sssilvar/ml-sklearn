from __future__ import print_function

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import Lasso
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report

# Set plt style
plt.style.use('ggplot')

# Load data: winequality-white.csv
df = pd.read_csv('winequality-white.csv', sep=';')
print(df.head(2))

# Determine X and y (target: quality greater than 5)
X = df.drop('quality', axis=1).values
y = df['quality'].values > 5

feature_names = df.drop('quality', axis=1).keys().values

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Select relevant features: coef
lasso = Lasso(alpha=0.4)
lasso.fit(X_train, y_train)
coef = lasso.coef_

# Plot results
plt.figure()
plt.plot(range(X.shape[1]), coef)
plt.xticks(range(X.shape[1]), feature_names, rotation=20)
plt.margins(0.02)

# Use the most significant features from lasso:
# 'total sulfur dioxide', 'free sulfur dioxide'
print('[INFO]: Starting Pipeline...')
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_jobs=-1, weights='distance'))
])

param_grid = {
    'knn__n_neighbors': range(5, 51)
}

pipeline = GridSearchCV(pipeline, param_grid)

# Select optimal features
print('[INFO]: splitting data...')
X = df.loc[:, ['total sulfur dioxide', 'free sulfur dioxide']].values
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

print('[INFO]: Fitting model...')
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print('Classification report: \n {}'.format(classification_report(y_test, y_pred)))
print('Score: {}'.format(pipeline.score(X_test, y_test)))
print('Best Params: {}'.format(pipeline.best_params_))

plt.show()
