import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time, copy

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

stdin = sys.stdin

ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
ns = lambda: stdin.readline().rstrip()  # ignore trailing spaces

h, w = na()
m = []
m = [ns() for _ in range(h)]
dp = [[inf] * w for _ in range(h)]
dp[0][0] = int(m[0][0] == '#')
for x in range(1, w):
    dp[0][x] = dp[0][x-1] + (int(m[0][x]=="#") if m[0][x-1]=="." else 0)
for y in range(1, h):
    dp[y][0] = dp[y-1][0] + (int(m[y][0]=="#") if m[y-1][0]=="." else 0)
    for x in range(1, w):
        dp[y][x] = min(
            dp[y][x-1] + (int(m[y][x]=="#") if m[y][x-1]=="." else 0),
            dp[y-1][x] + (int(m[y][x]=="#") if m[y-1][x]=="." else 0)
        )
print(dp[-1][-1])