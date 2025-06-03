from collections import deque
import copy
H, W = map(int, input().split())
maze = [list(input()) for _ in range(H)]

# すべての.についてスタート地点と仮定してBFS
def bfs(i, j):
    dq = deque()
    maze_c = copy.deepcopy(maze)
    maze_c[i][j] = 0
    dq.appendleft([i, j])
    res = 0
    while len(dq) > 0:
        ni, nj = dq.pop()
        if maze_c[ni][nj] == "#":
            continue
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            if ni + di < 0 or nj + dj < 0 or ni + di >= H or nj + dj >= W:
                continue
            if maze_c[ni + di][nj + dj] == ".":
                maze_c[ni + di][nj + dj] = maze_c[ni][nj] + 1
                res = max(res, maze_c[ni + di][nj + dj])
                dq.appendleft([ni + di, nj + dj])
    return res

ans = 0
for i in range(H):
    for j in range(W):
        if maze[i][j] == ".":
            ans = max(ans, bfs(i, j))
print(ans)