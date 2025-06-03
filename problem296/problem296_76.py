#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict,Counter
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

import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
S = input()
k = I()
from itertools import groupby
x = y = 0
g = [len(list(v)) for k,v in groupby(S)]
for c in g:
    x += c//2
if S[-1] == S[0]:
    if g[-1]%2 == 0 or g[0]%2 == 0:
        pass
    elif len(S) == 1:
        y = k//2
    elif len(S) == g[0]:
        y = k//2
    else:
        y = k-1
print(x * k + y)
