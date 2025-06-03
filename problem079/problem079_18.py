s = int(input())
mod = 10**9 + 7
dp = [0 for i in range(s+1)]
dp[0] = 1

for cp in range(1, s+1):
    dp[cp] = sum(dp[0:max(cp-2, 0)]) % mod

print(dp[s])