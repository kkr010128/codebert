a = [[0 for i in range(100)] for j in range(100)]
b = [[0 for i in range(100)] for j in range(100)]
n, m, l = map(int, input().split())
for i in range(n):
    a[i][:m] = map(int, input().split())
for i in range(m):
    b[i][:l] = map(int, input().split())
for i in range(n):
    for j in range(l):
        c = 0
        for k in range(m):
            c += a[i][k] * b[k][j]
        if j == l-1:
            break
        print(c, end=' ')
    print(c)