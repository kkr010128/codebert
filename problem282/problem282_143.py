N, T = map(int, input().split())
A = [0]*N
B = [0]*N
AB = [list(map(int, input().split())) for _ in range(N)]
AB.sort(key=lambda x: x[0])
dp = [[0]*(T) for _ in range(N+1)]
ans = 0
for i in range(N):
    for j in range(T):
        dp[i+1][j] = dp[i][j]
        ans = max(ans, dp[i][j] + AB[i][1])
        # 上は この時刻jまでで商品i-1個を入れた後に時間制約の無いi個目の商品を追加している
        if j - AB[i][0] >= 0:
            dp[i+1][j] = max(dp[i][j], dp[i][j-AB[i][0]] + AB[i][1])
print(ans)
