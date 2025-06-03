mod=10**9+7
n,k=map(int,input().split())
l=[0]*(k+1)
for i in range(k):
    num=(k-i)
    if k//num==1:
        l[num]=1
    else:
        ret=pow(k//num,n,mod)
        for j in range(2,k//num+1):
            ret-=l[num*j]
            ret%=mod
        l[num]=(ret)%mod
ans=0
for i in range(k+1):
    ans+=(l[i]*i)%mod
print(ans%mod)
