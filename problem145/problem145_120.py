from collections import deque

N,M = map(int, input().split())

AB = [list(map(int, input().split())) for _ in range(M)]

G = {i:[] for i in range(N+1)}
for a,b in AB:
    G[a].append(b)
    G[b].append(a)
    
parent = [0]*(N+1)
parent[0]==-1
parent[1]==-1
q = deque()
q.append(1)
while len(q)>0:
    room = q.popleft()
    child = G[room]
    
    for i in child:
        if parent[i] == 0:
            parent[i] = room
            q.append(i)
    
    
if min(parent[2:])==0:
    print('No')
else:
    print('Yes')
    for i in parent[2:]:
        print(i)