n,k=map(int,input().split())
a=sorted(list(map(int,input().split())))
mod=10**9+7
ans=0
MOD=10**9+7

factorial = [1]
inverse = [1]
for i in range(1, n+2):
    factorial.append(factorial[-1] * i % MOD)
    inverse.append(pow(factorial[-1], MOD - 2, MOD))
 
 
# 組み合わせ計算
def nCr(n, r):
    if n < r or r < 0:
        return 0
    elif r == 0:
        return 1
    return factorial[n] * inverse[r] * inverse[n - r] % MOD
for i in range(n-k+1):
    ans-=a[i]*nCr(n-i-1,k-1)%mod
    ans%=mod
a=a[::-1]
for i in range(n-k+1):
    ans+=a[i]*nCr(n-i-1,k-1)%mod
    ans%=mod

print(ans%mod)