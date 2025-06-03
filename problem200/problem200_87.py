A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
xyc = [map(int, input().split()) for _ in range(M)]
x, y, c = [list(x) for x in zip(*xyc)]

m = min(a)+min(b)
for i in range(M):
    tmp = a[x[i]-1]+b[y[i]-1]-c[i]
    m = min(m, tmp)

print(m)