n,m=map(int,input().split())
c=list(map(int,input().split()))
dp=[10**5 for i in range(50001)]
dp[0]=0
dp[1]=1
for i in range(1,n+1):
    for j in range(m):
        if i>=c[j]:
            dp[i]=min(dp[i-c[j]]+1,dp[i])
print(dp[n])
