def bfs(x0, y0, maze, dis):
    from collections import deque
    max_x = len(maze[0])
    max_y = len(maze)

    dis[y0][x0] = 0
    dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    q = deque()
    q.append([x0, y0, dis[y0][x0]])

    while len(q) > 0:
        x, y, d = q.popleft()

        for dx, dy in dxy:
            nx = x + dx
            ny = y + dy

            if 0 > nx or max_x <= nx or 0 > ny or max_y <= ny:
                continue
            if maze[ny][nx] == "#":
                continue
            if dis[ny][nx] != -1:
                continue

            dis[ny][nx] = d + 1
            q.append([nx, ny, dis[ny][nx]])

    return


h, w = map(int, input().split())

s = [[] for _ in range(h)]

for i in range(h):
    s[i] = input()

ans = 0
for i in range(h):
    for j in range(w):
        dis = [[-1] * w for _ in range(h)]

        if s[i][j] != "#":
            bfs(j, i, s, dis)

        d = 0

        for k in range(h):
            for l in range(w):
                d = max(d, dis[k][l])

        ans = max(ans, d)

print(ans)