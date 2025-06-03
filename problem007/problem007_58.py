n = int(input())
dp = [1] * (50)
for i in range(n):
    dp[i + 2] = dp[i + 1] + dp[i]

print(dp[n])
