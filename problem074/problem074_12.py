N, K = map(int, input().split())

L = []
R = []

for _ in range(K):
  l, r = map(int, input().split())
  L.append(l)
  R.append(r)
  
dp = [0]*(N+5)
dp[1] = 1

for i in range(2, N+1):
  dp[i] = dp[i-1]
  for j in range(K):
    if i-L[j] >= 0:
      dp[i] += dp[i-L[j]]
    if i-R[j]-1 >= 0:
      dp[i] -= dp[i-R[j]-1]
    dp[i] %= 998244353
    
print((dp[N]-dp[N-1])%998244353)