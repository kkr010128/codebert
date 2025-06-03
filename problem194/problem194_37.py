H, W = map(int,input().split())
grid = [input() for _ in range(H)]
dp = [[float('inf')]*(W) for _ in range(H)]
dp[0][0] = 0 if grid[0][0] == '.' else 1
for i in range(H):
    for k in range(W):
        if i+1 < H:
            if grid[i][k] == '.' and grid[i+1][k] == '#':
                dp[i+1][k] = min(dp[i][k]+1,dp[i+1][k])
            else:
                dp[i+1][k] = min(dp[i][k],dp[i+1][k])
        if k+1 < W:
            if grid[i][k] == '.' and grid[i][k+1] == '#':
                dp[i][k+1] = min(dp[i][k]+1,dp[i][k+1])
            else:
                dp[i][k+1] = min(dp[i][k],dp[i][k+1])
print(dp[-1][-1])