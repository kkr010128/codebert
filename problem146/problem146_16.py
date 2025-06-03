from collections import defaultdict
from math import gcd as g
n = int(input())
mod = 10**9+7
sardines = set()
Ddic = defaultdict(int)
ans = 1
zcount = 0
for i in range(n):
  a,b = map(int,input().split())
  if a == 0 and b == 0:
    zcount += 1
    continue

  if a == 0:
    Ddic[(0,1)] += 1
    sardines.add((0,1))
    continue

  if b == 0:
    sardines.add((1,0))
    Ddic[(1,0)] += 1
    continue

  A,B = abs(a),abs(b)
  G = g(A,B)
  a //= G
  b //= G

  if b < 0:
    a = -a
    b = -b

  Ddic[(a,b)] += 1
  sardines.add((a,b))

for i in sardines:
  if i == (0,0) or (i[0] <= 0 and Ddic[(i[1],-i[0])] != 0):continue
  if i[0] <= 0:
    ans *= (2**Ddic[i] + 2**(Ddic[(i[1],-i[0])]))-1
  else:
    ans *= (2**Ddic[i] + 2**(Ddic[(-i[1],i[0])]))-1

  ans %= mod
print((ans+zcount-1)%mod)
