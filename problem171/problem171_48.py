n = int(input())
a = sorted([(v, i) for i, v in enumerate(list(map(int, input().split())))])[::-1]

dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

ans = 0
for i in range(n):
    for j in range(n - i):
        v, p = a[i + j]
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + v * abs(n - 1 - i - p))
        dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + v * abs(j - p))
        ans = max(ans, dp[i + 1][j], dp[i][j + 1])
print(ans)
