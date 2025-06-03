R,C,K = map(int,input().split())
mat = {}
for _ in range(K):
  r,c,v = map(int,input().split())
  mat[(r,c)] = v

# dp[i][j][k] = i,jまでで、i列のものをk個取ったときのスコア
dp0 = [[0] * (C+1) for _ in range(R+1) ]
dp1 = [[0] * (C+1) for _ in range(R+1) ]
dp2 = [[0] * (C+1) for _ in range(R+1) ]
dp3 = [[0] * (C+1) for _ in range(R+1) ]

for i in range(1,R+1):
  for j in range(1,C+1):
    if (i,j) in mat:
      m = mat[(i,j)]
      # 左からの遷移
      dp1[i][j] = max(dp1[i][j-1], dp0[i][j-1]+m)
      dp2[i][j] = max(dp2[i][j-1], dp1[i][j-1]+m)
      dp3[i][j] = max(dp3[i][j-1], dp2[i][j-1]+m)
    else:
      dp1[i][j] = dp1[i][j-1]
      dp2[i][j] = dp2[i][j-1]
      dp3[i][j] = dp3[i][j-1]

    # 上からの遷移
    x = max(dp0[i-1][j], dp1[i-1][j], dp2[i-1][j], dp3[i-1][j])
    dp0[i][j] = max(dp0[i][j-1], x)
    if (i,j) in mat:
      m = mat[(i,j)]
      dp1[i][j] = max(dp1[i][j], x+m)
    else:
      dp1[i][j] = max(dp1[i][j], x)

print(max(dp0[R][C], dp1[R][C], dp2[R][C], dp3[R][C]))