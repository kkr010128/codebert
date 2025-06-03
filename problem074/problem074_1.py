N, K = map(int, input().split())

INF = 998244353

LR = []
for i in range(K):
    LR.append(list(map(int, input().split())))

dp = [0] * N
dp[0] = 1
a_sum = [0] * N
a_sum[0] = 1
for i in range(1, N):
    for lr in LR:
        if i - lr[0] >= 0:
            if i - lr[1]-1 >= 0:
                # print(i, lr, dp[i], i-lr[0], i-lr[1]-1, a_sum[i-lr[0]], a_sum[i-lr[1]-1])
                dp[i] = dp[i] + a_sum[i-lr[0]] - a_sum[i-lr[1]-1]
            else:
                dp[i] = dp[i] + a_sum[i-lr[0]]
    dp[i] %= INF
    a_sum[i] = a_sum[i-1] + dp[i]
    a_sum[i] %= INF
    # print(i, dp, a_sum)
print(dp[-1])
