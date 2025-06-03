N,K=map(int,input().split())
S=[list(map(int,input().split())) for _ in range(K)]

NUM=998244353
dp=[0]*(N+1)
dp[1]=1
sums=[0]*(N+1)
sums[1]=1
for i in range(2,N+1):
    for s in S:
        _l,_r=i-s[0],i-s[1]-1
        if _l<0:
            continue
        elif _r<0:
            _r=0
        dp[i]+=sums[_l]-sums[_r]
        dp[i]%=NUM
    sums[i]=dp[i]+sums[i-1]
    sums[i]%=NUM

print(dp[N])
