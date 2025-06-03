n=int(input())
a=list(map(int,input().split()))
mod=10**9+7
ans=0
for i in range(61):
    count0=0
    count1=0
    for j in a:
        if not (j>>i & 1):
            count0+=1
        if j>>i & 1:
            count1+=1
    ans+=((count0*count1)*(2**i))%mod
    
print(ans%mod)