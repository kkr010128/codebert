n, m, l = map(int, raw_input().split(" "))
a = [[0 for i in range(m)] for j in range(n)]
b = [[0 for k in range(l)] for i in range(m)]
for j in range(n):
    a[j] = map(int, raw_input().split(" "))
for i in range(m):
    b[i] = map(int, raw_input().split(" "))

c = [[0 for k in range(l)] for j in range(n)]
for j in range(n):
    for k in range(l):
        for i in range(m):
            c[j][k] += a[j][i] * b[i][k]
for j in range(n):
    print " ".join(map(str, (c[j])))