# (c) midandfeed
q = []
for i in range(4):
	b = []
	for j in range(3):
		a = [0 for x in range(10)]
		b.append(a)
	q.append(b)

t = int(input())
for _ in range(t):
	b, f, r, v = [int(x) for x in input().split()]
	q[b-1][f-1][r-1] += v

a = 0
for x in q:
	a += 1
	for y in x:
		for z in range(len(y)):
			print(" {}".format(y[z]), end='')
			if (z==(len(y))-1):
				print()
	if (a!=4):	
		print("#"*20)