n = int(input())
buf = list(map(int,input().split()))
a = []
for i in range(n):
    a.append([buf[i],i])
a = sorted(a,reverse=True)

dp = [[0]*(n+1) for i in range(n+1)]
for i in range(n):
    for j in range(n-i):
        cur = i+j
        temp1 = dp[i][j]+a[cur][0]*abs(n-1-a[cur][1]-j)
        temp2 = dp[i][j]+a[cur][0]*abs(a[cur][1]-i)
        dp[i+1][j] = max(dp[i+1][j],temp2)
        dp[i][j+1] = max(dp[i][j+1],temp1)

print(max([max(i) for i in dp]))