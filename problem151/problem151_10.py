import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)

def inv(x):
    return pow(x, mod2 - 2, mod2)

cms = 10**6
cm = [0] * cms

def comb_init():
    cm[0] = 1
    for i in range(1, cms):
        cm[i] = cm[i-1] * i % mod2

def comb(a, b):
    return (cm[a] * inv(cm[a-b]) % mod2) * inv(cm[b]) % mod2

def main():
    n,m,k = LI()
    comb_init()

    a = [0] * n
    a[0] = m
    for i in range(1,n):
        a[i] = a[i-1] * (m-1) % mod2

    r = 0
    for i in range(k+1):
        r += a[n-i-1] * comb(n-1, i)
        r %= mod2

    return r

print(main())



