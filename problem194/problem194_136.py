h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

# ある経路をきめる.
# そのとき(白マスから黒マスに移動する回数)＝(その経路がいい経路にするための操作回数）
dp = [[float("inf")]*w for _ in range(h)]
if s[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0
# dp[i][j]は00からijに行くときに白マスから黒マスに移動する回数の最小値
for i in range(h):
    for j in range(w):
        if i+1 < h:
            count1 = dp[i][j]
            if s[i][j] == "." and s[i+1][j] == "#":
                count1 += 1
            dp[i+1][j] = min(dp[i+1][j], count1)
        if j+1 < w:
            count2 = dp[i][j]
            if s[i][j] == "." and s[i][j+1] == "#":
                count2 += 1
            dp[i][j+1] = min(dp[i][j+1], count2)
print(dp[h-1][w-1])
