n, m = map(int, input().split())
c = [int(i) for i in input().split()]
dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][1] = i
for j in range(1, m + 1):
    dp[0][j] = 0
    # dp[1][j] = 1
for i in range(n + 1):
    for j in range(1, m):
        if c[j] > i:
            dp[i][j + 1] = dp[i][j]
        else:
            dp[i][j + 1] = min(dp[i][j], dp[i - c[j]][j + 1] + 1)
print(dp[n][m])

