from sys import stdin
#入力
readline=stdin.readline
N,K=map(int,readline().split())
A=list(map(int,readline().split()))
A.sort()

mod=10**9+7
fact=[1]*(N+1)
finv=[1]*(N+1)
inv=[1]*(N+1)
inv[0]=0
for i in range(2,N+1):
    fact[i]=(fact[i-1]*i%mod)
    inv[i]=(-inv[mod%i]*(mod//i))%mod
    finv[i]=(finv[i-1]*inv[i])%mod

def com(N,K,mod):
    if (K<0) or (N<K):
        return 0
    return fact[N]*finv[K]*finv[N-K]%mod

s=0
for i in range(N-1,K-2,-1):
    s+=A[i]*com(i,K-1,mod)
for i in range(N-K+1):
    s-=A[i]*com(N-i-1,K-1,mod)
s%=mod
print(s)