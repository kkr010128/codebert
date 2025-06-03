n,t=map(int,input().split())
l=[list(map(int,input().split())) for i in range(n)]
l.sort()
dp=[[0]*(t+1) for i in range(n+1)]
for i in range(1,n+1):
  for j in range(t+1):
    if j!=t:
      if j-l[i-1][0]>=0:
        dp[i][j]=max(dp[i-1][j],dp[i-1][j-l[i-1][0]]+l[i-1][1])
    else:
      dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+l[i-1][1])
    dp[i][j]=max(dp[i-1][j],dp[i][j])
print(max(dp[n]))