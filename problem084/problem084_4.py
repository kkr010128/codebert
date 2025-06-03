N,Q = map(int,input().split())
par = [-1]*(N+1)
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x]) #経路圧縮
        return par[x]
def same(x,y):
    return find(x) == find(y)
def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y:
        return 0
    else:
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
def size(x):
    return -par[find(x)]


for i in range(Q):
    a,b = map(int,input().split())
    a-=1
    b-=1
    unite(a,b)

M = 0 
for i in range(N):
    M = max(size(i),M)
print(M)