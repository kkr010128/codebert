N = int(input())
X = list(map(int, input().split()))
ans = 100 ** 100

for p in range(1, 101):
	now = 0
	for x in X:
		now += (p - x) ** 2
	ans = min(ans, now)
print(ans)
