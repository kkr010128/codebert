height,width=map(int,input().split())
A=[]
for i in range(height):
	A.append([int(j) for j in input().split()])


for i in range(height):
	print(' '.join(map(str,A[i])),str(sum(A[i])))

B=[]
C=[0 for _ in range(width)]
for i in range(width):
	for j in range(height):
		s=0
		s+=A[j][i]
		B.append(s)
	C[i]=sum(B)
	B=[]
print(' '.join(map(str,C)),str(sum(C)))