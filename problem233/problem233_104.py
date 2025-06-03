from sys import stdin
import sys
import math
from functools import reduce
import itertools

n = int(stdin.readline().rstrip())
p = [int(x) for x in stdin.readline().rstrip().split()]

m = n
count = 0
for i in range(n):
    m = min([m, p[i]])
    if m == p[i]: count = count + 1

print(count)