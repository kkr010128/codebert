

r, c, k = map(int, input().split())
v = [[0 for _ in range(c)] for _ in range(r)]
for _ in range(k):
    ri, ci, vi = map(int, input().split())
    v[ri - 1][ci - 1] = vi

dp = [[0, 0, 0, 0] for _ in range(c)]
for i in range(r):
    for j in range(c):
        dpj = dp[j][:]
        if j == 0:
            dp[j] = [max(dpj), max(dpj) + v[i][j], 0, 0]
        else:
            dp[j][0] = max(max(dpj), dp[j - 1][0])
            dp[j][1] = dp[j - 1][1]
            dp[j][2] = dp[j - 1][2]
            dp[j][3] = dp[j - 1][3]
            if v[i][j] > 0:
                dp[j][1] = max(dp[j][1], dp[j - 1][0] + v[i][j], max(dpj) + v[i][j])
                dp[j][2] = max(dp[j][2], dp[j - 1][1] + v[i][j])
                dp[j][3] = max(dp[j][3], dp[j - 1][2] + v[i][j])

print(max(dp[c - 1]))
