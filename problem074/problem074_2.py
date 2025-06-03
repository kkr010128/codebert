N,K=map(int,input().split())
MOD = 998244353
dp = [0]*(N+1)

LR = []
for _ in range(K):
    l, r = map(int, input().split())
    LR.append((l,r))

LR.sort()
dp[1] = 1
dp_sum = [0]*(N+1) # dp[i]の累積和
dp_sum[1] = 1

for i in range(2, N+1):
    for l, r in LR:
        if i - l >= 1:
            dp[i] += dp_sum[i-l] - dp_sum[max(0, i-r-1)]
            dp[i] %= MOD
    dp[i] %= MOD
    dp_sum[i] = dp_sum[i-1] + dp[i]
        
print(dp[N]%MOD)