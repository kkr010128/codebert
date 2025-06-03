n,m = map(int,input().split())
A = []
B = []
for i in range(n):
	tmp = list(map(int,input().split()))
	A.append(tmp)
	tmp=[]
for i in range(m):
	num = int(input())
	B.append(num)
for i in range(n):
	c = 0
	for j in range(m):
		c += A[i][j]*B[j]
	print(c)
