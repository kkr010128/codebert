dp = [0, 1]

s = input()
s = s[::-1]
s += "0"

for i in range(len(s)):
    dp0, dp1 = dp
    dp[0] = min(dp0, dp1 + 1) + int(s[i])
    dp[1] = min(dp0, dp1 - 1) + 10 - int(s[i])

print(min(dp))