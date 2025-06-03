from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
INF = float("inf")


# 処理内容
def main():
    H, N = map(int, input().split())
    A = [0]*N
    B = [0]*N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    
    dp = [INF] * 10000100
    dp[0] = 0
    for i in range(H):
        if dp[i] == INF:
            continue
        for n in range(N):
            dp[i+A[n]] = min(dp[i+A[n]], dp[i] + B[n])
    
    ans = INF
    for i in range(H, 10000100):
        ans = min(ans, dp[i])
    print(ans)


if __name__ == '__main__':
    main()