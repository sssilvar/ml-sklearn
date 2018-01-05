from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

# Set matplotlib style to ggplot
plt.style.use('ggplot')

# Load dataset (Digits)
digits = datasets.load_digits()

X = digits.data
y = digits.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.7, random_state=21, stratify=y)

# Set cost array
svm_c = np.linspace(0.01, 100, 20)

svm_train_score = np.empty(svm_c.shape)
svm_test_score = np.empty(svm_c.shape)
for i, c in enumerate(svm_c):
    "Vary cost parameter for SVC model"
    # Set up SVM and fit model
    svm = SVC(C=c, kernel='poly')
    svm.fit(X_train, y_train)

    # Scores for train and test sets
    svm_train_score[i] = svm.score(X_train, y_train)
    svm_test_score[i] = svm.score(X_test, y_test)

# Create and set figure up
plt.figure()
plt.title('Cost-Performance cost')
plt.xlabel('Cost value')
plt.ylabel('Accuracy')
plt.xlim([svm_c.min(), svm_c.max()])
plt.ylim([0, 1.1])
plt.xscale('log')

plt.plot(svm_c, svm_train_score)
plt.plot(svm_c, svm_test_score)
plt.legend(['Training set', 'Testing Set'])
plt.show()
