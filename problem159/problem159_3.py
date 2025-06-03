from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    x = ri()
    steps = 0
    bal = 100
    while bal < x:
        steps += 1
        bal += bal // 100
    print (steps)






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
