INF = 10**18

N,M = map(int,input().split())
C = list(map(int,input().split()))

dp = [INF for _ in range(N+1)]
dp[0] = 0

for i in range(M):
    for j in range(N+1):
        if j-C[i] >= 0:
            dp[j] = min(dp[j],dp[j-C[i]]+1)

print(dp[N])
