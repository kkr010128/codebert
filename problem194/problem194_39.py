from collections import deque


H, W = map(int, input().split())
grid = [input() for _ in range(H)]

INF = 1000
path = [[INF] * W for _ in range(H)]

q = deque()
q.append((0, 0, 0))
path[0][0] = 0
while q:
    s, i, j = q.popleft()
    c = grid[i][j]
    for di, dj in [(1, 0), (0, 1)]:
        ni, nj = i + di, j + dj
        if 0 <= ni < H and 0 <= nj < W:
            nc = grid[ni][nj]
            ns = s + (c != nc)
            if path[ni][nj] > ns:
                path[ni][nj] = ns
                if c == nc:
                    q.appendleft((ns, ni, nj))
                else:
                    q.append((ns, ni, nj))

ans = path[-1][-1]
ans += (grid[0][0] == '#') + (grid[-1][-1] == '#')
print(ans // 2)
