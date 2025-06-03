n,k=map(int,input().split())
mod=10**9+7
def f(i):
    return (1+i*(n-i+1))%mod
ans=0
for i in range(k,n+2):
    ans=(ans+f(i))%mod
print(ans)    