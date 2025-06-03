from sys import stdin
def solve():
    s = int(stdin.readline())
    mod = 10**9+7
    if s < 3: return 0
    dp = [0]*(s+1)
    dp[0] = 1
    for i in range(3,s+1):
        dp[i] = dp[i-1] + dp[i-3]
    return dp[s]%mod
print(solve())