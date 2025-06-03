import math
from collections import deque

N, D, A = list(map(int, input().split()))
data = []
for _ in range(N):
    x, h = list(map(int, input().split()))
    data.append((x, math.ceil(h/A)))
data = sorted(data, key=lambda x: x[0])

c = 0
damage_que = deque()
attack = 0 # 有効なダメージ合計
for i in range(N):
    x, h = data[i]

    # 爆破範囲が届いていなければ削除していく
    while damage_que and x > damage_que[0][0]:
        _, a = damage_que.popleft()
        attack -= a
    
    # 有効な過去の爆破攻撃を受ける
    remain = max(h - attack, 0)
    # 0になるまで爆破    
    attack += remain
    c += remain

    # 爆破回数追加    
    damage_que.append([x+2*D, remain])

print(c)