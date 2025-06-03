N=int(input())
DP=[0]*(N+1)
tmp=0
mod=10**9+7
if N<3:
   print(0)
   exit()
DP[3]=1
for i in range(4,N+1):
   DP[i]=(DP[i-1]+DP[i-3])%mod
print(DP[N]%mod)