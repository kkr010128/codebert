#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
#from fractions  import gcd
#input=sys.stdin.readline
import bisect
s=input()
t=input()
n=len(s)
ans=0
for i in range(n):
    if s[i]!=t[i]:
        ans+=1
print(ans)