N, = map(int, input().split())
X = [(i+1, x) for i, x in enumerate(map(int, input().split()))]
dp = [[0]*(N+1) for _ in range(N+1)]
X = sorted(X, key=lambda x:x[1])[::-1]
for i in range(1, N+1):
    ai, a = X[i-1]
    dp[i][0] = dp[i-1][0]+a*abs(ai-(N-i+1))
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1]+a*abs(ai-j), dp[i-1][j]+a*abs(ai-(N-(i-j)+1)))
    dp[i][i] = dp[i-1][i-1]+a*abs(ai-i)
print(max(dp[-1]))
