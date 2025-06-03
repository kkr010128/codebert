n, W = map(int, input().split())
ab = [tuple(map(int, input().split()))for _ in range(n)]
ab.sort()

dp = [[0]*W for _ in range(n+1)]
for i in range(1, n+1):
    w, v = ab[i-1]
    for j in range(W):
        if dp[i][j] < dp[i-1][j]:
            dp[i][j] = dp[i-1][j]

        if 0 <= j-w and dp[i][j] < dp[i-1][j-w]+v:
            dp[i][j] = dp[i-1][j-w]+v


ans = 0
for i in range(n):
    a, b = ab[i]
    if ans < dp[i][W-1]+b:
        ans = dp[i][W-1]+b
print(ans)
