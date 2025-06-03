h, w = map(int, input().split())
maze = [list(input()) for i in range(h)]

dp = [[0] * w for i in range(h)]
    
for i in range(h):
    for j in range(w):
        if i == j == 0:
            if maze[i][j] == "#":
                dp[i][j] += 1
                
        if i == 0 and j != 0:
            if maze[0][j] != maze[0][j - 1]:
                dp[0][j] = dp[0][j - 1] + 1
            else:
                dp[0][j] = dp[0][j - 1]
        
        if j == 0 and i != 0:
            if maze[i][0] != maze[i - 1][0]:
                dp[i][0] = dp[i - 1][0] + 1
            else:
                dp[i][0] = dp[i - 1][0]
        
        if i != 0 and j != 0:
            dp[i][j] = min(dp[i - 1][j] + (1 if maze[i][j] != maze[i - 1][j] else 0), dp[i][j - 1] + (1 if maze[i][j] != maze[i][j - 1] else 0))
        
        if i == h - 1 and j == w - 1:
            if maze[i][j] == "#":
                dp[i][j] += 1
                
ans = dp[h - 1][w - 1] // 2

print(ans)