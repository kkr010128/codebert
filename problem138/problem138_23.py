#!/usr/bin/env python3
import sys
input = sys.stdin.readline
MOD = 998244353

n, s = map(int, input().split())
a = [int(item) for item in input().split()]

dp = [[0] * (s + 1) for _ in range(n+1)]
dp[0][0] = 1

for i, item in enumerate(a):
    for j in range(s, -1, -1):
        if dp[i][j] == 0:
            continue
        if j + item <= s:
            dp[i+1][j+item] += dp[i][j] 
        dp[i+1][j] += dp[i][j] * 2
        dp[i+1][j] %= MOD

print(dp[-1][-1] % MOD)