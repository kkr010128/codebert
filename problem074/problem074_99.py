N, K =map(int,input().split())
K = [tuple(map(int,input().split())) for i in range(K)]
M = 998244353

dp = [0] * N
dp[1] = 1
prefix = [1] * N

for i in range(1, N):
    cur = 0
    for L, R in K:
        a = i - R
        b = i - L
        if b < 0:
            continue
        cur += prefix[b] - (prefix[a - 1] if a - 1 >= 0 else 0)
    dp[i] = cur % M
    prefix[i] = prefix[i - 1] + dp[i]
    prefix[i] %= M
print(dp[N - 1])