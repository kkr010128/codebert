# -*- coding: utf-8 -*-
N, K = map(int, input().split())

kukan = list()
for i in range(K):
  l, r =  map(int, input().split())
  kukan.append((l, r))
dp = [0] * (N+1)
dp[1] = 1
dp_sum = [0] * (N+1)
dp_sum[1] = 1
for i in range(0, N+1):
  for j in range(K):
    from_l = i - kukan[j][1]
    from_r = i - kukan[j][0]
    if from_r < 0:
      continue
    else:
      from_l = max(1, from_l)
      dp[i] += dp_sum[from_r] - dp_sum[from_l - 1]
      dp[i] %= 998244353
  dp_sum[i] = dp[i] + dp_sum[i-1]
print(dp[N] % 998244353)