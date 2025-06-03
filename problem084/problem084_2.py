#D
from queue import Queue

N,M=map(int,input().split())
Friend=[[] for i in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    Friend[a].append(b)
    Friend[b].append(a)
    

Flag=[False for i in range(N+1)]
ans=1

for i in range(1,N+1):
    if Flag[i]:
        continue
    q=Queue()
    q.put(i)
    cnt=1
    while not q.empty():
        st=q.get()
        Flag[st]=True
        for j in Friend[st]:
            if Flag[j]:
                continue
            cnt+=1
            Flag[j]=True
            q.put(j)
            
        ans=max(ans,cnt)
print(ans)