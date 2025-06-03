r,c = [int(i) for i in input().split()]
a = [[int(i) for i in input().split()] for j in range(r)]
b = [sum(a[i]) for i in range(r)]
[a[i].append(b[i]) for i in range(r)]
d = [0 for i in range(c + 1)]
for i in range(r):
    for j in range(c + 1):
        d[j] += a[i][j]
a.append(d)
for i in range(r + 1):
    print(' '.join(map(str,a[i])))