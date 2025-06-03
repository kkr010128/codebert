N,S=map(int,input().split())
*a,=map(int,input().split())
mod=998244353

dp=[[0]*(S+1) for _ in range(N+1)]
dp[0][0]=1

for i in range(N):
    for j in range(S+1):
        dp[i+1][j]=2*dp[i][j]

        if j>=a[i]:
            dp[i+1][j]+=dp[i][j-a[i]]
        
        dp[i+1][j]%=mod

print(dp[N][S])