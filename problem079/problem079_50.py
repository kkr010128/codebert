s = int(input())
MOD = 10**9 + 7
dp = [0] * (s+10)
dp[0] = 1

for i in range(3, s+10):
    dp[i] = sum(dp[:i-2])
    dp[i] %= MOD

print(dp[s]%MOD)