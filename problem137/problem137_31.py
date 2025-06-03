import sys
N=int(sys.stdin.readline().strip())
A=[]
B=[]
for _ in range(N):
    a,b=map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
A.sort()
B.sort()
if N%2==0:
    A_med=float(A[N/2]+A[N/2-1])/2
    B_med=float(B[N/2]+B[N/2-1])/2
    print int((B_med-A_med)*2+1)
else:
    A_med=A[N/2]
    B_med=B[N/2]
    print B_med-A_med+1
