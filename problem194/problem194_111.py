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
    dx = [1,0]
    dy = [0,1]
    INF = float('inf')
    h,w = readInts()
    dp = [[INF]*w for _ in range(h)]
    FIELD = [input() for _ in range(h)]
    # dp[j][i] = i番目とj番目にかかる魔法の度合い
    # 初期値 魔法1, なし 0
    if FIELD[0][0] == '#':
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    for i in range(w):
        for j in range(h):
            for x,y in dx,dy:
                ny = j + y
                nx = i + x
                if ny >= h or nx >= w:
                    continue
                add = 0
                if FIELD[ny][nx] == '#' and FIELD[j][i] == '.':
                    add = 1
                dp[ny][nx] = min(dp[ny][nx], dp[j][i] + add)
    print(dp[h-1][w-1])
if __name__ == '__main__':
  main()
