def shu(a,b):
	for i in range(a):
		b[i]=list(map(int,input().split()))
n,m,l = map(int,input().split())
A=[[]for i in range(n)]
B=[[]for i in range(m)]
C=[[0 for i in range(l)]for i in range(n)]
shu(n,A)
shu(m,B)
for k in range(m):
	for i in range(n):
		for j in range(l):
			C[i][j] += (A[i][k]*B[k][j])
for i in range(n):
	print(' '.join(map(str,C[i])))
