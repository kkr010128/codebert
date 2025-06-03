n = list(map(int, input()))
dp = (0, 1)
for i in n:
  dp = (min(dp[0] + i, dp[1] + 10 - i), min(dp[0] + i + 1, dp[1] + 9 - i))
print(dp[0])