# coding: utf-8
import sys
from fractions import gcd
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7

N = ir()
A = lr()
lcm = 1
for a in A:
    lcm *= a // gcd(lcm, a)

A = np.array(A)
answer = (lcm // A).sum() % MOD
print(answer % MOD)
# np.int64とint型の違いに注意
