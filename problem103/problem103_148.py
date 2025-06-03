n = int(input())
a = list(map(int, input().split()))

dp = [0]*(n+1)
dp[0] = 1000

for i in range(1, n):
    dp[i] = dp[i-1]
    for j in range(i):
        stock = dp[j]//a[j]
        cost = dp[j]+(a[i]-a[j])*stock
        dp[i] = max(dp[i], cost)
print(dp[n-1])
