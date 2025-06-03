n , m = list(map(int, input().split()))
par=[i for i in range(n)]
rank=[0 for _ in range(n)]

def find(x):
    if x==par[x]:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

def unit(x,y):
    x=find(x) ; y=find(y)
    if find(x)==find(y):
        return
    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x]==rank[y]:
            rank[x]+=1

for _ in range(m):
    x , y=list(map(int, input().split()))
    x -= 1 ; y-=1
    unit(x,y)
count=[0 for _ in range(n)]
for i in range(n):
    count[find(i)]+=1
print(max(count))
