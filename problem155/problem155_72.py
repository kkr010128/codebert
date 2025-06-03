n,m = map(int,input().split())
h = list(map(int,input().split()))
l = [list(map(int,input().split())) for i in range(m)]
a,b = [list(i) for i in zip(*l)]
z = [1] * n

for i in range(m):
    x = a[i] - 1
    y = b[i] - 1
    if h[x] < h[y]:
        z[x] = 0
    elif h[x] > h[y]:
        z[y] = 0
    else:
        z[x] = 0
        z[y] = 0

print(n - z.count(0))