N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

dp = [0] * (N + 1)

for i in range(1, N + 1):
    tmp = float("inf")
    for j in A:
        if i - j >= 0:
            tmp = min(tmp, dp[i - j])
    dp[i] = tmp + 1

print(dp[N])



