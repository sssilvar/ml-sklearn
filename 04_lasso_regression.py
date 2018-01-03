from __future__ import print_function

import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn import datasets

plt.style.use('ggplot')

boston = datasets.load_boston()
X = boston.data
y = boston.target
feature_names = boston.feature_names


# lasso = Lasso(alpha=0.4, normalize=True)
lasso = Lasso(alpha=0.4)
lasso.fit(X, y)

lasso_coef = lasso.coef_
print(lasso_coef)

# Plot features
plt.figure()
plt.plot(range(X.shape[1]), lasso_coef)
plt.xticks(range(X.shape[1]), feature_names, rotation=60)
plt.margins(0.02)
plt.show()
