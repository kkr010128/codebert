from collections import deque
import sys
n,m = map(int,input().split())
 
turo = [[] for i in range(n)]
q = deque()
his = [False]*n
for i in range(m):
    a,b = map(int,input().split())
    turo[a-1].append(b-1)
    turo[b-1].append(a-1)
 
par = [i for i in range(n)]
rank = [sys.maxsize for i in range(n)]
rank[0] = 0
q.append(0)
 
while len(q) > 0:
    #print(q)
    room = q.popleft()
    
    if not his[room] :
        his[room] = True
    else:
        continue
    for room2 in turo[room]:
        if rank[room] < rank[room2]:
            q.append(room2)
            par[room2] = room
            rank[room2] = rank[room]+1
 
if len(his) < n:
    print("No")
    exit()
 
print("Yes")
for i in range(1,n):
    print(par[i]+1)