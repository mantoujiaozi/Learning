# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 16:14
# @Author  : 馒头饺子
# @FileName: batch-gradient-descent.py
# @Software: PyCharm

import pandas as pd
import numpy as np

train = pd.read_csv('data/descent_train.csv')

# 初始设置初始点beta = [1, 1],学习率alpha = 0.2,损失函数的变动的阈值tolL
beta = [1, 1]
alpha = 0.2
tol_L = 0.1

# 对x进行归一化
max_x = max(train['id'])
x = train['id'] / max_x
y = train['questions']


# 定义计算梯度的函数
def compute_grad(beta, x, y):
    grad = [0, 0]
    grad[0] = 2 * np.mean(beta[0] + beta[1] * x - y)
    grad[1] = 2 * np.mean(x * (beta[0] + beta[1] * x - y))
    return np.array(grad)


# 定义更新beta的函数
def update_beta(beta, alpha, grad):
    new_beta = np.array(beta) - alpha * grad
    return new_beta


# 定义计算损失函数
def rmse(beta, x, y):
    squared_err = (beta[0] + beta[1] * x - y) ** 2
    res = np.sqrt(np.mean(squared_err))
    return res


# 进行第一次计算
grad = compute_grad(beta, x, y)
loss = rmse(beta, alpha, grad)
beta = update_beta(beta, alpha, grad)
loss_new = rmse(beta, x, y)

i = 1
while np.abs(loss_new - loss) > tol_L:
    beta = update_beta(beta, alpha, grad)
    grad = compute_grad(beta, x, y)
    loss = loss_new
    beta = update_beta(beta, alpha, grad)
    loss_new = rmse(beta, x, y)
    i += 1
    print('第 %s 循环，损失函数的变化为 %s' % (i, abs(loss_new - loss)))
print('系数2: %s \n系数1 %s' % (beta[1] / max_x, beta[0]))
res = rmse(beta, x, y)
print('误差: %s' % res)

#调用sklearn.linear_model.LinearRegression
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(train[['id']], train[['questions']])
print('Sklearn 系数2: %s' % lr.coef_[0][0])
print('Sklearn 系数1: %s' % lr.intercept_[0])
res = rmse([lr.intercept_[0], lr.coef_[0][0]], train['id'], y)
print('Sklearn 误差: %s' % res)