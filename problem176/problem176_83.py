n,k=map(int,input().split())
mod=10**9+7
ans=0
l=[0]*(k+1)
 
for i in range(k,0,-1):
    l[i]=pow(k//i,n,mod)
    for j in range(2*i,k+1,i):
        l[i]-=l[j]
        l[i]=pow(l[i],1,mod)
    ans+=l[i]*i
    ans=pow(ans,1,mod)
 
print(ans)