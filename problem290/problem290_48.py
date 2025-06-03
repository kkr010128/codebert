"""

AtCoder Beginner Contest 144  E - Gluttony


愚直解
・修行の順序は結果に影響しないから、修行を誰に割り振るか：N^K
・メンバーN人をどの問題に当てるか（N人の並べ方）：N!
-> N^K * N! 
間に合わない。

完食にかかる時間のうち最大値がチーム全体の成績なので、
・消化コストAiを修行で下げる
・消化コストAiの大きい人に、食べにくさFiの小さい食べ物を割り当てる
のが良さそう

最大値の最小化、なので、二分探索が使えそうな気もする。

A,F <= 10^6
かかる時間を X 以下にできるか、を考える。
・消化コストが大きい人に、食べにくさが小さい問題を当てるようにする
・Ai * Fi > Xであれば、(Ai - m) * Fi <= X となるような最小のmをカウントする
全メンバーに対しこれを数え上げた時に、
mの合計 > K
であれば、X以下になるように修行することができない（K回までしか修行できず、回数が足りない）ので、最大値の最小はXより上
mの合計 <= K
であれば、X以下になるように修行できるので、最大値の最小はX以下

A*F <= 10^12 までなので、40~50程度繰り返せば行けそう
"""
import math

N,K = map(int, input().split())
A = list(map(int, input().split()))
F = list(map(int, input().split()))

if K >= sum(A):
    print(0)
    exit()

A.sort(reverse=True)
F.sort()

def is_ok(mid):
    cnt = 0
    for i in range(N):
        if A[i] * F[i] <= mid:
            continue
        else:
            cnt += math.ceil((A[i] * F[i] - mid) / F[i]) # A[i]が1減少するごとにF[i]減るのでF[i]で割る  
    
    return cnt <= K

# okは全員がX以下になる最小値に着地するので、A*F<=10**12 なので＋１して最大のケースにも対応する
ok = 10**12 + 1
# 0ではないことが上で保証されてるので、条件を満たさない最大値の0にしておく
ng = 0
while ok - ng > 1:
    
    mid = (ok + ng) // 2
    #print(ok,ng,mid)
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

#print(ok,ng,mid)
print(ok)