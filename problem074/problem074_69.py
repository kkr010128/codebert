n,k=map(int,input().split())
lst=[list(map(int,input().split())) for i in range(k)]
mod=998244353

dp=[0]*(2*n+10)
dp[0]=1
dp[1]=-1
for i in range(n):
    for l,r in lst:
        dp[i+l]+=dp[i]
        dp[i+r+1]-=dp[i]
    
    dp[i+1]+=dp[i]
    dp[i+1]%=mod


print(dp[n-1])