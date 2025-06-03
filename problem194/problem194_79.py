H, W = map(int, input().split())
S = [[i for i in input()] for j in range(H)]
dp = [[0 for i in range(W)] for j in range(H)]
if S[0][0] == "#":
    dp[0][0] = 1

for i in range(1, H):
    if S[i-1][0] == "." and S[i][0] == "#":
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

for j in range(1, W):
    if S[0][j-1] == "." and S[0][j] == "#":
        dp[0][j] = dp[0][j-1] + 1
    else:
        dp[0][j] = dp[0][j-1]

for h in range(1, H):
    for w in range(1, W):

        if S[h][w] == "#":
            if S[h-1][w] == ".":
                c1 = dp[h-1][w] + 1
            else:
                c1 = dp[h-1][w]

            if S[h][w-1] == ".":
                c2 = dp[h][w-1] + 1
            else:
                c2 = dp[h][w-1]

            dp[h][w] = min(c1, c2)

        else:
            dp[h][w] = min(dp[h-1][w], dp[h][w-1])

print(dp[H-1][W-1])