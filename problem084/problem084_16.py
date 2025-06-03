n, m = map(int, input().split())
ab = []
for i in range (m):
    ab.append(list(map(int, input().split())))

par = [-1] * (n+1)
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
        return
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return 

for j in range(m):
    unite(ab[j][0], ab[j][1])

m = -1*min(par)
print(m)

