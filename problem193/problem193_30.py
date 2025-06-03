import itertools
H, W, K = map(int, input().split())
grid = []
for _ in range(H):
    line = list(input())
    grid.append(line)
# 横に割る方法は2**(H-1)、高々2**9=512通り
# これを決め打ちして、縦の割り方はGreedyに

ans = 10**9

# 割る場合を1, 割らない場合を0で表すことにする
for ptn in itertools.product([0, 1], repeat=H - 1):

    # 不可能な場合、そのパターンはスキップする############################
    able = True
    for w in range(W):
        # それぞれのブロックにおける白の数
        lines = [0] * (sum(ptn) + 1)
        # 今、上から何ブロック目か
        line_num = 0
        for h in range(H):
            # 白の場合
            if grid[h][w] == "1":
                lines[line_num] += 1

            # 境界を引く場合
            # h=H-1の時、indexが範囲外になるのでminを使って調整
            if ptn[min(h, H - 2)] == 1:
                line_num += 1
        # 1列でK個を超えるブロックがある場合、その割り方は不適。
        if max(lines) > K:
            able = False
            break
    if able == False:
        continue
    # 以下、実現が可能なものとして考える################################

    # それぞれのブロックにおける白の数
    lines = [0] * (sum(ptn) + 1)
    # 横に割った回数
    cnt = sum(ptn)
    # ダメだったら1個前に戻る、という処理をしたいのでwhileで書く
    # for内でデクリメントしてもループにならない(自戒)
    w = 0
    while w < W:
        line_num = 0
        for h in range(H):
            # 白の場合
            if grid[h][w] == "1":
                lines[line_num] += 1
            # 境界を引く場合
            # h=H-1の時、indexが範囲外になるのでminを使って調整
            if ptn[min(h, H - 2)] == 1:
                line_num += 1
        # Kを超えるブロックができてしまう場合
        # 一つ前の列で切って、今の列からlinesを数え直す
        if max(lines) > K:
            cnt += 1
            lines = [0] * (sum(ptn) + 1)
            w -= 1
        w += 1
    ans = min(ans, cnt)

print(ans)
