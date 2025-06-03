h, n = map(int, input().split())
ab = []
for _ in range(n):
    ab.append(map(int, input().split()))

m = 20010
dp = [1000000000] * m
dp[0] = 0
for a, b in ab:
    for i in range(m):
        if i - a >= 0:
            dp[i] = min(dp[i], dp[i - a] + b)
print(min(dp[h:]))
