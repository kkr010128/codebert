### ----------------
### ここから
### ----------------

import sys
from io import StringIO
import unittest
import collections

def resolve():
    readline=sys.stdin.readline
    n=int(readline())
    arr=list(map(int, readline().rstrip().split()))
    c=collections.Counter(arr)
    tb=[False]*(10**6 + 10)
    ans=0
    for x in c.keys():
        for j in range(x*2,10**6+5,x):
            tb[j]=True
    for x in c.keys():
        if tb[x]==0 and c[x]==1:
            ans+=1
    print(ans)

    return

if 'doTest' not in globals():
    resolve()
    sys.exit()

### ----------------
### ここまで 
### ----------------