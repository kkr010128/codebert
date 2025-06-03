# 解説を見て解き直し
N, K = [int(x) for x in input().split()]

ranges = [tuple(int(x) for x in input().split()) for _ in range(K)]
ranges.sort()
p = 998244353

dp = [0] * (N + 1)
dpsum = [0] * (N + 1)
dp[1] = 1
dpsum[1] = 1

for i in range(2, N + 1):
    for l, r in ranges:
        rj = i - l
        lj = max(1, i - r)  # 1以上
        if rj <= 0: continue

        dp[i] += dpsum[rj] - dpsum[lj - 1]
        dp[i] %= p
    dpsum[i] = dpsum[i - 1] + dp[i]
    dpsum[i] %= p

print(dp[N])