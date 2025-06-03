#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
import decimal
import re
#import bisect
#
#    d = m - k[i] - k[j]
#    if kk[bisect.bisect_right(kk,d) - 1] == d:
#
#
#
# pythonで無理なときは、pypyでやると正解するかも！！
#
#
# my_round_int = lambda x:np.round((x*2 + 1)//2)
# 四捨五入
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
import math
a,b,h,m = readInts()
h = h-12 if h>=12 else h
h_ = 30 * h + 30 * m/60
m_ = 360 * m / 60
kakudo = min(abs(m_ - h_), 360 - abs(m_ - h_))
c = pow(a**2 + b**2 - 2*a*b*math.cos(math.radians(kakudo)),.5)
print(c)
