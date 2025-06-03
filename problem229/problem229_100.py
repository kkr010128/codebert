h,n = map(int,input().split())
Mag = []
for i in range(n):
    AB = list(map(int,input().split()))
    Mag.append(AB)
dp = [[float("inf")]*(h+1) for i in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(h+1):
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        dp[i+1][min(j+Mag[i][0],h)] = min(dp[i+1][min(j+Mag[i][0],h)],dp[i+1][j]+Mag[i][1])
        
print(dp[n][h])