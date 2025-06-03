from collections import deque

H, W = list(map(int,input().split()))
s = []
for i in range(H):  s.append(input())

dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]
           
def bfs(sx, sy):
    q = deque([])
    d = [[-1 for _ in range(W)] for _ in range(H)]
    q.append([sx, sy])
    d[sx][sy] = 0
    
    while(q):
        pop = q.popleft()
        x, y = pop[0], pop[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < H and ny >= 0 and ny < W:
                if s[nx][ny] != "#" and d[nx][ny] == -1:
                    q.append([nx, ny])
                    d[nx][ny] = d[x][y] + 1
    return d

def max_dim2(d):
    ret = 0
    for i in range(len(d)):
        for j in d[i]:
            ret = max(ret, j)
    return ret

ans = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == ".":
            ret = bfs(i, j)
            temp = max_dim2(ret)
            ans = max(ans, temp)
print(ans)    