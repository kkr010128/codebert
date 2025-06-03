n=int(input())
ps=[0 for j in range(n+1)]

for i in range(n):
    p,d,*vs=[int(j) for j in input().split()]
    ps[p]=vs
    
dist=[-1 for i in range(n+1)]    
    
d=0
queue=[1]

while queue:
    pos=queue.pop(0)
    if dist[pos] == -1:
        dist[pos]=d
    for i in ps[pos]:
        if dist[i]==-1:
            queue.append(i)
            dist[i]=dist[pos]+1

for i in range(1,n+1):
    print(i,dist[i])
    
