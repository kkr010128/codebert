from collections import deque

h, w = map(int, input().split())
meiro = [list(input()) for i in range(h)]
# meiro[y][x]


def bfs(a, b):  # a縦b横
    mx_dist = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dist = [[-1] * w for i in range(h)]
    dist[a][b] = 0
    que = deque([])
    que.append((a, b))
    while que:
        y, x = que.popleft()
        D = dist[y][x]
        for i in range(4):
            X = x + dx[i]
            Y = y + dy[i]
            if 0 <= Y and Y <= h - 1 and X <= w - 1 and 0 <= X:
                if meiro[Y][X] == ".":
                    if dist[Y][X] == -1:
                        dist[Y][X] = D + 1
                        que.append((Y, X))
                        mx_dist = max(mx_dist, D + 1)

    return mx_dist


saidai = 0
for i in range(h):
    for j in range(w):
        if meiro[i][j] == ".":
            saidai = max(saidai, bfs(i, j))
print(saidai)
