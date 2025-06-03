n = int(input())
a = list(map(int, input().split()))
l = sorted(zip(a, range(0, n)), reverse=True)
p = [0] * n
for i in range(n):
    p[i] = l[i][1]
a.sort(reverse=True)
dp = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i + 1):
        k = i - j
        if j == 0:
            dp[j][k] = dp[j][k - 1] + abs(n - k - p[i - 1]) * a[i - 1]
        elif k == 0:
            dp[j][k] = dp[j - 1][k] + abs(j - 1 - p[i - 1]) * a[i - 1]
        else:
            dp[j][k] = max(dp[j][k - 1] + abs(n - k - p[i - 1]) * a[i - 1],
                           dp[j - 1][k] + abs(j - 1 - p[i - 1]) * a[i - 1])
ans = 0
for i in range(n):
    ans = max(ans, dp[n - i][i])
print(ans)
