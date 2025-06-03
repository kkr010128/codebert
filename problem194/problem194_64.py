import numpy as np
h,w=map(int,input().split())
s=[input() for _ in range(h)]
dp=np.zeros((h,w),np.int64)
if s[0][0]=='#':
      dp[0,0]=1
for i in range(h):
  for j in range(w):
    if (i,j)==(0,0):
      continue
    elif i==0:
      if s[i][j-1]=='.' and s[i][j]=='#':
        dp[i,j]=dp[i,j-1]+1
      else:
        dp[i,j]=dp[i,j-1]
    elif j==0:
      if s[i-1][j]=='.' and s[i][j]=='#':
        dp[i,j]=dp[i-1,j]+1
      else:
        dp[i,j]=dp[i-1,j]
    else:
      dp[i,j]=min(dp[i,j-1]+1 if s[i][j-1]=='.' and s[i][j]=='#' else dp[i,j-1],dp[i-1,j]+1 if s[i-1][j]=='.' and s[i][j]=='#' else dp[i-1,j])
print(dp[-1,-1])
#print(dp)