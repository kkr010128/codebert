#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
n=input()
l=len(n)
ans=0
d=[(0,0)]*l
d[0]=min(int(n[0]),10-int(n[0])+1),min(int(n[0])+1,10-int(n[0]))
for i in range(1,l):
    ori=min(int(n[i])+d[i-1][0],10-int(n[i])+d[i-1][1])
    ori_1=min(int(n[i])+1+d[i-1][0],10-int(n[i])-1+d[i-1][1])
    d[i]=ori,ori_1
print(d[l-1][0])