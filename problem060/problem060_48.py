n, m, ll = map(int, input().split())

a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    b.append(list(map(int, input().split())))

for i in range(n):
    prt = []
    for j in range(ll):
        s = 0
        for k in range(m):
            s += a[i][k] * b[k][j]
        prt.append(s)
    print(*prt)

