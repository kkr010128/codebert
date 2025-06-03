from collections import deque
import numpy as np

H, W = map(int, input().split())
grid = [input() for _ in range(H)]

ini = -1
q = deque()

dy = (-1, 0, 1, 0)
dx = (0, 1, 0, -1)
ans = 0

for y in range(H):
    for x in range(W):
        dist = [[ini for _ in range(W)] for _ in range(H)]
        if grid[y][x] == "#": continue
        dist[y][x] = 0
        q.append((y, x))

        while(len(q) > 0):
            oy, ox = q.popleft()
            for di in range(4):
                ny = oy + dy[di]
                nx = ox + dx[di]

                if (ny < 0 or ny >= H or nx < 0 or nx >= W): continue
                if grid[ny][nx] == "#": continue
                if dist[ny][nx] != ini: continue

                dist[ny][nx] = dist[oy][ox] + 1
                q.append((ny, nx))

        ans = max(np.max(dist), ans)

print(ans)