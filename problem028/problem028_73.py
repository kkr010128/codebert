n,m=map(int,input().split())
C=list(map(int,input().split()))

dp=[[float('inf')]*(n+1) for i in range(m+1)]
for i in range(m+1):
    dp[i][0]=0

for i in range(1,m+1):
    c=C[i-1]
    for j in range(1,n+1):
        dp[i][j]=dp[i-1][j]
        if j>=c:
            dp[i][j]=min(dp[i][j],dp[i-1][j-c]+1,dp[i][j-c]+1)

print(dp[m][n])
        
