N = int(input())
# [[1番の人の証言], [2番の人の証言], ..., [N番の人の証言]]
l = [[-1 for i in range(N)] for j in range(N)]
# N人についてそれぞれ証言をまとめる
for i in range(N):
    # 証言の数
    a = int(input())
    # 各証言をlに格納
    for _ in range(a):
        x, y = map(int, input().split())
        l[i][x - 1] = y

ans = 0

# bit全探索
# N人について聖人/狂人の計2**N通り
for i in range(2**N):
    # iをN桁2bitに変換, 1が聖人に対応
    d = [0 for _ in range(N)]
    # 下からj桁目のbitが立っているか否か
    for j in range(N):
        if i >> j & 1:
            d[j] = 1
    """
    ex. N=3の時、
    i = 0,1,2,3,4,5,6,7 この時、dはそれぞれ 
    [0, 0, 0],[1, 0, 0],[0, 1, 0],[1, 1, 0],
    [0, 0, 1],[1, 0, 1],[0, 1, 1],[1, 1, 1]
    """

    flag = True

    # dの中身を左から順に見ていく
    for j in range(N):
        # jの全員に対する証言について
        for k in range(N):
            # 狂人(d[j]==0)の証言は意味がないので無視して良い
            if d[j] == 1:
                # l[j][k] == -1 なら、その人に対する証言は存在しない
                if l[j][k] == -1:
                    continue
                # kについての証言と、kの実情が異なる場合（矛盾）
                if l[j][k] != d[k]:
                    flag = False
                    break

    # 一つも矛盾が存在しなかった場合
    # sum(d)は聖人の総数を表す
    if flag == True:
        ans = max(ans, sum(d))

print(ans)
