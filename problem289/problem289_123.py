import sys
#import time
from collections import deque, Counter, defaultdict
#from fractions import gcd
import bisect
#import heapq
import math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = 10**18
MOD = 1000000007
ri = lambda : int(input())
rs = lambda : input().strip()
rl = lambda : list(map(int, input().split()))
a,b,x = rl()
if x<=a*a*b/2:

    print(180*math.atan(b**2*a/x/2)/math.pi)
else:
    t = 2*(a*a*b-x)/a/a
    print(180/math.pi*math.atan(t/a))