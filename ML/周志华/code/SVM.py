# *_*coding:utf-8 *_*
import random


def loadDataSet(filename):
    dataMat = []
    labelMat = []
    fr = open(filename)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append(float(lineArr[2]))

    return dataMat, labelMat


def selectTrand(i, m):

    j = i
    while (j == i) :
        j = int(random.uniform(0, m))
    return j


def clipAlpha(aj, high, low):

    if aj > high:
        aj = high
    if low > aj:
        aj = low

    return aj


