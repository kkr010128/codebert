n, s = map(int, input().split())
a  = list(map(int, input().split()))
MOD = 998244353
 
dp = [[0]*(s+1) for _ in range(n+1)]
dp[0][0] = 1
 
for i in range(n):
    for j in range(s+1):
        dp[i+1][j] = dp[i+1][j] + dp[i][j] * 2
        dp[i+1][j] = dp[i+1][j] % MOD
        if j + a[i] <= s:
            dp[i+1][j+a[i]] = dp[i+1][j+a[i]] + dp[i][j]
            dp[i+1][j+a[i]] = dp[i+1][j+a[i]] % MOD
 
print(dp[n][s])