n, m, l = list(map(int, input().split()))
a = [[int(j) for j in input().split()] for i in range(n)]
b = [[int(j) for j in input().split()] for i in range(m)]
c = [[0 for j in range(l)] for i in range(n)]

for i in range(n):
    for j in range(l):
        value = 0
        for k in range(m):
            value = value + a[i][k] * b[k][j]
        c[i][j] = value

for i in c:
    print(*i)
