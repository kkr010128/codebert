from math import atan,pi
A,B,X=map(int,input().split())

if 2*X>=A*A*B:
    P=atan(2*(A*A*B-X)/(A*A*A))*180/pi
    print(P)
else:
    Q=atan((A*B*B)/(2*X))*180/pi
    print(Q)
