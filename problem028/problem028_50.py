n,m=map(int,input().split())
lst=list(map(int,input().split()))

dp=[[float("inf") for i in range(n+1)] for j in range(m+1)]

for i in range(m+1):
    dp[i][0]=0

for i in range(1,m+1):
    for j in range(1,n+1):
        if j-lst[i-1]>=0:
            dp[i][j]=min(dp[i-1][j],dp[i][j-lst[i-1]]+1)
        else : dp[i][j]=dp[i-1][j]

print(int(dp[m][n]))
