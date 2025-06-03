n, m, l = [int(x) for x in input().split()]
a = [[int(x) for x in input().split()] for y in range(n)]
b = [[int(x) for x in input().split()] for y in range(m)]
c = [[0 for x in range(l)] for y in range(n)]

for i in range(n):
    for j in range(l):
        c[i][j] = sum([a[i][x] * b[x][j] for x in range(m)])

for i in c:
    print(*i)