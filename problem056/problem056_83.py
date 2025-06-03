n,m=map(int,raw_input().split())
A,B=[],[]
c=0
for i in xrange(n):
	A.append(map(int,raw_input().split()))
for i in xrange(m):
	B.append(int(raw_input()))
for i in xrange(n):
	for j in xrange(m):
		c+=A[i][j]*B[j]
	print c
	c=0