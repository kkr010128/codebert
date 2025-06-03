h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]
dp = [[0] * w for _ in range(h)]
if s[0][0] == "#":
    dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if i == j == 0:
            continue
        elif i == 0:
            dp[i][j] = dp[i][j - 1]
            if not s[i][j] == s[i][j - 1]:
                dp[i][j] += 1
        elif j == 0:
            dp[i][j] = dp[i - 1][j]
            if not s[i][j] == s[i - 1][j]:
                dp[i][j] += 1
        else:
            a, b = dp[i][j - 1], dp[i - 1][j]
            if not s[i][j] == s[i][j - 1]:
                a += 1
            if not s[i][j] == s[i - 1][j]:
                b += 1
            dp[i][j] = min(a, b)
print((dp[h - 1][w - 1] - dp[0][0] + [s[0][0], s[h - 1][w - 1]].count("#")) // 2)