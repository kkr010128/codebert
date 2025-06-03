#AGC043-A
h,w = map(int,input().split())
grid = [input() for _ in range(h)]

dp = [[1000]*w for _ in range(h)]
dp[0][0] = 1 if grid[0][0] == "#" else 0
#進む前の相対位置
d = [(-1, 0), (0, -1)]

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            pass
        else:
            tmp = 1000
            for k in d:
                bx,by = j+k[0],i+k[1]
                if 0 <= bx <w and 0 <= by < h:
                    if grid[i][j] == '#' and grid[by][bx] == '.':
                        tmp = dp[by][bx] + 1
                    else:
                        tmp = dp[by][bx]
                dp[i][j] = min(dp[i][j],tmp)
                
print(dp[-1][-1])