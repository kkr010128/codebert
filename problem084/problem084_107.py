import sys
sys.setrecursionlimit(10**8)

def find(x):
    if par[x]==x:
        return x
    else:
        par[x]=find(par[x])
        return par[x]

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    
    if rank[a]<rank[b]:
        par[a]=b
        rank[b]+=rank[a]
        rank[a]=rank[b]
    else:
        par[b]=a
        rank[a]+=rank[b]
        rank[b]=rank[a]

    return

def chk(a,b):
    if par[a]==par[b]:
        print('Yes')
    else:
        print('No')

    return

N,M=map(int, input().split())

par=(list(range(N+1)))
rank=[1]*(N+1)

for _ in range(M):
    A,B=map(int, input().split())
    union(A,B)

print(max(rank))