n,m,k=map(int, input().split())

mod=998244353
ans=0
c=1
for i in range(k+1):
    ans+=c*m*pow(m-1, n-1-i, mod)
    ans%=mod
    c*=(n-i-1)*pow(i+1, mod-2, mod)
    c%=mod
print(ans%mod)
