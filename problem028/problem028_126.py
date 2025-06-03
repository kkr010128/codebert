n, m = map(int, input().split())
c = [int(i) for i in input().split()]
inf = 10**10

dp = [[inf] * (n+1) for i in range(m+1)]
dp[0][0] = 0

for i in range(m):
  for j in range(n+1):
        if j>=c[i]:
            dp[i+1][j] = min(dp[i][j], dp[i][j-c[i]]+1, dp[i+1][j-c[i]]+1)
        else:
            dp[i+1][j] = dp[i][j]

print(dp[m][n])
