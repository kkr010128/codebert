a=b=ab=[]
n, m, l = map(int, input().strip().split())
for i in range(m+n):
    ab.append(list(map(int, input().strip().split())))
a,b=ab[:n],ab[n:]
for i in range(n):
    c = [sum(a[i][k]*b[k][j] for k in range(m)) for j in range(l)]
    print(*c)