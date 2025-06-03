n,m=map(int,raw_input().split())
c=map(int,raw_input().split())
dp=[[0]+[float('inf')]*n]+[[0]+[float('inf')]*n for i in xrange(m)]
for i in xrange(m):
    for j in xrange(n+1):
        if c[i]>j:
            dp[i+1][j]=dp[i][j]
        else:
            dp[i+1][j]=min(dp[i][j],dp[i+1][j-c[i]]+1)
print(dp[m][n])