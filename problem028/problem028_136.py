N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [[1<<60]*(N+1) for _ in range(M+1)]
dp[0][0] = 0

for i in range(M):
    for j in range(N+1):
        if A[i] <= j:
            dp[i+1][j] = min(dp[i][j], dp[i+1][j-A[i]] + 1)
        else:
            dp[i + 1][j] = dp[i][j]
print(dp[M][N])
