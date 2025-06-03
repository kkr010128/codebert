N, S = map(int, input().split())

A = list(map(int, input().split()))
mod = 998244353

dp = [0] * (S+1)
dp[0] = 1

for a in A:
    for j in range(S, -1, -1):
        if j-a >= 0:
            dp[j] = dp[j]*2 + dp[j-a]
        else:
            dp[j] = dp[j]*2

print(dp[S]%mod)