n,m,l = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(n)]
b = [[int(i) for i in input().split()] for j in range(m)]
c = [[0 for i in range(l)] for j in range(n)]
for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]
for i in range(n):
    print(' '.join(map(str,c[i])))