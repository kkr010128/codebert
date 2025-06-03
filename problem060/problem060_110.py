n, m, l = map(int, input().split())
a = []
b = []
c = []

for i in range(n):
    ai = list(map(int, input().split()))
    a.append(ai)

for i in range(m):
    bi = list(map(int, input().split()))
    b.append(bi)

for i in range(n):
    ci = []
    for j in range(l):
        cij = 0
        for k in range(m):
            cij += a[i][k] * b[k][j]
        ci.append(cij)
    c.append(ci)

for i in range(n):
    print(" ".join(list(map(str, c[i]))))