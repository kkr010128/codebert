n, k = map(int, input().split())
lr = [list(map(int, input().split())) for _ in range(k)]
mod = 998244353

dp = [0] * n
dp[0] = 1
acc = 0

for i in range(1, n):
    # 例4のi=13, lr=[[5, 8], [1, 3], [10, 15]]の場合を想像すると書きやすい
    for li, ri in lr:
        if i - li >= 0:
            acc += dp[i - li]
            acc %= mod
        if i - ri - 1 >= 0:
            acc -= dp[i - ri - 1]
            acc %= mod
    dp[i] = acc
print(dp[-1])