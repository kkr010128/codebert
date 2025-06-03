s = int(input())
mod = 10 ** 9 + 7

dp = [1, 0, 0]
for _ in range(s - 2):
    dp.append((dp[-1] + dp[-3]) % mod)
print(dp[s])
