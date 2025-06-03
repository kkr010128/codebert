from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)


N = int(input())

a = [[0]*10 for i in range(10)]

for i in range(1,N+1):
    n = str(i)
    a[int(n[0])][int(n[-1])] += 1

ans = 0
for i in range(1,10):
    for j in range(1, 10):
        ans += a[i][j]*a[j][i]

print(ans)



