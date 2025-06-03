import sys
from math import sqrt

readline = sys.stdin.readline
readlines = sys.stdin.readlines
ns = lambda: readline().rstrip() # input string
ni = lambda: int(readline().rstrip()) # input int
nm = lambda: map(int, readline().split()) # input multiple int 
nl = lambda: list(map(int, readline().split())) # input multiple int to list

a, b, c = nm()
if 4*a*b < (c-a-b)**2 and c-a-b>0:
    print('Yes')
else:
    print('No')