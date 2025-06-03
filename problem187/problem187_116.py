# -*- coding: utf-8 -*-
import sys
from collections import deque, defaultdict
from math import sqrt, factorial, gcd, ceil, atan, pi
# def input(): return sys.stdin.readline()[:-1] # warning not \n
# def input(): return sys.stdin.buffer.readline().strip() # warning bytes
# def input(): return sys.stdin.buffer.readline().decode('utf-8')
import string
# string.ascii_lowercase
from bisect import bisect_left
MOD = int(1e9)+7
INF = float('inf')


g = defaultdict(list)
n = 0
ans = defaultdict(int)
def bfs(x):
    q = deque([(x, 0)])
    w = set([x])
    while q:
        v, dis = q.popleft()
        if v > x:
            ans[dis] += 1
        for to in g[v]:
            if to not in w:
                w.add(to)
                q.append((to, dis + 1))
    

def solve():
    # n, m = [int(x) for x in input().split()]
    n, X, Y = [int(x) for x in input().split()]
    X -= 1
    Y -= 1
    g[X].append(Y)
    g[Y].append(X)
    for i in range(1, n):
        g[i].append(i-1)
        g[i-1].append(i)
    
    for i in range(n-1):
        bfs(i)

    for i in range(1, n):
        print(ans[i])

t = 1
# t = int(input())
for case in range(1,t+1):
    ans = solve()


"""

azyxwvutsrqponmlkjihgfedcb

"""
