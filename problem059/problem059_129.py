r, c = map(int, raw_input().split())
a = []
for _ in range(r):
	a.append(map(int, raw_input().split()))

for i in range(r):
	a[i].append(sum(a[i]))
	print ' '.join(map(str, a[i]))

b = [0 for _ in range(c+1)]
for j in range(c+1):
	for i in range(r):
		b[j] += a[i][j]
print " ".join(map(str, b))