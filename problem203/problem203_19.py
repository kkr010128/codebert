from sys import stdin
import sys
import math
from functools import reduce

a,b = [int(x) for x in stdin.readline().rstrip().split()]

c = int(b*10)

for i in range(10):
    if a == int(c*0.08):
        print(c)
        sys.exit()
    c = c + 1

print(-1)
