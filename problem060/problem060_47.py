n,m,l = map(int,input().split())
a = [[0 for i2 in range(m)] for i1 in range(n)]
b = [[0 for i2 in range(l)] for i1 in range(m)]

for i in range(n):
    row = list(map(int,input().split()))
    for j in range(m):
        a[i][j] = row[j]

for i in range(m):
    row = list(map(int,input().split()))
    for j in range(l):
        b[i][j] = row[j]

c = [[0 for i2 in range(l)] for i1 in range(n)]

for i in range(n):
    for j in range(l):
        for k in range(m):
            c[i][j] += a[i][k]*b[k][j]

for i in range(n):
    for j in range(l-1):
        print(c[i][j],end = ' ')
    print(c[i][-1])