from pprint import pprint
n,m=map(int,input().split())
c=list(map(int,input().split()))
dp=[[10**5]*(n+1) for _ in range(m+1)]
dp[0][0]=0
for i in range(m):
    for j in range(n+1):
        if c[i]>j:
            dp[i+1][j]=dp[i][j]
        else:
            dp[i+1][j]=min(dp[i][j],dp[i][j-c[i]]+1,dp[i+1][j-c[i]]+1)
# pprint(dp)
print(dp[m][n])
