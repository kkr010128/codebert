digits = [0] + [int(c) for c in input()]

dp = [0, 1]
for digit in reversed(digits):
    dp0, dp1 = dp
    dp[0] = min(dp0, dp1 + 1) + digit
    dp[1] = min(dp0, dp1 - 1) + 10 - digit

print(min(dp))