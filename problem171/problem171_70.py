n = int(input())
a = list(map(int, input().split()))
a = [(a[i], i) for i in range(n)]
a.sort(key=lambda x: -x[0])
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for x in range(n+1):
    for y in range(n+1):
        if x + y > n:
            break
        active, idx = a[x+y-1]
        if x > 0:
            dp[x][y] = max(dp[x][y],
                           dp[x-1][y] + active * abs(idx - (x-1)))

        if y > 0:
            dp[x][y] = max(dp[x][y],
                           dp[x][y-1] + active * abs(idx - (n-y)))

ans = 0
for x in range(n+1):
    ans = max(ans, dp[x][n-x])

print(ans)