# C Sum of gcd of Tuples (Easy)

import math
from itertools import combinations_with_replacement as C

K = int(input())

ans = 0
ABC = list(C(range(1, K+1), 3))
for a, b, c in ABC:
  if a == b == c:
    ans += math.gcd(math.gcd(a, b), c)
  elif a == b or b == c or c == a:
    ans += math.gcd(math.gcd(a, b), c) * 3
  else:
    ans += math.gcd(math.gcd(a, b), c) * 6
print(ans)