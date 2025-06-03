#Union Find

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
#        print(par)
        return par[x]
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True

#xとyが同じ集合に属するかの判定
def same(x,y):
    return find(x) == find(y)

#xが属する集合の個数
def size(x):
    return -par[find(x)]


N, M = map(int, input().split())
A = [0 for _ in range(M)]
B = [0 for _ in range(M)]

#初期化
#根なら-size,子なら親の頂点
par = [-1]*N

for i in range(M):
    a, b = map(int, input().split())
    unite(a-1, b-1)
#    print(par)

#print()
group = set([])

for i in range(N):
    group.add(find(i))

#print(group)
    
ans = 0
for g in group:
#    print(size(g))
    ans = max(ans, size(g))
print(ans)