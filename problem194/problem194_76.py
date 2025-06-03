def agc043_a():
    ''' 解説放送見てやってみた '''
    H, W = map(int, input().split())
    grid = []
    grid.append(['#'] * (W+2))  # 周辺埋め
    for _ in range(H):
        grid.append(['#'] + [c for c in str(input())] + ['#'])
    grid.append(['#'] * (W+2))
    grid[1][0] = grid[H][W+1] = '.'  # グリッド外側に白を置く, (1,1)(H,W)が黒の場合に反転カウントするため

    # 白黒が反転する回数を数える
    cost = [[10**6] * (W+2) for _ in range(H+2)]
    cost[1][0] = 0

    for i in range(1, H+1):
        for j in range(1, W+2):
            if i != H and j == W+1: continue  # ゴールの外側のときだけ通過
            rt = cost[i][j-1]
            if grid[i][j-1] != grid[i][j]: rt += 1
            dw = cost[i-1][j]
            if grid[i-1][j] != grid[i][j]: dw += 1
            cost[i][j] = min(rt, dw)

    ans = cost[H][W+1] // 2  # 区間の始まりと終わりを両方カウントしているので半分にする
    print(ans)

agc043_a()