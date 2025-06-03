#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations,permutations,accumulate, product # (string,3) 3回
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
# 四捨五入g
import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
n,m,x = readInts()
C = [readInts() for _ in range(n)]
INF = float('inf')
ans = INF
for bit in range(1 << n):
    all = [0] * m
    money = 0
    for i in range(n):
        if bit & (1 << i):
            money += C[i][0]
            for j in range(m):
                all[j] += C[i][j+1]
    flag = True
    for k in range(m):
        if all[k] >= x:
            pass
        else:
            flag = False
            break
    if flag:
        ans = min(ans, money)
print(ans if ans != INF else '-1')
