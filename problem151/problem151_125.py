mod=998244353
N,M,K=map(int,input().split())
MAX_N=N+1
Fact=[0 for i in range(MAX_N+1)]
Finv=[0 for i in range(MAX_N+1)]
Fact[0]=1
for i in range(MAX_N):
    Fact[i+1]=(i+1)*Fact[i]
    Fact[i+1]%=mod
Finv[-1]=pow(Fact[-1],mod-2,mod)
for i in range(MAX_N-1,-1,-1):
    Finv[i]=(i+1)*Finv[i+1]
    Finv[i]%=mod
def C(n,k):
    return (Fact[n]*Finv[k]*Finv[n-k])%mod
'''
i in range(K+1)で総和を取る
隣り合うブロックの色が同じ色なのはi通り
隣り合うブロックの色が異なるのはN-1-i通り
｜の選び方はN-1Ci
同じものをつなげてN-i個のブロックと見なせる
これに対してM*((M-1)のN-1-i)乗だけある
0<=i<=K
よりN-1-i>=N-1-K>=0
問題なし
'''
ans=0
for i in range(K+1):
    ans+=(C(N-1,i)*M*pow(M-1,N-1-i,mod))%mod
    ans%=mod
print(ans)