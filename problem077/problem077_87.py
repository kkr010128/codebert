
import numpy as np
from functools import *
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def array(size, init=0):
    return [[init for j in range(size[1])] for i in range(size[0])]


def acinput():
    return list(map(int, input().split(" ")))


def II():
    return int(input())


def nitti(x, y):
    count = 0
    for i in range(len(x)):
        if x[i] == y[i]:
            count += 1
    return count


x = acinput()


res = 10**20*(-1)

for i in range(2):
    for j in range(2, 4):
        res = max(res, x[i]*x[j])

print(res)
