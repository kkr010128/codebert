n = int(input())
dp = [1] * (n+1)

for j in range(n-1):
    dp[j+2] = dp[j+1] + dp[j]
print(dp[n])

