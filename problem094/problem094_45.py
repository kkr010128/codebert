import sys
input = sys.stdin.readline
R, C, K = map(int, input().split())

item = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
for _ in range(K):
    r, c, v = map(int, input().split())
    item[r][c] = v

# dp[n][i][j] = その行で取得したアイテムがn個で、(i,j)でのmax_value
dp = [[[0 for _ in range(C + 1)]for _ in range(R + 1)]for _ in range(4)]

for i in range(R + 1):
    for j in range(C + 1):
        # 下に移動
        if i <= R - 1:
            # アイテムを取らない
            dp[0][i + 1][j] = max(dp[0][i + 1][j],
                                  dp[0][i][j],
                                  dp[1][i][j],
                                  dp[2][i][j],
                                  dp[3][i][j])
            # アイテムを取る
            dp[1][i + 1][j] = max(dp[1][i + 1][j],
                                  dp[0][i][j] + item[i + 1][j],
                                  dp[1][i][j] + item[i + 1][j],
                                  dp[2][i][j] + item[i + 1][j],
                                  dp[3][i][j] + item[i + 1][j])

        # 右に移動
        if j <= C - 1:
            # アイテムを取らない
            dp[0][i][j + 1] = max(dp[0][i][j + 1], dp[0][i][j])
            dp[1][i][j + 1] = max(dp[1][i][j + 1], dp[1][i][j])
            dp[2][i][j + 1] = max(dp[2][i][j + 1], dp[2][i][j])
            dp[3][i][j + 1] = max(dp[3][i][j + 1], dp[3][i][j])
            # アイテムを取る
            dp[1][i][j + 1] = max(dp[1][i][j + 1],
                                  dp[0][i][j] + item[i][j + 1])
            dp[2][i][j + 1] = max(dp[2][i][j + 1],
                                  dp[1][i][j] + item[i][j + 1])
            dp[3][i][j + 1] = max(dp[3][i][j + 1],
                                  dp[2][i][j] + item[i][j + 1])

ans = max(dp[0][R][C], dp[1][R][C], dp[2][R][C], dp[3][R][C])
print(ans)
