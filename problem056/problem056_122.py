n, m = map(int, raw_input().split())
a = []
for _ in range(n):
	a.append(map(int, raw_input().split()))
b = []
for _ in range(m):
	b.append(int(raw_input()))
for i in range(n):
	c = []
	for j in range(m):
		c.append(a[i][j]*b[j])
	print sum(c)