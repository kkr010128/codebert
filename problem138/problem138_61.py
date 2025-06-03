N,S = map(int,input().split())

A = list(map(int,input().split()))
MOD = 998244353
dp = [0 for _ in range(S+1)]
#i個目までの和がjの数となるのは何通りあるかdp[i][j]
dp[0] = 1
#dp = [0 if i==0 else INF for i in range(S + 1)]

for i in range(N): #i個目まで見て。
  p = [0 for _ in range(S+1)]
  p,dp = dp,p
  for j in range(S+1):
    dp[j] = (dp[j]+p[j]*2)%MOD
    if j >= A[i]:
      #print(j,A[i],p[j-A[i]])
      dp[j] += p[j-A[i]]
  #print(dp)
ans = dp[S]%MOD
print(ans)

