n,k=map(int,input().split())
ans=0
xs=[0]*k
mod=10**9+7
for i in range(k-1,-1,-1):
    a=i+1
    xs[i]=pow(k//a,n,mod)
    for j in range(2,k+1):
        if a*j>k:
            break
        xs[i]-=xs[a*j-1]
        xs[i]=(xs[i]+mod)%mod

for i in range(k):
    a=i+1
    ans+=a*xs[i]
    ans%=mod
print(ans)