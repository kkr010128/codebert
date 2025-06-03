n=int(input())
a=list(map(int,input().split()))
for i in range(n):
  a[i]=[a[i],i]
a.sort()
a.reverse()
dp=[[0 for i in range(n+1)] for j in range(n+1)]
for i in range(n):
  for j in range(n):
    if i+j<=n-1:
      dp[i+1][j]=max(dp[i+1][j],dp[i][j]+a[i+j][0]*abs(a[i+j][1]-i))
      dp[i][j+1]=max(dp[i][j+1],dp[i][j]+a[i+j][0]*abs(a[i+j][1]-(n-j-1)))
ans=[]
for i in range(n):
  ans.append(dp[i][n-i])
print(max(ans))