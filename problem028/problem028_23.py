n,m=[int(j) for j in input().split()]
c=[int(j) for j in input().split()]
dp=[10**18]*(n+1)
dp[0]=0
for i in c:
    for j in range(i,n+1):
        dp[j]=min(dp[j],dp[j-i]+1)
print(dp[-1])
