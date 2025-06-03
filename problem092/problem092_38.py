X,K,D=map(int,input().split())

import math

X=abs(X)
U=min(math.floor(X/D),K)
K=K-U
A=X-U*D

if K%2==0:
    print(A)
else:
    print(abs(A-D))