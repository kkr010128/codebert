def li():
    return [int(x) for x in input().split()]


MOD = 998244353
N, K = li()
L, R = [], []
for _ in range(K):
    l, r = li()
    L.append(l)
    R.append(r)

#dp[i]: マスiにいく場合の数

dp = [0] * (2 * N + 1)
dp[1] = 1
dp[2] = -1

for i in range(1, N):
    dp[i+1] += dp[i]
    dp[i+1] %= MOD
    for k in range(K):
        l, r = L[k], R[k]
        dp[i+l] += dp[i]
        dp[i+l] %= MOD
        dp[i+r+1] -= dp[i]
        dp[i+r+1] %= MOD

print(dp[N])
