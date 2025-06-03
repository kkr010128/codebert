a = []
b = []
n, m, l = [int(n) for n in input().split()]
c = [[0 for i in range(l)] for j in range(n)]
for i in range(n):
    a.append([int(n) for n in input().split()])
for i in range(m):
    b.append([int(n) for n in input().split()])
for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k] * b[k][j]
for num in c:
    print(' '.join(str(n) for n in num))