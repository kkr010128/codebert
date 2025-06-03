from collections import defaultdict as dd
from collections import deque
import bisect
import heapq

def ri():
    return int(input())

def rl():
    return list(map(int, input().split()))


def solve():
    a,b,n = rl()
    if n >= b:
        ans = (a * (b - 1)) // b - a * ((b - 1) // b)
    else:
        ans = a * n // b

    print (ans)






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
