# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect

sys.setrecursionlimit(10**6)
def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()


def C(line):
    return [sys.stdin.readline() for _ in range(line)]

N = z()
A = [0]*N
X = {}
Y = {}
for i in range(N):
    A[i] = z()
    X[i] = [0]*A[i]
    Y[i] = [0]*A[i]
    for j in range(A[i]):
        x, y = zz()
        X[i][j] = x-1
        Y[i][j] = y
ans = 0
for bits in itertools.product([0, 1], repeat=N):
    # print("================")
    # print(bits)
    false_flg = False
    for i, b in enumerate(bits):
        if (b == 1):
            # print('i=', i)
            for x, y in zip(X[i], Y[i]):
                # print(x, y)
                if (bits[x] != y):
                    # print(False)
                    false_flg = True
                if false_flg:
                    break
            if false_flg:
                break
    if false_flg:
        continue
    else:
        ans = max(ans, sum(bits))
print(ans)