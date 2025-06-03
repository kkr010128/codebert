import sys
from collections import deque

input = sys.stdin.readline
H, W = map(int, input().split())

grid = []
for _ in range(H):
    grid.append(list(input().strip()))

q = deque()
# x, y, count, pre color
q.append((0, 0, 1 if grid[0][0] == "#" else 0, grid[0][0]))

visited = [[-1 for _ in range(W)] for _ in range(H)]
ans = float("inf")
while q:
    x, y, count, pre = q.popleft()
    # print(x, y, count, pre)
    v_score = visited[y][x]
    if v_score != -1 and v_score <= count:
        continue
    visited[y][x] = count

    for dx, dy in ((1, 0), (0, 1)):
        nx = x + dx
        ny = y + dy
        nc = count
        if nx < 0 or W <= nx or ny < 0 or H <= ny:
            continue
        n_color = grid[ny][nx]
        if n_color != pre and n_color == "#":
            nc += 1
        if nx == W-1 and ny == H-1:
            ans = min(ans, nc)
            print(ans)
            sys.exit()
        else:
            if visited[ny][nx] != -1 and visited[ny][nx] <= nc:
                continue
            if count == nc:
                q.appendleft((nx, ny, nc, n_color))
            else:
                q.append((nx, ny, nc, n_color))

# print(visited)
print(ans)  