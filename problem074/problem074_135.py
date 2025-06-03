import numpy as np
# import math
# import copy
# from collections import deque
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10000)
from numba import njit,i8


@njit(i8(i8,i8,i8,i8[:,:],i8[:],i8,i8))
def give_dp(N,K,mod,LR,dp,l,r):
    for i in range(N):
        if i > 0:
            dp[i] += dp[i-1]
            dp[i] %= mod
        for k in range(K):
            l = LR[k][0]
            r = LR[k][1]
            if i + l < N:
                dp[i+l] += dp[i]
                dp[i+1] %= mod
            if i + r < N:
                dp[i+r+1] -= dp[i]
                dp[i+1] %= mod
    return dp[-1]


def main():
    N,K = map(int,input().split())
    LR = [list(map(int,input().split())) for i in range(K)]
    LR = np.array(LR)

    mod = 998244353

    dp = [0 for i in range(N)]
    dp[0] = 1
    dp[1] = -1
    dp = np.array(dp)

    res = give_dp(N,K,mod,LR,dp,0,0)
    res %= mod

    print(res)



main()
