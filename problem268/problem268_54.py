n=int(input())
*a,=map(int,input().split())

cnt=[0,0,0]
ans=1
mod=10**9+7

for aa in a:
    tmp=0
    for c in cnt:
        if aa==c:
            tmp+=1
    
    if tmp>0:
        for i in range(3):
            if cnt[i]==aa:
                cnt[i]+=1
                break
    
    ans*=tmp
    ans%=mod

print(ans)