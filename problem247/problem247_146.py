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
 
 
from functools import reduce
# from math import *
from fractions import *
N, M = map(int, readline().split())
A = list(map(lambda x: int(x) // 2, readline().split()))

def f(n):
    cnt = 0
    while n % 2 == 0:
        n //= 2
        cnt += 1
    return cnt
t = f(A[0])
for i in range(N):
    if f(A[i]) != t:
        print(0)
        exit(0)
    A[i] >>= t
M >>= t
lcm = reduce(lambda a, b: (a * b) // gcd(a, b), A)
if lcm > M:
    print(0)
    exit(0)

print((M // lcm + 1) // 2)
