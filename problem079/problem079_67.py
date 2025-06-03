mod = 10 ** 9 + 7

S = int(input())

dp = [0] * 3 + [1] * (S - 2)
for i in range(3, S + 1):
    dp[i] = (1 + sum(dp[0:i - 2])) % mod

print(dp[S])