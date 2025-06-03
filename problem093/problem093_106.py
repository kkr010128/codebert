'''
参考
https://marco-note.net/abc-175-work-log/
'''
N, K = map(int, input().split())        # コマ数、最大移動可能回数
P = list(map(int, input().split()))     # 移動先のコマ番号
C = list(map(int, input().split()))     # そのコマに立ち寄った時に加算される得点

ans = -float('inf')             # 解を-∞で初期化

for piece in range(N):          # 各コマについて、スタート地点とした場合の得点を調べる
    S = []                      # 累積和
    mov = P[piece] - 1          # 1回目の移動：移動先（indexなので-1する）
    S.append(C[mov])            # 1回目の移動：得点

    while mov != piece:             # 2回目以降の移動（スタート地点に戻ったらループ終了）
        mov = P[mov] - 1            # 2回目以降：移動先
        S.append(S[-1] + C[mov])    # 2回目以降：得点（最終要素に加算した値をリストに追加）
    
    if K <= len(S):             # 【パターン1】与えられた移動可能回数では一巡できない
        score = max(S[:K])      # 得点=移動可能回数までの最大得点
    elif S[-1] <= 0:            # 【パターン2】一巡できるが一巡してしまうと得点が減る
        score = max(S)          # 得点=一巡するまでの最大得点
    else:
        score_a = S[-1] * (K // len(S))     # 【パターン3-1】与えられた移動可能回数で廻れるだけ廻る
        rem = K % len(S)
        if rem != 0:
            score_a += max(0, max(S[:rem]))
        score_b = S[-1] * (K // len(S) - 1) # 【パターン3-2】1周少なく廻りあとは最高得点のところで止める
        score_b += max(S)
        score = max(score_a, score_b)
    
    ans = max(ans, score)

print(ans)