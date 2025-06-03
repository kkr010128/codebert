N,M,K=map(int,input().split())
MOD=998244353
ans=0
x,y=1,1
for k in range(K+1):
    ans=ans+M*x*pow(y,MOD-2,MOD)*pow(M-1,N-1-k,MOD)
    ans=ans%MOD
    x=x*(N-k-1)
    y=y*(k+1)
    x=x%MOD
    y=y%MOD
print(ans%MOD)