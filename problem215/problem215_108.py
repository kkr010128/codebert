n,k=list(map(int,input().split()))

mod=10**9+7

def modinv(x):
    return pow(x,mod-2,mod)

ans=1
comb1=1
comb2=1

for i in range(1,min(n-1,k)+1):
    comb1*=(n-i+1)*modinv(i)
    comb2*=(n-i)*modinv(i)
    comb1%=mod
    comb2%=mod

    ans+=comb1*comb2
    ans%=mod

print(ans)