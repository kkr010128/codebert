N, S = map(int, input().split())
A = list(map(int, input().split()))
MOD = 998244353
dp = [[0]*(S+1) for _ in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for s in range(S+1):
        if s-A[i-1] >= 0:
            dp[i][s] = (dp[i-1][s] * 2 + dp[i-1][s-A[i-1]]) % MOD
        else:
            dp[i][s] = dp[i-1][s] * 2 % MOD
print(dp[N][S])

