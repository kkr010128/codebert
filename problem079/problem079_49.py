s = int(input())
dp = [0] * (s + 11)
mod = 10 ** 9 + 7
dp[0] = 1
dp[1] = 0
dp[2] = 0
dp[3] = 1
c = 2
for i in range(4, s + 1):
    dp[i] = (c - dp[i - 1] - dp[i - 2]) % mod
    c = (c + dp[i]) % mod
print(dp[s])