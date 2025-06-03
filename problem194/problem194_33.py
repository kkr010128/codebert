H,W = (int(x) for x in input().split())
lines = [input() for i in range(H)]
dp = [[0] * W for _ in range(H)]
if lines[0][0] == "#":
    dp[0][0] = 1
q = r = dp[0][0]
for i in range(H):
    for j in range(W):
        if i == j == 0: continue
        if j > 0:
            q = dp[i][j-1]
            if lines[i][j] == "#" and lines[i][j-1] == ".":
                q = dp[i][j-1] + 1
        if i > 0:
            r = dp[i-1][j]
            if lines[i][j] == "#" and lines[i-1][j] == ".":
                r = dp[i-1][j] + 1
        if j == 0: 
            dp[i][j] = r
        elif i == 0:
            dp[i][j] = q
        else:
            dp[i][j] = min(q,r)
print(dp[H-1][W-1])