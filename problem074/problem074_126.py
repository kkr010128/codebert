N, K = map(int, input().split())
MOD = 998244353

move = []
for _ in range(K):
  L, R = map(int, input().split())
  move.append((L, R))

dp = [0]*(N+1)
dp[0] = 1
dp[1] = -1

for i in range(1, N+1):
  dp[i] += dp[i-1]
  for l, r in move:
    if i - l >= 0:
      dp[i] += dp[i-l]
    if i - r - 1 >= 0:
      dp[i] -= dp[i-r-1]
  dp[i] %= MOD

print(dp[N-1])