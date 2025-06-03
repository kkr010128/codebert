# 163_b
N,M=map(int,input().split())
A=input().split()
for i in range(len(A)):
    A[i]=int(A[i])
if (1<=N and N<=10**6)and(1<=M and M<= 10**4):
    for j in range(len(A)):
        N-=A[j]
    if N >= 0:
        print(N)
    if N < 0:
        print('-1')