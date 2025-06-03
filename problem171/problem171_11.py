n = int(input())
a = list(map(int, input().split()))
p = sorted([(x, i) for i, x in enumerate(a)], reverse=True)
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for s in range(1, n+1):
	for x in range(s+1):
		y = s-x
		if x > 0:
			dp[x][y] = max(dp[x][y], dp[x-1][y] + abs(p[s-1][1] - x + 1) * p[s-1][0])
		if y > 0:
			dp[x][y] = max(dp[x][y], dp[x][y-1] + abs(n-y - p[s-1][1]) * p[s-1][0])
print(max(dp[x][n-x] for x in range(n+1)))