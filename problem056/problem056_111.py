n,m = [int(s) for s in input().split(' ')]
A,b,c = [],[],[]
[A.append([int(s) for s in input().split(' ')]) for i in range(n)]
[b.append(int(input())) for i in range(m)]

for Ai in A:
	ci = []
	for aij,bj in zip(Ai,b):
		ci.append(aij * bj)
	c.append(sum(ci))

[print(ci) for ci in c]