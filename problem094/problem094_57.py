import sys
input = sys.stdin.readline
H, W, K = map(int, input().split())
mat = [[0]*W for i in range(H)]

for i in range(K):
    r, c, v = map(int, input().split())
    r, c = r-1, c-1
    mat[r][c] = v

dp0 = [[-1 for i in range(W)] for i in range(H)]
dp1 = [[-1 for i in range(W)] for i in range(H)]
dp2 = [[-1 for i in range(W)] for i in range(H)]
dp3 = [[-1 for i in range(W)] for i in range(H)]

dp0[0][0] = 0
if mat[0][0] != 0:
    dp1[0][0] = mat[0][0]

for i in range(H):
    for j in range(W):
        m = max(dp0[i][j], dp1[i][j], dp2[i][j], dp3[i][j])
        if i+1 < H:
            dp1[i+1][j] = max(dp1[i+1][j], m+mat[i+1][j])
            dp0[i+1][j] = max(dp0[i+1][j], m)
        if j+1 < W:
            dp0[i][j+1] = 0
            dp1[i][j+1] = max(dp1[i][j+1], dp1[i][j], dp0[i][j]+mat[i][j+1])
            dp2[i][j+1] = max(dp2[i][j+1], dp2[i][j], dp1[i][j]+mat[i][j+1])
            dp3[i][j+1] = max(dp3[i][j+1], dp3[i][j], dp2[i][j]+mat[i][j+1])

print(max(dp0[H-1][W-1], dp1[H-1][W-1], dp2[H-1][W-1], dp3[H-1][W-1]))
