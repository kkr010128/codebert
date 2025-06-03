#もらうDP + 累積和
n, k = map(int, input().split())
mod = 998244353
li = []
for _ in range(k):
    l, r = map(int, input().split())
    li.append((l, r))
li.sort()
dp = [0]*(2*n+1)
s = [0] * (2*n+1)
dp[1] = 1
s[1] = 1
for i in range(2, n+1):
    for t in li:
        l, r = t
        dp[i] += s[max(i-l, 0)]
        dp[i] -= s[max(i-r-1, 0)]
        dp[i] %= mod
    s[i] = s[i-1] + dp[i]
    s[i] %= mod
print(dp[i]%mod)