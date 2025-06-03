n, m, l = list(map(int, input().split()))
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(m)]
for i in range(n):
	line = []
	for j in range(l):
		c = 0
		for k in range(m):
			c += a[i][k] * b[k][j]
		line.append(str(c))
	print(*line)
	
