import bisect,collections,copy,heapq,itertools,math,string
import numpy as np
from numba import njit
import sys
sys.setrecursionlimit(10**7)

def _S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

A,B = LI()

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

Ad = make_divisors(A)
Bd = make_divisors(B)
# c = list(Ad.intersection(Bd))
c = list(set(Ad) & set(Bd))

def is_prime_custom(n):
    # custom
    if n == 1: return True

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

count = 0
for i in c:
    if is_prime_custom(i):
        count += 1
print(count)