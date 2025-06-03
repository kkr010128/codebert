import sys
sys.setrecursionlimit(1000000000)
from itertools import count
from functools import lru_cache
from collections import defaultdict
ii = lambda: int(input())
mis = lambda: map(int, input().split())
lmis = lambda: list(mis())
INF = float('inf')
def meg(f, ok, ng):
    while abs(ok-ng)>1:
        mid = (ok+ng)//2
        if f(mid):
            ok=mid
        else:
            ng=mid
    return ok
#


def main():
    T1,T2 = mis()
    A1,A2 = mis()
    B1,B2 = mis()
    d1 = T1*A1 - T1*B1
    d2 = T2*A2 - T2*B2
    if d1 + d2 == 0:
        print('infinity')
    elif d1 < 0 > d2 or d1 > 0 < d2:
        print(0)
    else:
        if d1 < 0:
            d1 *= -1
            d2 *= -1
        if d1 + d2 > 0:
            print(0)
        elif d1 % (d1+d2) == 0:
            print(d1 // abs(d1+d2) * 2)
        else:
            print(d1 // abs(d1+d2) * 2 + 1)




main()
