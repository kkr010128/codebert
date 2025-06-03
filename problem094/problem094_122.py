import sys
 
read = sys.stdin.read
readline = sys.stdin.readline

R,C,K = map(int,readline().split())
board = [[0]*C for _ in range(R)]
for _ in range(K):
  r,c,v = map(int,readline().split())
  board[r-1][c-1] = v

dp0 = [[0]*C for _ in range(R)]
dp1 = [[0]*C for _ in range(R)]
dp2 = [[0]*C for _ in range(R)]
dp3 = [[0]*C for _ in range(R)]

for i in range(R):
  for j in range(C):
    if dp1[i][j] < dp0[i][j]+board[i][j]:
      dp1[i][j] = dp0[i][j]+board[i][j]
    if j>0:
      if dp0[i][j] < dp0[i][j-1]:
        dp0[i][j] = dp0[i][j-1]
      if dp1[i][j] < dp1[i][j-1]:
        dp1[i][j] = dp1[i][j-1]
      if dp2[i][j] < dp2[i][j-1]:
        dp2[i][j] = dp2[i][j-1]
      if dp3[i][j] < dp3[i][j-1]:
        dp3[i][j] = dp3[i][j-1]
      if dp1[i][j] < dp0[i][j-1]+board[i][j]:
        dp1[i][j] = dp0[i][j-1]+board[i][j]
      if dp2[i][j] < dp1[i][j-1]+board[i][j]:
        dp2[i][j] = dp1[i][j-1]+board[i][j]
      if dp3[i][j] < dp2[i][j-1]+board[i][j]:
        dp3[i][j] = dp2[i][j-1]+board[i][j]
    if i>0:
      if dp0[i][j] < dp0[i-1][j]:
        dp0[i][j] = dp0[i-1][j]
      if dp0[i][j] < dp1[i-1][j]:
        dp0[i][j] = dp1[i-1][j]
      if dp0[i][j] < dp2[i-1][j]:
        dp0[i][j] = dp2[i-1][j]
      if dp0[i][j] < dp3[i-1][j]:
        dp0[i][j] = dp3[i-1][j]
      if dp1[i][j] < dp0[i-1][j]+board[i][j]:
        dp1[i][j] = dp0[i-1][j]+board[i][j]
      if dp1[i][j] < dp1[i-1][j]+board[i][j]:
        dp1[i][j] = dp1[i-1][j]+board[i][j]
      if dp1[i][j] < dp2[i-1][j]+board[i][j]:
        dp1[i][j] = dp2[i-1][j]+board[i][j]
      if dp1[i][j] < dp3[i-1][j]+board[i][j]:
        dp1[i][j] = dp3[i-1][j]+board[i][j]
print(max(dp0[-1][-1],dp1[-1][-1],dp2[-1][-1],dp3[-1][-1]))