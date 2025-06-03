# coding: utf-8

import itertools
from functools import reduce
from collections import deque

N, K = list(map(int, input().split(" ")))
A = list(map(int, input().split(" ")))

for i in range(N):
    if i > K-1:
        if A[i] > A[i-K]:
            print("Yes")
        else:
            print("No")
