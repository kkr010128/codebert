K=int(input())
S=input()
M=10**9+7
#----------------------------------------------------------------
f=1
Fact=[f]
for i in range(1,len(S)+K+1):
    f=(f*i)%M
    Fact.append(f)

Inv=[0]*(len(S)+K+1)
g=pow(f,M-2,M)
Inv=[0]*(len(S)+K+1)
Inv[-1]=g
for j in range(len(S)+K-1,-1,-1):
    Inv[j]=(Inv[j+1]*(j+1))%M

def nCr(n,r):
    if 0<=r<=n:
        return (Fact[n]*Inv[r]*Inv[n-r])%M
    else:
        return 0

A=len(S)

T=0
for i in range(K+1):
    T=(T+nCr(A+K-1-i,K-i)*pow(25,K-i,M)*pow(26,i,M))%M
print(T)
