n, m, l = map(int, raw_input().split(" "))
a = [map(int, raw_input().split(" ")) for j in range(n)]
b = [map(int, raw_input().split(" ")) for i in range(m)]

c = [[0 for k in range(l)] for j in range(n)]
for j in range(n):
    for k in range(l):
        for i in range(m):
            c[j][k] += a[j][i] * b[i][k]
for j in range(n):
    print " ".join(map(str, (c[j])))