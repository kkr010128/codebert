import math
from numba import jit

k=int(input())

@jit
def f():
  ans=0
  for a in range(1,k+1):
    for b in range(1,k+1):
      for c in range(1,k+1):
        g=math.gcd(math.gcd(a,b),c)
        ans+=g
  return ans

print(f())


