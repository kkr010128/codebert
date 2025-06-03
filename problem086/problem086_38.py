from sys import stdin
from math import ceil
inp = lambda : stdin.readline().strip()

n, x, t = [int(x) for x in inp().split()]
print(ceil(n/x)*t)