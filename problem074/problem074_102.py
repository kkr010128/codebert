N,K=map(int,input().split())
MOD = 998244353
dp = [0]*(N*3)

LR = []
for _ in range(K):
    l, r = map(int, input().split())
    LR.append((l,r))

LR.sort()

imos = [0]*(N*3)
dp[1] = 1
imos[1] = 1
for i in range(1, N):
    if i >= 2:
        dp[i+1] += dp[i]

    for l, r in LR:
        dp[i+l] += dp[i]
        dp[i+l] %= MOD
        dp[i+r+1] -= dp[i]
        dp[i+r+1] %= MOD
    
    

print(dp[N]%MOD)

