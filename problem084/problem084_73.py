#D - Friends
N,M = map(int,input().split())
par = [i for i in range(N)]
rank = [1] * (N)

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x]) #経路圧縮
        return par[x]

def size(x):
    return par.count(find(x))

def unite(x,y):
    x = find(x)
    y = find(y)
    if x == y : return 0
    if par[x] > par[y]:
        x,y = y,x
    par[y] = x
#    par[x] = x
    if par[x] == par[y]:
        rank[x] += rank[y]
#        rank[y] += rank[x]
#print(par)
#print(rank)
for i in range(M):
    a,b = map(int,input().split())
    a -= 1
    b -= 1
    unite(a,b)
#    print(par)
#    print(rank)
group_count = 0

group_count = max(rank)

# 出力
print(group_count)
