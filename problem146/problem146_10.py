import math
n = int(input())
from collections import defaultdict
d = defaultdict(list)
s = set()
zc = 0
for i in range(n):
    a,b = map(int, input().split())
    g = math.gcd(a,b)
    if g!=0:
        a //= g; b //= g
        if a<0:
            a,b = -a, -b
        elif a==0 and b<0:
            b *= -1
        d[a,b].append(i)
    if a==b==0:
        zc += 1
v = 1
s = set()
M = 10**9+7
for (a,b),val in d.items():
    aa,bb = b,-a
    if aa<0:
        aa,bb = -aa, -bb
    elif aa==0 and bb<0:
        bb *= -1
    if (a,b) in s or (aa,bb) in s:
        continue
    if (aa,bb) in d.keys():
        v *= (pow(2, len(val), M) + pow(2, len(d[aa,bb]), M) - 1)
    else:
        v *= pow(2, len(val), M)
    v %= M
    s.add((a,b))
    s.add((aa,bb))
v -= 1
v += zc
print(v%M)