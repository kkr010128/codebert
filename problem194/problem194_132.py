H, W = map(int, input().split())
S = [input() for _ in range(H)]

INF = 10 ** 18
dp = [[INF for _ in range(W)] for _ in range(H)]

if S[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(H):
    for j in range(W):
        if S[i][j] == ".":
            dp[i][j] = min(dp[i][j], dp[i - 1][j], dp[i][j - 1])
        else:
            dp[i][j] = min(dp[i][j],
                            dp[i - 1][j] if S[i - 1][j] == "#" else dp[i - 1][j] + 1,
                            dp[i][j - 1] if S[i][j - 1] == "#" else dp[i][j - 1] + 1)

print(dp[-1][-1])