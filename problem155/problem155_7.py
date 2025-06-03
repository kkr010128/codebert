from sys import stdin,stdout
from collections import defaultdict
n,e=list(map(int,stdin.readline().split()))
h=list(map(int,stdin.readline().split()))
g=defaultdict(list)
for _ in range(e):
    a,b=map(int,stdin.readline().split())
    g[a]+=[b]
    g[b]+=[a]
ans=0
for cur in range(1,n+1):
    f=1
    for neigh in g[cur]:
        if h[neigh-1]>=h[cur-1]:
            f=0
            break
    if f:ans+=1
print(ans)