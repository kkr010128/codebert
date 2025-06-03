H, W, K = map(int, input().split())
s = [list(input()) for _ in range(H)]

c = [[0 for _ in range(W)] for _ in range(H)]

# 1×ｗの一次元の配列で考える。分割したマスをそれぞれホワイトチョコをカウントする
# データを加工してから貪欲法を行う

# bit全探索: 横線で割るパターン全てについて、縦線での折り方を考える
ans = (H-1) * (W-1)
for div in range(1<<(H-1)):
    g = 0 # g: 横線で分割するグループ番号（０、１、２...）
    id = [0] * H #何行目であるかを識別するid: i=1なら　グループiになる
    for i in range(H):
        id[i] = g
        if div>>i&1: # 2進法でdivのi桁目が1の時、そこで分割する
            g += 1 #分割線がきたらgを増やす
    g += 1 # グループ数は分割線+１になる
    #　集計に使うｃ配列を初期化
    for i in range(g):
        for j in range(W):
            c[i][j] = 0
    # グループごとを各列ごとのホワイトチョコを集計する
    for i in range(H):
        for j in range(W):
            c[id[i]][j] += int(s[i][j])

    num = g - 1 #すでに横線で折った回数（グループ数-１）
    now = [0] * g #現状で何個のホワイトチョコがあるか
    # 各グループの縦割りの確認
    def add(j):
        for i in range(g):
            now[i] += c[i][j] #ｊ列目のホワイトチョコを足していく
        for i in range(g):
            
            if now[i] > K: return False
        return True

    for j in range(W):
        if not (add(j)): # ホワイトチョコがKを超えていれば、縦で織る。
            num += 1
            now = [0] * g
            if not (add(j)):
                num = (H-1) * (W-1)
                break
    #print(g, c, num) # 横割りの回数、各グループの集計、最終的に折った回数
    ans = min(ans, num) # 割った回数値の最小を更新 

print(ans)