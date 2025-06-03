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
import statistics
# mod = 10**9+7
mod = 998244353

N ,S = list(map(int, input().split()))
A = [0] + list(map(int, input().split()))

dp = [[0 for j in range(S+1)] for i in range(N+1)]
dp[0][0] = 1

for i in range(1,N+1):
    for y in range(S+1):
        dp[i][y] = (dp[i][y] + dp[i-1][y] * 2) % mod
        if y - A[i] >= 0:
            dp[i][y] = (dp[i][y] + dp[i-1][y-A[i]]) % mod

print(dp[N][S] % mod)
