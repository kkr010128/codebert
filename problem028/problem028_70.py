n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [[10**8]*(n+1) for i in range(m+1)]
dp[0][0] = 0
for i in range(m):
    for j in range(n+1):
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        if j + c[i] <= n:
            dp[i+1][j+c[i]] = min(dp[i+1][j]+1, dp[i+1][j+c[i]])

print(dp[m][n])

