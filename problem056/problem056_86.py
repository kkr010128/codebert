n, m = map(int, raw_input().split())
a, b = [], []
c = [0 for _ in range (n)]
for _ in range(n):
	a.append(map(int, raw_input().split()))
for _ in range(m):
	b.append(int(raw_input()))
for i in range(n):
	c[i] = 0
	for j in range(m):
		c[i] += a[i][j]*b[j]
	print c[i]