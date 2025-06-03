N,S = map(int,input().split())
*A, = map(int,input().split())

A.sort()

MOD = 998244353

dp = [[0]*(S+1) for _ in [0]*(N+1)]
dp[0][0] = 1
for i,a in enumerate(A):
    for s in range(S+1):
        dp[i+1][s] = dp[i][s]*2
        if s-a>=0:
            dp[i+1][s] += dp[i][s-a]
        dp[i+1][s] %= MOD
print(dp[-1][S])