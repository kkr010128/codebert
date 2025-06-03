K,N=map(int,input().split())
A=[int(i) for i in input().split()]

dlist=[]

for i in range(1,N):
    d=A[i]-A[i-1]
    dlist.append(d)

dlist.append(A[0]+K-A[N-1])

print(K-max(dlist))