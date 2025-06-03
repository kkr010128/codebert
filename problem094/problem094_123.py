import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby, combinations_with_replacement
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce
from decimal import Decimal, ROUND_CEILING
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

R, C, K = MAP()

dp = [[0]*4 for _ in range(C+1)]
field = [[0]*(C+1)] + [[0]*(C+1) for _ in range(R)]

for _ in range(K):
    r, c, v = MAP()
    field[r][c] = v

for i in range(1, R+1):
    dp_next = [[0]*4 for _ in range(C+1)]
    for j in range(1, C+1):
        up_max = max(dp[j])
        p = field[i][j]
        dp_next[j][0] = max(up_max, dp[j-1][0])
        dp_next[j][1] = max(up_max+p, dp_next[j-1][1], dp_next[j-1][0]+p)
        dp_next[j][2] = max(dp_next[j-1][2], dp_next[j-1][1]+p)
        dp_next[j][3] = max(dp_next[j-1][3], dp_next[j-1][2]+p)
    dp = dp_next

print(max(dp[-1]))
