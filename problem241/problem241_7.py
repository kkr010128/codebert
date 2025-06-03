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

import sys
sys.setrecursionlimit(10000000)
mod = 10**9 + 7
#mod = 9982443453
def readInts():
  return list(map(int,input().split()))
def I():
  return int(input())
dx = [-1,0,1,0]
dy = [0,-1,0,1]
h,w = readInts()
S = [list(input()) for _ in range(h)]
def bfs(y,x):
    dq = deque()
    dq.append((y,x))
    res = -1
    dist = [[-1] * w for _ in range(h)]
    dist[y][x] = 0
    while dq:
        y,x = dq.popleft()
        res = max(res,dist[y][x])
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if not(0 <= ny < h and 0 <= nx < w):
                continue
            if S[ny][nx] == '#' or dist[ny][nx] != -1:
                continue
            dist[ny][nx] = dist[y][x] + 1
            dq.append((ny,nx))
    return res
ans = -1
for y in range(h):
    for x in range(w):
        if S[y][x] != '#':
            ans = max(ans,bfs(y,x))
print(ans)
