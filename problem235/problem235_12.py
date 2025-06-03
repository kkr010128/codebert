n=int(input())
a=list(map(int,input().split()))
mod=10**9+7

def eucrid(a,b):
  a,b=max(a,b),min(a,b)
  while True:
    if a%b==0:
      return b
    else:
      a,b=b,a%b
m=a[0]
for i in range(n):
  m=m//eucrid(m,a[i])*a[i]
b=0
m=m%mod
for i in a:
  b+=m*pow(i,mod-2,mod)%mod
print(b%mod)