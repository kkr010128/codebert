#Union Find

#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        tank = []
        while par[x] >= 0:
            tank.append(x)
            x = par[x]
        for elt in tank:
            par[elt] = x
        return x
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

#集合の数
def numb():
    l = len(par)
    num = 0
    for ij in range(l):
        if par[ij] < 0:
            num += 1
    return num

n, m = map(int, input().split())
ab = []
for i in range(m):
    ab.append(list(map(int, input().split())))
par = [-1]*(n+1)
for j in range(m):
    unite(ab[j][0], ab[j][1])

print(numb() - 2)


