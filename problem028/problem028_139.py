N, M = map(int, input().split())

def solve(N,M):
    dp = [[float('inf')]*(N+1) for _ in range(M+1)]
    C = list(map(int, input().split()))
    dp[0][0] = 0
    for i in range(1,M+1):
        dp[i][0] = 0
        for j in range(1,N+1):
            dp[i][j] = dp[i-1][j]
            if j>=C[i-1]:
                dp[i][j] = min(dp[i][j],dp[i][j-C[i-1]]+1)
    ans = dp[M][N]
    return ans
print(solve(N,M))
