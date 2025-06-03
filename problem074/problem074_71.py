mod = 998244353
N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]
dp = [0] * (N+1)
dpsum = [0] * (N+1)
dp[1] = 1
dpsum[1] = 1
for i in range(2, N+1):
    for l, r in LR:
        li = i-r
        ri = i-l
        if ri < 0: continue
        li = max(1, li)
        dp[i] += dpsum[ri] - dpsum[li-1]
        dp[i] = dp[i] % mod
    
    dpsum[i] = dpsum[i-1] + dp[i] 
    dpsum[i] = dpsum[i] % mod

print(dp[N])