from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    k = ri()
    a, b = rl()
    for i in range(k, 1001, k):
        if a <= i <= b:
            print ("OK")
            return
    print ("NG")







mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
