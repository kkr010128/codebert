from math import gcd

n = int(input())
ab = [map(int, input().split()) for _ in range(n)]
mod = 1000000007

pair = []
d = {}
d[0] = {}
d[0][0] = 0

for a, b in ab:
   x = gcd(a, b)
   if x != 0:
      a //= x
      b //= x
   pair.append((a, b))

   d.setdefault(a, {})
   d[a].setdefault(b, 0)
   d[a][b] += 1
used = set()
ans = 1
for a, b in pair:
   if (a, b) in used:
      continue
   used.add((a, b))

   if a == 0 and b == 0:
      continue

   i = d[a][b]
   j, k, l = 0, 0, 0
   if -a in d and -b in d[-a]:
      j = d[-a][-b]
      used.add((-a, -b))
   if -b in d and a in d[-b]:
      k = d[-b][a]
      used.add((-b, a))
   if b in d and -a in d[b]:
      l = d[b][-a]
      used.add((b, -a))

   ans *= pow(2, i+j, mod) + pow(2, k+l, mod) - 1
   ans %= mod

ans += d[0][0] - 1
ans %= mod
print(ans)
