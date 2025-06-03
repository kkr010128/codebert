H, W = map(int, input().split())
S = [input() for _ in range(H)]

INF = H + W

dp = [[INF] * W for _ in range(H)]

if S[0][0] == '#':
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(H):
    for j in range(W):
        if i - 1 >= 0:
            if S[i][j] == '#' and S[i-1][j] == '.':
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
        if j - 1 >= 0:
            if S[i][j] == '#' and S[i][j-1] == '.':
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[H-1][W-1])