R, C, K = map(int, input().split())

V = [[0]*(C+1) for _ in range(R+1)]
for _ in range(K):
    r, c, v = map(int, input().split())
    V[r][c] = v

dp0 = [[0]*(C+1) for _ in range(R+1)]
dp1 = [[0]*(C+1) for _ in range(R+1)]
dp2 = [[0]*(C+1) for _ in range(R+1)]
dp3 = [[0]*(C+1) for _ in range(R+1)]
for i in range(R+1):
    for j in range(C+1):
        v = V[i][j]

        la = lb = lc = ld = 0
        if j > 0:
            la = dp0[i][j-1]
            lb = dp1[i][j-1]
            lc = dp2[i][j-1]
            ld = dp3[i][j-1]
            dp2[i][j] = max(dp2[i][j], lc, lb + v)
            dp3[i][j] = max(dp3[i][j], ld, lc + v)

        if i > 0:
            max_p = max(dp0[i-1][j], dp1[i-1][j], dp2[i-1][j], dp3[i-1][j])
            dp0[i][j] = max(dp0[i][j], max_p, la)
            dp1[i][j] = max(dp1[i][j], max_p + v, lb, la + v)

print(max(dp0[R][C], dp1[R][C], dp2[R][C], dp3[R][C]))
