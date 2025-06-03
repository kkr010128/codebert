R, C, K = map(int, input().split())
goods = [[0] * C for _ in range(R)]
for _ in range(K):
    r, c, v = map(int, input().split())
    goods[r-1][c-1] = v

dp = [[[0] * C for _ in range(4)] for _ in range(R)]
dp[0][1][0] = goods[0][0]
for i in range(R):
    for j in range(4):
        for k in range(C):
            if i < R - 1:
                dp[i+1][0][k] = max(dp[i+1][0][k], dp[i][j][k])
                dp[i+1][1][k] = max(dp[i+1][1][k], dp[i][j][k] + goods[i+1][k])
        
            if k < C - 1:
                dp[i][j][k+1] = max(dp[i][j][k+1], dp[i][j][k])
                if j < 3:
                    dp[i][j+1][k+1] = max(dp[i][j+1][k+1], dp[i][j][k] + goods[i][k+1])

res = 0
for i in range(4):
    res = max(res, dp[R-1][i][C-1])

print(res)