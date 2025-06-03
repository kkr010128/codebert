n,t=map(int,input().split())
F=[list(map(int,input().split())) for i in range(n)]
dp1=[[0]*(t+1) for i in range(n)]
for i in range(1,n):
  for j in range(1,t+1):
    if j-F[i-1][0]>=0:
      dp1[i][j]=max(dp1[i-1][j],dp1[i][j-1],dp1[i-1][j-F[i-1][0]]+F[i-1][1])
    else:
      dp1[i][j]=max(dp1[i-1][j],dp1[i][j-1])
dp2=[[0]*(t+1) for i in range(n)]
for i in range(1,n):
  for j in range(1,t+1):
    if j-F[n-i][0]>=0:
      dp2[i][j]=max(dp2[i-1][j],dp2[i][j-1],dp2[i-1][j-F[n-i][0]]+F[n-i][1])
    else:
      dp2[i][j]=max(dp2[i-1][j],dp2[i][j-1])
ans=0
for i in range(n):
  for j in range(1,t):
    a=dp1[i][j]+dp2[n-i-1][t-j-1]+F[i][1]
    if a>ans:
      ans=a
print(ans)