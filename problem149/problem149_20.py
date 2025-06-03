import sys
import numpy as np
from math import ceil as C, floor as F, sqrt
from collections import defaultdict as D, Counter as CNT
from functools import reduce as R
 
ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alp = 'abcdefghijklmnopqrstuvwxyz'
def _X(): return sys.stdin.readline().rstrip().split(' ')
def _S(ss): return tuple(ss) if len(ss) > 1 else ss[0]
def S(): return _S(_X())
def Ss(): return list(S())
def _I(ss): return tuple([int(s) for s in ss]) if isinstance(ss, tuple) else int(ss)
def I(): return _I(S())
def _Is(ss): return list(ss) if isinstance(ss, tuple) else [ss]
def Is(): return _Is(I())

n, m, x = Is()
books = []
for _ in range(n):
  xs = Is()
  cost = xs[0]
  skills = xs[1:]
  books.append((cost, skills))

ans = []
stack = [(0, books, [0] * m)]

def doit(cost, books, skills):
  book = books[0]
  books = books[1:]
  
  ns = np.add(skills, book[1])
  if all([n >= x for n in ns]):
    ans.append(cost + book[0])
    
  if books:
    stack.append((cost+book[0], books, ns))
    stack.append((cost, books, skills))

while stack:
  state = stack.pop(0)
  doit(state[0], state[1], state[2])

print(min(ans) if ans else '-1')