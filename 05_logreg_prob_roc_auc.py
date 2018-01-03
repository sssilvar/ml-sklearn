from __future__ import print_function

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, roc_auc_score, classification_report, confusion_matrix
plt.style.use('ggplot')

digits = datasets.load_digits()
data_idx = np.array(np.where(np.logical_or(digits.target == 1, digits.target == 0)))

X = digits.data[data_idx.ravel(), :]
y = digits.target[data_idx].ravel()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=42)

# Fit model
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

y_pred = logreg.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))


# Predict a continuous model
y_pred_prob = logreg.predict_proba(X_test)[:,1]
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# Plot ROC
plt.figure()
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr, label='Logistic Regression')
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('Logistic regression ROC curve')
plt.margins(0.02)
plt.show()
