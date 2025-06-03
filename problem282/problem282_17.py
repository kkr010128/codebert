import sys
def input():
	return sys.stdin.readline()[:-1]
n, p = map(int, input().split())
snacks = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])
dp = [0 for _ in range(p)]
ans = snacks[0][1]

for i in range(1, n):
	x, y = snacks[i-1]
	z = snacks[i][1]
	for j in range(p-1, 0, -1):
		if j >= x:
			dp[j] = max(dp[j], dp[j-x]+y)
		ans = max(ans, dp[j]+z)

print(ans)