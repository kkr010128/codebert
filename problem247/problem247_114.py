import numpy as np
from fractions import gcd
def lcm(a,b):
  return a*b//gcd(a,b)
N,M=map(int,input().split())
a=[i//2 for i in map(int,input().split())]
b=np.array(a)
cnt=0
while all(b%2==0):
  b//=2
if any(b%2==0):
  print(0)
  exit()
ans=1
for i in a:
  ans=lcm(ans,i)
print((M//ans-1)//2+1)
