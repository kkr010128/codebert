a, b = map(int, input().split())
al = []
b_lis = []

for _ in range(a):
    g = list(map(int, input().split()))
    g.append(sum(g))
    al.append(g)
for i in range(b+1):
    p = 0
    for j in range(a):
        p += al[j][i]
    b_lis.append(p)
al.append((b_lis))
for i in al:
    print(' '.join([str(v) for v in i]))
