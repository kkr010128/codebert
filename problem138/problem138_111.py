n,s=map(int,input().split())
a=list(map(int,input().split()))
mod=998244353

dp=[[0]*s for _ in range(n)]    
tmp=1
for i in range(n):
    if a[i]<=s:
        dp[i][a[i]-1]=tmp
    for j in range(s):
        if i>0:
            dp[i][j]+=dp[i-1][j]*2
            dp[i][j]%=mod
            if j+a[i]<s:
                dp[i][j+a[i]]+=dp[i-1][j]
                dp[i][j+a[i]]%=mod
    tmp*=2
    tmp%=mod
            
print(dp[n-1][s-1])