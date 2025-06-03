from collections import *
import copy
N,v,u=map(int,input().split())
AB=[list(map(int,input().split())) for i in range(N-1)]
data=[[] for i in range(N+1)]
for A,B in AB:
    data[A].append(B)
    data[B].append(A)

stack=deque([[v,0]])
visited=set([v])
while stack:
    a,m=stack.popleft()
    for p in data[a]:
        if p==u:
            K=m+1
        if not p in visited:
            visited.add(p)
            stack.append([p,m+1])


for i in range(len(data)):
    if len(data[i])>1:
        visited=set([i])
        stack=deque([i])
        End=set()
        break

if N==2:
    print(0)
    exit()
while stack:
    a=stack.popleft()
    flag=0
    for p in data[a]:
        if not p in visited:
            visited.add(p)
            stack.append(p)
            flag=1
    if flag==0:
        End.add(a)

Uvisited=set([u])
Vvisited=set([])
if not v in End:
    Vvisited.add(v)
Ustack=deque([[u,0]])
Vstack=deque([[v,0]])
ans=[]
M=1

while Ustack:
    while Vstack:
        a,m=Vstack.popleft()
        if m==M:
            Vstack.append([a,m])
            break
        for p in data[a]:
            if not p in End:
                if p in Uvisited:
                    pass
                    #ans.append(m)
                elif not p in Vvisited:
                    Vvisited.add(p)
                    Vstack.append([p,m+1])
    while Ustack:
        a,m=Ustack.popleft()
        if m==M:

            Ustack.append([a,m])
            break
        for p in data[a]:

            if not p in Uvisited:
                if p in Vvisited:
                    ans.append(m+1)
                Uvisited.add(p)
                Ustack.append([p,m+1])
    M+=1
print(max(ans))
