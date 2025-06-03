
def solve(s):
    dp = [0]*(s+1)
    dp[0] = 1
    MOD = 10**9+7
    x = 0
    for i in range(1,s+1):
        for j in range(0,i-3+1):
            dp[i] += dp[j]
            dp[i] %= MOD
    return dp[s]

s = int(input())

print(solve(s))