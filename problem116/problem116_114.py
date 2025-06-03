import sys
import numpy as np

def S(): return sys.stdin.readline().rstrip().split(' ')
def Ss(): return list(S())
def I(): return _I(Ss())
def Is(): return list(I())
def _I(ss): return map(int, ss) if len(ss) > 1 else int(ss[0])

s = S()[0]
t = S()[0]

ans = 0
for i, j in zip([c for c in s], [c for c in t]):
  if i != j:
    ans += 1
print(ans)