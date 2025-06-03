from collections import deque

N, D, A = map(int, input().split())
monsters = []
for _ in range(N):
    monsters.append(list(map(int, input().split())))

monsters.sort()
d = deque()
ans = 0
damage = 0
for x, h in monsters:
    while d:
        if d[0][0] >= x - D:
            break
        _, power = d.popleft()
        damage -= power
    h -= damage
    if h <= 0:
        continue
    attack = (h - 1) // A + 1
    
    ans += attack
    d.append((x + D, attack * A))
    damage += attack * A
print(ans)
