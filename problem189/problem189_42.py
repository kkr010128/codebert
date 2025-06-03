# -*- coding: utf-8 -*-

# combinationを使う

import math

def comb(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n, m = map(int, input().split())

counter = 0

if n >= 2:
    counter = counter + comb(n, 2)

if m >= 2:
    counter = counter + comb(m, 2)

print(counter)