mod = 998244353

n, k = map(int, input().split())

s = []
for _ in range(k):
    l, r = map(int, input().split())
    s.append((l, r))

dp = [0] * (n + 1)
dp[1] = 1
for i in range(2, n+1):
    for l, r in s:
        jl = max(i - l, 0)
        jr = max(i - r - 1, 0)
        dp[i] = (dp[i] + dp[jl] - dp[jr]) % mod
    dp[i] += dp[i-1]
print((dp[n] - dp[n-1]) % mod)
