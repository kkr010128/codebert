mod = 10**9+7
s = int(input())
dp = [0]*2500

dp[0] = 1
for i in range(1, s+1):
    for j in range(0, i-2):
        dp[i]+=dp[j]
        dp[i]%=mod
print(dp[s])