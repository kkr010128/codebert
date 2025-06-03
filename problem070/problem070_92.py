n,m = list(map(int, input().split()))
parent = list(range(n))

def root(x):
    if parent[x] == x: return x
    rt = root(parent[x])
    parent[x] = rt
    return rt

def unite(x,y):
    x = root(x)
    y = root(y)
    if x == y: return
    parent[y] = x

for _ in range(m):
    a,b = list(map(lambda x: int(x)-1, input().split()))
    unite(a,b)

for i in range(n):
    root(i)

cnt = len(set(parent)) - 1
print(cnt)