import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, y =  map(int, readline().split())

if x < y:
    x, y = y, x

b = (2 * x - y) // 3 
if (2 * x - y) % 3  != 0:
    print(0)
    exit()

a = x - 2 * b
if a < 0:
    print(0)
    exit()

MOD = 10 ** 9 + 7
a %= MOD
b %= MOD

MAX = 10 ** 6 * 2 + 2
fac = [0 for i in range(MAX)]
finv = [0 for i in range(MAX)]
inv = [0 for i in range(MAX)]

def comInit(mod):
    fac[0], fac[1] = 1, 1
    finv[0], finv[1] = 1, 1
    inv[1] = 1
    for i in range(2, MAX):
        fac[i] = fac[i - 1] * i % mod
        inv[i] = mod - inv[mod % i] * (mod // i) % mod
        finv[i] = finv[i - 1] * inv[i] % mod

def com(n, r, mod):
    if n < r:
        return 0
    if n < 0 or r < 0:
        return 0
    return fac[n] * (finv[r] * finv[n - r] % mod) % mod
    
comInit(MOD)
print(com(a + b, b, MOD))