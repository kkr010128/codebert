x,y=map(int,raw_input().split())
a=[map(int,raw_input().split()) for i in range(x)]
for i in range(x):
	a[i].append(sum(a[i]))
	for j in range(y+1):
		print a[i][j],
	print
for i in range(y+1):
	print sum([row[i] for row in a]),