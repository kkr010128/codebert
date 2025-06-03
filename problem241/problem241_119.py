import heapq

s = []
h, w = map(int, input().split())
for _ in range(h):
    s.append(list(input().strip()))

ans = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            continue

        q = [(0, (i, j))]
        mins = [[h * w for _ in range(w)] for _ in range(h)]
        visited = [[0 for _ in range(w)] for _ in range(h)]
        while len(q) > 0:
            c, (x, y) = heapq.heappop(q)
            ans = max(ans, c)
            if visited[x][y]:
                continue
            visited[x][y] = True
            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if nx < 0 or nx >= h or ny < 0 or ny >= w or s[nx][ny] == '#':
                    continue
                if visited[nx][ny]:
                    continue
                if mins[nx][ny] > c + 1:
                    mins[nx][ny] = c + 1
                    heapq.heappush(q, (c + 1, (nx, ny)))

print(ans)
