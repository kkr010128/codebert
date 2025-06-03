H, W, K = map(int, input().split())
A = [[0] * W for _ in range(H)]
for i in range(K):
    y, x, v = map(int, input().split())
    A[y - 1][x - 1] = v
dp = [[0] * 4 for i in range(W)]
pre = []
dp[0][1] = A[0][0]
for i in range(H):
    for j in range(W):
        if i:
            dp[j][0] = max(dp[j][0], max(pre[j]))
            dp[j][1] = max(dp[j][1], max(pre[j]) + A[i][j])
        for k in range(4):
            if j:
                if 0 < k:
                    dp[j][k] = max(dp[j][k], dp[j - 1][k - 1] + A[i][j])
                dp[j][k] = max(dp[j][k], dp[j - 1][k])
    pre = dp
ans = 0
for j in range(W):
    ans = max(ans, max(dp[j]))
print(ans)
