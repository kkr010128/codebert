H, N = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

inf = 10 ** 9 + 7
dp = [[inf] * (H + 1) for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(H + 1):
        dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        dp[i + 1][min(j + X[i][0], H)] = min(dp[i + 1][min(j + X[i][0], H)],
                                             dp[i][j] + X[i][1],
                                             dp[i + 1][j] + X[i][1])
        
print(dp[-1][-1])
