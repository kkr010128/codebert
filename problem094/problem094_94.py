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

dp1 = [[0]*4 for _ in range(C+1)]
dp2 = [[0]*4 for _ in range(C+1)]

field = [[0]*(C+1)] + [[0]*(C+1) for _ in range(R)]

for _ in range(K):
    r, c, v = MAP()
    field[r][c] = v

for i in range(1, R+1):
    for j in range(1, C+1):
        if i%2 == 0:       
            up_max = max(dp1[j])
            p = field[i][j]
            dp2[j][0] = max(up_max, dp1[j-1][0])
            dp2[j][1] = max(up_max+p, dp2[j-1][1], dp2[j-1][0]+p)
            dp2[j][2] = max(dp2[j-1][2], dp2[j-1][1]+p)
            dp2[j][3] = max(dp2[j-1][3], dp2[j-1][2]+p)
        else:
            up_max = max(dp2[j])
            p = field[i][j]
            dp1[j][0] = max(up_max, dp2[j-1][0])
            dp1[j][1] = max(up_max+p, dp1[j-1][1], dp1[j-1][0]+p)
            dp1[j][2] = max(dp1[j-1][2], dp1[j-1][1]+p)
            dp1[j][3] = max(dp1[j-1][3], dp1[j-1][2]+p)

a = max(dp1[-1])
b = max(dp2[-1])
print(max(a, b))
