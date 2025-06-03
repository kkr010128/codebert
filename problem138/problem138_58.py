mod=998244353
n,s=map(int,input().split())
ar=list(map(int,input().split()))
dp=[0 for y in range(s+1)]
dp[0]=1
for i in range(n):
    for j in range(s,-1,-1):
        if j+ar[i]<=s:
            dp[j+ar[i]]=(dp[j]+dp[j+ar[i]])%mod
        dp[j]=(dp[j]*2)%mod
print(dp[s])
