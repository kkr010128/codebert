n, m = map(int, input().split())
d = list(map(int, input().split()))
dp = [10000 for i in range(n + 1)]
dp[0] = 0

for i in range(0, n + 1):
    if dp[i] < 10000:
        for j in d:
            if i + j <= n:
                dp[i + j] = min(dp[i] + 1, dp[i + j])

print(dp[n])