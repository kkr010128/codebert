N, K = map(int, input().split())
X = list(map(int, input().split()))
MOD = 998244353

dp = [[0]*(K+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(N):
    x = X[i]
    for j in range(K+1):
        dp[i+1][j] = 2*dp[i][j]
        if j-x>=0:
            dp[i+1][j] += dp[i][j-x]
        dp[i+1][j] %= MOD
print(dp[-1][-1])
