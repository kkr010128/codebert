from collections import Counter
import math
n = int(input())
pp = []
a0 = 0
b0 = 0
z = 0

for i in range(n):
  a,b = map(int,input().split())
  if a==0 and b==0:
    z += 1
  elif a==0:
    a0 += 1
  elif b==0:
    b0 += 1
  else:
    gomi = math.gcd(a,b)
    if a < 0:
      a *= -1
      b *= -1
    pp.append((a//gomi,b//gomi))
    
mod = 10**9+7
a0 %= mod
b0 %= mod
z %= mod
p = Counter(pp)
r = 1
s = set()

for i,j in p.keys():
  if (i,j) in s:
    continue
  ans = p[(i,j)]
  if j < 0:
    f = (-j,i)
  else:
    f = (j,-i)
  chk = p[f]
  r *= (pow(2,ans,mod)+pow(2,chk,mod)-1)%mod
  r %= mod
  s.add(f)
r *= (pow(2,a0,mod)+pow(2,b0,mod)-1)%mod
r %= mod
print((r+z-1)%mod)