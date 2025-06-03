MOD=10**9+7
def facinv(N):
    fac,finv,inv=[0]*(N+1),[0]*(N+1),[0]*(N+1)
    fac[0]=1;fac[1]=1;finv[0]=1;finv[1]=1;inv[1]=1
    for i in range(2,N+1):
        fac[i]=fac[i-1]*i%MOD
        inv[i]=MOD-inv[MOD%i]*(MOD//i)%MOD
        finv[i]=finv[i-1]*inv[i]%MOD
    return fac,finv,inv

fac,finv,inv=facinv(2*(10**6))

#nCr
def COM(n,r):
    if n<r or r<0:
        return 0
    else:
        return ((fac[n]*finv[r])%MOD*finv[n-r])%MOD

K=int(input())
S=input()
L=len(S)
M=L+K
ans=0
for i in range(M):
    if i<L-1:
        continue
    c=COM(i,L-1)
    l=pow(25,i-(L-1),MOD)
    r=pow(26,M-i-1,MOD)
    ans=(ans+c*l%MOD*r%MOD)%MOD
print(ans)