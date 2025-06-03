h, w = map(int, input().split())
 
mat = [[] for _ in range(h)]
 
for i in range(h):
    mat[i] = input()
 
dp = [[float("inf")] * w for _ in range(h)]
 
if mat[0][0] == "#":
    dp[0][0] = 1
else:
    dp[0][0] = 0
 
for i in range(h):
    for j in range(w):
 
        if mat[i][j - 1] != mat[i][j]:
            left = dp[i][j - 1] + 1
        else:
            left = dp[i][j - 1]
 
        if mat[i - 1][j] != mat[i][j]:
            top = dp[i - 1][j] + 1
        else:
            top = dp[i - 1][j]
 
        dp[i][j] = min(dp[i][j], left, top)
 
print((dp[h - 1][w - 1] + 1) // 2)