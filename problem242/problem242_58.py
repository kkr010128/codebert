N,K=list(map(int,input().split()))
A=sorted(list(map(int,input().split())))

mod=10**9+7

def modinv(x):
    return pow(x,mod-2,mod)

comb=1
ans=0

for i in range(N-K+1):
    ans+=comb*A[K-1+i]
    ans-=comb*A[N-K-i]

    ans%=mod

    comb*=(K+i)*modinv(i+1)
    comb%=mod

print(ans)
