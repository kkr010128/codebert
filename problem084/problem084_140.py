n, m = map(int,input().split())
par = [-1 for i in range(n + 1)]
par[0] = 0
def find(x):
    if (par[x] < 0):
        return x
    else:
        x = par[x]
        return find(x)
def unit(x, y):
    if (find(x) == find(y)):
        pass
    else:
        x = find(x)
        y = find(y)
        if (x > y):
            x, y = y, x
        s = par[y]
        par[y] = x
        par[x] = par[x] + s

for i in range(m):
    a, b = map(int,input().split())
    unit(a, b)

par.sort()
print(-par[0])
