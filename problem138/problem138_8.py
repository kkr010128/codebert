n,s = map(int,input().split())
a = list(map(int,input().split()))
if n == 1:
    if a[0] == s:
        print(1)
        quit()
    else:
        print(0)
        quit()

mod = 998244353
dp = [[0]*(s+1) for _ in range(n+1)]
dp[0][0] = 1
for i in range(n):
    dp[i+1][0] = 2*dp[i][0]%mod
    for j in range(s+1):
        dp[i+1][j] = dp[i][j]*2%mod
    if a[i] <= s:
        for j in range(a[i],s+1):
            dp[i+1][j] += dp[i][j-a[i]]
            dp[i+1][j] %= mod
print(dp[-1][-1]%mod)