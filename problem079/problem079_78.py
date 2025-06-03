N=int(input())

DP=[-1]*10000

DP[0]=1
DP[1]=0
DP[2]=0
mod=10**9+7

for i in range(3,N+1):
    DP[i]=(DP[i-3]+DP[i-1])%mod

print(DP[N])
