from collections import deque

H, W, K = map(int, input().split())
S = []
for _ in range(H):
    S.append(list(input()))


def cut(bit):

    """
    横の切れ目の場所をビットで管理する。
    "00...0" <= bit <= "11...1"(H - 1桁)の時に、縦に入れる切れ目の最小回数を返す。
    """

    end = [] # 板チョコを横区切りにした結果、上から何段目で各板チョコのピースが終わるか
    for i in range(H - 1):
        if bit[i] == '1':
            end.append(i)
    end.append(H - 1)
    chocolates = [0] * (len(end))
    #print("end={}".format(end))

    """
    ここまでで板チョコを横に切ったわけだが、こうして分割した横長の部分板チョコを
    上からsection = 0, 1, 2,..., len(end)-1と呼び分けることにする。
    """

    cut = 0
    whites_sum = [0] * len(end) # w列目までの白チョコの累積数をsectionごとに管理。cutが入れば初期化。
    for w in range(W):
        whites = [0] * len(end) # whites[section] = (w列目にある白チョコをsectionごとに保存)
        section = 0 # 現在のsection
        coarse = False # 横切りが荒過ぎて１列に白チョコがK個より多く並んだ場合に探索を打ち切るフラグ

        for h in range(H + 1):
            # sectionを跨いだ場合の処理
            if h > end[section]:
                if whites[section] > K:
                    coarse = True
                    break
                elif whites_sum[section] + whites[section] > K:
                    cut += 1
                    whites_sum = whites
                    whites = [0] * len(end)
                    section += 1
                else:
                    whites_sum[section] += whites[section]
                    section += 1

            # 白チョコカウント
            if h < H and S[h][w] == '1':
                whites[section] += 1

        # coarseフラグが立っていたら-1を返す。
        if coarse:
            return -1
    return cut


ans = 10 ** 10
for h in range(2 ** (H - 1)):
    bit = bin(h)[2:] # "0b..."を除くため
    l = len(bit)
    bit = '0' * (H - 1 - l) + bit # bitの桁数をH - 1にする。
    #print("bit={}".format(bit))

    vertical_cuts = cut(bit)
    if vertical_cuts != -1:
        preans = vertical_cuts + bit.count('1')
        ans = min(ans, preans)
        #print("vertical_cut={}, cut={} -> ans={}".format(vertical_cuts, preans, ans))


print(ans)
