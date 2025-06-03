def e_picking_goods():
    # 参考: https://atcoder.jp/contests/abc175/submissions/16044254
    R, C, K = [int(i) for i in input().split()]
    Goods = [[0] * (C + 1) for _ in range(R + 1)]
    for _ in range(K):
        r, c, v = [int(i) for i in input().split()]
        Goods[r][c] = v

    # editorial に対し、行の情報を除去する
    dp = [[0] * 4 for _ in range(C + 1)]
    for i in range(1, R + 1):
        dp_next = [[0] * 4 for _ in range(C + 1)]
        for j in range(1, C + 1):
            up_max = max(dp[j])  # 上のマスで 0~3 回アイテムを拾っていたときの、価値の最大値
            v = Goods[i][j]

            # 左か上から来て、アイテムを拾わない
            dp_next[j][0] = max(up_max, dp_next[j - 1][0])
            # 上から来て拾う or 左から来て拾う or 左から来て拾わない
            dp_next[j][1] = max(up_max + v, dp_next[j - 1][0] + v, dp_next[j - 1][1])
            # 左から来て k-1 個拾っており、ここで拾う or k 個拾っており、ここで拾わない
            for k in range(2, 4):
                dp_next[j][k] = max(dp_next[j - 1][k - 1] + v, dp_next[j - 1][k])
        dp = dp_next  # 次の行へ注目を移す
    return max(dp[-1])

print(e_picking_goods())