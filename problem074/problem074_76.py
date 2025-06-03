# D - Leaping Tak
n,k = map(int,input().split())
lr = [tuple(map(int,input().split())) for _ in range(k)]
MOD = 998244353

# 累積和を使ってもらうdpを効率よく実現する。

dp = [0 for _ in range(n+1)]
dpsum = [0 for _ in range(n+1)]
dp[1] = 1
dpsum[1] = 1
for i in range(2,n+1):
  for li,ri in lr:
    r = i-li
    if r < 1:
      continue
    l = max(i-ri-1,0)
    dp[i] += dpsum[r]-dpsum[l]
    dp[i] %= MOD
  dpsum[i] += dpsum[i-1]+dp[i]
  dpsum[i] %= MOD
print(dp[n])