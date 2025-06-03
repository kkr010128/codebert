import sys

input = sys.stdin.buffer.readline

n, s = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353
dp = [[0] * (s + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(n):
    ni = i + 1
    for j in range(s + 1):
        nj = j
        dp[ni][nj] += 2 * dp[i][j]
        dp[ni][nj] %= mod
        nj = j + A[i]
        if nj <= s:
            dp[ni][nj] += dp[i][j]
            dp[ni][nj] %= mod
print(dp[n][s] % mod)
