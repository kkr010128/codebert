h,w=map(int,input().split())
s=[input() for _ in range(h)]
dp=[[float('inf')]*w for _ in range(h)]
if s[0][0]=='#':
    dp[0][0] = 1
else:
    dp[0][0] = 0
dx=[1,0]
dy=[0,1]
for i in range(h):
    for j in range(w):
        for dir in range(2):
            ni=i+dy[dir]
            nj=j+dx[dir]
            if ni>=h or nj>=w:
                continue
            add=0
            if s[ni][nj]=='#' and s[i][j]=='.':
                add=1
            dp[ni][nj] = min(dp[ni][nj], dp[i][j]+add)
print(dp[-1][-1])