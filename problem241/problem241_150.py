from collections import deque

h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]

def bfs(sx, sy):
    que = deque([])
    que.append((sx, sy))
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    d = [[-1] * w for i in range(h)]
    d[sy][sx] = 0
    while que:
        s = que.popleft()
        for i in range(4):
            nx = s[0] + dx[i]
            ny = s[1] + dy[i]
            
            if 0 <= nx < w and 0 <= ny < h and maze[ny][nx] != "#" and d[ny][nx] == -1:
                que.append((nx, ny))
                d[ny][nx] = d[s[1]][s[0]] + 1
    
    tmp = 0
    for i in range(h):
        for j in range(w):
            tmp = max(tmp, d[i][j])
    
    return tmp

ans = 0
for i in range(w):
    for j in range(h):
        if maze[j][i] == ".":
            ans = max(ans, bfs(i, j))

print(ans)