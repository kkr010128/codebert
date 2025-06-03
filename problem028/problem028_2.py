n, m = map(int, input().split())
coins = list(map(int, input().split()))
coins = sorted(coins, reverse=False)
dp = [[float('inf')] * (n + 1) for _ in range(m)]

for j in range(n+1):
    dp[0][j] = j

for i in range(m-1):
    for j in range(n+1):
        if j - coins[i+1] >= 0:
            dp[i+1][j] = min(dp[i][j],
                             dp[i][j - coins[i+1]] + 1,
                             dp[i+1][j - coins[i+1]] + 1)
        else:
            dp[i+1][j] = dp[i][j]

print(dp[m-1][n])

