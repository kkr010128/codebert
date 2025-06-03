n, k = list(map(int, input().split()))
# 先頭に0番要素を追加すれば、配列の要素番号と入力pが一致する
p = [0] + list(map(int, input().split()))
c = [0] + list(map(int, input().split()))

ans = -float('inf')
# 開始ノードをsi
for si in range(1, n+1):

    # 閉ループのスコアを取り出す
    x = si
    s = list()  # ノードの各スコアを保存
    #s_len = 0
    tot = 0     # ループ1周期のスコア
    while 1:
        x = p[x]
        s.append(c[x])
        #s[s_len] = c[x]
        #s_len += 1
        tot += c[x]
        if (x == si): break # 始点に戻ったら終了
    
    # siを開始とする閉ループのスコア(s)を全探
    s_len = len(s)
    t = 0
    for i in range(s_len):
        t += s[i]   # i回移動したときのスコア
        if (i+1 > k): break # 移動回数の上限を超えたら終了
        # 1周期のスコアが正ならば、可能な限り周回する
        if tot > 0:
            e = (k-(i+1))//s_len # 周回数
            now = t + tot*e      # i回移動と周回スコアの合計
        else:
            now = t
        ans = max(ans, now)

print(ans)
