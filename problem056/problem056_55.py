import sys

#fin = open("test.txt", "r")
fin = sys.stdin

n, m = map(int, fin.readline().split())

A = [[] for i in range(n)]
for i in range(n):
	A[i] = list(map(int, fin.readline().split()))

b = [0 for i in range(m)]

for i in range(m):
	b[i] = int(fin.readline())

c = [0 for i in range(n)]

for i in range(n):
	for j in range(m):
		c[i] += A[i][j] * b[j]

for i in range(n):
	print(c[i])