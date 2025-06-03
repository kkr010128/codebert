from sys import stdin
import sys
import math
from functools import reduce
import itertools

n = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split()]

if len(set(a)) == n:
    print('YES')
else:
    print('NO')