from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")
MOD = 998244353

# 処理内容
def main():
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    dp = [[0]*(S+1) for _ in range(N+1)]
    dp[0][0] = 1
    for i in range(N):
        for j in range(S+1):
            dp[i+1][j] += dp[i][j] * 2
            dp[i+1][j] %= MOD
            if j + A[i] > S:
                continue
            dp[i+1][j+A[i]] += dp[i][j]
            dp[i+1][j+A[i]] %= MOD
    
    print(dp[N][S])


if __name__ == '__main__':
    main()