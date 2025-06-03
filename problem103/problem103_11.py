n=int(input())
A=list(map(int,input().split()))
INF=float('inf')
dp=[-INF]*(n+1)
dp[0]=1000

for i in range(1,n+1):
  dpi=dp[i-1]
  for j in range(1,i):
    dpi=max(dpi,dp[j]+(dp[j]//A[j-1])*(A[i-1]-A[j-1]))
  dp[i]=dpi
  
print(dp[n])