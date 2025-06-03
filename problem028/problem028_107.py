n, m = map(int, input().split())
c = sorted([int(i) for i in input().split()])
dp = [[0 for j in range(n+1)] for i in range(m+1)]
dp[1] = [int(i) for i in range(n+1)]
for i in range(2, m+1):
    for j in range(n+1):
        if j - c[i-1] > -1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-c[i-1]]+1)
        else:
            dp[i][j] = dp[i-1][j]
print(dp[m][n])
