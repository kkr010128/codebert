N, K = map(int, input().split())
P = [0] + list(map(int, input().split()))
C = [0] + list(map(int, input().split()))

#マスに与えられたスコアが全部負だった場合には，その中で最もダメージの小さいマスを一つ踏んで終わる。
C_max = max(C[1:])
if C_max < 0:
    print(C_max)
    exit()


ans = 0

done = [False] * (N + 1) #チェック済みのマスはTrueにしていく。(loopはバラバラの構成員で構成されてるので。)

#loopの構成員をもらう。 -→ loopの中でマスaから始まりマスbで止まる操作をする場合の最大スコアを数える。
#の順番で解く。

for i in range(1, N + 1):
    if done[i]:
        continue
        #マスiがチェック済みの場合には何もせずiを次に進める。（continue）

    loop = [i] #ここにloopの構成員が記録される。iは最初から入れておく。
    now = P[i] #iから一歩進んだマスを起点として，loop構成員の記録を開始する。
    while now != i:
        loop.append(now)
        done[now] = True
        now = P[now]
        #今立っているマスがiでない場合は，loop構成員リストに記録して，doneをTrueにして，足を一歩進める。

    #print(loop)
    #loopの構成員のメモが完了！

    L = len(loop)
    S = sum(C[v] for v in loop) #loopを一周した時のスコア

    for a_ind in range(L):
        a = loop[a_ind]
        score_ab = -C[a]
        #例えば[3, 6, 4, 7]のloopがあった時，a = 3→6→4→7 と移っていきたいので，a_ind = 0→1→2...として，a =  loop[0]→loop[1]→loop[2]→loop[3]とする。bもまた然り。
        for b_ind in range(a_ind, a_ind + L):#aから数週してaに戻るプレイも可能なので，b == aとなる場合も含んでおかなければならない。
            dist_ab = b_ind - a_ind
            if dist_ab > K:
                break
            b = loop[b_ind % L]
            score_ab += C[b]

            max_score = score_ab + max(0, S) * ((K - dist_ab) // L)
            #スコアの最大値は，
            # S > 0の場合，[aからbまで移動した時のスコア] ＋ S * [可能な限りloopを周回する]　（周回した方が得なので）
            # S < 0の場合，[aからbまで移動した時のスコア]　（周回した方が損なので）
            #上の場合分けの切り替えを　max(0, S)　で行っている！地味にすごい！

            ans = max(ans, max_score)

print(ans)