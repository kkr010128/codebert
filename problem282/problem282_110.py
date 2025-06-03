n,t=map(int,input().split())
dp=[[0]*(t+3001)for _ in range(n+1)]
ans=0
ab=[list(map(int,input().split()))for _ in range(n)]
ab.sort()
for i in range(1,n+1):
    a,b=ab[i-1]
    for j in range(t):
        dp[i][j]=max(dp[i-1][j],dp[i][j])
        dp[i][j+a]=dp[i-1][j]+b
        ans=max(dp[i][j],dp[i][j+a],ans)
print(ans)   