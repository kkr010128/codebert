n,t = map(int,input().split())
dishes = [[int(i) for i in input().split()] for _ in range(n)]
dishes.sort(key=lambda x: x[0])
dp = [[0]*(t+1) for _ in range(n+1)]

for i in range(n):
    a,b = dishes[i]
    for j in range(t+1):
        if j < t: dp[i+1][min(j+a,t)] = max(dp[i+1][min(j+a,t)],dp[i][j]+b)
        dp[i+1][j] = max(dp[i+1][j],dp[i][j])
print(dp[n][t])