R,C,K=map(int,input().split())
l=[[0] * C for i in range(R)]
for i in range(K):
  a,b,c=map(int,input().split())
  a-=1
  b-=1
  l[a][b]=c
dp=[[0] * C for i in range(R)]
for i in range(R):
  kdp=[0]*4
  for j in range(C):
    if i>0:
      kdp[0]=max(kdp[0],dp[i-1][j])
    for k in range(2,-1,-1):
      kdp[k+1]=max(kdp[k+1],kdp[k]+l[i][j])
      dp[i][j]=max(dp[i][j],kdp[k+1])
print(dp[R-1][C-1])