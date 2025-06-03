import math
from sys import stdin

a, b, c = map(int, stdin.readline().rstrip().split())
if (c - a - b) > 0:
    if (c - a - b) ** 2 > 4 * a * b:
        print('Yes')
    else:
        print('No')
else:
    print('No')