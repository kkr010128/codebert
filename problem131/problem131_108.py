from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    a, v = rl()
    b, w = rl()
    t = ri()
    d = abs(a - b)
    s = v - w
    if t * s >= d:
        print ("YES")
    else:
        print ("NO")





mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
