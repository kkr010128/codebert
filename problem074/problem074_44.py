n,k=map(int,input().split())
lr=[list(map(int,input().split())) for _ in range(k)]

mod=998244353

dp=[0]*(n+1)
csum=[0]*(n+2)
dp[0]=1

for i in range(n):
    for j in range(k):
        l,r=lr[j]
        dp[i]+=csum[max(i+1-l,0)]-csum[max(i-r,0)]
        dp[i]%=mod
    csum[i+1]+=dp[i]+csum[i]
    csum[i+1]%=mod

print(dp[n-1])