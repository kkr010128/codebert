#!/usr/bin/env python3

import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
from heapq import heappush, heappop,heappushpop
from collections import defaultdict
from itertools import accumulate
from collections import Counter
from collections import deque
from operator import itemgetter
from itertools import permutations
mod = 10**9 + 7
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n, t = LI()
ab = [LI() for _ in range(n)]
ab.sort(key = itemgetter(0))

dp = [[0] * (t+3001) for _ in range(n+1)]
for i in range(1, n+1):
    a, b = ab[i-1]
    for j in range(t + 3001):
        dp[i][j] = dp[i-1][j]
    for j in range(t):
        dp[i][j+a] = max(dp[i-1][j+a], dp[i-1][j] + b)

ans = 0
for i in range(t-1, t + 3001):
    ans = max(ans, dp[n][i])
print(ans)