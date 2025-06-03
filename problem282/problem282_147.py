n,t = map(int, input().split())

x = [list(map(int, input().split())) for i in range(n)]
x.sort()

# n-1品目までで、t-1分までで達成できる美味しさ計算
dp = [[0]*t for i in range(n)]
for i in range(1,n):
    a,b = x[i-1]
    for j in range(1,t):
        if j-a>=0:
            dp[i][j] = max(dp[i-1][j-a]+b, dp[i][j-1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# 最後に一番時間かかるの食べるときの美味しさを計算
ans = 0
for i in range(n):
    ans = max(ans, dp[n-1-i][t-1]+x[-i-1][1])
print(ans)