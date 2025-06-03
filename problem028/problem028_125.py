n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
DP = [i for i in range(n + 1)]
for cost in c:
	for i in range(cost, n + 1):
		DP[i] = min(DP[i], DP[i - cost] + 1)
print(DP[n])

