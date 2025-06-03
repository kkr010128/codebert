n,m = map(int,input().split())
D = list(map(int,input().split()))

INF = 10**5
dp = [INF for i in range(n+1)]
dp[0] = 0

for i in range(n+1):
    for d in D:
        if i+d <= n:
            dp[i+d] = min(dp[i+d],dp[i]+1)
print(dp[n])

