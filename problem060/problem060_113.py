[n,m,l] = map(int, input().split())
a = []
b = []
c = [[0 for k in range(l)] for i in range(n)]
for i in range(n):
    a.append(list(map(int, input().split())))

for j in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    for k in range(l):
        s = 0
        for j in range(m):
            s += a[i][j] * b[j][k]
        c[i][k] = s

for i in range(n):
    for k in range(l):
        print(c[i][k],end='')
        if k!= l-1:    
            print(' ',end='')
        else:
            print()