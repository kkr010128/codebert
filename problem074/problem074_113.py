import sys
N,K=map(int, sys.stdin.readline().split())
LR=[ map(int, sys.stdin.readline().split()) for _ in range(K) ]

dp=[0]*(N+1)
sum_dp=[0]
mod=998244353

i=1
dp[i]=1
sum_dp.append(sum_dp[-1]+dp[i])

for i in range(2,N+1):
    for l,r in LR:
        dp[i]+=sum_dp[max(0,i-l)]-sum_dp[max(0,i-r-1)]
        dp[i]%=mod
    sum_dp.append( (sum_dp[-1]+dp[i])%mod )

print dp[-1]
