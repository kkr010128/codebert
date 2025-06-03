from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque,Counter,defaultdict
from operator import mul
import copy
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
import heapq
sys.setrecursionlimit(10**6)
INF =  float("inf")
import bisect

N, K = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))

s = list(itertools.accumulate(a))

# print(s)
for i in range(0, N+1):
    s[i] = (s[i] - i) % K

# print(s)

d = defaultdict(int)

count = 0
for j in range(1,N+1):
    d[s[j-1]] += 1
    if j-K >= 0:
        d[s[j-K]] -= 1
    # print(j,s[j],d)
    count += d[s[j]]

# print(d)
print(count)


