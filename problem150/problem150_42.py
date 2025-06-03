N,K=map(int,input().split())
A=[int(x)-1 for x in input().split()]

dist={0:0}
t=i=0
while K>0:
    K-=1
    i+=1
    t=A[t]
    if t in dist:
        K%=i-dist[t]
    else:
        dist[t]=i

print(t+1)
