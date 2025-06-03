import heapq
N,M=map(int,input().split())
G=[[] for i in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
dist=[10**15 for i in range(N)]
prev=[-1 for i in range(N)]
dist[0]=0
q=[]
heapq.heappush(q,(0,0))
while(len(q)>0):
    c,v=heapq.heappop(q)
    if dist[v]<c:
        continue
    for d in G[v]:
        if dist[d]>dist[v]+1:
            dist[d]=dist[v]+1
            heapq.heappush(q,(dist[d],d))
            prev[d]=v
print("Yes")
for i in range(1,N):
    print(prev[i]+1)
