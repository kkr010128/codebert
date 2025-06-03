n,m=map(int,input().split())
a=list(map(int,input().split()))

import math
def lcm(x, y):
    return (x * y) // math.gcd(x, y)
x=1
for i in range(n):
  x=lcm(x,a[i]//2)

power=[0]*n
for i in range(n):
  while a[i]%2==0:
    a[i]//=2
    power[i]+=1
    
if power.count(power[0])==n:  
  print((m+x)//(2*x))
else:
  print(0)