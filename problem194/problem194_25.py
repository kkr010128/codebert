H,W = map(int,input().split())
grid = [[0] for _ in range(H)]
for i in range(H):
    grid[i] = input()
dp = [[float('inf')]*W for _ in range(H)]
if grid[0][0] == '.':
    dp[0][0] = 0
else:
    dp[0][0] = 1
for y in range(H):
    for x in range(W):
        if x > 0:
            if grid[y][x-1] == '.' and grid[y][x] == '#':
                dp[y][x] = min(dp[y][x],dp[y][x-1]+1)
            else:
                dp[y][x] = min(dp[y][x],dp[y][x-1])
        if y > 0:
            if grid[y-1][x] == '.' and grid[y][x] == '#':
                dp[y][x] = min(dp[y][x],dp[y-1][x]+1)
            else:
                dp[y][x] = min(dp[y][x],dp[y-1][x])
print(dp[-1][-1])