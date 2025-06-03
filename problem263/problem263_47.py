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

def bit(S, j):
    # Sの右からj bit目(0-indexed)
    return (S>>j)&1

N = int(input())
A = list(map(int, input().split()))

B = [0 for i in range(61)]
for i in range(61):
    for j in range(N):
        B[i] += bit(A[j], i)

for i in range(61):
    B[i] = B[i]*(N-B[i]) % mod

ans = 0
for i in range(61):
    ans = (ans + 2**i*B[i]) % mod

print(ans % mod)