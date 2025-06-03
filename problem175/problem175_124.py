import sys
from operator import mul
from functools import reduce
from collections import Counter

n = int(input())
s = input()

c = Counter(s)
if len(c) != 3:
    print(0)
    sys.exit()

ans = reduce(mul, c.values())

for i in range(n - 1):
    x, y, z = i, i + 1, i + 2
    while z <= n - 1:
        if s[x] != s[y] and s[x] != s[z] and s[y] != s[z]:
            ans -= 1
        y += 1
        z += 2

print(ans)