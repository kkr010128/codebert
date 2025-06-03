n, m, l = map(int, input().split())
a = [[int(num) for num in input().split()] for i in range(n)]
b = [[int(num) for num in input().split()] for i in range(m)]
c = [[0 for i in range(l)] for j in range(n)]
for i in range(l):
    for j in range(n):
        for k in range(m):
            c[j][i] += a[j][k] * b[k][i]

for i in range(n):
    for j in range(l):
        if j == l - 1:
            print(c[i][j])
        else:
            print("{0} ".format(c[i][j]), end = "")