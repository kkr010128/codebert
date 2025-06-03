S = int(input())
dp = [0 for _ in range(S+1)]
dp[0] = 1
MOD = 10**9+7
for i in range(3,S+1):
    dp[i] = dp[i-1]+dp[i-3]

print(dp[S]%MOD)