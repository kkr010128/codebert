def resolve():
    mod=998244353
    n,k=map(int,input().split())
    d=[[],[]]
    for _ in range(k):
        l,r=map(int,input().split())
        d[0].append(l)
        d[1].append(r)
    dp=[0]*(n+1)
    a=[0]*(n+2)
    a[1]=dp[1]=1
    for i in range(2,n+1):
        for j in range(k):
            if i-d[0][j]>0:
                dp[i]=(dp[i]+a[i-d[0][j]]-a[max(i-d[1][j]-1,0)]+mod)%mod
        #print(dp[i])
        a[i]=(a[i-1]+dp[i])%mod
    print(dp[n])
resolve()