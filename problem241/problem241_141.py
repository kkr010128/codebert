from collections import deque
H, W =  map(int, input().split())
S=[]
for _ in range(H):
    S.append(input())
vx = [1, 0, -1, 0]
vy = [0, 1, 0, -1]
ans = 0

def func(si, sj):
    queue = deque([si, sj])  
    seen = [[-1]*W for _ in range(H)]
    seen[si][sj] = 0
    while queue:
        x = queue.popleft()
        y = queue.popleft()
        
        for i in range(4):
            nx = x + vx[i]
            ny = y + vy[i]
            if nx<0 or nx>=H or ny<0 or ny>=W:
                continue
            if S[nx][ny]=="#" or seen[nx][ny]>=0:
                continue
            seen[nx][ny]=seen[x][y]+1
            queue.append(nx)
            queue.append(ny)
    return seen[x][y]
    
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j]==".":
            ans = max(ans, func(i, j))
print(ans)