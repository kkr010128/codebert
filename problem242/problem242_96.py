from math import factorial
n,k=map(int,input().split())
a=list(map(int,input().split()))
mod=10**9+7
ans=0
a.sort()
x=(factorial(n-1)*pow(factorial(k-1),mod-2,mod)*pow(factorial(n-k),mod-2,mod))%mod
y=1
for i in range(n-k+1):
  ans-=a[i]*x
  ans%=mod
  x=(x*(n-k-i)*pow(n-i-1,mod-2,mod))%mod
for i in range(k-1,n):
  ans+=a[i]*y
  ans%=mod
  y=(y*(i+1)*pow(i-k+2,mod-2,mod))%mod
print(ans)