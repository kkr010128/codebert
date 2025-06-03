import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random,resource

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
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
    s = S()

    m = {}
    m[0] = 0
    def f(i):
        if i in m:
            return m[i]

        c = 0
        ii = i
        while ii > 0:
            c += ii % 2
            ii //= 2

        t = i % c
        m[i] = f(t) + 1
        return m[i]

    c = len([_ for _ in s if _ == '1'])
    t = int(s, 2)
    cm = (c+1) * c * (c-1)
    if c > 1:
        t %= cm

    r = []
    k = 1
    for i in range(n-1,-1,-1):
        if t == k:
            r.append(0)
        elif s[i] == '1':
            r.append(f((t - k) % (c-1)) + 1)
        else:
            r.append(f((t + k) % (c+1)) + 1)
        k *= 2
        if c > 1:
            k %= cm

    return JA(r[::-1], "\n")


print(main())


