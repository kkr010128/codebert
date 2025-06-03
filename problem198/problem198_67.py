from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
from fractions import gcd
from itertools import combinations # (string,3) 3回
from collections import deque
from collections import defaultdict
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
    n = int(input())
    # 一番大きいものは何か、それを保存してdfs
    def dfs(cnt, s):
        if cnt == n:
            print(s)
            return
        biggest = 'a'
        c = 0
        while c < len(s):
            if s[c] == biggest:
                biggest = chr(ord(biggest)+1)
                c += 1
            else:
                c += 1
        for i in range(0,ord(biggest) - ord('a') + 1):
            sc = chr(ord('a')+i)
            s += sc
            dfs(cnt + 1, s)
            s = s[:-1]
    dfs(0,"")
if __name__ == '__main__':
  main()
