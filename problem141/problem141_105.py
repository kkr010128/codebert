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


def main():
    n = I()
    aa = LI()

    if n == 0:
        if aa[0] == 1:
            return 1
        return -1

    if aa[0] != 0:
        return -1

    b = [1]
    c = 1
    for a in aa[1:-1]:
        if a > c * 2:
            return -1
        c = c * 2 - a
        b.append(c)

    if c * 2 < aa[-1]:
        return -1

    r = c = aa[-1]
    for a,b in list(zip(aa[:-1],b))[::-1]:
        t = (c+1) // 2
        if t > b:
            return -1
        c = a + min(b, c)
        r += c

    if c != 1:
        return -1

    return r

print(main())



