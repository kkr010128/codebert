n, m = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
dp = [100000] * (n + 1)
dp[0] = 0
for k in C:
    for j in range(k, n + 1):
        if dp[j] > dp[j - k] + 1:
            dp[j] = dp[j - k] + 1
print(dp[n])