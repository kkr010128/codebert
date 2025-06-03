import math
from bisect import bisect_right  # クエリより真に大きい値が初めて現れるインデックスを教えてくれる
# 初めて爆弾が届かない範囲を記録しながら前から順に倒していく
N, D, A = map(int, input().split())  # N体のモンスター, 爆弾の範囲D, 爆弾の威力A
XH = []
X = []
for _ in range(N):
    x, h = map(int, input().split())
    XH.append((x, math.ceil(h/A)))
    X.append(x)
# 座標で昇順ソート
XH.sort()
X.sort()
# 前から倒していく
now = 0
ans = 0
T = [0]*(N+1)  # 爆弾の範囲が切れる場所を記録しておく
for i in range(N):
    x, h = XH[i]  # 今見ているモンスターの座標, 体力
    now -= T[i]  # そのモンスターに届いていない爆弾があるなら引く
    if now >= h:  # 今残っている爆弾だけで倒せるならcontinue
        continue
    else:
        ans += h - now  # 足りない分(h-now個)の爆弾を使う
        T[bisect_right(X, x+2*D)] += h - now  # 爆弾の範囲が切れる場所を記録しておく
        now = h  # 今影響が残っている爆弾の威力
print(ans)
