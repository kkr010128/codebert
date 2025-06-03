from collections import deque


def BFS():
    color=["white" for _ in range(h)]
    D=[-1 for _ in range(h)]
    M=[[] for _ in range(h)]

    for i in range(h-1):
        M[i].append(i+1)
        M[i+1].append(i)

    queue=deque([])
    for i in line:
        queue.append(i)
        D[i]=i
        color[i]="gray"

    while len(queue)>0:
        u=queue.popleft()
        for i in M[u]:
            if D[i]==-1 and color[i]=="white":
                D[i]=D[u]
                color[i]="gray"
                queue.append(i)

    return D


h,w,k=map(int,input().split())
S=[list(input()) for _ in range(h)]
M=[[0 for _ in range(w)] for _ in range(h)]

num,line=0,[]
for i in range(h):
    if S[i].count("#")!=0:
        p=num
        for j in range(w):
            if S[i][j]=="#":
                num +=1
            elif num==p:
                M[i][j]=num+1
                continue
            M[i][j]=num
        line.append(i)

D=BFS()
for i in range(h):
    M[i]=M[D[i]]

for i in range(h):
    print(*M[i])