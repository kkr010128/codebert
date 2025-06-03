a,b=map(int,input().split())
A=[]
B=[]
for i in range(a):
	A.append([int(j) for j in input().split()])

for i in range(b):
	B.append(int(input()))


for i in range(a):
	s=0
	for j in range(b):
		s+=A[i][j]*B[j]
	print(s)