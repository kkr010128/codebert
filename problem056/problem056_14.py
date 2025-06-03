n,m = list(map(int,input().split()))

A = [[0 for w in range(m)] for h in range(n)]
B = [0 for h in range(m)]

for i in range(n) :
	A[i] = list(map(int, input().split()))
for i in range(m) :
	B[i] = int(input())


for i in range(n):
	c = 0
	for j in range(m):
		c += A[i][j] * B[j]
	print(c)