n,k=map(int,input().split())
l=[0]*k
r=[0]*k
mod=998244353
for i in range(k):
    l[i],r[i]=map(int,input().split())
dp=[0]*n
sum_dp=[0]*n
dp[0]=1
sum_dp[0]=1
for i in range(1,n):
    for j in range(k):
        if (i-l[j]>=0):
            dp[i]+=sum_dp[i-l[j]]
            dp[i]%=mod
        if (i-r[j]-1>=0):
            dp[i]-=sum_dp[i-r[j]-1]
            dp[i]+=mod
            dp[i]%=mod
    sum_dp[i]=sum_dp[i-1]+dp[i]
    sum_dp[i]%=mod
print(dp[n-1])