import collections

h,w=map(int,input().split())
board=[list(input()) for _ in range(h)]
q=collections.deque()
if board[0][0]=='#':
  q.append((0,0,1,1))
else:
  q.append((0,0,0,0))
dp=[[10**18]*w for _ in range(h)]
ans=10**18
while len(q)!=0:
  x,y,cnt,flag=q.popleft()
  if x==w-1 and y==h-1:
    ans=min(ans,cnt)
  else:
    if x!=w-1:
      if flag==0:
        if board[y][x+1]=='#':
          if dp[y][x+1]>cnt+1:
            q.append((x+1,y,cnt+1,1))
            dp[y][x+1]=cnt+1
        else:
          if dp[y][x+1]>cnt:
            q.append((x+1,y,cnt,0))
            dp[y][x+1]=cnt
      else:
        if board[y][x+1]=='#':
          if dp[y][x+1]>cnt:
            q.append((x+1,y,cnt,1))
            dp[y][x+1]=cnt
        else:
          if dp[y][x+1]>cnt:
            q.append((x+1,y,cnt,0))
            dp[y][x+1]=cnt
    if y!=h-1:
      if flag==0:
        if board[y+1][x]=='#':
          if dp[y+1][x]>cnt+1:
            q.append((x,y+1,cnt+1,1))
            dp[y+1][x]=cnt+1
        else:
          if dp[y+1][x]>cnt:
            q.append((x,y+1,cnt,0))
            dp[y+1][x]=cnt
      else:
        if board[y+1][x]=='#':
          if dp[y+1][x]>cnt:
            q.append((x,y+1,cnt,1))
            dp[y+1][x]=cnt
        else:
          if dp[y+1][x]>cnt:
            q.append((x,y+1,cnt,0))
            dp[y+1][x]=cnt
print(dp[-1][-1])