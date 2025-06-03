R, C, K = map(int, input().split())

items = [[0] * C for _ in range(R)]
for i in range(K):
    r, c, v = map(int, input().split())
    items[r-1][c-1] = v

dp = [[0] * 4 for _ in range(C)]

for i in range(R):
    dp2 = [[0] * 4 for _ in range(C)]
    for j in range(C):
        if j != 0:
            dp2[j] = dp2[j-1][:]

        dp2[j][0] = max(dp2[j][0], max(dp[j]))

        for k in range(3, 0, -1):
            dp2[j][k] = max(dp2[j][k], dp2[j][k-1] + items[i][j])

    dp = dp2

print(max(dp[-1]))
