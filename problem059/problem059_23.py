n, m = map(int, input().split())
a = []
b = []
for i in range(n):
    a += [list(map(int, input().split()))]
    a[i] += [sum(a[i])]
for i in range(m+1):
    b += [sum(x[i] for x in a)]
a += [b]
for i in range(n+1):
    print(*a[i])
