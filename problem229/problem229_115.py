h, n = map(int, input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())

dp = [[1e18] * (h + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(h + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        dp[i + 1][min(j + a[i], h)] = min(dp[i + 1][min(j + a[i], h)], dp[i + 1][j] + b[i])

print(dp[n][h])