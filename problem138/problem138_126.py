import sys
input = sys.stdin.readline

M, MOD = 3005, 998244353

dp = [[0 for i in range(M)] for j in range(M)]
n, s = map(int, input().split())
a = list(map(int, input().split()))
dp[0][0] = 1
for i in range(n):
    for j in range(s + 1):
        dp[i + 1][j] += dp[i][j] * 2
        dp[i + 1][j] %= MOD
        if s >= j + a[i]:
            dp[i + 1][j + a[i]] += dp[i][j]
            dp[i + 1][j + a[i]] %= MOD
print(dp[n][s])