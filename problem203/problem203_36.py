import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

a,b = na()
ans = -1
for i in range(1, 1001):
    if a == math.floor(i * 0.08) and b == math.floor(i * 0.10):
        ans = i
        break
print(ans)
