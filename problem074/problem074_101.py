N, K = map(int, input().split())
MOD = 998244353
t = []
for _ in range(K):
    l, r = map(int, input().split())
    t.append((l, r))
dp = [0]*(N+1)
dp[1] = 1
dps = [0]*(N+1)
dps[1] = 1
for i in range(2, N+1):
    for j in range(K):
        li = i-t[j][0]
        ri = i-t[j][1]
        if li < 0:
            continue
        ri = max(ri, 1)
        dp[i] += dps[li]-dps[ri-1]
        dp[i] %= MOD
    dps[i] = dps[i-1]+dp[i]
    dps[i] %= MOD
print(dp[N])
