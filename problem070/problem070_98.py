n,m = map(int,input().split())
par = [i for i in range(n+1)]
root = [i for i in range(n+1)]
par[0] = 1
def find(x):
    if par[x] == x:
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
    par[x] = y
    
for i in range(m):
    a,b = map(int,input().split())
    unite(a,b)
for i in range(n+1):
  root[i] = find(i)
print(len(set(root))-1)