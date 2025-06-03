n,m = [int(i) for i in input().split()]
a = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
	a[i] = [int(j) for j in input().split()]
b = [0 for i in range(m)]
for i in range(m):
	b[i] = int(input())
for i in range(n):
	sum = 0
	for j in range(m):
		sum += a[i][j] * b[j]
	print(sum)