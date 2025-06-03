"""
E
"""
mod=10**9+7
MAX=4*10**5+100

g1=[1,1]
for i in range(2,MAX+1):
    num_1=g1[-1]*i%mod
    g1.append(num_1)
    
def cmb(n,r):
    return g1[n]*pow(g1[r],mod-2,mod)*pow(g1[n-r],mod-2,mod)%mod


N,K=map(int,input().split())

ans=cmb(2*N-1,N)


if K>=N:
    print(ans)
    
else:
    num=cmb(N,N-K-1)
    S=0
    for i in range(N-K-1,0,-1):
        S=(S+cmb(N-1,i-1)*cmb(N,i))%mod
        
    ans=(ans-S)%mod
    print(ans)