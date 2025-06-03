MOD=10**9+7
def facinv(N):
    fac,finv,inv=[0]*(N+1),[0]*(N+1),[0]*(N+1)#階乗テーブル、逆元テーブル、逆元
    fac[0]=1;fac[1]=1;finv[0]=1;finv[1]=1;inv[1]=1
    for i in range(2,N+1):
        fac[i]=fac[i-1]*i%MOD
        inv[i]=MOD-inv[MOD%i]*(MOD//i)%MOD
        finv[i]=finv[i-1]*inv[i]%MOD
    return fac,finv,inv


def COM(n,r):
    if n<r or r<0:
        return 0
    else:
        return ((fac[n]*finv[r])%MOD*finv[n-r])%MOD
        
n,k=map(int,input().split())
fac,finv,inv=facinv(2*n)

if k>=n-1:
    print(COM(2*n-1,n-1))
else:
    ans=COM(2*n-1,n-1)
    for i in range(1,n-k):
        ans=(ans-COM(n,i)*COM(n-1,i-1)%MOD+MOD)%MOD
    print(ans%MOD)