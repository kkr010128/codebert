K,N=map(int,input().split())

array=input().split()
A=[]
for i in array:
    A.append(int(i))

dist=[]
for i in range(N):
    if i!=N-1:
        dist.append(A[i+1]-A[i])
    else:
        dist.append((K-A[i])+A[0])

dist=sorted(dist)

ans=0
for i in range(N-1):
    ans+=dist[i]

print(ans)