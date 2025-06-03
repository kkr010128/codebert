from collections import defaultdict
from collections import deque
from collections import Counter
import itertools
import math

def readInt():
  return int(input())
def readInts():
  return list(map(int, input().split()))
def readChar():
  return input()
def readChars():
  return input().split()

n,k = readInts()
r,s,p = readInts()
t = list(input())

his = ["-1"]
ans = 0
for i in range(len(t)):
  if t[i]=="r":
    me = "p"
    point = p
  elif t[i]=="s":
    me = "r"
    point = r
  else:
    me = "s"
    point = s
  if his[max(0,i-k+1)]==me:
    his.append(i)
  else:
    ans+=point
    his.append(me)

print(ans)