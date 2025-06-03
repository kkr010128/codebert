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
# INF =  float("inf")
INF = 10**18
import bisect
import statistics
mod = 10**9+7
# mod = 998244353

N = int(input())
L = list(map(int, input().split()))

L.sort()

ans = 0
for i in range(N):
    for j in range(i+1,N):
        p = L[i]+L[j]
        k = bisect.bisect_left(L[j+1:], p)
        ans += k

print(ans)


