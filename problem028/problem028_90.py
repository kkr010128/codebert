n,m = map(int,input().split())
c = [int(i) for i in input().split()]
dp = [[float("INF")]*(n+1) for _ in range(m+1)]

dp[0][0] = 0
for i in range(m):
    for yen in range(n+1):
        if yen - c[i] < 0: dp[i+1][yen] = dp[i][yen]
        else: dp[i+1][yen] = min(dp[i][yen],dp[i+1][yen-c[i]]+1)
print(dp[m][n])
