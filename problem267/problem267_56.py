# -*- coding: utf-8 -*-
import numpy as np
import sys
from collections import deque
from collections import defaultdict
import heapq
import collections
import itertools
import bisect
from scipy.special import comb
import copy
sys.setrecursionlimit(10**6)


def zz():
    return list(map(int, sys.stdin.readline().split()))


def z():
    return int(sys.stdin.readline())


def S():
    return sys.stdin.readline()[:-1]


def C(line):
    return [sys.stdin.readline() for _ in range(line)]


N = z()
S = S()
after_lis = [set() for _ in range(N+1)]
i = N-1
for s in reversed(S):
    after_lis[i] = (after_lis[i] | after_lis[i+1])
    after_lis[i].add(int(s))
    i -= 1

left_index = {}
for i, s in enumerate(S):
    if s not in left_index:
        left_index[s] = i

ans_lis = np.zeros([10, 10, 10], dtype=np.int32)

for char in left_index:
    s_100 = int(char)
    for i_10 in range(left_index[char]+1, N-1):
        # print("s_10")
        s_10 = int(S[i_10])
        ans_lis[s_100, s_10, list(after_lis[i_10+1])] = 1

        # sは暗証番号の一番左
# print(ans_lis)
print(np.sum(ans_lis))
