INF = 1145141919810364364334

n,m = map(int,input().split())
c = list(map(int,input().split()))
dp = [INF] * (n+1)
dp[0] = 0

for i in range(m):
    for j in range(n+1):
        if c[i] > j:
            continue
        else:
            dp[j] = min(dp[j] , dp[j-c[i]] + 1)
            
print(dp[n])
