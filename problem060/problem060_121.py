n,m,l = map(int,raw_input().split())
a = [map(int,raw_input().split()) for _ in range(n)]
b = [map(int,raw_input().split()) for _ in range(m)]
c = [[0 for i in range(l)] for j in range(n)]

for i in range(n):
    for j in range(l):
        s = 0
        for k in range(m):
            s += a[i][k] * b[k][j]
        c[i][j] = s

for i in range(n):
    print ' '.join(map(str,c[i]))