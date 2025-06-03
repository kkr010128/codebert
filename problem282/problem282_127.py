n,t=map(int,input().split())
ab=[[0]*2 for i in range(n+1)]
for i in range(1,n+1):
  ab[i][0],ab[i][1]=map(int,input().split())
dp=[[0]*(t+3001) for i in range(n+1)]
ab.sort(key=lambda x:x[0])
for i in range(1,n+1):
  for j in range(t):
    dp[i][j]=max(dp[i][j],dp[i-1][j])
    dp[i][j+ab[i][0]]=max(dp[i][j+ab[i][0]],dp[i-1][j]+ab[i][1])
ans=0
for i in range(n+1):
  ans=max(ans,max(dp[i]))
print(ans)