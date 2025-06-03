def find(x):
    if parent[x]<0:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]

def same(x,y):
    return find(x)==find(y)

def union(x,y):
    root_x=find(x)
    root_y=find(y)
    if root_x==root_y:
        return
    if parent[root_x]>parent[root_y]:
        root_x,root_y=root_y,root_x
    parent[root_x]+=parent[root_y]
    parent[root_y]=root_x

def members(n,x):
    root=find(x)
    return [i for i in range(n) if find(i)==root]

def get_size(x):
    return -parent[find(x)]

def get_root():
    return [i for i, root in enumerate(parent) if root<0]

N,M=map(int,input().split())
parent=[-1 for i in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    a=a-1
    b=b-1
    union(a,b)

ans=0
for i in parent:
    if i<0:
        ans+=1

print(ans-1)