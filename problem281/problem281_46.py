import math
mod=10**9+7
def mul(a, b):
    return ((a % mod) * (b % mod)) % mod
def div(a, b):
    return mul(a, pow(b, mod-2,mod))
x,y=map(int,input().split())
x,y=min(x,y),max(x,y)
s=y-x
if (x-s)<0 or 3*((x-s)//3)+2*s!=y:
  print(0)
else:
  a=(x-s)//3
  b=(y-2*s)//3+s
  A=1
  B=1
  C=1
  for i in range(1,a+b+1):
    A*=i
    A%=mod
  for i in range(1,a+1):
    B*=i
    B%=mod
  for i in range(1,b+1):
    C*=i
    C%=mod
  print(div(A,mul(B,C)))