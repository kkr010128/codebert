N=int(input())
A=list(map(int,input().split()))
S=A[0]
B=[0 for i in range(N)]
for i in range(1,N):
    S=S^A[i]
for i in range(N):
    B[i]=S^A[i]
print(*B)