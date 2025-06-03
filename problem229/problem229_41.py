h, n = map(int, input().split())
inf = 10 ** 9
dp = [inf for _ in range(h + 1)]
dp[0] = 0
for _ in range(n):
    a, b = map(int, input().split())
    for i in range(h + 1):
        if i < a:
            dp[i] = min(dp[i], b)
        else:
            dp[i] = min(dp[i], dp[i - a] + b)
print(dp[-1])