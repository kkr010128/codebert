n, t = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[0] * t for _ in range(n)]
ans = 0
a.sort()
for i in range(n-1):
    for j in range(t):
        if j - a[i][0] < 0:
            dp[i + 1][j] = dp[i][j]
        else:
            dp[i + 1][j] = max(dp[i][j], dp[i][j - a[i][0]] + a[i][1])
    ans = max(ans, dp[i + 1][-1] + a[i+1][1])
print(ans)