n, s = map(int, input().split())
a = list(map(int, input().split()))
mod = 998244353
ans = 0

inv_2 = pow(2, mod-2, mod)
dp = [[0 for _ in range(s+1)] for _ in range(n+1)]
dp[0][0] = pow(2, n, mod)

for i in range(n):
    for j in range(s+1):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= mod

        if j + a[i] <= s:
            dp[i+1][j+a[i]] += dp[i][j] * inv_2
            dp[i+1][j+a[i]] %= mod

#print(dp)
print(dp[n][s])