N, S = map(int, input().split())
A = list(map(int, input().split()))
dp = [[0]*(S+1) for _ in range(N+1)]
dp[0][0] = 1
mod = 998244353


for i in range(N):
  a = A[i]
  for j in range(S+1):
    if j >= a:
      dp[i+1][j] += dp[i][j-a] + dp[i][j]*2
      dp[i+1][j] %= mod
    else:
      dp[i+1][j] += dp[i][j]*2 
      dp[i+1][j] %= mod

print(dp[N][-1]%mod)