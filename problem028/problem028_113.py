n,m = map(int, input().split())
d = list(map(int, input().split()))
inf = float('inf')
dp = [inf for i in range(n+1)]
dp[0] = 0
for i in range(m):
    for j in range(d[i], n+1):
        dp[j] = min(dp[j], dp[j-d[i]]+1)

print(dp[-1])
