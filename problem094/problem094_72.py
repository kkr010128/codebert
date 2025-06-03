import sys
import copy
R, C, K = map(int, input().split())
item = [[0] * (C + 1) for _ in range(R + 1)]  # dp配列と合わせるために, 0行目, 0列目を追加している.
for s in sys.stdin.readlines():
    r, c, v = map(int, s.split())
    r -= 1
    c -= 1
    item[r][c] = v
    
dp0 = [[0] * (C+1) for r in range(R+1)]
dp1 = [[0] * (C+1) for r in range(R+1)]
dp2 = [[0] * (C+1) for r in range(R+1)]
dp3 = [[0] * (C+1) for r in range(R+1)]
 
for r in range(R):
   for c in range(C):
      dp3[r][c] = max(dp3[r][c], dp2[r][c] + item[r][c])
      dp2[r][c] = max(dp2[r][c], dp1[r][c] + item[r][c])
      dp1[r][c] = max(dp1[r][c], dp0[r][c] + item[r][c])
      dp1[r][c+1] = max(dp1[r][c], dp1[r][c+1])
      dp2[r][c+1] = max(dp2[r][c], dp2[r][c+1])
      dp3[r][c+1] = max(dp3[r][c], dp3[r][c+1])
      dp0[r+1][c] = max(dp0[r+1][c], dp1[r][c])
      dp0[r+1][c] = max(dp0[r+1][c], dp2[r][c])
      dp0[r+1][c] = max(dp0[r+1][c], dp3[r][c])
ans = max(dp0[R-1][C-1], dp1[R-1][C-1])
ans = max(ans, dp3[R-1][C-1])
ans = max(ans, dp2[R-1][C-1])
print(ans)