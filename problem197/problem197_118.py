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
a,b,c=map(int,input().split())
if 4*a*b<(c-a-b)**2 and (c-a-b)>0:
    print("Yes")
else:
    print("No")