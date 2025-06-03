
N, T = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * (T + 1) for _ in range(N + 1)]
dp[0][0] = 0
X.sort()

for i in range(N):
    for j in range(T + 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if dp[i][j] >= 0 and j < T:
            dp[i + 1][min(T, j + X[i][0])] = max(dp[i + 1][min(T, j + X[i][0])],
                                                 dp[i][j] + X[i][1])

print(max(dp[-1]))
