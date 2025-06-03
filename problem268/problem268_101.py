n=int(input())
a=list(map(int,input().split()))
cnt=[0]*(max(a)+4)
cnt[0]=3
mod=10**9+7
ans=1
for i in range(n):
    ans*=cnt[a[i]]
    ans%=mod
    cnt[a[i]]-=1
    cnt[a[i]+1]+=1
print(ans)
