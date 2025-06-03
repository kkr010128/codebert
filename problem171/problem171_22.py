import itertools
n = int(input())
l = list(map(int,input().split()))
li = [i for i in range(n)]

a = []
for i in range(n):
    a.append([l[i],i])
a.sort(reverse = True)

dp = [[-1]*(n+1) for i in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(i+1):
        le = j
        ri = i-le
        dp[le+1][ri] = max(dp[le+1][ri],dp[le][ri]+a[i][0]*abs(a[i][1]-le))
        dp[le][ri+1] = max(dp[le][ri+1],dp[le][ri]+a[i][0]*abs(n-1-a[i][1]-ri))

ans = 0
for i in range(n+1):
    j = n-i
    ans = max(ans,dp[i][j])
print(ans)