#!/usr/bin/env python3
import sys
from fractions import gcd
from functools import reduce
input = lambda: sys.stdin.readline().strip()
MOD = 1000000007
def lcm(a, b):
    return a // gcd(a, b) * b
n = int(input())
A = [int(x) for x in input().split()]
x = reduce(lcm, A)
print(sum(x // ai for ai in A) % MOD)
