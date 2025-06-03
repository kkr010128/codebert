h, w = map(int, input().split())
L = [str(input()) for _ in range(h)]
dp = [[float('inf')] * w for _ in range(h)]
dp[0][0] = 1 if L[0][0] =='#' else 0
for i in range(h):
    for j in range(w):
        if L[i][j] == '.':
            if i < h - 1:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] if L[i+1][j] == '.' else dp[i][j] + 1)
            if j < w - 1:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] if L[i][j+1] == '.' else dp[i][j] + 1)
        else:
            if i < h - 1:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j < w - 1:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j])
print(dp[h-1][w-1])
