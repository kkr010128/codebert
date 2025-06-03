H,W,*L = open(0).read().split()
H,W = map(int, (H,W))
dp = [[0]*W for i in range(H)]
for i in range(1,H):
  if L[i][0]!=L[i-1][0]:
    dp[i][0] = dp[i-1][0]+1
  else:
    dp[i][0] = dp[i-1][0]
for j in range(1,W):
  if L[0][j]!=L[0][j-1]:
    dp[0][j] = dp[0][j-1]+1
  else:
    dp[0][j] = dp[0][j-1]
for i in range(1,H):
  for j in range(1,W):
    if L[i][j]!=L[i-1][j] and L[i][j]!=L[i][j-1]:
      dp[i][j] = min(dp[i-1][j],dp[i][j-1])+1
    elif L[i][j]!=L[i-1][j]:
      dp[i][j] = min(dp[i-1][j]+1,dp[i][j-1])
    elif L[i][j]!=L[i][j-1]:
      dp[i][j] = min(dp[i-1][j],dp[i][j-1]+1)
    else:
      dp[i][j] = min(dp[i-1][j],dp[i][j-1])
if L[0][0]=='.':
  ans = (dp[H-1][W-1]+1)//2
else:
  ans = (dp[H-1][W-1]+2)//2
print(ans)