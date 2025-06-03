h,w = list(map(int,input().split()))
h += 2
w += 2
grid = '#'*w
for _ in range(h-2):
    grid += '#' + input() + '#'
grid += '#'*w

from collections import deque
ans = 0
for i in range(len(grid)):
    INF = 10**9
    dist = [INF]*(h*w)
    if grid[i]=='#':
        continue
    dist[i] = 0
    q = deque([i])
    while q:
        v = q.popleft()
        dv = dist[v]
        for m in (-1,1,w,-w):
            move = v + m
            if grid[move]=='#':
                continue
            dmove = dv + 1
            if dmove >= dist[move]:
                continue
            dist[move] = dmove
            q.append(move)
    # print([dist[i] if dist[i]!=INF else 0 for i in range(len(dist))])
    ans = max(ans, max([dist[i] if dist[i]!=INF else 0 for i in range(len(dist))]))
    # print(ans)
    
print(ans)