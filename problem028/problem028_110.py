n, m = map(int, input().split())
c = list(map(int, input().split()))

dp = [float('inf') for _ in range(n + 10001)]
dp[0] = 0

for i in range(n):
    for j in c:
        dp[i + j] = min(dp[i + j], dp[i] + 1)

print(dp[n])
