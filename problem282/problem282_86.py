n, t = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x:x[0])
dp = [[0]*(t+1) for _ in range(n+1)]
for i in range(n):
    for j in range(t+1):
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        res = j+ab[i][0]
        if res<=t: dp[i+1][res] = max(dp[i][res], dp[i][j]+ab[i][1])
    dp[i+1][t] = max(dp[i+1][t], dp[i][t], dp[i][t-1]+ab[i][1])
print(dp[n][t])