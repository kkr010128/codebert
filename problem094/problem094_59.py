import sys

R, C, K = map(int, sys.stdin.readline().split())

grid = [[0 for _ in range(C)] for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, sys.stdin.readline().split())
    grid[r-1][c-1] = v

# r行目、c列目にいるときに、その行でアイテムをi個取得している場合の最大価値
dp0 = [[0 for _ in range(C+1)] for _ in range(R+1)]
dp1 = [[0 for _ in range(C+1)] for _ in range(R+1)]
dp2 = [[0 for _ in range(C+1)] for _ in range(R+1)]
dp3 = [[0 for _ in range(C+1)] for _ in range(R+1)]
# print(dp)
for r in range(R):
    for c in range(C):
        # 取らない
        dp0[r+1][c] = max((dp0[r][c], dp1[r][c], dp2[r][c], dp3[r][c]))
        dp1[r][c+1] = max(dp1[r][c], dp1[r][c])
        dp2[r][c+1] = max(dp2[r][c], dp2[r][c])
        dp3[r][c+1] = max(dp3[r][c], dp3[r][c])

        if grid[r][c] == 0:
            continue
        # 取る
        dp0[r+1][c] = max(dp0[r][c] + grid[r][c], dp0[r+1][c])
        dp0[r+1][c] = max(dp1[r][c] + grid[r][c], dp0[r+1][c])
        dp0[r+1][c] = max(dp2[r][c] + grid[r][c], dp0[r+1][c])

        dp1[r][c+1] = max(dp0[r][c] + grid[r][c], dp1[r][c+1])
        dp2[r][c+1] = max(dp1[r][c] + grid[r][c], dp2[r][c+1])
        dp3[r][c+1] = max(dp2[r][c] + grid[r][c], dp3[r][c+1])

# print(dp0)
# print(dp1)
# print(dp2)
# print(dp3)
# print(max((dp0[R][C], dp1[R][C], dp2[R][C], dp3[R][C])))
print(dp0[R][C-1])