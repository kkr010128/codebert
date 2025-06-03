def max2(x,y):
    return x if x > y else y

R, C, K = map(int, input().split())
V = [[0]*R for _ in range(C)]
for _ in range(K):
    r, c, v = map(int, input().split())
    V[c-1][r-1] = v

dp = [[0]*4 for _ in range(R)]
for j in range(R):
    if V[0][j] != 0:
        dp[j][1] = max2(dp[j - 1][1], dp[j - 1][0]) + V[0][j]
    if j != 0:
        dp[j][0] = max2(dp[j - 1][1], dp[j - 1][0])
for i in range(1,C):
    for j in range(R):
        v = V[i][j]
        if v != 0:
            if dp[j][2] != 0:
                dp[j][3] = max2(dp[j][2] + v, dp[j][3])
            if dp[j][1] != 0:
                dp[j][2] = max2(dp[j][1] + v, dp[j][2])
            dp[j][1] = max2(v, dp[j][1])
        if j != 0:
            if v != 0:
                dp[j][1] = max2(max(dp[j - 1][k] for k in range(4)) + v, dp[j][1])
            dp[j][0] = max2(max(dp[j - 1][k] for k in range(4)), dp[j][0])
print(max(dp[-1]))
