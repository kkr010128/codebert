### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest

def yn(b):
    print("Yes" if b==1 else "No")
    return

def resolve():
    readline=sys.stdin.readline

    n,m=map(int, readline().rstrip().split())

    ac=[0]*n
    wa=[0]*n

    for i in range(m):
        p,s=readline().rstrip().split()
        p=int(p)-1
        if s=="AC":
            ac[p]=1
            continue
        if ac[p]==0:
            wa[p]+=1
    for i in range(n):
        wa[i]*=ac[i]
    
    print(sum(ac),sum(wa))

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------