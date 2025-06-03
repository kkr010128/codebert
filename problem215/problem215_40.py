n,k=map(int,input().split())
#階乗
F = 200005
mod = 10**9+7
fact = [1]*F
inv = [1]*F
for i in range(2,F):
    fact[i]=(fact[i-1]*i)%mod
inv[F-1]=pow(fact[F-1],mod-2,mod)
for i in range(F-2,1,-1):
    inv[i] = (inv[i+1]*(i+1))%mod

ans=1
for i in range(1,min(n,k+1)):
    comb=(fact[n]*inv[i]*inv[n-i])%mod
    h=(fact[n-1]*inv[i]*inv[n-1-i])%mod
    ans=(ans+comb*h)%mod
print(ans)