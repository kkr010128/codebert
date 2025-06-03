def Prime_Factorization(N):
    if N<0:
        R=[[-1,1]]
    else:
        R=[]

    N=abs(N)
    k=2
    while k*k<=N:
        if N%k==0:
            C=0
            while N%k==0:
                C+=1
                N//=k
            R.append([k,C])
        k+=1

    if N!=1:
        R.append([N,1])
    if not R:
        R.append([N,1])

    return R
#============================
from math import gcd
A,B=map(int,input().split())
G=gcd(A,B)

if G==1:
    print(1)
else:
    P=Prime_Factorization(G)
    print(len(P)+1)