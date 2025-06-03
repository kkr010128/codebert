from math import ceil
from collections import deque
n,d,a = map(int, input().split())

monster = [list(map(int,input().split())) for i in range(n)]

monster.sort()

damage = 0

finish = deque()

ans = 0

for i in range(n):
    x,h = monster[i]
    while finish:
        if finish[0][0]<x:
            damage -= finish.popleft()[1]
        else:
            break
    if h<=damage:
        continue
    else:
        b = ceil((h-damage)/a)
        ans += b
        damage += b*a
        finish.append([x+2*d,b*a])

print(ans)
