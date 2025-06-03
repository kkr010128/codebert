l = input().split()
n = int(l[0])
m = int(l[1])

a = []
for i in range(n):
    a.append(list(map(int, input().split())))

b = []
for i in range(m):
    b.append(int(input()))

c = [[] for i in range(n)]
for i in range(n):
    for j in range(m):
        c[i].append(a[i][j] * b[j])
    print(sum(c[i]))