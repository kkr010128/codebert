from collections import deque

h,w=map(int,input().split())

maze=[list(input()) for i in range(h)]

ans=0

dx=[1,-1,0,0]
dy=[0,0,1,-1]


for i in range(h):
  for j in range(w):
        Q=deque()
        Q.append((i,j,0))
        
        if maze[i][j]=='#':
          continue

        dp=[[-1]*w for i in range(h)]

        dp[i][j]=0

        while Q:
          p=Q.popleft()
          ans=max(ans,p[2])
          for k in range(4):
            nx=p[0]+dx[k]
            ny=p[1]+dy[k]

            if 0<=nx<h and 0<=ny<w and maze[nx][ny]=='.' and dp[nx][ny]==-1:
              Q.append((nx,ny,p[2]+1))
              dp[nx][ny]=p[2]+1


print(ans)
