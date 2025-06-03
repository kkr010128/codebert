N, K = map(int, input().split())
S = []
for _ in range(K):
    l, r = map(int, input().split())
    S.append((l, r))

mod = 998244353
 
dp = [0] * (N+1)
cumsum_dp = [0] * (N+1)
dp[1] = 1
cumsum_dp[1] = 1

for i in range(2, N+1):
    for s in S:
        fr = max(0, i-s[1]-1)
        to = max(0, i-s[0])
        dp[i] += (cumsum_dp[to]-cumsum_dp[fr]) % mod
    cumsum_dp[i] = (cumsum_dp[i-1] + dp[i]) % mod
    
print(dp[N]%mod)