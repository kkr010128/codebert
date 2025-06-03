X,K,D=list(map(int,input().split()))
X=abs(X)
import sys

if X > 0 and X-K*D>=0:
    print(X-K*D)
    sys.exit()

M=X//D
Q=X%D

if M%2 == K%2:
    print(Q)
else:
    print(D-Q)

