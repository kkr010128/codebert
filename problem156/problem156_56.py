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
    fifths = {i**5: i for i in range(10000)}

    a = 0
    while 1:
        if x - a**5 in fifths:
            print (a, -fifths[x - a**5])
            return
        elif a**5 - x in fifths:
            print (a, fifths[a**5 - x])
            return
        a += 1






mode = 's'

if mode == 'T':
    t = ri()
    for i in range(t):
        solve()
else:
    solve()
