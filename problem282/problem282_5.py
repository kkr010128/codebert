ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,t = mi()
data = []
for i in range(n):
    data.append(li())

data.sort()

dp = [[0]*t for i in range(n+1)]
for i in range(n):
    for k in range(t):
        dp[i+1][k] = max(dp[i+1][k],dp[i][k])
        if k + data[i][0] <= t-1:
            dp[i+1][k+data[i][0]] = max(dp[i+1][k+data[i][0]],dp[i][k] + data[i][1])
ans = 0
for i in range(n):
    ans = max(ans,dp[i][t-1] + data[i][1])
print(ans)




