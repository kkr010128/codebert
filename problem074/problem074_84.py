n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _i in range(k)]
mod = 998244353

dp = [0]*(n+1)
dp[1] = 1

for p in range(2, n+1):
    for i, j in lr:
        dp[p] += dp[max(p-i, 0)] - dp[max(p-j-1, 0)]
        dp[p] %= mod
    dp[p] += dp[p-1]

print((dp[n]-dp[n-1])%mod)