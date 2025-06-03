N, K = map(int, input().split())
LR = [list(map(int, input().split())) for _ in range(K)]
mod = 998244353

dp = [0] * N
dp[0] = 1

now = 0

for i in range(1, N):
    for l, r in LR:
        if i - l >= 0:
            now += dp[i - l]
            now %= mod
        if i - r - 1 >= 0:
            now -= dp[i - r - 1]
            now %= mod
        dp[i] = now
    #print(dp)
print(dp[-1])
