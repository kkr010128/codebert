N,K=map(int,input().split())
A=[]
B=[]
C=[]
D=[]
for i in range(2*K):
    A.append(list(map(int,input().split())))
for i in range(K):
    B.append(A[2*i-1])
for i in range(K):
    for j in range(len(B[i])):
        C.append(B[i][j])
for i in range(1,N+1):
    if i not in C:
        D.append(i)
print(len(D))