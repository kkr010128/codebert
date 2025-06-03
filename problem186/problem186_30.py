#C
K, N=map(int,input().split())
A=list(map(int,input().split()))
for i in range(N):
    A.append(A[i]+K)
    Right=[]
for i in range(N):
    Right.append(A[N-1+i]-A[i])
print(min(Right))