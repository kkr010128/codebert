import sys
from functools import lru_cache
from collections import defaultdict
inf = float('inf')
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()
def read():
  return int(readline())
def reads():
  return map(int, readline().split())
x=read()
a=list(reads())
dic=[]
dic2=defaultdict(int)
for i in range(x):
  dic.append(i+a[i])
  dic2[i-a[i]]+=1
ans=0
#print(dic,dic2)
for i in dic:
  ans+=dic2[i]
print(ans)
  
