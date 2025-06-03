import sys

A,B,K = (int(a) for a in input().split())
if A > K :
    A = A - K
    print(A,B)
    sys.exit()
else : 
    K = K - A
    A = 0
    if B > K :
        B = B - K
        print(A,B)
    else : 
        print(0,0)
