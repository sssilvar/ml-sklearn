from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV
from sklearn.metrics import classification_report, roc_curve, roc_auc_score

# Set plot style to ggplot
plt.style.use('ggplot')

# Load data
print('[INFO] Loading dataset...')
breast = datasets.load_breast_cancer()
X = breast.data
y = breast.target

# Split data into training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Start Classifying: SVM-RBF
svm = SVC(kernel='rbf', probability=True)

# Set up the parameters to evaluate
param_grid = {
    'C': np.logspace(-3, 2, 20),
    'gamma': np.logspace(-3, 2, 20)
}

clf_grid = GridSearchCV(svm, param_grid)
clf_grid.fit(X_train, y_train)

y_pred_proba = clf_grid.predict_proba(X_test)[:,1]

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)
auc = roc_auc_score(y_test, y_pred_proba)

plt.figure()
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(fpr, tpr)
plt.legend(['AUC = ' + str(auc)])
plt.xlabel('False positive rate')
plt.ylabel('True positive rate')
plt.title('Breast cancer classification ROC curve')

plt.show()
