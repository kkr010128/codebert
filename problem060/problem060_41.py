n, m, l = [int (x) for x in input().split(' ')]
a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for i in range(l)] for j in range(m)]
c = [[0 for i in range(l)] for j in range(n)]
for s in range(0,n):
    a[s] = [int (x) for x in input().split(' ')]
for s in range(0,m):
    b[s] = [int (x) for x in input().split(' ')]

for i in range(0,n):
    for k in range(0,l):
        result = 0
        for j in range(0,m):
            result += a[i][j] * b[j][k]
        c[i][k] = result

for i in range(0,n):
    c[i] = [str(c[i][j]) for j in range(0,l)]
    print(' '.join(c[i]))