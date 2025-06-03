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

  for i in range(2, N+1):
    for lr in LRs:
      left = max(i - lr[1] - 1, 0)
      right = max(i - lr[0], 0)
      dp[i] += dp_sum[right] - dp_sum[left]
      if dp[i] >= base:
        dp[i] %= base
      dp_sum[i] = dp_sum[i-1] + dp[i]
  print(dp[-1])

if __name__ == "__main__":
  resolve()