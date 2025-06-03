N,M=map(int,input().split())
par=[i for i in range(N+1)]
size=[1 for i in range(N+1)]
def find(x):
    if x!=par[x]:
        par[x]=find(par[x])
    return par[x]
def union(x,y):
    if find(x)!=find(y):
        x, y = par[x], par[y]
        par[y] = par[x]
        size[x] += size[y]
res=N
for i in range(M):
    s,e=map(int,input().split())
    union(s,e)
print(max(size))