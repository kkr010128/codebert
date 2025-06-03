#!/usr/bin/env python3
from fractions import gcd

n = int(input())
a = list(map(int, input().split()))
MOD = 10 ** 9 + 7
l = 1
for x in a:
    l = l * x // gcd(l, x)
ans = sum(l // x for x in a) % MOD
print(ans)
