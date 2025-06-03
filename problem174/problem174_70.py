#!/usr/bin/env python3
from functools import reduce
from itertools import combinations
from math import gcd

K = int(input())

sum = K * (K + 1) // 2

for i in combinations(range(1, K + 1), 2):
    sum += 6 * reduce(gcd, i)

for i in combinations(range(1, K + 1), 3):
    sum += 6 * reduce(gcd, i)

print(sum)
