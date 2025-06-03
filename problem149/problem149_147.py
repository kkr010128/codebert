n, m, x = map(int, input().split())
c = [0] * n
a = [[]] * n
for i in range(n):
	c[i], *a[i] = map(int, input().split())
ans = 2**32
for mask in range(1 << n):
	res = [0] * m
	cost = 0
	for i in range(n):
		if mask >> i & 1:
			cost += c[i]
			for j in range(m):
				res[j] += a[i][j]
	if all(v >= x for v in res):
		ans = min(ans, cost)
print(ans if ans != 2**32 else -1)