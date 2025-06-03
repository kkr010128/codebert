#!/usr/bin/env python3
import sys
import itertools
sys.setrecursionlimit(10**8)
INF = float("inf")
MOD = 10**9+7

N = int(input())
A = list(map(int, input().split()))


AA = [(a, i) for i, a in enumerate(A, start=1)]
AA.sort(reverse=True)
# print(AA)

DP = [[0]*(N+1) for _ in range(N+1)]

for wa in range(1, N+1):
    # AA[:wa]までを考える
    for x in range(wa+1):
        y = wa - x
        a, i = AA[wa-1]
        if x - 1 >= 0:
            DP[x][y] = max(DP[x][y], DP[x-1][y]+a*(i-x))
        if y - 1 >= 0:
            DP[x][y] = max(DP[x][y], DP[x][y-1]+a*(N-y-i+1))
        # print(wa, (x, y), (a, i), DP[x][y])

M = -INF
for x in range(N):
    y = N-x
    M = max(DP[x][y], M)
print(M)

