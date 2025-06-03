N, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(K)]
 
# dpの高速化 => 累積和によって、O(N)で解く
dp = [0] * N
acc = [0]* (N+1)
dp[0], acc[1] = 1, 1
# acc[0] = 0
# acc[1] = dp[0]
# acc[2] = dp[0] + dp[1]
# acc[n] = dp[0] + dp[1] + dp[n-1]

# dp[0] = acc[1] - acc[0]
# dp[1] = acc[2] - acc[1]
# dp[n-1] = acc[n] - acc[n-1]
mod = 998244353
 
for i in range(1, N):
  # acc[i] = dp[0] + ... + dp[i-1] が既知
  # 貰うdp
  for j in range(K):
    r = i - X[j][0]
    l = i - X[j][1]
    if r < 0: continue
    l = max(l, 0)
      
    dp[i] += acc[r+1] - acc[l] # s = dp[L] + ... + dp[R]
    dp[i] %= mod
  acc[i+1] = acc[i] + dp[i] # acc[i+1] = dp[0] + ... + dp[i]

print(dp[N-1])