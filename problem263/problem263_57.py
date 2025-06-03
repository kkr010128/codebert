n=int(input())
A=[int(i) for i in input().split()]
mod=10**9+7

ans=0
cnt=[0 for i in range(61)]

for i in range(n):
    now=A[i]
    bek=1
    for q in range(61):
        if now&1==0:
            ans+=cnt[q]*bek
        else:
            ans+=(i-cnt[q])*bek
        bek=bek*2%mod
        cnt[q]+=now&1
        now>>=1
    ans=ans%mod
    #print(ans)
print(ans)