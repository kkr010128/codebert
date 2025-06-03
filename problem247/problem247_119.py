#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n,m=map(int,input().split())
a=list(map(int,input().split()))

def lcm(a,b):
    g=math.gcd(a,b)
    return b*(a//g)
l=a[0]//2
for i in range(n):
    r=a[i]//2
    l=lcm(l,r)
for i in range(n):
    if (l//(a[i]//2))%2==0:
        print(0)
        exit()
res=m//l
print((res+1)//2)