import sys
import math
import string
import fractions
import random
from operator import itemgetter
import itertools
from collections import deque
import copy
import heapq
import bisect

MOD = 10 ** 9 + 7
INF = float('inf')
input = lambda: sys.stdin.readline().strip()

sys.setrecursionlimit(10 ** 8)

n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [[INF] * (n + 10) for _ in range(m + 10)]
for i in range(m+10):
    dp[i][0] = 0
for i in range(1, n + 1):
    if i % c[0] == 0:
        dp[1][i] = i // c[0]
for i in range(2, m + 1):
    for j in range(1, n + 1):
        if j - c[i - 1] >= 0:
            dp[i][j] = min(dp[i-1][j], dp[i][j - c[i - 1]] + 1)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[m][n])
