A=[]
b=[]
n=list(map(int,input().split()))
for i in range(n[0]):
	A.append(list(map(int,input().split())))
for i in range(n[1]):
	b.append(int(input()))
	
for i in range(n[0]):
	num=0
	for j in range(n[1]):
		num=num+A[i][j]*b[j]
	print(num)
