INF = 1 << 60

h, n = map(int, input().split())
a = [0 for i in range(n)]
b = [0 for i in range(n)]
for i in range(n):
    a[i], b[i] = map(int, input().split())

MAX = h - 1 + max(a)
dp = [[INF for j in range(MAX + 1)] for i in range(n)]
dp[0][0] = 0
if 0 <= a[0] < MAX + 1:
    dp[0][a[0]] = b[0]
for j in range(MAX + 1):
    if 0 <= j - a[0] < MAX + 1:
        dp[0][j] = min(dp[0][j], dp[0][j - a[0]] + b[0])
for i in range(1, n):
    for j in range(MAX + 1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        if 0 <= j - a[i] < MAX + 1:
            dp[i][j] = min(dp[i][j], dp[i][j - a[i]] + b[i])
ans = INF
for j in range(h, MAX + 1):
    ans = min(ans, dp[-1][j])
print(ans)