H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

dp = [[float('inf')]* W for _ in range(H)]

if s[0][0]=='#':
    dp[0][0]=1
else:
    dp[0][0]=0

for c in range(W):
    for r in range(H):
        if r > 0:
            count=0
            if s[r-1][c]=='.' and s[r][c]=='#':
                count = 1
            dp[r][c] = min(dp[r][c], dp[r-1][c]+count)
        if c > 0:
            count=0
            if s[r][c-1]=='.' and s[r][c]=='#':
                count = 1
            dp[r][c] = min(dp[r][c], dp[r][c-1]+count)
print(dp[H-1][W-1])