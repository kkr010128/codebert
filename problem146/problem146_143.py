from collections import defaultdict
from math import atan2, gcd

N = int(input())
MOD = 1000000007

d = defaultdict(lambda: [0, 0])

zero = 0
pos = []
neg = []
for _ in range(N):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        zero += 1
        continue
    if a < 0:
        a = -a
        b = -b
    elif a == 0 and b > 0:
        b = -b
    if b >= 0:
        pos.append((a, b))
    else:
        neg.append((a, b))

for a, b in pos:
    if b != 0:
        g = gcd(a, b)
    else:
        g = a
    d[(a // g, b // g)][0] += 1
for a, b in neg:
    a, b = -b, a
    if b != 0:
        g = gcd(a, b)
    else:
        g = a
    d[(a // g, b // g)][1] += 1

ans = 1
for p, n in d.values():
    ans *= pow(2, p, MOD) + pow(2, n, MOD) - 1
    ans %= MOD

ans += zero -1
ans %= MOD
print(ans)