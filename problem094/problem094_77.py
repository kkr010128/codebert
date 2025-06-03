R,C,K = map(int, input().split())

d = [[0 for _ in range(C+1)] for _ in range(R+1)]

#dp[行の中でピックした回数][行][列]　この順じゃないとTLEする
dp = [[[0 for _ in range(C+1)] for _ in range(R+1)] for _ in range(4)]

for i in range(K):
    r, c, v = map(int, input().split())
    d[r-1][c-1] = v
for i in range(R):
    for j in range(C):
        # kが大きい方からやらないとダメ。01ナップサックと同じ考え方。書き換えられた値を見ないように。
        for k in range(2, -1, -1):
            # 拾う遷移。d[i][j]を取るかどうかという判定
            dp[k+1][i][j] = max(dp[k+1][i][j], dp[k][i][j] + d[i][j])
        for k in range(4):
            dp[0][i+1][j] = max(dp[0][i+1][j], dp[k][i][j])
            dp[k][i][j+1] = max(dp[k][i][j+1], dp[k][i][j])
ans = 0

for k in range(4):
    ans = max(ans, dp[k][R-1][C-1])
print(ans)    