from collections import deque
inf=10**9


def BFS(num):
    color=["white" for _ in range(n+1)]
    D=[inf for _ in range(n+1)]
    queue=deque([num])

    color[num]="gray"
    D[num]=0

    while len(queue)>0:
        u=queue.popleft()
        for i in M[u]:
            if color[i]=="white" and D[u]+1<D[i]:
                D[i]=D[u]+1
                color[i]="gray"
                queue.append(i)
        color[u]="black"

    return D


n,x,y=map(int,input().split())
M=[[] for _ in range(n+1)]
for i in range(1,n):
    M[i].append(i+1)
    M[i+1].append(i)
M[x].append(y)
M[y].append(x)

ans=[0 for _ in range(n-1)]
for i in range(1,n+1):
    for j in BFS(i)[i+1:]:
        ans[j-1] +=1

for i in ans:
    print(i)