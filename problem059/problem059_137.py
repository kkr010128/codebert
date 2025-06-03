r, c = map(int, input().split())

matrix = []

vsum = [0]*(c+1)

for i in range(r):
	row = list(map(int, input().split()))
	row.append(sum(row))
	matrix.append(row)
	for j in range(c+1):
		vsum[j] += row[j]

matrix.append(vsum)

for row in matrix:
	print(' '.join(list(map(str, row))))
