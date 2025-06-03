import sys
from collections import deque
#import numpy as np
import math
#sys.setrecursionlimit(10**6)
def S(): return sys.stdin.readline().rstrip()
def SL(): return map(str,sys.stdin.readline().rstrip().split())
def I(): return int(sys.stdin.readline().rstrip())
def IL(): return map(int,sys.stdin.readline().rstrip().split())

def solve():
    ans = 0
    flag = True
    for rep in discount:
        pay = a[rep[0]-1] + b[rep[1]-1] - rep[2]
        if flag:
            ans = pay
            flag = False
        else:
            ans = min(ans,pay)
    
    ans = min(ans,min(a)+min(b))
    print(ans)
    return

if __name__=='__main__':
    A,B,M = IL()
    a = list(IL())
    b = list(IL())
    discount = [list(IL()) for _ in range(M)]
    solve()