# *_*coding:utf-8 *_*
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model


data = pd.read_csv('watermelon3_0_Ch.csv').values
X = data[:, 7:9].astype(float)
y = data[:, 9]

y[y == '是'] = 1
y[y == '否'] = 0
y = y.astype(int)

plt.scatter(data[:, 7][y == 1], data[:, 8][y == 1], c='k', marker='o')
plt.scatter(data[:, 7][y == 0], data[:, 8][y == 0], c='r', marker='x')

plt.xlabel(u'密度')
plt.ylabel(u'含糖量')


def likelihood(X, y, beta):
    cur_l = 0
    m, n = np.shape(X)
    for i in range(m):
        b_new = np.dot(beta.T, X[i])
        cur_l = cur_l + ((-y[i] * b_new) + np.log(1 + np.exp(b_new)))

    return cur_l


def gradDscent_1(X, y):
    alpha = 0.1  #步长
    max_times = 500  #迭代次数
    m, n =np.shape(X)

    delta_beta = np.ones((n,1)) * alpha
    llh = 0
    beta = np.zeros((n, 1))

    for i in range(max_times):
        beta_temp = beta.copy()

        for j in range(n):
            beta[j] += delta_beta[j]
            llh_temp = likelihood(X, y, beta)
            delta_beta[j] = -alpha * (llh_temp - llh) / delta_beta[j]
            beta[j] = beta_temp[j]

        beta += delta_beta
        llh = likelihood(X, y, beta)

    return beta


beta = gradDscent_1(X, y)
y_pre = X[:, 0] * beta[0] + X[:, 1] * beta[1]
# plt.contourf(X, y_pre, color="blue")
plt.show()
