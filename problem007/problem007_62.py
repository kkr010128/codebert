n = int(raw_input())

dp = [1, 1]

for i in range(50):
    dp += [dp[-1] + dp[-2]]

print dp[n]
