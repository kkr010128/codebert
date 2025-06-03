r, c = map(int, input().split())
array = []
for a in range(r):
	row = list(map(int, input().split()))
	array.append(row)

coltotal = [0 for i in range(c + 1)]
for a in range(r):
	array[a].append(sum(array[a]))
	for x in range(c + 1):
		coltotal[x] += array[a][x]

array.append(coltotal)

for a in range(r + 1):
	print(*array[a])