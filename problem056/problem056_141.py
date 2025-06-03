n, m = map(int, input().split())

a =[[0 for i in range(m)]for j in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

b = [0 for j in range(m)]
for j in range(m):
    b[j] = int(input())

c = [0 for i in range(n)]

for i in range(n):
    for j in range(m):
        c[i] += a[i][j] * b[j]
    print(c[i])