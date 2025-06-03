(n, m, l) = [int(i) for i in input().split()]
a = []
b = []

for i in range(n):
    a.append([int(i) for i in input().split()])
for j in range(m):
    b.append([int(j) for j in input().split()])

for x in range(n):
    c = []
    for y in range(l):
        d = 0
        for z in range(m):
            d += a[x][z] * b[z][y]
        c.append(str(d))
    print(' '.join(c))