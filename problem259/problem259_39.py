ii = lambda : int(input())
mi = lambda : map(int,input().split())
li = lambda : list(map(int,input().split()))

n,u,v = mi()
data = [[] for _ in range(n)]
for i in range(n-1):
    a,b = mi()
    a -= 1
    b -= 1
    data[a].append(b)
    data[b].append(a)
inf = -1
oni = [inf]*n
ko = [inf]*n

from collections import deque

def start(hazime,alis):
    d = deque()
    d.append((hazime-1,0))
    alis[hazime-1] = 0
    while d:
        ima,num = d.popleft()
        num += 1
        for i in data[ima]:
            if alis[i] != inf:
                continue
            alis[i] = num 
            d.append((i,num))
start(u,ko)
start(v,oni)

if len(data[u]) == 1 and data[u] == v:
    print(0) 
    exit()
ans = -1
for i in range(n):
    if ko[i] <= oni[i]:
        ans = max(ans,oni[i]-1)
print(ans)

