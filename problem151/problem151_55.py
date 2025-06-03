N,M,K=map(int,input().split())
P=998244353
class FactInv:
    def __init__(self,N,P):
        fact=[];ifact=[];fact=[1]*(N+1);ifact=[0]*(N+1)
        for i in range(1,N):
            fact[i+1]=(fact[i]*(i+1))%P
        ifact[-1]=pow(fact[-1],P-2,P)
        for i in range(N,0,-1):
            ifact[i-1]=(ifact[i]*i)%P
        self.fact=fact;self.ifact=ifact;self.P=P
    def comb(self,n,k):
        return (self.fact[n]*self.ifact[k]*self.ifact[n-k])%self.P
FI=FactInv(N+10,P)
ans=0
for k in range(0,K+1):
    ans+=(M*FI.comb(N-1,k)*pow(M-1,N-1-k,P))%P
    ans%=P
print(ans)