import itertools
import math
import fractions
import functools
s, t = input().split()
a, b = map(int,input().split())
u = input()

if u == s:
    print(a-1,b)
else:
    print(a,b-1)