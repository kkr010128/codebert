import math
from collections import Counter

N = int(input())

c = Counter()

ans = 0
for n in range(1, N + 1):
    left = n // (10 ** int(math.log10(n)))
    right = n % 10
    c[(left, right)] += 1

for left, right in c.keys():
    ans += c[(left, right)] * c[(right, left)]

print(ans)
