def mod(val, mod_base):
  if val >= mod_base:
    return val%mod_base
  return val

# 配るDP
def resolve():
  base = 998244353
  N, K = map(int, input().split(" "))

  LRs = []
  for _ in range(K):
    (L, R) = map(int, input().split(" "))
    LRs.append((L, R))

  dp = [0] * (N+1)
  dp_sum = [0] * (N+1)
  dp[1] = 1
  dp_sum[1] = 1

  for i in range(1, N):
    dp_sum[i] = dp[i] + dp_sum[i-1]

    for lr in LRs:
      left = i + lr[0]
      right = i + lr[1] + 1
      if left <= N:
        dp[left] += dp_sum[i]
        dp[left] = mod(dp[left], base)
      if right <= N:
        dp[right] -= dp_sum[i]
        dp[right] = mod(dp[right], base)
  print(mod(dp[-1], base))

if __name__ == "__main__":
  resolve()