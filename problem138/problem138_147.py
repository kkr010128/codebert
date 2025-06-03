n, s = map(int, input().split())
A = list(map(int, input().split()))
mod = 998244353

dp = [[0] * (s+1) for i in range(n+1)]
dp[0][0] = 1

for i in range(n):
    a = A[i]
    for j in range(s+1):
        if j < s:
            dp[i+1][j] = (dp[i+1][j] + 2*dp[i][j])%mod
        if j+a<s+1:
            dp[i+1][j+a] = (dp[i+1][j+a] + dp[i][j])%mod

ans = 0
for i in range(1, n+1):
    ans = (ans + dp[i][s] * pow(2, n-i, mod)) % mod
print(ans)


