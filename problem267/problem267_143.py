#import sys
#import numpy as np
import math
#import itertools
#from fractions import Fraction
#import itertools
from collections import deque
from collections import Counter
#import heapq
#from fractions  import gcd
#input=sys.stdin.readline
#import bisect
n=int(input())
a=list(input())
a=list(map(int,a))
ans=0
for i in range(10):
    s=set(a)
    if i in s:
        p=a.index(i)
        for j in range(10):
            s=set(a[p+1:])
            if j in s:
                q=a[p+1:].index(j)+p+1
                for k in range(10):
                    s=set(a[q+1:])
                    if k in s:
                        ans+=1
print(ans)