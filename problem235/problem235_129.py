def gcd(a,b):
  while b:a,b=b,a%b
  return a
def lcm(a,b):return a*b//gcd(a,b)
n=int(input())
a=list(map(int,input().split()))
ans=0
mod=10**9+7
l=a[0]
for i in range(1,n):l=lcm(l,a[i])
l%=mod
for i in a:
  ans+=l*pow(i,mod-2,mod)%mod
  ans%=mod
print(ans)