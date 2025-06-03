from sys import stdin
import sys
import math
from functools import reduce
import itertools

n,m = [int(x) for x in stdin.readline().rstrip().split()]

x = list('a'*n)

for i in range(m):
    a, b = [x for x in stdin.readline().rstrip().split()]
    a = int(a) - 1

    if x[a] == 'a' or x[a] == b:
        x[a] = b
    else:
        print(-1)
        sys.exit()

if x[0] == '0' and n != 1:
    print(-1)
    sys.exit()

if x[0] == 'a' and n > 1: x[0] = '1'
if x[0] == 'a' and n == 1: x[0] = '0'

for i in range(1,n):
    if x[i] == 'a': x[i] = '0'

print(''.join(x))

