import math
from functools import reduce
K = int(input())

def gcd(*numbers):
  return reduce(math.gcd, numbers)

ans = 0
for a in range(1,K+1):
  if (a==1):
    ans += K*K
    continue
  for b in range(1,K+1):
    t = gcd(a,b)
    if(t==1):
      ans += K
      continue
    for c in range(1,K+1):
      ans += gcd(t,c)
print(ans)