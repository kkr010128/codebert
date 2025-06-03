from math import gcd
from functools import reduce
def lcm_base(x, y):
    return (x * y) // gcd(x, y)
def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)
def evencount(n):
  cnt=0
  while n%2==0:
    cnt+=1
    n//=2
  return cnt
n,m=map(int,input().split())
a=list(map(int,input().split()))
for i in range(n):
  a[i]//=2
if all(evencount(i) == evencount(a[0]) for i in a):
  d=lcm(*a)
  print((m+d)//2//d)
else:print(0)