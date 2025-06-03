from sys import stdin

n, m, l = [int(x) for x in stdin.readline().rstrip().split()]
a = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(n)]
b = [[int(x) for x in stdin.readline().rstrip().split()] for _ in range(m)]
c = [[0] *l for _ in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k]*b[k][j]

for i in range(n):
    print(*c[i])
