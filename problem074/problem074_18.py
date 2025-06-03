n, k = map(int, input().split())
mod = 998244353
S = []
for _ in range(k):
    l, r = map(int, input().split())
    S.append([l, r])


dp = [0]*(n+1)
dp_s = [0]*(n+1)
dp[1] = 1
dp_s[1] = 1
for i in range(2, n+1):
    for l, r in S:
        li = max(i - r, 1)
        ri = max(i - l, 0)
        dp[i] = (dp[i] + (dp_s[ri] - dp_s[li-1])%mod) % mod
    dp_s[i] = (dp_s[i-1] + dp[i])%mod
print(dp[n]%mod)