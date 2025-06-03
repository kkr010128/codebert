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
n,m = readInts()
base = []
if n == 1 and m == 0:
    print(0)
    exit()
elif n == 2 and m == 0:
    print(10)
    exit()
elif n == 3 and m == 0:
    print(100)
    exit()
if n >= 1:
    base.append('1')
if n >= 2:
    base.append('0')
if n == 3:
    base.append('0')
dic = defaultdict(int)
for i in range(m):
    s,c = readInts()
    s -= 1
    if dic[s] != 0:
        if int(base[s]) == c:
            pass
        else:
            print(-1)
            exit()
    else:
        dic[s] = 1
        base[s] = str(c)
    if s == 0 and c == 0 and n >= 2:
        print(-1)
        exit()
print(*base,sep='')
