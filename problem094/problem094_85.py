r, c, k = map(int, input().split())

atlas = [[0]*c for i in range(r)]
dp = [[[0]*c for i in range(r)] for j in range(4)]

for i in range(k):
  x, y, v = map(int, input().split())
  atlas[x-1][y-1] = v
  
def max_sum(r, c, atlas):
  global dp

  if atlas[0][0] > 0:
    dp[1][0][0] = atlas[0][0]
    
  for i in range(r):
    for j in range(c):
      for h in range(4):
        
        if j+1 < c:
          dp[h][i][j+1] = max(dp[h][i][j+1], dp[h][i][j])
          if atlas[i][j+1] > 0 and h < 3:
            dp[h+1][i][j+1] = max(dp[h+1][i][j+1], dp[h][i][j]+atlas[i][j+1])
            
        if i+1 < r:
          dp[0][i+1][j] = max(dp[0][i+1][j], dp[h][i][j])
          if atlas[i+1][j] > 0:
            dp[1][i+1][j] = max(dp[1][i+1][j], dp[h][i][j]+atlas[i+1][j])
          
            
  return dp

max_sum(r, c, atlas)

ans = 0
for i in range(4):
  ans = max(ans, dp[i][r-1][c-1])
  
print(ans)