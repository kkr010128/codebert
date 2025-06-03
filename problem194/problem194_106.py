h,w = map(int,input().split())
grid = []
for _ in range(h):
    grid.append(list(input()))
 
dp = [[0]*(w+1) for i in range(h+1)]
#dp[i][j] = i,jでの最小の操作回数
 
if grid[0][0] == '#':
    dp[0][0] += 1
 
for i in range(1,h):
    p = 0
    if grid[i][0] == '#' and grid[i-1][0] == '.':
        p += 1
    dp[i][0] = dp[i-1][0] + p
 
for i in range(1,w):
    p = 0
    if grid[0][i] == '#' and grid[0][i-1] == '.':
        p += 1
    dp[0][i] = dp[0][i-1] + p
 
for x in range(1,h):
    for y in range(1,w):
        a,b = 0,0
        if grid[x][y] == '#' and grid[x-1][y] == '.':
            a += 1
        if grid[x][y] == '#' and grid[x][y-1] == '.':
            b += 1
        dp[x][y] = min(dp[x-1][y] + a,dp[x][y-1] + b)
print(dp[h-1][w-1])
#print(dp)