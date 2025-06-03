n, m = map(int, input().split())
a = []
b = []
c = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    b.append(int(input()))
for i in range(n):
    elm = 0
    for k in range(m):
        elm += a[i][k] * b[k]
    c.append(elm)
for i in c:
    print(i)
