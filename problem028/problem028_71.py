n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [float("inf")]*(n+1)
dp[0] = 0
for i in range(m):
    for j in range(c[i], n+1):
        dp[j] = dp[j - c[i]]+1 if dp[j - c[i]] < dp[j] else dp[j]
print(dp[n])