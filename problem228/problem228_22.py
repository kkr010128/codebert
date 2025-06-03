from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools

@functools.lru_cache(None)
def aa(k):
    if k > 1: return 2*aa(k//2) + 1
    return 1

h = int(stdin.readline().rstrip())

print(aa(h))