from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    s, w = rl()
    if s > w:
        print ("safe")
    else:
        print ("unsafe")






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
