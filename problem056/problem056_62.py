n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(list(map(int, input().split())))
b = []
for _ in range(m):
    b.append(int(input()))
c = []
for i in range(n):
    c.append(sum([a[i][j] * b[j] for j in range(m)]))
for i in c:
    print(i)

