import sys
input = sys.stdin.readline

H, W = map(int, input().split())
s = [input().rstrip() for _ in range(H)]

dp = [[1000]*W for _ in range(H)]

if s[0][0] == '#': dp[0][0] = 1
else: dp[0][0] = 0

for j in range(W):
    for i in range(H):
        if i <= H - 2:

            if s[i][j] == '.' and s[i+1][j] == '#':
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            else: dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j <= W - 2:

            if s[i][j] == '.' and s[i][j+1] == '#':
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            else: dp[i][j+1] = min(dp[i][j+1], dp[i][j])


print(dp[H-1][W-1])