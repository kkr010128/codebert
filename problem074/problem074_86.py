MOD = 998244353

N, K = list(map(int, input().split()))

dp = [0] * (N+1)
dp[1] = 1

LR = []

for i in range(K):
  l, r = list(map(int, input().split()))
  LR.append([l, r])

for i in range(2, N+1):
  dp[i] = dp[i-1]
  for j in range(K):
    l, r = LR[j]
    dp[i] += dp[max(i-l, 0)] - dp[max(i-r-1, 0)]
    dp[i] %= MOD

print((dp[N]-dp[N-1]) % MOD)