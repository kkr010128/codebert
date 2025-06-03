from math import ceil
from collections import deque
n,d,a = map(int,input().split())
m = [list(map(int,input().split())) for _ in range(n)]
m.sort()
l = [(x, ceil(h/a)) for x,h in m]

ans = 0
damage = 0
que = deque([])

for x,h in l:
    while que and que[0][0] < x:
            s,t = que.popleft()
            damage -= t
    need = max(0, h - damage)
    ans += need
    damage += need
    if need:
        que.append((x+2*d, need))
print(ans)