R, C, K = map(int, input().split())
dp0 = [[0]*(R+1) for _ in range(C+1)]
dp1 = [[0]*(R+1) for _ in range(C+1)]
dp2 = [[0]*(R+1) for _ in range(C+1)]
dp3 = [[0]*(R+1) for _ in range(C+1)]
val = [[0]*(R+1) for _ in range(C+1)]

for i in range(K):
    r, c, v = map(int, input().split())
    val[c][r] = v

for i in range(1, C+1):
    for j in range(1, R+1):
        temp = max(dp0[i][j-1], dp1[i][j-1])
        temp = max(dp2[i][j-1], temp)
        temp = max(dp3[i][j-1], temp)
        dp0[i][j] = max(temp, dp0[i-1][j])
        if val[i][j]>0:
            dp1[i][j] = max(dp0[i-1][j]+val[i][j], dp1[i-1][j],temp+val[i][j])
            dp2[i][j] = max(dp1[i-1][j]+val[i][j], dp2[i-1][j])
            dp3[i][j] = max(dp2[i-1][j]+val[i][j], dp3[i-1][j])
        else:
            dp1[i][j] = dp1[i-1][j]
            dp2[i][j] = dp2[i-1][j]
            dp3[i][j] = dp3[i-1][j]

print(max(dp0[-1][-1], dp1[-1][-1], dp2[-1][-1],dp3[-1][-1]))