r,c,k = list(map(int, input().split()))
import copy
dp=[[[0]*4 for _ in range(c)] for _ in range(2)]


F = [[0]*c for _ in range(r)]

for _ in range(k):
  x,y,v = list(map(int, input().split()))
  x-=1
  y-=1
  F[x][y] = v
  
for nn in range(r):
  for j in range(c):
    i = 1
    val = F[nn][j]
  
      
    mxv = max(dp[i-1][j][0], dp[i-1][j][1], dp[i-1][j][2], dp[i-1][j][3])

    dp[i][j][3] = max(dp[i][j-1][3], dp[i][j-1][2] + val)
    dp[i][j][2] = max(dp[i][j-1][2], dp[i][j-1][1] + val)
    dp[i][j][1] = max(dp[i][j-1][1], dp[i][j-1][0] + val, mxv + val)
    dp[i][j][0] = mxv

  dp[0] = dp[1] 
  dp[1] = [[0]*4 for _ in range(c)]

best = 0


for k in range(4):
  best = max(best, dp[0][c-1][k])
    
print(best)
