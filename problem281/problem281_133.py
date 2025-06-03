from math import factorial as fac
x,y=map(int,input().split())
a=(2*y-x)/3
b=(2*x-y)/3
mod=10**9+7
if a>=0 and b>=0 and a==int(a) and b==int(b):
  a=int(a)
  b=int(b)
  a1=1
  a2=1  
  n3=10**9+7
  for i in range(a):
    a1*=a+b-i
    a2*=i+1
    a1%=n3
    a2%=n3
  a2=pow(a2,n3-2,n3)
  print((a1*a2)%n3)
else:
  print(0)