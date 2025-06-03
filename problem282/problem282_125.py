n,t = map(int,input().split())
ab = [list(map(int,input().split())) for _ in range(n)]
ab.sort() # 食べるのが早い順にソート

# ナップザック問題に落とし込む
dp = [[0 for i in range(t+1)]for j in range(n+1)]

for i in range(n):
    ti,vi = ab[i]
    for j in range(t+1):
        # 食べたほうがよい(t秒以内かつ満足度が上がるならば)
        if j + ti <= t:
            dp[i+1][j+ti] = max(dp[i+1][j+ti],dp[i][j]+vi)
        # 食べなかった場合の最高値を更新
        dp[i+1][j] = max(dp[i][j],dp[i+1][j])

ma = 0

for i in range(n):
    # 最後にi番目の皿を食べることができる
    ma = max(ma,dp[i][t-1]+ab[i][1])

print(ma)