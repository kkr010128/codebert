from collections import deque

h,w = map(int, input().split())
maze = [list(input()) for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = 0

for a in range(h):
    for b in range(w):
        if maze[a][b] == ".":
            DQ = deque([(a, b)])
            visit = [[-1] * w for _ in range(h)]
            visit[a][b] = 0
            tmp = 0
            while DQ:
                px, py = DQ.popleft()
                for i in range(4):
                    nx = px + dx[i]
                    ny = py + dy[i]
                    if 0<=nx<=h-1 and 0<=ny<=w-1 and maze[nx][ny]=="." and visit[nx][ny]==-1:
                        visit[nx][ny] = visit[px][py] + 1
                        tmp = visit[nx][ny]
                        DQ.append((nx, ny))
            ans = max(ans, tmp)

print(ans)