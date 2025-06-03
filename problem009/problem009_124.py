#=============================================================================
# Breadth First Search
#=============================================================================
import queue

N=int(input())
Graph=[[] for _ in range(N+1)]
dist=[-1 for _ in range(N+1)]
for i in range(1,N+1):
    Graph[i]=list(map(int,input().split()))[2:]


que=queue.Queue()
que.put(1)
dist[1]=0
while not que.empty():
    v=que.get()
    for nv in Graph[v]:
        if dist[nv] != -1:
            continue
        dist[nv]=dist[v]+1
        que.put(nv)
for i in range(1,N+1):
    print(i,dist[i],sep=" ")

