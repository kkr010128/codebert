from collections import deque


def bfs(i, j):
    dist = [[0] * w for _ in range(h)]
    q = deque()
    q.append((i, j))
    dist[i][j] = 1
    while q:
        nx, ny = q.pop()
        for dx, dy in D:
            X, Y = nx + dx, ny + dy
            if X < 0 or Y < 0 or X >= h or Y >= w:
                continue
            if m[X][Y] == "#":
                continue
            if dist[X][Y] != 0:
                continue

            q.appendleft((X, Y))
            dist[X][Y] = 1 + dist[nx][ny]
    mx = 0
    for i in dist:
        mx = max(mx, max(i))
    return mx


h, w = map(int, input().split())
m = [input() for _ in range(h)]
D = [(-1, 0), (0, -1), (1, 0), (0, 1)]
ans = 0
for i in range(h):
    for j in range(w):
        if m[i][j] == ".":
            ans = max(ans, bfs(i, j))

print(ans - 1)