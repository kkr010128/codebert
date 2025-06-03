
def resolve():
    R, C, K = map(int, input().split())
    G = [[0] * (C + 1) for _ in range(R + 1)]
    for _ in range(K):
        r, c, v = map(int, input().split())
        G[r][c] = v

    dp = [[[0] * (C + 1) for _ in range(R + 1)] for _ in range(4)]
    for i in range(R + 1):
        for j in range(C + 1):
            for k in range(4):
                here = dp[k][i][j]
                # 次の行に移動する場合
                if i + 1 <= R:
                    # 移動先のアイテムを取らない場合
                    dp[0][i + 1][j] = max(dp[0][i + 1][j], here)
                    # 移動先のアイテムを取る場合
                    dp[1][i + 1][j] = max(dp[1][i + 1][j], here + G[i + 1][j])
                # 次の列に移動する場合
                if j + 1 <= C:
                    # 移動先のアイテムを取らない場合
                    dp[k][i][j + 1] = max(dp[k][i][j + 1], here)
                    # 現在のkが3未満のときのみ, 移動先のアイテムを取ることが可能
                    if k < 3:
                        dp[k + 1][i][j + 1] = max(dp[k + 1][i][j + 1], here + G[i][j + 1])
    ans = 0
    for k in range(4):
        ans = max(ans, dp[k][-1][-1])
    print(ans)


if __name__ == "__main__":
    resolve()