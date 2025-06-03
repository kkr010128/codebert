N, K = map(int, input().split())
mod = 998244353
move = []

for _ in range(K):
  L, R = map(int, input().split())
  move.append((L, R))

S = [0]*K
dp = [0]*(2*N)
dp[N] = 1

for i in range(N+1, 2*N):
  for k, (l, r) in enumerate(move):
    S[k] -= dp[i-r-1]
    S[k] += dp[i-l]
    dp[i] += S[k]
  dp[i] %= mod

print(dp[-1])