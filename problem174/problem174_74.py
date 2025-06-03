import math
# from functools import reduce
import itertools


def gcd(a, b, c):
    ans = math.gcd(a, b)
    ans = math.gcd(ans, c)

    return ans

# def gcd(*numbers):
#     return reduce(math.gcd, numbers)

k = int(input())

elem = [i+1 for i in range(k)]

combs = itertools.combinations_with_replacement(elem, 3)

tmp = [1, 2, 3]

s = 0
for comb in combs:
    s += sum(tmp[:len(set(comb))]) * gcd(comb[0], comb[1], comb[2])
# for a in range(1, k+1):
#     for b in range(1, k+1):
#         for c in range(1, k+1):
#             s += gcd(a, b, c)

print(s)
