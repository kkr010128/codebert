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
n,m,q=map(int,input().split())
l=[i for i in range(1,m+1)]
ab=[list(map(int,input().split())) for _ in range(q)]
ans=0
for res in itertools.combinations_with_replacement(l, n):
    ans_r=0
    for i in range(q):
        a,b,c,d=ab[i]
        if c==res[b-1]-res[a-1]:
            ans_r+=d
    ans=max(ans,ans_r)
print(ans)