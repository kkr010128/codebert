import sys
input = sys.stdin.readline
INF = 10**18
sys.setrecursionlimit(10**6)
import itertools as it
import collections as cl
from collections import deque
import math
from functools import reduce
from collections import defaultdict
MOD = 998244353


def li():
    return [int(x) for x in input().split()]

N, K = li()

L, R = [], []
for _ in range(K):
    l, r = li()
    L.append(l)
    R.append(r)

# dp[i]: i番目のマスにいく場合の数
dp = [0] * (N+1)
dp[1] = 1
# 区間 [left, right)の和はdpsum[right] - dpsum[left]
# 区間 [left, right]の和はdpsum[right+1] - dpsum[left]
# マス a~bは区間だと[a-1,b-1]に対応。よってマスliからriの和はdpsum[right] - dpsum[left - 1]
dpsum = [0] * (N+1)
dpsum[1] = 1
for i in range(2, N+1):
    for j in range(K):
        li = max(i - R[j], 1)
        ri = i - L[j]
        if ri >= 0:
            dp[i] += dpsum[ri] - dpsum[li-1]
            dp[i] %= MOD
    dpsum[i] = dpsum[i-1] + dp[i]
    dpsum[i] %= MOD

print(dp[N])
