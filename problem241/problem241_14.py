from collections import deque
import sys


H, W = map(int, input().split())
field = ["o" for _ in range(H+2)] #indexed from 1
for i in range(1, H+1):
    field[i] = "#" + input() + "#"
field[0] = "#"*(W+2)
field[H+1] = "#"*(W+2)

idxs = []
dxdy = [(1,0), (-1,0), (0,1), (0,-1)]
for row in range(1, H+1):
    for col in range(1, W+1):
        if field[row][col] == ".":
            idxs.append((row, col))
# graph = {idx: deque() for idx in idxs}
# for idx in idxs:
#     x = idx[0]
#     y = idx[1]
#     for dx, dy in dxdy:
#         if field[x+dx][y+dy] == ".":
#             graph[idx].append((x+dx, y+dy))


def bfs(u,v):
    dist = [[-1] * (W+1) for _ in range(H+1)] #indexed from 1
    seen = [[0] * (W+1) for _ in range(H+1)] #indexed from 1
    queue = deque()
    seen[u][v] = 1
    dist[u][v] = 0
    queue.append((u,v))
    graph = {idx: deque() for idx in idxs}
    for idx in idxs:
        x = idx[0]
        y = idx[1]
        for dx, dy in dxdy:
            if field[x+dx][y+dy] == ".":
                graph[idx].append((x+dx, y+dy))
    while queue:
        p, q = queue[0]
        if not graph[(p,q)]:
            queue.popleft()
            continue
        g,h = graph[(p,q)].popleft()
        if seen[g][h]:
            continue
        seen[g][h] = 1
        dist[g][h] = dist[p][q] + 1
        queue.append((g,h))
    ans = -1
    for i in range(1, H+1):
        for j in range(1, W+1):
            ans = max(ans, dist[i][j])
    return ans


res = -1
for sx, sy in idxs:
    res = max(res, bfs(sx, sy))
print(res)
