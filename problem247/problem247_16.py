import sys
import itertools
# import numpy as np
import time
import math
import heapq
from collections import defaultdict
sys.setrecursionlimit(10 ** 7)
 
INF = 10 ** 9 + 7
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())

N, M = map(int, input().split())
A = list(map(lambda x: int(x) // 2, input().split()))

def f(n):
    res = 0
    while n % 2 == 0:
        n //= 2
        res += 1
    return res

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

x = f(A[0])
for a in A:
    y = f(a)
    if y != x:
        print(0)
        exit()

lcm = A[0]
for i in range(1, N):
    lcm = lcm * A[i] //  gcd(lcm, A[i])

print((M // lcm + 1) // 2)