n,m = map(int,raw_input().split())
a = [[0 for i in range (m)]for j in range(n)]
b = [0 for i in range(m)]
c = [0 for i in range(n)]

for i in range(n):
    x = map(int,raw_input().split())
    for j in range(m):
        a[i][j] = x[j]
for i in range(m):
    b[i] = int(raw_input())

for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]
    print c[i]