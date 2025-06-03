dp = [-1] * 2005

mod = 1000000007

def DP(S):
    if S == 0:
        return 1
    if(dp[S] != -1):
        return dp[S]
    ret = 0
    for i in range(3, S+1):
        ret = (ret + DP(S-i)) % mod
    dp[S] = ret
    return ret

n = int(input())

print(DP(n))