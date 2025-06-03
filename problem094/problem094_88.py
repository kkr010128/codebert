import sys
input = sys.stdin.buffer.readline

R, C, K = map(int, input().split())
G = [[None for j in range(C)] for i in range(R)]

for _ in range(K):
    r, c, v = map(int, input().split())
    G[r - 1][c - 1] = v

dp = [[0, 0, 0, 0] for _ in range(C)]

for i in range(R):
    for j in range(C):
        if G[i][j] is not None:
            dp[j][0], dp[j][1] = max(dp[j]), max(dp[j]) + G[i][j]
            dp[j][2], dp[j][3] = 0, 0
        else:
            dp[j][0] = max(dp[j])
            dp[j][1], dp[j][2], dp[j][3] = 0, 0, 0
    for j in range(1, C):
        if G[i][j] is not None:
            dp[j][0] = max(dp[j - 1][0], dp[j][0])
            dp[j][1] = max(dp[j - 1][1], dp[j - 1][0] + G[i][j], dp[j][1])
            if dp[j - 1][1] != 0:
                dp[j][2] = max(dp[j - 1][2], dp[j - 1][1] + G[i][j], dp[j][2])
            if dp[j - 1][2] != 0:
                dp[j][3] = max(dp[j - 1][3], dp[j - 1][2] + G[i][j], dp[j][3])
        else:
            dp[j][0] = max(dp[j - 1][0], dp[j][0])
            dp[j][1] = max(dp[j - 1][1], dp[j][1])
            dp[j][2] = max(dp[j - 1][2], dp[j][2])
            dp[j][3] = max(dp[j - 1][3], dp[j][3])

print(max(dp[-1]))