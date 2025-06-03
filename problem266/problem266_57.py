X = int(input())
dp = [0] * (X + 110)
dp[0] = 1
for i in range(X):
    if dp[i]:
        for j in range(100, 106):
            dp[i + j] = 1
print(dp[X])
