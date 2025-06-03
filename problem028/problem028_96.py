n,m=map(int,input().split())
a=list(map(int,input().split()))

dp=[10**5]*(n+1)
dp[0]=0
dp[a[0]]=1

for i in range(n+1):
    for j in range(m):
        if i-a[j]>=0:
            dp[i]=min(dp[i],dp[i-a[j]]+1)
print(dp[-1])
