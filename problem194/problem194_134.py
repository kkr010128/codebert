h, w = map(int, input().split())
hw = [input() for _ in range(h)]
dp = [[1000]*w for _ in range(h)]
if hw[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0

for i in range(h):
    for j in range(w):
        if i > 0:
            if hw[i][j] == "#" and hw[i-1][j] == ".":
                dp[i][j] = min(dp[i][j], dp[i-1][j] + 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i-1][j])
        if j > 0:
            if hw[i][j] == "#" and hw[i][j-1] == ".":
                dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)
            else:
                dp[i][j] = min(dp[i][j], dp[i][j-1])

print(dp[h-1][w-1])