n, m, l = map(int,input().split())
a = list()
for i in range(n):
    a.append(list(map(int,input().split())))

b = list()
for i in range(m):
    b.append(list(map(int,input().split())))

for i in range(n):
    line = list()
    for j in range(l):
        c = 0
        for k in range(m):
            c += a[i][k] * b[k][j]
        line.append(str(c))
    print(' '.join(line))
