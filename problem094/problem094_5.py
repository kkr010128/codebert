import sys
input = sys.stdin.buffer.readline
H, W, K = map(int, input().split())
B = {}
for _ in range(K):
    r, c, v = map(int, input().split())
    B[(r, c)] = v

dp = [[0]*(W+1) for _ in range(4)]

for i in range(1, H+1):
    for j in range(1, W+1):
        if (i, j) in B:
            v = B[(i, j)]
            dp[0][j] = max(dp[0][j-1], dp[0][j], dp[1][j], dp[2][j], dp[3][j])
            dp[1][j] = max(dp[1][j-1], dp[0][j]+v)
            dp[2][j] = max(dp[2][j-1], dp[1][j-1]+v)
            dp[3][j] = max(dp[3][j-1], dp[2][j-1]+v)
        else:
            dp[0][j] = max(dp[0][j-1], dp[0][j], dp[1][j], dp[2][j], dp[3][j])
            dp[1][j] = dp[1][j-1]
            dp[2][j] = dp[2][j-1]
            dp[3][j] = dp[3][j-1]

print(max(dp[i][-1] for i in range(4)))
