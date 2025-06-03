# (c) midandfeed
r, c = [int(x) for x in input().split()]
q = []
sumr = [0]*c
tempr = 0
for i in range(r):
	col = [int(x) for x in input().split()]
	for j in range(c):
		sumr[j] += col[j]
	col.append(sum(col))
	q.append(col)
sumr.append(sum(sumr))
q.append(sumr)
for i in range(r+1):
	for j in range(c+1):
		print(q[i][j], end='')
		if (j != (c)):
			print(' ', end='')
	# if (i != (r) ):
	print()