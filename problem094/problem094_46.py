R, C, K = map(int, input().split())
grid = [[0]*C for _ in range(R)]
for i in range(K):
    r, c, v= map(int, input().split())
    grid[r-1][c-1] = v
dp = [[[0]*(C+1) for _ in range(R+1)] for _ in range(4)]
for i in range(1,R+1):
    for k in range(1,C+1):
        tmp = max(dp[0][i-1][k],dp[1][i-1][k],dp[2][i-1][k],dp[3][i-1][k])
        target = grid[i-1][k-1]
        dp[0][i][k] = max(dp[0][i][k-1],tmp)
        dp[1][i][k] = dp[1][i][k-1]
        dp[2][i][k] = dp[2][i][k-1]
        dp[3][i][k] = dp[3][i][k-1]
        if target != 0:
            dp[1][i][k] = max(dp[0][i][k-1]+target,tmp+target,dp[1][i][k])
            if dp[1][i][k-1] != 0:
                dp[2][i][k] = max(dp[1][i][k-1]+target,dp[2][i][k])
            if dp[2][i][k-1] != 0:
                dp[3][i][k] = max(dp[2][i][k-1]+target,dp[3][i][k])
print(max(dp[0][-1][-1],dp[1][-1][-1],dp[2][-1][-1],dp[3][-1][-1]))