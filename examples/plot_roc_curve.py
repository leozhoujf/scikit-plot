from __future__ import absolute_import
import matplotlib.pyplot as plt
from scikitplot.scikitplot import classifier_factory
from sklearn.naive_bayes import GaussianNB
from sklearn.datasets import load_digits as load_data


X, y = load_data(return_X_y=True)
nb = classifier_factory(GaussianNB())
nb.plot_roc_curve(X, y, random_state=1)
plt.show()
