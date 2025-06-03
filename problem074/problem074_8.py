N, K = map(int, input().split())
mod = 998244353
lr = [0] * K
for i in range(K):
    lr[i] = list(map(int, input().split()))
    lr[i][1] += 1

dp = [0] * (N+1)
dp[1] = 1
s = 0
for i in range(1, N):
    s += dp[i]
    for j in range(K):
        if (i + lr[j][0]) <= N:
            dp[i + lr[j][0]] = (dp[i + lr[j][0]] + s) % mod
        if (i + lr[j][1]) <= N:
            dp[i + lr[j][1]] = (dp[i + lr[j][1]] - s) % mod
        

print(dp[N])