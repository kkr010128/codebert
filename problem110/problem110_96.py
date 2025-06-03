h, w, k = map(int, input().split())

c = []
for _ in range(h):
	c.append([c for c in input()])

ans = 0

for i in range(1 << h):
	for j in range(1 << w):
		cnt = 0
		for n in range(h):
			for m in range(w):
				if i >> n & 1:
					continue
				if j >> m & 1:
					continue
				if c[n][m] == '#':
					cnt += 1
		if cnt == k:
			ans += 1
print(ans)