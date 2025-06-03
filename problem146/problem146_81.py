mod = 10 ** 9 + 7
from math import gcd
N = int(input())
from collections import defaultdict
X = defaultdict(lambda: [0, 0])
x = 0
y = 0
z = 0
for i in range(N):
  a, b = map(int, input().split())
  g = abs(gcd(a, b))
  if a * b > 0:
    X[(abs(a) // g, abs(b) // g)][0] += 1
  elif a * b < 0:
    X[(abs(b) // g, abs(a) // g)][1] += 1
  else:
    if a:
      x += 1
    elif b:
      y += 1
    else:
      z += 1
ans = 1
pow2 = [1]
for i in range(N):
  pow2 += [pow2[-1] * 2 % mod]
for i in X.values():
  ans *= pow2[i[0]] + pow2[i[1]]- 1
  ans %= mod
ans *= pow2[x] + pow2[y] - 1
ans += z - 1
ans %= mod
print(ans)