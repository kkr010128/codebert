from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    n, m = rl()
    A = rl()
    print (max(n - sum(A), -1))






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
