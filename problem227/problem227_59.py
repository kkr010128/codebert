from sys import stdin
import sys
import math
from functools import reduce
import itertools

n,k = [int(x) for x in stdin.readline().rstrip().split()]
h = [int(x) for x in stdin.readline().rstrip().split()]

if k<n:
    h.sort()
    print(sum(h[:n-k]))
else:
    print(0)