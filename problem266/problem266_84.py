#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
from collections import deque,defaultdict
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
X = I()
shop = [100,101,102,103,104,105]
dp = [False] * (X+1) #全部の値段を探索する10**5なので
dp[0] = True
for i in range(X+1):
    for s in shop:
        if i - s >= 0:
            dp[i] = dp[i - s] | dp[i]
print('1' if dp[X] else '0')
