r,c = [int(i) for i in input().split()]
a = [[0 for i in range(c+1)] for j in range(r+1)]
for i in range(r):
	a[i] = [int(j) for j in input().split()]
for i in range(r):
	rowSum = 0
	for j in range(c):
		rowSum += a[i][j]
	a[i].append(rowSum)
for i in range(c+1):
	columnSum = 0
	for j in range(r):
		columnSum += a[j][i]
	a[r][i] = columnSum
for i in range(r+1):
	for j in range(c):
		print(a[i][j],end=' ')
	print(a[i][c])