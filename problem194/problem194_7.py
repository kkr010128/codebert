h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
dp = [[float("inf")] * w for i in range(h)]
dp[0][0] = 1 if s[0][0] == "#" else 0
d = [(-1, 0), (0, -1)]
for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            pass
        else:
            m = float("inf")
            for k in d:
                x = i + k[0]
                y = j + k[1]
                if 0 <= x < h and 0 <= y < w:
                    if s[i][j] == "#" and s[x][y] == ".":
                        m = dp[x][y] + 1
                    else:
                        m = dp[x][y]
                dp[i][j] = min(dp[i][j], m)
print(dp[h - 1][w - 1])