from math import gcd

def mod_prod(X,M):
    c=1
    for x in X:
        c*=x
        c%=M
    return c

N=int(input())
A=list(map(int,input().split()))
Mod=10**9+7

E=[0]*N
a=1
for i in range(N):
    E[i]=A[i]//gcd(a,A[i])
    a*=E[i]

P=mod_prod(E,Mod)

Q=0
for a in A:
    Q+=pow(a,Mod-2,Mod)
    Q%=Mod
print((P*Q)%Mod)