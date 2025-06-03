S = int(input())

dp = [0] * (S + 1)
dp[0] = 1
M = 10 ** 9 + 7

for i in range(1, S + 1):
    num = 0
    for j in range(i - 2):
        num += dp[j]
        dp[i] = num % M

print(dp[S])

