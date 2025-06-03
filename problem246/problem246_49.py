import sys
from collections import deque
#import numpy as np
import math
#sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def order(l):
    flag = [True]*n
    ret = 0
    for i,item in enumerate(l):
        count = 0
        for j in range(n):
            if item-1==j:
                flag[j] = False
                break
            if not flag[j]:
                continue
            count += 1
        ret += fact[n-i-1]*count
    ret += 1
    return ret

def solve():
    a = order(p)
    b = order(q)
    print(abs(a-b))
    return

if __name__=='__main__':
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]
    n = I()
    p = list(IL())
    q = list(IL())
    solve()