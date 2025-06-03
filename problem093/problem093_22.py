import sys
from heapq import heappush, heappop, heapify
import math
from math import gcd
import itertools as it
from collections import deque 

def inp():
    return int(input())
def inpl():
    return list(map(int, input().split()))

INF = 1001001001

# ---------------------------------------



n, k = inpl()
p = [0] + inpl()
c = [0] + inpl()

ans = - INF

for i in range(1, n + 1):
    cycle_cnt = 0
    cycle_sum = 0
    v = i

    while True:
        v = p[v]
        cycle_cnt += 1
        cycle_sum += c[v]
        if v == i: break
    
    cnt = 0
    path = 0

    while True:
        v = p[v]
        cnt += 1
        path += c[v]

        if cnt > k: break

        num = (k - cnt) // cycle_cnt
        score = path + max(0, cycle_sum) * num
        ans = max(ans, score)

        if v == i: break

print(ans)
