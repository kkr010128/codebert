import sys
import time
import random
import math
from collections import deque
import heapq
import itertools
from decimal import Decimal
import bisect
from operator import itemgetter
MAX_INT = int(10e18)
MIN_INT = -MAX_INT
mod = 1000000000+7
sys.setrecursionlimit(1000000)
def IL(): return list(map(int,input().split()))
def SL(): return input().split()
def I(): return int(sys.stdin.readline())
def S(): return input()

def tami(ans):
  res = 0
  LastDay = [0]*26
  for i in range(D):
    res += s[i][ans[i]]
    for j in range(26):
      if ans[i] == j:
        continue
      res -= (i+1 - LastDay[j]) * c[j]
    LastDay[ans[i]] = i+1
  return res

def nasu():
  res = []
  LastDay = [0]*26
  for d in range(1,D+1):
    tmp = ["", 0]
    for i in range(26):
      if tmp[1] < s[d-1][i] + (d - LastDay[i]) * c[i]:
        tmp = [i, s[d-1][i] + (d - LastDay[i]) * c[i]]
    res.append(tmp[0])
    LastDay[tmp[0]] = d
  return res

def nbo(ans, score, num):
  tmp_ans = ans[:]
  for _ in range(num):
    random_date = random.randint(0,D-1)
    random_val = random.randint(0,25)
    tmp_ans[random_date] = random_val
  scoscore = tami(tmp_ans)
  if scoscore > score:
    return (True, tmp_ans, scoscore)
  else:
    return (False, tmp_ans, scoscore)

start = time.time()
D = I()
c = IL()
s = [IL() for i in range(D)]

ans = nasu()
#print(ans)

score = tami(ans)
#print(score)

end = time.time()
num = 10
cnt = 0
while (time.time() - start) < 1.8:
  judge, anans, scoscore = nbo(ans, score, num)
  if judge == True:
    ans, score = anans, scoscore
    #print(ans)
    #print(tami(ans))
  cnt += 1
  if cnt == 1000:
    cnt = 0
    num = max(2, num-1)
for i in ans:
  print(i+1)