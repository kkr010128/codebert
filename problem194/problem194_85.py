def check(i, j):
    if s[i][j] == '.':
        return 1
    else:
        return 0
H, W = map(int, input().split())
s = [input() for i in range(H)]
dp = [[0]*W for i in range(H)]
dp[0][0] = int(s[0][0] == '#')
for i in range(H):
    for j in range(W):
        if s[i][j] == '.':
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1])
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]
        else:
            if i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j]+check(i-1, j), dp[i][j-1]+check(i, j-1))
            elif i > 0:
                dp[i][j] = dp[i-1][j]+check(i-1, j)
            elif j > 0:
                dp[i][j] = dp[i][j-1]+check(i, j-1)
print(dp[H-1][W-1])
