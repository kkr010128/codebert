n, m =map(int,input().split())
c = list(map(int,input().split()))

INF = 10**100
dp = [INF]*500000
dp[0] = 0

for i in range (n+1):
    for j in c:
        dp[i+j] = min(dp[i+j],dp[i]+1)
print(dp[n])
