p = 998244353

n, k = map(int, input().split())
num = [tuple(map(int, input().split())) for _ in range(k)]

dp = [0] * (2*n + 1)

dp[0] = 1
dp[1] = -1

for i in range(n):
    for l, r in num:
        dp[i+l] += dp[i]
        dp[i+r+1] -= dp[i]
    dp[i+1] += dp[i]
    dp[i+1] %= p

print(dp[n-1])