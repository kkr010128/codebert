n = int(input())
mod = 10**9+7
dp = [1]*(n+1)
if n <= 2:
    print(0)
    exit()
for i in range(3):
    dp[i] = 0

for j in range(3, 10):
    if j <= n:
        dp[j] = 1

for i in range(3, n+1):
    for j in range(3, n):
        if i+j <= n:
            dp[i+j] += dp[i]
            dp[i+j] %= mod
print(dp[-1])
