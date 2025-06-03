n,m=map(int,input().split())
g=[[] for i in range(n)]
for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a-1].append(b)
    g[b-1].append(a)
from collections import deque
x=[0]*n
s=1
for i in range(1,n+1):
    if x[i-1]==0:
        x[i-1]=s
        q=deque([i])
        while q:
            v = q.popleft()
            for j in g[v-1]:
                if x[j-1]==0:
                    q.append(j)
                    x[j-1]=s
        s+=1
print(s-2)