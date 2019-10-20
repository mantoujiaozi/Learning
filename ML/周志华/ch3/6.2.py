# *_*coding:utf-8 *_*
import numpy as np
import pandas as pd
from sklearn import svm
from matplotlib import pyplot as plt

data = pd.read_csv('watermelon3_0_Ch.csv').values
X = data[:, 7:9].astype(float)
y = data[:, 9]
y[y == '是'] = 1
y[y == '否'] = 0
y = y.astype(int)

c = 1000
clf_rbf = svm.SVC(C=c)
clf_rbf.fit(X, y)
print('高斯核：')
print('预测值：', clf_rbf.predict(X))
print('真实值：', y.astype(int))
print('支持向量：', clf_rbf.support_)

clf_linear = svm.SVC(C=c, kernel='linear')
clf_linear.fit(X, y)
print('线性核：')
print('预测值：', clf_linear.predict(X))
print('真实值：', y.astype(int))
print('支持向量：', clf_linear.support_)


def plt_support_(clf, X_, y_, kernel, c):
    pos = y_ == 1
    neg = y_ == -1
    ax = plt.subplot()

    x_tmp = np.linspace(0, 1, 600)
    y_tmp = np.linspace(0, 0.8, 600)

    X_tmp, Y_tmp = np.meshgrid(x_tmp, y_tmp)

    Z_rbf = clf.predict(np.c_[X_tmp.ravel(), Y_tmp.ravel()]).reshape(X_tmp.shape)

    # ax.contourf(X_, Y_, Z_rbf, alpha=0.75)
    cs = ax.contour(X_tmp, Y_tmp, Z_rbf, [0], colors='orange', linewidths=1)
    ax.clabel(cs, fmt={cs.levels[0]: 'decision boundary'})

    set_ax_gray(ax)

    ax.scatter(X_[pos, 0], X_[pos, 1], label='1', color='c')
    ax.scatter(X_[neg, 0], X_[neg, 1], label='0', color='lightcoral')

    ax.scatter(X_[clf.support_, 0], X_[clf.support_, 1], marker='o', c='', edgecolors='g', s=150,
               label='support_vectors')

    ax.legend()
    ax.set_title('{} kernel, C={}'.format(kernel, c))
    plt.show()


def set_ax_gray(ax):
    ax.patch.set_facecolor("gray")
    ax.patch.set_alpha(0.1)
    ax.spines['right'].set_color('none')  # 设置隐藏坐标轴
    ax.spines['top'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.grid(axis='y', linestyle='-.')


plt_support_(clf_rbf, X, y, 'rbf', c)


plt_support_(clf_linear, X, y, 'linear', c)
