n,k=[int(x) for x in input().split()]
ans=0
l=[0]*(k+1)
i=k
mod=1000000007
while i>0:
    l[i]=pow(k//i,n,mod)
    j=2*i
    while j<=k:
        l[i]=(l[i]-l[j]+mod)%mod
        j+=i
    i-=1
for i in range(1,k+1):
    ans+=(l[i]*i)%mod
print(ans%mod)
