n, m = map(int, input().split())
a = list(map(int, input().split()))

dp = [float('inf') for _ in range(n+1)]
dp[0] = 0

for i in range(n):
    for money in a:
        next_money = i + money
        if next_money > n:
            continue
        dp[next_money] = min(dp[i] + 1, dp[next_money])

print(dp[n])
