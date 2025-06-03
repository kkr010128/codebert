from collections import deque

H, W = map(int, input().split())
maze = [input() for _ in range(H)]

v = {(1,0), (-1,0), (0,1), (0,-1)}
q = deque()
ans = 0

for i in range(H):
    for j in range(W):
        if maze[i][j] == '.':
                    
            #bfs
            dist = [[-1 for _ in range(W)] for _ in range(H)]
            dist[i][j] = 0
            q.append([j, i])
            while len(q) > 0:
                now = q.popleft()
                x, y = now[0], now[1]
                d = dist[y][x]
                for dx, dy in v:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<W and 0<=ny<H and dist[ny][nx]==-1 and maze[ny][nx]=='.':
                        dist[ny][nx] = d+1
                        q.append([nx, ny])
            
            ans = max(ans, d)
print(ans)