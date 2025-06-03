import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
from collections import Counter
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 18
MOD = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N = int(input())
zero = 0
d = defaultdict(lambda: [0, 0])
for i in range(N):
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        zero += 1
        continue
    g = gcd(x, y)
    x //= g
    y //= g
    if y < 0:
        x = -x
        y = -y
    if y == 0 and x < 0:
        x = -x
    rotate = x <= 0
    if rotate:
        x, y = y, -x
        d[(x, y)][0] += 1
    else:
        d[(x, y)][1] += 1

ans = 1
for v in d.values():
    now = 1
    now += (2 ** v[0] - 1) % MOD
    now += (2 ** v[1] - 1) % MOD
    ans *= now
    ans %= MOD
print((ans - 1 + zero) % MOD)


    

