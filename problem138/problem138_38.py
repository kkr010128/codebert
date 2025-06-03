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
mod = 998244353
inf = float('inf')
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))

n, s = LI()
a = LI()

dp = [[0]*(s+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(1, n+1):
    x = a[i-1]
    for j in range(s+1):
        if j == 0:
            dp[i][j] += dp[i-1][j] + 1
            dp[i][j] %= mod
        elif dp[i-1][j]:
            dp[i][j] += dp[i-1][j] * 2
            dp[i][j] %= mod
        if j - x < 0:
            continue
        if j - x == 0:
            dp[i][j] += pow(2, dp[i-1][j-x], mod)
            dp[i][j] %= mod
        elif dp[i-1][j-x]:
            dp[i][j] += dp[i-1][j-x]
            dp[i][j] %= mod
print(dp[-1][-1])
