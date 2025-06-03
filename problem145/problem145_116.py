import sys, bisect, math, itertools, string, queue, copy
# import numpy as np
# import scipy
# from collections import Counter,defaultdict,deque
# from itertools import permutations, combinations
# from heapq import heappop, heappush
# from fractions import gcd
# input = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
def inp(): return int(input())
def inpm(): return map(int,input().split())
def inpl(): return list(map(int, input().split()))
def inpls(): return list(input().split())
def inplm(n): return list(int(input()) for _ in range(n))
def inplL(n): return [list(input()) for _ in range(n)]
def inplT(n): return [tuple(input()) for _ in range(n)]
def inpll(n): return [list(map(int, input().split())) for _ in range(n)]
def inplls(n): return sorted([list(map(int, input().split())) for _ in range(n)])

n,m = inpm()
way = [[] for _ in range(n+1)]
for i in range(m):
    a,b = inpm()
    way[a].append(b)
    way[b].append(a)

ans = [0 for i in range(n+1)]
q = queue.Queue()
q.put((1,0))
while not q.empty():
    room,sign = q.get()
    if ans[room] != 0:
        continue
    ans[room] = sign

    for i in way[room]:
        q.put((i,room))

print('Yes')
for i in range(2,n+1):
    print(ans[i])