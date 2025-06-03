import math
import numpy as np
import queue
from collections import deque
import heapq
mod = 10**9+7
ans = 1
iw0 = 0

def twoxxn(t,mod):
    ni = t
    an = 1
    n2 = 2
    while ni > 0:
        if ni%2 == 1:
            an = (an*n2)%mod
        n2 = (n2**2)%mod
        ni >>= 1
    return an

n = int(input())
d = dict()
for i in range(n):
    a,b = map(int,input().split())
    if a == 0 and b == 0:
        iw0 += 1
        continue
    if a == 0:
        b = 1
        g = 1
    elif b == 0:
        a = 1
        g = 1
    else:
        g = math.gcd(abs(a),abs(b))
    if a < 0 :
        a = -a
        b = -b
    p1 = a//g, b//g
    if p1 in d:
        d[p1] += 1
    else:
        d[p1] = 1
done = []
for (i0,i1), din in d.items():
    if d.get((-i1,i0),1) == 0 or d.get((i1,-i0),1) == 0:
        continue
    w = d.get((i1,-i0),0) + d.get((-i1,i0),0)
    aaa = (twoxxn(w,mod)+twoxxn(din,mod)-1)%mod
    ans = (ans*aaa)%mod
    d[(i0,i1)] = 0

if len(d.keys()) == 0:
    print(iw0)
    exit()

ans = (iw0+ans+mod-1)%mod
print(ans)
