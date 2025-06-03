from math import gcd
from itertools import combinations_with_replacement

k = int(input())
lst = [i for i in range(1,k+1)]
itr = combinations_with_replacement(lst, 3)
ans = 0

for i in itr:
  st = set(i)
  num = len(st)
  if num == 1:
    ans += i[0]
  elif num == 2:
    a,b = st
    ans += gcd(a,b) * 3
  else:
    ans += gcd(gcd(i[0],i[1]), i[2]) * 6

print(ans)