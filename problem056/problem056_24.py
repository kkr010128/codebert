from sys import stdin

n, m = [int(x) for x in stdin.readline().rstrip().split()]
a = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(n)]
b = [[int(stdin.readline().rstrip())] for _ in range(m)]
c = [[0] for _ in range(n)]
for i in range(n):
    for j in range(m):
    	c[i][0] += (a[i][j]*b[j][0])

for i in range(n):
    print(*c[i])
