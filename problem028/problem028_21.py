n, m = map(int, input().split())
c = list(map(int, input().split()))
INF = float("inf")

dp = [INF]*(n+1)
dp[0] = 0

for i in range(m):
    for j in range(n+1):
        if j + c[i] > n:
            break
        else:
            dp[j + c[i]] = min(dp[j + c[i]], dp[j] + 1)

print(dp[n])
