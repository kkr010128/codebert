h,w = map(int,input().split())
s = [input() for _ in range(h)]
dp = [[float('inf')]*w for i in range(h)]
dp[0][0] = 1 if s[0][0]=='#' else 0
for x in range(h):
    for y in range(w):
        if x+1<h:
            a = 1 if s[x][y]=='.' and s[x+1][y]=='#' else 0
            dp[x+1][y] = min(dp[x][y]+a,dp[x+1][y])
        if y+1<w:
            a = 1 if s[x][y]=='.' and s[x][y+1]=='#' else 0
            dp[x][y+1] = min(dp[x][y]+a,dp[x][y+1])

print(dp[h-1][w-1])

