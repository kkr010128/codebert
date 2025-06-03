r,c,k = map(int,input().split())
v = [[0]*(c+1) for i in range(r+1)]
for i in range(k):
  x,y,z = map(int,input().split())
  v[x][y] = z
dp = [[0]*4 for i in range(r+1)]
for i in range(1,c+1):
  for j in range(1,r+1):
    if v[j][i]>0:
      dp[j][3] = max(dp[j][2]+v[j][i],dp[j][3])
      dp[j][2] = max(dp[j][1]+v[j][i],dp[j][2])
      dp[j][1] = max(dp[j][0]+v[j][i],dp[j][1],max(dp[j-1])+v[j][i])
    dp[j][0] = max(dp[j][0],max(dp[j-1]))
print(max(dp[r]))