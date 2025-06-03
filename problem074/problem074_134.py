
N, K = map(int, input().split())
mod = 998244353
move = []

for _ in range(K):
  L, R = map(int, input().split())
  move.append((L, R))

dp = [0]*(2*N+1)
dp[0] = 1

for i in range(N):
  for l, r in move:
    dp[i+l] += dp[i]
    dp[i+l] %= mod
    dp[i+r+1] -= dp[i]
    dp[i+r+1] %= mod
  if i:
    dp[i+1] += dp[i]
  dp[i] %= mod

print(dp[N-1])