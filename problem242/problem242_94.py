n,k=map(int,input().split())
A=list(map(int,input().split()))
MOD=10**9+7
ans=0

L=[1]*(n+1)
Linv=[1]*(n+1)
inv=[0]+[1]*n

for i in range(2,n+1):
    L[i]=(L[i-1]*i)%MOD
    inv[i]=(MOD-inv[MOD%i]*(MOD//i))%MOD
    Linv[i]=(Linv[i-1]*inv[i])%MOD

def cmb(n,k):
    return (((L[n]*Linv[k])%MOD)*Linv[n-k])%MOD

A.sort()

for j in range(n-k+1):
    ans+=((A[-1-j]-A[j])*cmb(n-1-j,k-1))%MOD

if ans>=0:
    print(ans%MOD)
else:
    print(MOD+ans)
