#!/usr/bin/env python3
r, c, k = map(int, input().split())
items = [[0] * (c+1) for _ in range(r+1)]
for _ in range(k):
    R, C, V = map(int, input().split())
    items[R][C] = V

dp1 = [[0] * (c+1) for _ in range(r+1)]
dp2 = [[0] * (c+1) for _ in range(r+1)]
dp3 = [[0] * (c+1) for _ in range(r+1)]

for i in range(1, r+1):
    for j in range(1, c+1):
        v = items[i][j]
        dp1[i][j] = max(dp1[i][j-1], dp1[i-1][j] + v, dp2[i-1][j] + v, dp3[i-1][j] + v)
        dp2[i][j] = max(dp2[i][j-1], dp1[i][j-1] + v)
        dp3[i][j] = max(dp3[i][j-1], dp2[i][j-1] + v)

ans = max(dp1[r][c], dp2[r][c], dp3[r][c])
print(ans)