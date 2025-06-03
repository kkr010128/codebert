K,N=map(int,input().split())
A=list(map(int,input().split()))
l=[]
A.append(A[0]+K)
for i in range(N):
    l.append(A[i+1]-A[i])
print(K-max(l))
