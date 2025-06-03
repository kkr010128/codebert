from sys import stdin
import sys
import math
from functools import reduce
import itertools

n,m = [int(x) for x in stdin.readline().rstrip().split()]

check = [0 for i in range(n)]
count = [0 for i in range(n)]

for i in range(m):
    p, q = [x for x in stdin.readline().rstrip().split()]
    p = int(p)

    if q == 'AC':
        check[p-1] = 1

    if q == 'WA' and check[p-1] == 0:
        count[p-1] = count[p-1] + 1

for i in range(n):
    if check[i] == 0: count[i] = 0

print(sum(check), sum(count))
