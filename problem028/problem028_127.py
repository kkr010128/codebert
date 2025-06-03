
n, m = list(map(int, input().split(" ")))
c = list(map(int, input().split(" ")))
dp = [10**5 for i in range(n + 1)]
dp[0] = 0

for i in range(0, n+1):
    for coin in c:
        if i >= coin:
            dp[i] = min(dp[i-coin] + 1, dp[i])
print(dp[n])

