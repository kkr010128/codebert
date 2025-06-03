N, M = map(int, input().split())
coins = list(map(int, input().split()))

dp = [[N for _ in range(N+1)] for _ in range(M+1)]
dp[0][0] = 0

for i in range(M):
    c = coins[i]
    for j in range(N+1):
        if j-c >= 0:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j-c]+1)
        else:
            dp[i+1][j] = dp[i][j]

print(dp[M][N])

