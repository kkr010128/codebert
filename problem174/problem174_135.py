def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)
import collections
K = int(input())
ans = 0
cnt = collections.defaultdict(int)
# count the number of combination of a, b
for a in range(1, K + 1):
  for b in range(1, K + 1):
    cnt[gcd(a, b)] += 1
for c in range(1, K + 1):
  for gcd_of_ab in cnt.keys():
    ans += gcd(gcd_of_ab, c) * cnt[gcd_of_ab]
print(ans)