#!/usr/bin/env python3
import sys
import numpy as np
import numba
from numba import i8

input = sys.stdin.buffer.readline
mod = 998244353


def I():
    return int(input())


def MI():
    return map(int, input().split())


@numba.njit((i8, i8[:]), cache=True)
def main(N, LR):
    L, R = LR[::2], LR[1::2]
    K = len(L)

    dp = np.zeros(N + 1, np.int64)
    dpsum = np.zeros(N + 1, np.int64)
    dp[1] = 1
    dpsum[1] = 1

    for i in range(2, N + 1):
        for k in range(K):
            li = i - R[k]
            ri = i - L[k]
            if ri < 0:
                continue
            li = max(li, 1)
            dp[i] += dpsum[ri] - dpsum[li - 1]
            dp[i] %= mod
        dpsum[i] = dpsum[i - 1] + dp[i]
        dpsum[i] %= mod

    return dp[N]


N, K = MI()
LR = np.array(sys.stdin.buffer.read().split(), np.int64)

print(main(N, LR))
