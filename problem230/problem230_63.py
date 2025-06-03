import bisect
from collections import deque
import math
n, d, A = map(int, input().split())
xh = []
for _ in range(n):
    x, h = map(int, input().split())
    xh.append([x, h])
xh.sort(key=lambda x: x[0])

monster_x = []
monster_hp = []
for i in range(n):
    monster_x.append(xh[i][0])
    monster_hp.append(xh[i][1])

dist = 2 * d
ans = 0
damage = 0
cum_damage = [0] * (n + 1)
for i in range(n):
    cum_damage[i + 1] += cum_damage[i]
    damage = cum_damage[i + 1] * A
    if damage < monster_hp[i]:
        min_attack_num = math.ceil((monster_hp[i] - damage) / A) 
        index = bisect.bisect_right(monster_x, monster_x[i] + dist)
        cum_damage[i + 1] += min_attack_num
        if index < n:
            t = min(index + 1, n)
            cum_damage[t] -= min_attack_num
        ans += min_attack_num

print(ans)
