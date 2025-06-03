N=int(input())
l=list(map(int,input().split()))
ans=1
cnt=[0]*(N+1)
mod=10**9+7
cnt[0]=3
for i in l:
   ans=ans*cnt[i]%mod
   cnt[i]-=1
   cnt[i+1]+=1
print(ans)