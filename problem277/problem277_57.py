def ddcc2020q_c():
    H, W, _ = map(int, input().split())
    stable = [[s for s in str(input())] for _ in range(H)]
    atable = [[0] * W for _ in range(H)]
    num = 1  # '#'につけるラベル
    for i in range(H):
        for j in range(W):  # 左から右へ
            if stable[i][j] == '#':
                atable[i][j] = num
                num += 1
            if j == 0: continue
            if atable[i][j] == 0 and atable[i][j-1] > 0:
                atable[i][j] = atable[i][j-1]
    for i in range(H):
        for j in range(W-2, -1, -1):  # 右から左へ
            if atable[i][j] == 0 and atable[i][j+1] > 0:
                atable[i][j] = atable[i][j+1]
    for i in range(1, H):  # 上から下へ
        for j in range(W):
            if atable[i][j] == 0 and atable[i-1][j] > 0:
                atable[i][j] = atable[i-1][j]
    for i in range(H-2, -1, -1):  # 下から上へ
        for j in range(W):
            if atable[i][j] == 0 and atable[i+1][j] > 0:
                atable[i][j] = atable[i+1][j]
    # 出力
    for row in atable:
        print(*row, sep=' ')
    return

ddcc2020q_c()