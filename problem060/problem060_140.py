n,m,l = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for y in range(n)]
b = [[int(x) for x in input().split()] for y in range(m)]
c = [[0 for x in range(l)] for y in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]
for i in range(n):
    print(" ".join(map(str,c[i])))