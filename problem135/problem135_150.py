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
a,b=input().split()
a=int(a)
ans=math.floor(((a*int(b[0]))*100+(a*int(b[2]))*10+(a*int(b[3])))//100)
print(ans)