import sys
import itertools
# import numpy as np
import time
import math
from heapq import heappop, heappush
from collections import defaultdict
from collections import Counter
from collections import deque
from itertools import permutations
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
MOD = 998244353
N, K = map(int, input().split())
S = [0] * K
for i in range(K):
    l, r = map(int, input().split())
    S[i] = (l, r)

dp = [0] * (N + 2)
acc = [0] * (N + 2)
dp[1] = 1
acc[1] = 1
for i in range(1, N + 1):
    for j in range(K):
        li = i - S[j][1]
        ri = i - S[j][0]
        if ri < 0:
            continue
        li = max(li, 0)
        dp[i] += (acc[ri] - acc[li - 1]) % MOD
    acc[i] = (acc[i - 1] + dp[i]) % MOD
print(dp[N] % MOD)
