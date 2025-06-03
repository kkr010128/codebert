def solve(n,m,c):
    INF=50001
    dp=[INF]*(n+1)
    dp[0]=0
    for i in range(m):
        v=c[i]
        for j in range(v,n+1):
            if dp[j-v]!=INF:
                dp[j]=min(dp[j-v]+1,dp[j])
    return dp[n]


n,m=map(int,input().split())
c=tuple(map(int,input().split()))
print(solve(n,m,c))
