import sys
(n, m, l) = [int(i) for i in sys.stdin.readline().split()]

a = []
for i in range(n):
    a.append([int(i) for i in sys.stdin.readline().split()])
b = []
for i in range(m):
    b.append([int(j) for j in sys.stdin.readline().split()])

for i in range(n):
    row = []
    for j in range(l):
        c_ij = 0
        for k in range(m):
            c_ij += a[i][k] * b[k][j]
        row.append(str(c_ij))
    print(" ".join(row))