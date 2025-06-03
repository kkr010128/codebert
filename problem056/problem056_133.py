A=map(int,raw_input().split(" "))
vec=A[0]
col=A[1]

def zero(n):
	zerolist=list()
	for i in range(n):
		zerolist+=[0]
	return(zerolist)
A=list()
for i in range(vec):
	A+=[zero(col)]



for i in range(vec):
	k=map(int,raw_input().split(" "))
	for j in range(col):
		A[i][j]=k[j]

#ok

v=zero(col)

for i in range(col):
	v[i]=int(raw_input())

k=0
for i in range(vec):
	for j in range(col):
		k+=A[i][j]*v[j]
	print k
	k=0