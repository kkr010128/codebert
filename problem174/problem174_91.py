import math
from functools import reduce

def gcd(*numbers):
    return reduce(math.gcd, numbers)

k = int(input())
ans = 0
for a in range(1, k+1):
  for b in range(a, k+1):
    for c in range(b, k+1):
      t = len({a,b,c})
      if t == 3:
        ans += gcd(a,b,c) * 6
      elif t == 2:
        ans += gcd(a,b,c) * 3
      else:
        ans += gcd(a,b,c)
        
print(ans)