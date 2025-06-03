from sys import stdin
import sys
import math
from functools import reduce
import functools
import itertools
from collections import deque
from operator import mul
from functools import reduce

n = int(input())

m = 0
for i in range(1,n+1):
    a = n // i
    m += a*(a+1)*i//2

print(m)