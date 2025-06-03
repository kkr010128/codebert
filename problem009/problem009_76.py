from collections import deque
n=int(input())
l=[0]+[list(map(int,input().split()))[2:] for _ in range(n)]

flg=["white"]*(n+1)
dist=[-1]*(n+1)

def BFS(x):

    queue = deque([x])
    dist[x]=0
    flg[x]="gray"

    while queue:
        current=queue.popleft()
        for i in l[current]:
            if flg[i]=="white":
                queue.append(i)
                flg[i]="gray"
                dist[i]=dist[current]+1
        flg[current]="black"

BFS(1)

for num,i in enumerate(dist[1:],1):
    print(num,i)
