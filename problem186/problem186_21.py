import sys
a=sys.stdin.buffer.read
K,N,*A=map(int,a().split())
A+=[A[0]+K]
print(K-max(y-x for x,y in zip(A,A[1:])))