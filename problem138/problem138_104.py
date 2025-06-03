N, S = map(int, input().split())
As = list(map(int, input().split()))
mod = 998244353
dp = [[0]*(S+1) for i in range(N+1)]
dp[0][0] = 1
for i in range(1, N+1):
    a = As[i-1]
    for s in range(S+1):
        if s-a>=0:
            dp[i][s] += dp[i-1][s-a] + dp[i-1][s]*2
        else:
            dp[i][s] += dp[i-1][s]*2
        dp[i][s] %= mod
print(dp[-1][-1]%mod)