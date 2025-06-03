#from statistics import median
#import collections
#aa = collections.Counter(a) # list to list || .most_common(2)で最大の2個とりだせるお a[0][0]
#from fractions import gcd
#from itertools import combinations # (string,3) 3回
#from collections import deque
#from collections import defaultdict
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
H,W,K = readInts()
cake = [input() for _ in range(H)]
ans = []
no = 0
cnt = 0
for h in range(H):
    if cake[h] == "."*W:
        no += 1
        continue
    else:
        cnt += 1
        same = []
        arrived = False
        for w in range(W):
            if cake[h][w] == "#":
                if not arrived:
                    arrived = True
                else:
                    cnt += 1
            same.append(cnt)
        for _ in range(no+1):
            ans.append(same)
        no = 0
for _ in range(no):
    ans.append(ans[-1])
for a in ans:
    print(*a,sep=" ")
