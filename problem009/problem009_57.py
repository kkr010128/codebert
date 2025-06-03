n=int(input())
ne=[[] for _ in range(n+1)]
for _ in range(n):
    u,k,*v=map(int,input().split())
    ne[u]=v
dis=[-1]*(n+1)
dis[1]=0
q=[1]
while q:
    p=q.pop(0)
    for e in ne[p]:
        if dis[e]==-1:
            dis[e]=dis[p]+1
            q.append(e)
for i in range(1,n+1):
    print(i,dis[i])
