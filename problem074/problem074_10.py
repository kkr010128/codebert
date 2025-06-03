N,K = map(int,input().split())
LR = []
for _ in range(K): LR.append(list(map(int,input().split())))
MOD = 998244353
dp = [0]*(N+1)
dp[0] = 1
for i in range(N):
  for L,R in LR:
    if i+L<N: dp[i+L] += dp[i]
    if i+R+1<N: dp[i+R+1] -= dp[i]
  if i>0: dp[i+1] = (dp[i+1]+dp[i])%MOD
print(dp[-1])