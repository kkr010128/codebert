mod=pow(10,9)+7
n,k=map(int,input().split())
a=[0 for i in range(100000+1)]
ans=0
for i in range(k,0,-1):
    a[i]=k//i
    a[i]=pow(a[i],n,mod)
    j=2*i
    while j<=k:
        a[i]=(a[i]-a[j]+mod)%mod
        j += i
    ans=(ans+a[i]*i)%mod
print(ans)