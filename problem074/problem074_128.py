import sys

n, k = map(int, input().split())
mod = 998244353

dp = [0] * (n+1)
dp[1] = 1
r = [tuple(map(int, input().split())) for _ in range(k)]
s = [0 for _ in range(k)]

for i in range(2, n + 1):
    sums = 0
    for j in range(k):
        s[j] += dp[max(0, i - r[j][0])] - dp[max(0, i - r[j][1] - 1)]
        s[j] %= mod
        sums = (sums + s[j]) % mod
    dp[i] = sums

print(dp[n])
