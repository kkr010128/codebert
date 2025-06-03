from collections import deque

h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

res = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            continue
        dist = [[-1] * w for _ in range(h)]
        dist[i][j] = 0
        d = deque()
        d.append([i, j])

        while d:
            pos_x, pos_y = d.popleft()
            dist_max = dist[pos_x][pos_y]
            for k in range(4):
                x, y = pos_x + dx[k], pos_y + dy[k]
                if 0 <= x < h and 0 <= y < w and s[x][y] == "." and dist[x][y] == -1:
                    dist[x][y] = dist[pos_x][pos_y] + 1
                    d.append([x, y])

        res = max(res, dist_max)

print(res)