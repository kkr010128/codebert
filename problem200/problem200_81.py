from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from itertools import combinations # (string,3) 3回
from collections import deque
from collections import defaultdict
from fractions import gcd
import bisect
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

def readInts():
  return list(map(int,input().split()))
def main():
    a,b,m = readInts()
    A = readInts()
    B = readInts()
    ans = float('inf')
    for i in range(m):
        x,y,c = readInts()
        x -=1
        y -=1
        ans = min(ans,A[x] + B[y] - c)
    # Aの商品の中で1番最小のやつを買うだけでもいいかもしれない
    # Bの商品の中で1番最小のやつを買うだけでもいいかもしれない
    ans = min(ans,min(A) + min(B))
    print(ans)
if __name__ == '__main__':
  main()
