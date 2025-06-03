from collections import Counter
import math

n = int(input())
ab = []
mod = 10**9+7

num_ab0 = 0
num_a0 = 0
num_b0 = 0

for i in range(n):
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        num_ab0 += 1
    elif A == 0:
        num_a0 += 1
    elif B == 0:
        num_b0 += 1
    else:
        g = math.gcd(A, B)
        if A < 0:
            A = -A
            B = -B
        ab.append((A//g, B//g))

c = Counter(ab)

total = 2 ** num_a0 + 2 ** num_b0 - 1
for k, v in c.items():
    if k[1] < 0:
        num = c.get((-k[1], k[0]))
    else:
        num = c.get((k[1], -k[0]))

    if num:
        if k[1] > 0:
            total *= (2 ** v + 2 ** num - 1)
    else:
        total *= 2 ** v

print((total - 1 + num_ab0) % mod)
